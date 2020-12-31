# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DmsClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(DmsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdms.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DmsClient":
            raise TypeError("client type error, support client type is DmsClient")

        return ClientBuilder(clazz)

    def batch_create_or_delete_queue_tag(self, request):
        """批量添加或删除队列标签

        批量添加或删除队列标签。

        :param BatchCreateOrDeleteQueueTagRequest request
        :return: BatchCreateOrDeleteQueueTagResponse
        """
        return self.batch_create_or_delete_queue_tag_with_http_info(request)

    def batch_create_or_delete_queue_tag_with_http_info(self, request):
        """批量添加或删除队列标签

        批量添加或删除队列标签。

        :param BatchCreateOrDeleteQueueTagRequest request
        :return: BatchCreateOrDeleteQueueTagResponse
        """

        all_params = ['queue_id', 'batch_create_or_delete_queue_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queue/{queue_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateOrDeleteQueueTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def confirm_consumption_messages(self, request):
        """确认已消费指定消息

        确认已经消费指定消息。  在消费者消费消息期间，消息仍然停留在队列中，但消息从被消费开始的30秒内不能被该消费组再次消费，若在这30秒内没有被消费者确认消费，则DMS认为消息未消费成功，将可以被继续消费。  如果消息被确认消费成功，消息将不能被该消费组再次消费，但是消息仍然保持在队列中，并且可以被其它消费组消费，消息在队列中的保留时间默认为72小时（除非队列被删除），72小时后会被删除。  消息批量消费确认时，必须严格按照消息消费的顺序提交确认，DMS按顺序判定消息是否消费成功，如果某条消息未确认或消费失败，则不再继续检测，默认后续消息全部消费失败。建议当对某一条消息处理失败时，不再需要继续处理本批消息中的后续消息，直接对已正确处理的消息进行确认。  确认消费失败后，可以再次重新消费和确认。当开启死信时，消息进行多次重复消费仍然失败后，DMS会将该条消息转存到死信队列中，有效期为72小时，用户可以根据需要对死信消息进行重新消费。

        :param ConfirmConsumptionMessagesRequest request
        :return: ConfirmConsumptionMessagesResponse
        """
        return self.confirm_consumption_messages_with_http_info(request)

    def confirm_consumption_messages_with_http_info(self, request):
        """确认已消费指定消息

        确认已经消费指定消息。  在消费者消费消息期间，消息仍然停留在队列中，但消息从被消费开始的30秒内不能被该消费组再次消费，若在这30秒内没有被消费者确认消费，则DMS认为消息未消费成功，将可以被继续消费。  如果消息被确认消费成功，消息将不能被该消费组再次消费，但是消息仍然保持在队列中，并且可以被其它消费组消费，消息在队列中的保留时间默认为72小时（除非队列被删除），72小时后会被删除。  消息批量消费确认时，必须严格按照消息消费的顺序提交确认，DMS按顺序判定消息是否消费成功，如果某条消息未确认或消费失败，则不再继续检测，默认后续消息全部消费失败。建议当对某一条消息处理失败时，不再需要继续处理本批消息中的后续消息，直接对已正确处理的消息进行确认。  确认消费失败后，可以再次重新消费和确认。当开启死信时，消息进行多次重复消费仍然失败后，DMS会将该条消息转存到死信队列中，有效期为72小时，用户可以根据需要对死信消息进行重新消费。

        :param ConfirmConsumptionMessagesRequest request
        :return: ConfirmConsumptionMessagesResponse
        """

        all_params = ['queue_id', 'consumer_group_id', 'confirm_consumption_messages_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']
        if 'consumer_group_id' in local_var_params:
            path_params['consumer_group_id'] = local_var_params['consumer_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}/groups/{consumer_group_id}/ack',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConfirmConsumptionMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def confirm_dead_letters_messages(self, request):
        """确认已消费死信消息

        确认已经消费指定的死信消息。  在消费者消费死信消息期间，死信消息仍然停留在队列中，但死信消息从被消费开始的30秒内不能被该消费组再次消费，若在这30秒内没有被消费者确认消费，则DMS认为死信消息未消费成功，将可以被继续消费。  如果死信消息被确认消费成功，该死信消息将不能被该消费组再次消费，死信消息的保留时间为72小时（除非消费组被删除），72小时后会被删除。  消息批量消费确认时，必须严格按照消息消费的顺序提交确认，DMS按顺序判定消息是否消费成功，如果某条消息未确认或消费失败，则不再继续检测，默认后续消息全部消费失败。建议当对某一条消息处理失败时，不再需要继续处理本批消息中的后续消息，直接对已正确处理的消息进行确认。  仅NORMAL队列和FIFO队列可以开启死信消息，因为只有NORMAL队列和FIFO队列可消费死信消息。

        :param ConfirmDeadLettersMessagesRequest request
        :return: ConfirmDeadLettersMessagesResponse
        """
        return self.confirm_dead_letters_messages_with_http_info(request)

    def confirm_dead_letters_messages_with_http_info(self, request):
        """确认已消费死信消息

        确认已经消费指定的死信消息。  在消费者消费死信消息期间，死信消息仍然停留在队列中，但死信消息从被消费开始的30秒内不能被该消费组再次消费，若在这30秒内没有被消费者确认消费，则DMS认为死信消息未消费成功，将可以被继续消费。  如果死信消息被确认消费成功，该死信消息将不能被该消费组再次消费，死信消息的保留时间为72小时（除非消费组被删除），72小时后会被删除。  消息批量消费确认时，必须严格按照消息消费的顺序提交确认，DMS按顺序判定消息是否消费成功，如果某条消息未确认或消费失败，则不再继续检测，默认后续消息全部消费失败。建议当对某一条消息处理失败时，不再需要继续处理本批消息中的后续消息，直接对已正确处理的消息进行确认。  仅NORMAL队列和FIFO队列可以开启死信消息，因为只有NORMAL队列和FIFO队列可消费死信消息。

        :param ConfirmDeadLettersMessagesRequest request
        :return: ConfirmDeadLettersMessagesResponse
        """

        all_params = ['queue_id', 'consumer_group_id', 'confirm_dead_letters_messages_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']
        if 'consumer_group_id' in local_var_params:
            path_params['consumer_group_id'] = local_var_params['consumer_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}/groups/{consumer_group_id}/deadletters/ack',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConfirmDeadLettersMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def consume_deadletters_message(self, request):
        """消费死信消息

        消费指定消费组产生的死信消息。可同时消费多条消息，每次消费的消息负载不超过512KB。  仅NORMAL队列和FIFO队列可以开启死信消息，因为只有NORMAL队列和FIFO队列可消费死信消息。

        :param ConsumeDeadlettersMessageRequest request
        :return: ConsumeDeadlettersMessageResponse
        """
        return self.consume_deadletters_message_with_http_info(request)

    def consume_deadletters_message_with_http_info(self, request):
        """消费死信消息

        消费指定消费组产生的死信消息。可同时消费多条消息，每次消费的消息负载不超过512KB。  仅NORMAL队列和FIFO队列可以开启死信消息，因为只有NORMAL队列和FIFO队列可消费死信消息。

        :param ConsumeDeadlettersMessageRequest request
        :return: ConsumeDeadlettersMessageResponse
        """

        all_params = ['queue_id', 'consumer_group_id', 'max_msgs', 'time_wait', 'ack_wait']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']
        if 'consumer_group_id' in local_var_params:
            path_params['consumer_group_id'] = local_var_params['consumer_group_id']

        query_params = []
        if 'max_msgs' in local_var_params:
            query_params.append(('max_msgs', local_var_params['max_msgs']))
        if 'time_wait' in local_var_params:
            query_params.append(('time_wait', local_var_params['time_wait']))
        if 'ack_wait' in local_var_params:
            query_params.append(('ack_wait', local_var_params['ack_wait']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}/groups/{consumer_group_id}/deadletters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConsumeDeadlettersMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def consume_messages(self, request):
        """消费消息

        消费指定队列中的消息。可同时消费多条消息，每次消费的消息负载不超过512KB。  当队列中消息较少时，单次消费返回的消息数量可能会少于指定条数，但多次消费最终可获取全部消息，当队列为空时，返回为空。  每个消费组只支持一种Label规则，如果第二次消费更换了Label规则，则消费失败。

        :param ConsumeMessagesRequest request
        :return: ConsumeMessagesResponse
        """
        return self.consume_messages_with_http_info(request)

    def consume_messages_with_http_info(self, request):
        """消费消息

        消费指定队列中的消息。可同时消费多条消息，每次消费的消息负载不超过512KB。  当队列中消息较少时，单次消费返回的消息数量可能会少于指定条数，但多次消费最终可获取全部消息，当队列为空时，返回为空。  每个消费组只支持一种Label规则，如果第二次消费更换了Label规则，则消费失败。

        :param ConsumeMessagesRequest request
        :return: ConsumeMessagesResponse
        """

        all_params = ['queue_id', 'consumer_group_id', 'max_msgs', 'time_wait', 'ack_wait', 'tag', 'tag_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']
        if 'consumer_group_id' in local_var_params:
            path_params['consumer_group_id'] = local_var_params['consumer_group_id']

        query_params = []
        if 'max_msgs' in local_var_params:
            query_params.append(('max_msgs', local_var_params['max_msgs']))
        if 'time_wait' in local_var_params:
            query_params.append(('time_wait', local_var_params['time_wait']))
        if 'ack_wait' in local_var_params:
            query_params.append(('ack_wait', local_var_params['ack_wait']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'tag_type' in local_var_params:
            query_params.append(('tag_type', local_var_params['tag_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}/groups/{consumer_group_id}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConsumeMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_consumer_group(self, request):
        """创建消费组

        创建消费组。  可同时为指定队列创建多个消费组。  > 创建消费组后系统内部完成初始化需要1-3秒，如果创建消费组后立即进行操作，可能会导致消费失败。建议3秒后再操作该队列。

        :param CreateConsumerGroupRequest request
        :return: CreateConsumerGroupResponse
        """
        return self.create_consumer_group_with_http_info(request)

    def create_consumer_group_with_http_info(self, request):
        """创建消费组

        创建消费组。  可同时为指定队列创建多个消费组。  > 创建消费组后系统内部完成初始化需要1-3秒，如果创建消费组后立即进行操作，可能会导致消费失败。建议3秒后再操作该队列。

        :param CreateConsumerGroupRequest request
        :return: CreateConsumerGroupResponse
        """

        all_params = ['queue_id', 'create_consumer_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}/groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateConsumerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_queue(self, request):
        """创建队列

        每个project_id默认只能创建30个队列。 > 创建队列时系统内部完成初始化需要1-3秒，如果创建队列后立即进行操作，可能会导致生产消息、消费消息、查询队列详情、创建消费组和删除队列等操作失败。建议3秒后再操作该队列。

        :param CreateQueueRequest request
        :return: CreateQueueResponse
        """
        return self.create_queue_with_http_info(request)

    def create_queue_with_http_info(self, request):
        """创建队列

        每个project_id默认只能创建30个队列。 > 创建队列时系统内部完成初始化需要1-3秒，如果创建队列后立即进行操作，可能会导致生产消息、消费消息、查询队列详情、创建消费组和删除队列等操作失败。建议3秒后再操作该队列。

        :param CreateQueueRequest request
        :return: CreateQueueResponse
        """

        all_params = ['create_queue_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_queue(self, request):
        """删除指定队列

        删除指定的队列。

        :param DeleteQueueRequest request
        :return: DeleteQueueResponse
        """
        return self.delete_queue_with_http_info(request)

    def delete_queue_with_http_info(self, request):
        """删除指定队列

        删除指定的队列。

        :param DeleteQueueRequest request
        :return: DeleteQueueResponse
        """

        all_params = ['queue_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_specified_consumer_group(self, request):
        """删除指定消费组

        删除指定消费组。

        :param DeleteSpecifiedConsumerGroupRequest request
        :return: DeleteSpecifiedConsumerGroupResponse
        """
        return self.delete_specified_consumer_group_with_http_info(request)

    def delete_specified_consumer_group_with_http_info(self, request):
        """删除指定消费组

        删除指定消费组。

        :param DeleteSpecifiedConsumerGroupRequest request
        :return: DeleteSpecifiedConsumerGroupResponse
        """

        all_params = ['queue_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}/groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSpecifiedConsumerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_consumer_groups(self, request):
        """查看指定队列的所有消费组

        获取指定队列的所有消费组。

        :param ListConsumerGroupsRequest request
        :return: ListConsumerGroupsResponse
        """
        return self.list_consumer_groups_with_http_info(request)

    def list_consumer_groups_with_http_info(self, request):
        """查看指定队列的所有消费组

        获取指定队列的所有消费组。

        :param ListConsumerGroupsRequest request
        :return: ListConsumerGroupsResponse
        """

        all_params = ['queue_id', 'include_deadletter', 'include_messages_num', 'page_size', 'current_page']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []
        if 'include_deadletter' in local_var_params:
            query_params.append(('include_deadletter', local_var_params['include_deadletter']))
        if 'include_messages_num' in local_var_params:
            query_params.append(('include_messages_num', local_var_params['include_messages_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'current_page' in local_var_params:
            query_params.append(('current_page', local_var_params['current_page']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListConsumerGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_queues(self, request):
        """查看所有队列

        查看所有队列。

        :param ListQueuesRequest request
        :return: ListQueuesResponse
        """
        return self.list_queues_with_http_info(request)

    def list_queues_with_http_info(self, request):
        """查看所有队列

        查看所有队列。

        :param ListQueuesRequest request
        :return: ListQueuesResponse
        """

        all_params = ['include_deadletter']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_deadletter' in local_var_params:
            query_params.append(('include_deadletter', local_var_params['include_deadletter']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQueuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def send_messages(self, request):
        """向指定队列发送消息

        向指定队列发送消息，可同时发送多条消息。  - 每次最多发送10条。 - 每次发送的消息总负载不超过512KB。 - Kafka队列的消息保存时间在创建队列时可以设置，可设置范围为1~72小时。其他队列的消息最大保存时长为72小时。

        :param SendMessagesRequest request
        :return: SendMessagesResponse
        """
        return self.send_messages_with_http_info(request)

    def send_messages_with_http_info(self, request):
        """向指定队列发送消息

        向指定队列发送消息，可同时发送多条消息。  - 每次最多发送10条。 - 每次发送的消息总负载不超过512KB。 - Kafka队列的消息保存时间在创建队列时可以设置，可设置范围为1~72小时。其他队列的消息最大保存时长为72小时。

        :param SendMessagesRequest request
        :return: SendMessagesResponse
        """

        all_params = ['queue_id', 'send_messages_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}/messages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_project_tags(self, request):
        """查询项目标签

        查询项目标签。

        :param ShowProjectTagsRequest request
        :return: ShowProjectTagsResponse
        """
        return self.show_project_tags_with_http_info(request)

    def show_project_tags_with_http_info(self, request):
        """查询项目标签

        查询项目标签。

        :param ShowProjectTagsRequest request
        :return: ShowProjectTagsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queue/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_queue(self, request):
        """查看指定队列

        查看指定的队列。

        :param ShowQueueRequest request
        :return: ShowQueueResponse
        """
        return self.show_queue_with_http_info(request)

    def show_queue_with_http_info(self, request):
        """查看指定队列

        查看指定的队列。

        :param ShowQueueRequest request
        :return: ShowQueueResponse
        """

        all_params = ['queue_id', 'include_deadletter']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []
        if 'include_deadletter' in local_var_params:
            query_params.append(('include_deadletter', local_var_params['include_deadletter']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queues/{queue_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_queue_tags(self, request):
        """查询队列标签

        查询队列标签。

        :param ShowQueueTagsRequest request
        :return: ShowQueueTagsResponse
        """
        return self.show_queue_tags_with_http_info(request)

    def show_queue_tags_with_http_info(self, request):
        """查询队列标签

        查询队列标签。

        :param ShowQueueTagsRequest request
        :return: ShowQueueTagsResponse
        """

        all_params = ['queue_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/queue/{queue_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQueueTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_quotas(self, request):
        """查看租户配额

        查看当前项目的配额。

        :param ShowQuotasRequest request
        :return: ShowQuotasResponse
        """
        return self.show_quotas_with_http_info(request)

    def show_quotas_with_http_info(self, request):
        """查看租户配额

        查看当前项目的配额。

        :param ShowQuotasRequest request
        :return: ShowQuotasResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)

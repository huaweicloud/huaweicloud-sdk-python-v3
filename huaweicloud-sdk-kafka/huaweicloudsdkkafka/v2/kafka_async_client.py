# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class KafkaAsyncClient(Client):
    def __init__(self):
        super(KafkaAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkafka.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "KafkaAsyncClient":
                raise TypeError("client type error, support client type is KafkaAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_or_delete_kafka_tag_async(self, request):
        """批量添加或删除实例标签

        批量添加或删除实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOrDeleteKafkaTag
        :type request: :class:`huaweicloudsdkkafka.v2.BatchCreateOrDeleteKafkaTagRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchCreateOrDeleteKafkaTagResponse`
        """
        return self._batch_create_or_delete_kafka_tag_with_http_info(request)

    def _batch_create_or_delete_kafka_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/kafka/{instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateOrDeleteKafkaTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_group_async(self, request):
        """Kafka实例批量删除Group

        该接口用于向Kafka实例批量删除Group。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteGroup
        :type request: :class:`huaweicloudsdkkafka.v2.BatchDeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchDeleteGroupResponse`
        """
        return self._batch_delete_group_with_http_info(request)

    def _batch_delete_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/groups/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_instance_topic_async(self, request):
        """Kafka实例批量删除Topic

        该接口用于向Kafka实例批量删除Topic。批量删除多个Topic时，部分删除成功，部分失败，此时接口返回删除成功，并在返回中显示删除失败的Topic信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteInstanceTopic
        :type request: :class:`huaweicloudsdkkafka.v2.BatchDeleteInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchDeleteInstanceTopicResponse`
        """
        return self._batch_delete_instance_topic_with_http_info(request)

    def _batch_delete_instance_topic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteInstanceTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_instance_users_async(self, request):
        """批量删除用户

        批量删除Kafka实例的用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteInstanceUsers
        :type request: :class:`huaweicloudsdkkafka.v2.BatchDeleteInstanceUsersRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchDeleteInstanceUsersResponse`
        """
        return self._batch_delete_instance_users_with_http_info(request)

    def _batch_delete_instance_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/users',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteInstanceUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_restart_or_delete_instances_async(self, request):
        """批量重启或删除实例

        批量重启或删除实例。
        
        在实例重启过程中，客户端的生产与消费消息等请求会被拒绝。
        
        实例删除后，实例中原有的数据将被删除，且没有备份，请谨慎操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRestartOrDeleteInstances
        :type request: :class:`huaweicloudsdkkafka.v2.BatchRestartOrDeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchRestartOrDeleteInstancesResponse`
        """
        return self._batch_restart_or_delete_instances_with_http_info(request)

    def _batch_restart_or_delete_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRestartOrDeleteInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def close_kafka_manager_async(self, request):
        """关闭kafka manager

        关闭kafka manager，相应的原来开放出的management相关接口也将不可用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CloseKafkaManager
        :type request: :class:`huaweicloudsdkkafka.v2.CloseKafkaManagerRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CloseKafkaManagerResponse`
        """
        return self._close_kafka_manager_with_http_info(request)

    def _close_kafka_manager_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/kafka/instances/{instance_id}/management',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CloseKafkaManagerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_connector_async(self, request):
        """创建实例的转储节点

        创建实例的转储节点。
        
        **当前通过调用API，只支持按需实例创建转储节点。**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConnector
        :type request: :class:`huaweicloudsdkkafka.v2.CreateConnectorRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateConnectorResponse`
        """
        return self._create_connector_with_http_info(request)

    def _create_connector_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/connector',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_delete_connector_order_async(self, request):
        """创建关闭实例转储节点的订单

        创建删除实例转储节点的订单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDeleteConnectorOrder
        :type request: :class:`huaweicloudsdkkafka.v2.CreateDeleteConnectorOrderRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateDeleteConnectorOrderResponse`
        """
        return self._create_delete_connector_order_with_http_info(request)

    def _create_delete_connector_order_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/kafka/instances/{instance_id}/delete-connector-order',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDeleteConnectorOrderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_by_engine_async(self, request):
        """创建实例

        创建实例。
        
        该接口支持创建按需和包周期两种计费方式的实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceByEngine
        :type request: :class:`huaweicloudsdkkafka.v2.CreateInstanceByEngineRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateInstanceByEngineResponse`
        """
        return self._create_instance_by_engine_with_http_info(request)

    def _create_instance_by_engine_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{engine}/{project_id}/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstanceByEngineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_topic_async(self, request):
        """Kafka实例创建Topic

        该接口用于向Kafka实例创建Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceTopic
        :type request: :class:`huaweicloudsdkkafka.v2.CreateInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateInstanceTopicResponse`
        """
        return self._create_instance_topic_with_http_info(request)

    def _create_instance_topic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstanceTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_user_async(self, request):
        """创建用户

        创建Kafka实例的用户，用户可连接开启SASL的Kafka实例。 [ 2023年7月15日前创建的Kafka实例，一个实例最多创建20个用户。2023年7月15日及以后创建的Kafka实例，一个实例最多创建500个用户。](tag:hws,hws_hk)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceUser
        :type request: :class:`huaweicloudsdkkafka.v2.CreateInstanceUserRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateInstanceUserResponse`
        """
        return self._create_instance_user_with_http_info(request)

    def _create_instance_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstanceUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_kafka_consumer_group_async(self, request):
        """创建消费组

        实例创建消费组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKafkaConsumerGroup
        :type request: :class:`huaweicloudsdkkafka.v2.CreateKafkaConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateKafkaConsumerGroupResponse`
        """
        return self._create_kafka_consumer_group_with_http_info(request)

    def _create_kafka_consumer_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/kafka/instances/{instance_id}/group',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateKafkaConsumerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_partition_async(self, request):
        """新增Kafka实例指定Topic分区

        新增Kafka实例指定Topic分区。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePartition
        :type request: :class:`huaweicloudsdkkafka.v2.CreatePartitionRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreatePartitionResponse`
        """
        return self._create_partition_with_http_info(request)

    def _create_partition_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions-reassignment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePartitionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_post_paid_instance_async(self, request):
        """创建实例

        [创建按需计费类型的Kafka实例。](tag:sbc,hk_sbc,cmcc)[创建kafka实例。](tag:otc)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostPaidInstance
        :type request: :class:`huaweicloudsdkkafka.v2.CreatePostPaidInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreatePostPaidInstanceResponse`
        """
        return self._create_post_paid_instance_with_http_info(request)

    def _create_post_paid_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePostPaidInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_reassignment_task_async(self, request):
        """Kafka实例开始分区重平衡任务

        该接口用于向Kafka实例提交分区重平衡任务，若成功则返回重平衡任务的job id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReassignmentTask
        :type request: :class:`huaweicloudsdkkafka.v2.CreateReassignmentTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateReassignmentTaskResponse`
        """
        return self._create_reassignment_task_with_http_info(request)

    def _create_reassignment_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/kafka/{project_id}/instances/{instance_id}/reassign',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateReassignmentTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_sink_task_async(self, request):
        """创建转储任务

        创建转储任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSinkTask
        :type request: :class:`huaweicloudsdkkafka.v2.CreateSinkTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateSinkTaskResponse`
        """
        return self._create_sink_task_with_http_info(request)

    def _create_sink_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSinkTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_background_task_async(self, request):
        """删除后台任务管理中的指定记录

        删除后台任务管理中的指定记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackgroundTask
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteBackgroundTaskResponse`
        """
        return self._delete_background_task_with_http_info(request)

    def _delete_background_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBackgroundTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_connector_async(self, request):
        """关闭实例转储节点

        关闭实例转储节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConnector
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteConnectorRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteConnectorResponse`
        """
        return self._delete_connector_with_http_info(request)

    def _delete_connector_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v2/{project_id}/kafka/instances/{instance_id}/delete-connector',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instance_async(self, request):
        """删除指定的实例

        删除指定的实例，释放该实例的所有资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteInstanceResponse`
        """
        return self._delete_instance_with_http_info(request)

    def _delete_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_sink_task_async(self, request):
        """删除单个转储任务

        删除单个转储任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSinkTask
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteSinkTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteSinkTaskResponse`
        """
        return self._delete_sink_task_with_http_info(request)

    def _delete_sink_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSinkTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_available_zones_async(self, request):
        """查询可用区信息

        在创建实例时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableZones
        :type request: :class:`huaweicloudsdkkafka.v2.ListAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListAvailableZonesResponse`
        """
        return self._list_available_zones_with_http_info(request)

    def _list_available_zones_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/available-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailableZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_background_tasks_async(self, request):
        """查询实例的后台任务列表

        查询实例的后台任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackgroundTasks
        :type request: :class:`huaweicloudsdkkafka.v2.ListBackgroundTasksRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListBackgroundTasksResponse`
        """
        return self._list_background_tasks_with_http_info(request)

    def _list_background_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBackgroundTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_engine_products_async(self, request):
        """查询产品规格列表

        查询产品规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEngineProducts
        :type request: :class:`huaweicloudsdkkafka.v2.ListEngineProductsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListEngineProductsResponse`
        """
        return self._list_engine_products_with_http_info(request)

    def _list_engine_products_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{engine}/products',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEngineProductsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_consumer_groups_async(self, request):
        """查询所有消费组

        查询所有消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceConsumerGroups
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupsResponse`
        """
        return self._list_instance_consumer_groups_with_http_info(request)

    def _list_instance_consumer_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceConsumerGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_topics_async(self, request):
        """Kafka实例查询Topic

        该接口用于查询指定Kafka实例的Topic详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceTopics
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstanceTopicsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstanceTopicsResponse`
        """
        return self._list_instance_topics_with_http_info(request)

    def _list_instance_topics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceTopicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_async(self, request):
        """查询所有实例列表

        查询租户的实例列表，支持按照条件查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstancesResponse`
        """
        return self._list_instances_with_http_info(request)

    def _list_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'include_failure' in local_var_params:
            query_params.append(('include_failure', local_var_params['include_failure']))
        if 'exact_match_name' in local_var_params:
            query_params.append(('exact_match_name', local_var_params['exact_match_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_products_async(self, request):
        """查询产品规格列表

        在创建kafka实例时，需要配置订购的产品ID（即product_id），可通过该接口查询产品规格。
        
        例如，要订购按需计费、基准带宽为100MB的kafka实例，可从接口响应消息中，查找Hourly的消息体，然后找到bandwidth为100MB的记录对应的product_id，该product_id的值即是创建上述kafka实例时需要配置的产品ID。
        
        同时，unavailable_zones字段表示资源不足的可用区列表，如果为空，则表示所有可用区都有资源，如果不为空，则表示字段值的可用区没有资源。所以必须确保您购买的资源所在的可用区有资源，不在该字段列表内。
        
        [例如，响应消息中bandwidth字段为1200MB的记录，unavailable_zones字段包含cn-east-2b、cn-east-2a和cn-east-2d，表示在华东-上海2的可用区1、可用区2、可用区3都没有该资源。](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkkafka.v2.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListProductsResponse`
        """
        return self._list_products_with_http_info(request)

    def _list_products_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/products',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProductsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sink_tasks_async(self, request):
        """查询转储任务列表

        查询转储任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSinkTasks
        :type request: :class:`huaweicloudsdkkafka.v2.ListSinkTasksRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListSinkTasksResponse`
        """
        return self._list_sink_tasks_with_http_info(request)

    def _list_sink_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSinkTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_topic_partitions_async(self, request):
        """查询Topic的分区列表

        查询Topic的分区列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopicPartitions
        :type request: :class:`huaweicloudsdkkafka.v2.ListTopicPartitionsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListTopicPartitionsResponse`
        """
        return self._list_topic_partitions_with_http_info(request)

    def _list_topic_partitions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        return self.call_api(
            resource_path='/v2/{project_id}/kafka/instances/{instance_id}/topics/{topic}/partitions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTopicPartitionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_topic_producers_async(self, request):
        """查询Topic的当前生产者列表

        查询Topic的当前生产者列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopicProducers
        :type request: :class:`huaweicloudsdkkafka.v2.ListTopicProducersRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListTopicProducersResponse`
        """
        return self._list_topic_producers_with_http_info(request)

    def _list_topic_producers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        return self.call_api(
            resource_path='/v2/{project_id}/kafka/instances/{instance_id}/topics/{topic}/producers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTopicProducersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_manager_password_async(self, request):
        """重置Manager密码

        重置Manager密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetManagerPassword
        :type request: :class:`huaweicloudsdkkafka.v2.ResetManagerPasswordRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetManagerPasswordResponse`
        """
        return self._reset_manager_password_with_http_info(request)

    def _reset_manager_password_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/kafka-manager-password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetManagerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_message_offset_async(self, request):
        """重置消费组消费进度到指定位置

        Kafka实例不支持在线重置消费进度。在执行重置消费进度之前，必须停止被重置消费组客户端。
        
        停止待重置消费组客户端，然后等待一段时间（即ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG配置的时间，默认为1000毫秒）后，服务端才认为此消费组客户端已下线。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetMessageOffset
        :type request: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetResponse`
        """
        return self._reset_message_offset_with_http_info(request)

    def _reset_message_offset_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/groups/{group}/reset-message-offset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetMessageOffsetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_password_async(self, request):
        """重置密码

        重置密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkkafka.v2.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetPasswordResponse`
        """
        return self._reset_password_with_http_info(request)

    def _reset_password_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_user_passwrod_async(self, request):
        """重置用户密码

        重置用户密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetUserPasswrod
        :type request: :class:`huaweicloudsdkkafka.v2.ResetUserPasswrodRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetUserPasswrodResponse`
        """
        return self._reset_user_passwrod_with_http_info(request)

    def _reset_user_passwrod_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/users/{user_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetUserPasswrodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_engine_instance_async(self, request):
        """实例规格变更

        实例规格变更。[当前通过调用API，只支持按需实例进行实例规格变更。](tag:hws,hws_hk,ctc,cmcc,hws_eu)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeEngineInstance
        :type request: :class:`huaweicloudsdkkafka.v2.ResizeEngineInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResizeEngineInstanceResponse`
        """
        return self._resize_engine_instance_with_http_info(request)

    def _resize_engine_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{engine}/{project_id}/instances/{instance_id}/extend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeEngineInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_instance_async(self, request):
        """实例规格变更

        实例规格变更。[当前通过调用API，只支持按需实例进行实例规格变更。](tag:hws,hws_hk,ctc,cmcc,hws_eu)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkkafka.v2.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResizeInstanceResponse`
        """
        return self._resize_instance_with_http_info(request)

    def _resize_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/extend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_manager_async(self, request):
        """重启Manager

        重启Manager。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartManager
        :type request: :class:`huaweicloudsdkkafka.v2.RestartManagerRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.RestartManagerResponse`
        """
        return self._restart_manager_with_http_info(request)

    def _restart_manager_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/restart-kafka-manager',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartManagerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_background_task_async(self, request):
        """查询后台任务管理中的指定记录

        查询后台任务管理中的指定记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackgroundTask
        :type request: :class:`huaweicloudsdkkafka.v2.ShowBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowBackgroundTaskResponse`
        """
        return self._show_background_task_with_http_info(request)

    def _show_background_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBackgroundTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ces_hierarchy_async(self, request):
        """查询实例在CES的监控层级关系

        查询实例在CES的监控层级关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCesHierarchy
        :type request: :class:`huaweicloudsdkkafka.v2.ShowCesHierarchyRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowCesHierarchyResponse`
        """
        return self._show_ces_hierarchy_with_http_info(request)

    def _show_ces_hierarchy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/ces-hierarchy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCesHierarchyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cluster_async(self, request):
        """查询Kafka集群元数据信息

        查询Kafka集群元数据信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCluster
        :type request: :class:`huaweicloudsdkkafka.v2.ShowClusterRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowClusterResponse`
        """
        return self._show_cluster_with_http_info(request)

    def _show_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/cluster',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_coordinators_async(self, request):
        """查询Kafka实例的协调器信息

        查询Kafka实例的协调器信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoordinators
        :type request: :class:`huaweicloudsdkkafka.v2.ShowCoordinatorsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowCoordinatorsResponse`
        """
        return self._show_coordinators_with_http_info(request)

    def _show_coordinators_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/coordinators',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCoordinatorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_engine_instance_extend_product_info_async(self, request):
        """查询实例的扩容规格列表

        查询实例的扩容规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEngineInstanceExtendProductInfo
        :type request: :class:`huaweicloudsdkkafka.v2.ShowEngineInstanceExtendProductInfoRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowEngineInstanceExtendProductInfoResponse`
        """
        return self._show_engine_instance_extend_product_info_with_http_info(request)

    def _show_engine_instance_extend_product_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{engine}/{project_id}/instances/{instance_id}/extend',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEngineInstanceExtendProductInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_groups_async(self, request):
        """查询消费组信息

        查询消费组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroups
        :type request: :class:`huaweicloudsdkkafka.v2.ShowGroupsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowGroupsResponse`
        """
        return self._show_groups_with_http_info(request)

    def _show_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/groups/{group}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_async(self, request):
        """查询指定实例

        查询指定实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceResponse`
        """
        return self._show_instance_with_http_info(request)

    def _show_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_extend_product_info_async(self, request):
        """查询实例的扩容规格列表

        查询实例的扩容规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceExtendProductInfo
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceExtendProductInfoRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceExtendProductInfoResponse`
        """
        return self._show_instance_extend_product_info_with_http_info(request)

    def _show_instance_extend_product_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/extend',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceExtendProductInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_messages_async(self, request):
        """查询消息

        查询消息的偏移量和消息内容。
        先根据时间戳查询消息的偏移量，再根据偏移量查询消息内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceMessages
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceMessagesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceMessagesResponse`
        """
        return self._show_instance_messages_with_http_info(request)

    def _show_instance_messages_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'topic' in local_var_params:
            query_params.append(('topic', local_var_params['topic']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'download' in local_var_params:
            query_params.append(('download', local_var_params['download']))
        if 'message_offset' in local_var_params:
            query_params.append(('message_offset', local_var_params['message_offset']))
        if 'partition' in local_var_params:
            query_params.append(('partition', local_var_params['partition']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_topic_detail_async(self, request):
        """查询Kafka实例Topic详细信息

        查询Kafka实例Topic详细信息。(单个实例调用不要超过1s一次)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceTopicDetail
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailResponse`
        """
        return self._show_instance_topic_detail_with_http_info(request)

    def _show_instance_topic_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceTopicDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_users_async(self, request):
        """查询用户列表

        查询用户列表。
        
        Kafka实例开启SASL功能时，才支持多用户管理的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceUsers
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceUsersRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceUsersResponse`
        """
        return self._show_instance_users_with_http_info(request)

    def _show_instance_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_kafka_project_tags_async(self, request):
        """查询项目标签

        查询项目标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaProjectTags
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaProjectTagsResponse`
        """
        return self._show_kafka_project_tags_with_http_info(request)

    def _show_kafka_project_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/kafka/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowKafkaProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_kafka_tags_async(self, request):
        """查询实例标签

        查询实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaTags
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaTagsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaTagsResponse`
        """
        return self._show_kafka_tags_with_http_info(request)

    def _show_kafka_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/kafka/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowKafkaTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_kafka_topic_partition_diskusage_async(self, request):
        """查询topic的磁盘存储情况

        查询topic在Broker上磁盘占用情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaTopicPartitionDiskusage
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaTopicPartitionDiskusageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaTopicPartitionDiskusageResponse`
        """
        return self._show_kafka_topic_partition_diskusage_with_http_info(request)

    def _show_kafka_topic_partition_diskusage_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'min_size' in local_var_params:
            query_params.append(('minSize', local_var_params['min_size']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))
        if 'percentage' in local_var_params:
            query_params.append(('percentage', local_var_params['percentage']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics/diskusage',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowKafkaTopicPartitionDiskusageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_maintain_windows_async(self, request):
        """查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMaintainWindows
        :type request: :class:`huaweicloudsdkkafka.v2.ShowMaintainWindowsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowMaintainWindowsResponse`
        """
        return self._show_maintain_windows_with_http_info(request)

    def _show_maintain_windows_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/instances/maintain-windows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMaintainWindowsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_messages_async(self, request):
        """查询分区指定时间段的消息

        查询分区指定时间段的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMessages
        :type request: :class:`huaweicloudsdkkafka.v2.ShowMessagesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowMessagesResponse`
        """
        return self._show_messages_with_http_info(request)

    def _show_messages_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'partition' in local_var_params:
            query_params.append(('partition', local_var_params['partition']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_partition_beginning_message_async(self, request):
        """查询分区最早消息的位置

        查询分区最早消息的位置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartitionBeginningMessage
        :type request: :class:`huaweicloudsdkkafka.v2.ShowPartitionBeginningMessageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowPartitionBeginningMessageResponse`
        """
        return self._show_partition_beginning_message_with_http_info(request)

    def _show_partition_beginning_message_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']
        if 'partition' in local_var_params:
            path_params['partition'] = local_var_params['partition']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/beginning-message',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPartitionBeginningMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_partition_end_message_async(self, request):
        """查询分区最新消息的位置

        查询分区最新消息的位置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartitionEndMessage
        :type request: :class:`huaweicloudsdkkafka.v2.ShowPartitionEndMessageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowPartitionEndMessageResponse`
        """
        return self._show_partition_end_message_with_http_info(request)

    def _show_partition_end_message_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']
        if 'partition' in local_var_params:
            path_params['partition'] = local_var_params['partition']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/end-message',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPartitionEndMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_partition_message_async(self, request):
        """查询分区指定偏移量的消息

        查询分区指定偏移量的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartitionMessage
        :type request: :class:`huaweicloudsdkkafka.v2.ShowPartitionMessageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowPartitionMessageResponse`
        """
        return self._show_partition_message_with_http_info(request)

    def _show_partition_message_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']
        if 'partition' in local_var_params:
            path_params['partition'] = local_var_params['partition']

        query_params = []
        if 'message_offset' in local_var_params:
            query_params.append(('message_offset', local_var_params['message_offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/message',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPartitionMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sink_task_detail_async(self, request):
        """查询单个转储任务

        查询单个转储任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSinkTaskDetail
        :type request: :class:`huaweicloudsdkkafka.v2.ShowSinkTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowSinkTaskDetailResponse`
        """
        return self._show_sink_task_detail_with_http_info(request)

    def _show_sink_task_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'topic_info' in local_var_params:
            query_params.append(('topic-info', local_var_params['topic_info']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSinkTaskDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_topic_access_policy_async(self, request):
        """查询用户权限

        查询用户权限。
        
        Kafka实例开启SASL功能时，才支持多用户管理的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTopicAccessPolicy
        :type request: :class:`huaweicloudsdkkafka.v2.ShowTopicAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowTopicAccessPolicyResponse`
        """
        return self._show_topic_access_policy_with_http_info(request)

    def _show_topic_access_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic_name' in local_var_params:
            path_params['topic_name'] = local_var_params['topic_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/instances/{instance_id}/topics/{topic_name}/accesspolicy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTopicAccessPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_async(self, request):
        """修改实例信息

        修改实例信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceResponse`
        """
        return self._update_instance_with_http_info(request)

    def _update_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_auto_create_topic_async(self, request):
        """开启或关闭实例自动创建topic功能

        开启或关闭实例自动创建topic功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceAutoCreateTopic
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceAutoCreateTopicRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceAutoCreateTopicResponse`
        """
        return self._update_instance_auto_create_topic_with_http_info(request)

    def _update_instance_auto_create_topic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/autotopic',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceAutoCreateTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_consumer_group_async(self, request):
        """编辑消费组

        编辑消费组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceConsumerGroup
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceConsumerGroupResponse`
        """
        return self._update_instance_consumer_group_with_http_info(request)

    def _update_instance_consumer_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

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
            resource_path='/v2/{engine}/{project_id}/instances/{instance_id}/groups/{group}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceConsumerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_cross_vpc_ip_async(self, request):
        """修改实例跨VPC访问的内网IP

        修改实例跨VPC访问的内网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceCrossVpcIp
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceCrossVpcIpRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceCrossVpcIpResponse`
        """
        return self._update_instance_cross_vpc_ip_with_http_info(request)

    def _update_instance_cross_vpc_ip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/crossvpc/modify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceCrossVpcIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_topic_async(self, request):
        """修改Kafka实例Topic

        修改Kafka实例Topic
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceTopic
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceTopicResponse`
        """
        return self._update_instance_topic_with_http_info(request)

    def _update_instance_topic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_user_async(self, request):
        """修改用户参数

        修改用户参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceUser
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceUserRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceUserResponse`
        """
        return self._update_instance_user_with_http_info(request)

    def _update_instance_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{engine}/{project_id}/instances/{instance_id}/users/{user_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_sink_task_quota_async(self, request):
        """修改转储任务的配额

        修改转储任务的配额。
        
        2022年9月前创建的实例支持调用此接口新增转储任务配额，2022年9月及以后创建的实例，转储任务配额默认为最大值，由于转储任务配额不支持减少，调用此接口修改转储任务配额会报错。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSinkTaskQuota
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateSinkTaskQuotaRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateSinkTaskQuotaResponse`
        """
        return self._update_sink_task_quota_with_http_info(request)

    def _update_sink_task_quota_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSinkTaskQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_topic_access_policy_async(self, request):
        """设置用户权限

        设置用户权限。
        
        Kafka实例开启SASL功能时，才支持多用户管理的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTopicAccessPolicy
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateTopicAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateTopicAccessPolicyResponse`
        """
        return self._update_topic_access_policy_with_http_info(request)

    def _update_topic_access_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/instances/{instance_id}/topics/accesspolicy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTopicAccessPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_topic_replica_async(self, request):
        """修改Kafka实例Topic分区的副本

        修改Kafka实例Topic分区的副本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTopicReplica
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateTopicReplicaRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateTopicReplicaResponse`
        """
        return self._update_topic_replica_with_http_info(request)

    def _update_topic_replica_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/replicas-reassignment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTopicReplicaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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

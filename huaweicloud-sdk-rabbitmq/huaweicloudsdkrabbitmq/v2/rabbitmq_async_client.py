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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkrabbitmq'")


class RabbitMQAsyncClient(Client):
    def __init__(self):
        super(RabbitMQAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrabbitmq.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "RabbitMQAsyncClient":
                raise TypeError("client type error, support client type is RabbitMQAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_or_delete_rabbit_mq_tag_async(self, request):
        r"""批量添加或删除实例标签

        批量添加或删除实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOrDeleteRabbitMqTag
        :type request: :class:`huaweicloudsdkrabbitmq.v2.BatchCreateOrDeleteRabbitMqTagRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.BatchCreateOrDeleteRabbitMqTagResponse`
        """
        http_info = self._batch_create_or_delete_rabbit_mq_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_create_or_delete_rabbit_mq_tag_async_invoker(self, request):
        http_info = self._batch_create_or_delete_rabbit_mq_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_or_delete_rabbit_mq_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/rabbitmq/{instance_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOrDeleteRabbitMqTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def batch_restart_or_delete_instances_async(self, request):
        r"""批量删除实例

        批量删除实例。
        
        实例删除后，实例中原有的数据将被删除，且没有备份，请谨慎操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRestartOrDeleteInstances
        :type request: :class:`huaweicloudsdkrabbitmq.v2.BatchRestartOrDeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.BatchRestartOrDeleteInstancesResponse`
        """
        http_info = self._batch_restart_or_delete_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_restart_or_delete_instances_async_invoker(self, request):
        http_info = self._batch_restart_or_delete_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_restart_or_delete_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRestartOrDeleteInstancesResponse"
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

    def create_post_paid_instance_async(self, request):
        r"""创建实例(按需)

        创建实例，该接口创建的实例为按需计费的方式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostPaidInstance
        :type request: :class:`huaweicloudsdkrabbitmq.v2.CreatePostPaidInstanceRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.CreatePostPaidInstanceResponse`
        """
        http_info = self._create_post_paid_instance_http_info(request)
        return self._call_api(**http_info)

    def create_post_paid_instance_async_invoker(self, request):
        http_info = self._create_post_paid_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_post_paid_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostPaidInstanceResponse"
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

    def create_post_paid_instance_by_engine_async(self, request):
        r"""创建实例

        创建实例[，该接口支持创建按需[和包周期](tag:hws,hws_eu,hws_hk,ctc,cmcc)计费方式的实例](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,cmcc,sbc)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostPaidInstanceByEngine
        :type request: :class:`huaweicloudsdkrabbitmq.v2.CreatePostPaidInstanceByEngineRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.CreatePostPaidInstanceByEngineResponse`
        """
        http_info = self._create_post_paid_instance_by_engine_http_info(request)
        return self._call_api(**http_info)

    def create_post_paid_instance_by_engine_async_invoker(self, request):
        http_info = self._create_post_paid_instance_by_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_post_paid_instance_by_engine_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostPaidInstanceByEngineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']

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

    def create_user_async(self, request):
        r"""创建用户

        创建用户（仅AMQP版本支持）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkrabbitmq.v2.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.CreateUserResponse`
        """
        http_info = self._create_user_http_info(request)
        return self._call_api(**http_info)

    def create_user_async_invoker(self, request):
        http_info = self._create_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_background_task_async(self, request):
        r"""删除后台任务管理中的指定记录

        删除后台任务管理中的指定记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackgroundTask
        :type request: :class:`huaweicloudsdkrabbitmq.v2.DeleteBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.DeleteBackgroundTaskResponse`
        """
        http_info = self._delete_background_task_http_info(request)
        return self._call_api(**http_info)

    def delete_background_task_async_invoker(self, request):
        http_info = self._delete_background_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_background_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackgroundTaskResponse"
            }

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

    def delete_instance_async(self, request):
        r"""删除指定实例

        删除指定实例，释放该实例的所有资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkrabbitmq.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_async_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_user_async(self, request):
        r"""删除用户

        删除用户（仅AMQP版本支持）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkrabbitmq.v2.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_async_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_user_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserResponse"
            }

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

    def enable_dns_async(self, request):
        r"""开启RabbitMQ实例域名访问能力

        开启RabbitMQ实例域名访问功能后，客户端可以通过域名连接RabbitMQ实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDns
        :type request: :class:`huaweicloudsdkrabbitmq.v2.EnableDnsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.EnableDnsResponse`
        """
        http_info = self._enable_dns_http_info(request)
        return self._call_api(**http_info)

    def enable_dns_async_invoker(self, request):
        http_info = self._enable_dns_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_dns_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/rabbitmq/instances/{instance_id}/dns",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDnsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_available_zones_async(self, request):
        r"""查询可用区信息

        在创建实例时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableZones
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListAvailableZonesResponse`
        """
        http_info = self._list_available_zones_http_info(request)
        return self._call_api(**http_info)

    def list_available_zones_async_invoker(self, request):
        http_info = self._list_available_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_available_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/available-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableZonesResponse"
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

    def list_background_tasks_async(self, request):
        r"""查询实例的后台任务列表

        查询实例的后台任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackgroundTasks
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListBackgroundTasksRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListBackgroundTasksResponse`
        """
        http_info = self._list_background_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_background_tasks_async_invoker(self, request):
        http_info = self._list_background_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_background_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackgroundTasksResponse"
            }

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

    def list_engine_products_async(self, request):
        r"""查询产品规格列表

        查询产品规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEngineProducts
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListEngineProductsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListEngineProductsResponse`
        """
        http_info = self._list_engine_products_http_info(request)
        return self._call_api(**http_info)

    def list_engine_products_async_invoker(self, request):
        http_info = self._list_engine_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_engine_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListEngineProductsResponse"
            }

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

    def list_instances_details_async(self, request):
        r"""查询所有实例列表

        查询租户的实例列表，支持按照条件查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesDetails
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListInstancesDetailsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListInstancesDetailsResponse`
        """
        http_info = self._list_instances_details_http_info(request)
        return self._call_api(**http_info)

    def list_instances_details_async_invoker(self, request):
        http_info = self._list_instances_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesDetailsResponse"
            }

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

    def list_plugins_async(self, request):
        r"""查询插件列表

        查询插件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlugins
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListPluginsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListPluginsResponse`
        """
        http_info = self._list_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_plugins_async_invoker(self, request):
        http_info = self._list_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/rabbitmq/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_products_async(self, request):
        r"""查询产品规格列表

        在创建实例时，需要配置订购的产品ID（即product_id），可通过该接口查询产品规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListProductsResponse`
        """
        http_info = self._list_products_http_info(request)
        return self._call_api(**http_info)

    def list_products_async_invoker(self, request):
        http_info = self._list_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

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

    def list_user_async(self, request):
        r"""查询用户列表

        查询用户列表（仅AMQP版本支持）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUser
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListUserRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListUserResponse`
        """
        http_info = self._list_user_http_info(request)
        return self._call_api(**http_info)

    def list_user_async_invoker(self, request):
        http_info = self._list_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserResponse"
            }

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

    def reset_password_async(self, request):
        r"""重置密码

        重置密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ResetPasswordResponse`
        """
        http_info = self._reset_password_http_info(request)
        return self._call_api(**http_info)

    def reset_password_async_invoker(self, request):
        http_info = self._reset_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def resize_engine_instance_async(self, request):
        r"""新规格实例的规格变更

        实例规格变更。
        
        [**当前通过调用API，只支持按需实例进行实例规格变更。**](tag:hws,hws_hk,ctc,cmcc,hws_eu)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeEngineInstance
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ResizeEngineInstanceRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ResizeEngineInstanceResponse`
        """
        http_info = self._resize_engine_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_engine_instance_async_invoker(self, request):
        http_info = self._resize_engine_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_engine_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeEngineInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']

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

    def resize_instance_async(self, request):
        r"""实例规格变更

        实例规格变更。
        
        [**当前通过调用API，只支持按需实例进行实例规格变更。**](tag:hws,hws_hk,ctc,cmcc,hws_eu)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ResizeInstanceResponse`
        """
        http_info = self._resize_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_instance_async_invoker(self, request):
        http_info = self._resize_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_background_task_async(self, request):
        r"""查询后台任务管理中的指定记录

        查询后台任务管理中的指定记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackgroundTask
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowBackgroundTaskResponse`
        """
        http_info = self._show_background_task_http_info(request)
        return self._call_api(**http_info)

    def show_background_task_async_invoker(self, request):
        http_info = self._show_background_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_background_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackgroundTaskResponse"
            }

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

    def show_ces_hierarchy_async(self, request):
        r"""查询实例在CES的监控层级关系

        查询实例在CES的监控层级关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCesHierarchy
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowCesHierarchyRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowCesHierarchyResponse`
        """
        http_info = self._show_ces_hierarchy_http_info(request)
        return self._call_api(**http_info)

    def show_ces_hierarchy_async_invoker(self, request):
        http_info = self._show_ces_hierarchy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ces_hierarchy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/ces-hierarchy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCesHierarchyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_engine_instance_extend_product_info_async(self, request):
        r"""查询新规格可扩容规格列表

        查询新规格实例可扩容列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEngineInstanceExtendProductInfo
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowEngineInstanceExtendProductInfoRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowEngineInstanceExtendProductInfoResponse`
        """
        http_info = self._show_engine_instance_extend_product_info_http_info(request)
        return self._call_api(**http_info)

    def show_engine_instance_extend_product_info_async_invoker(self, request):
        http_info = self._show_engine_instance_extend_product_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_engine_instance_extend_product_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEngineInstanceExtendProductInfoResponse"
            }

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

    def show_instance_async(self, request):
        r"""查询指定实例

        查询指定实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_async_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_instance_extend_product_info_async(self, request):
        r"""查询可扩容规格列表

        查询可扩容规格列表。
        
        RabbtiMQ只支持只增加节点数的扩容方式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceExtendProductInfo
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowInstanceExtendProductInfoRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowInstanceExtendProductInfoResponse`
        """
        http_info = self._show_instance_extend_product_info_http_info(request)
        return self._call_api(**http_info)

    def show_instance_extend_product_info_async_invoker(self, request):
        http_info = self._show_instance_extend_product_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_extend_product_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceExtendProductInfoResponse"
            }

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

    def show_maintain_windows_async(self, request):
        r"""查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMaintainWindows
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowMaintainWindowsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowMaintainWindowsResponse`
        """
        http_info = self._show_maintain_windows_http_info(request)
        return self._call_api(**http_info)

    def show_maintain_windows_async_invoker(self, request):
        http_info = self._show_maintain_windows_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_maintain_windows_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances/maintain-windows",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMaintainWindowsResponse"
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

    def show_quotas_async(self, request):
        r"""查看租户配额

        查询租户最大可以创建的实例个数和已创建的实例个数，以及每个实例最大可以创建标签的个数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_async_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasResponse"
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

    def show_rabbit_mq_product_cores_async(self, request):
        r"""查询RabbitMQ产品规格核数

        查询RabbitMQ产品规格核数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRabbitMqProductCores
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowRabbitMqProductCoresRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowRabbitMqProductCoresResponse`
        """
        http_info = self._show_rabbit_mq_product_cores_http_info(request)
        return self._call_api(**http_info)

    def show_rabbit_mq_product_cores_async_invoker(self, request):
        http_info = self._show_rabbit_mq_product_cores_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rabbit_mq_product_cores_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rabbitmq/products/cores",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRabbitMqProductCoresResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))

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

    def show_rabbit_mq_project_tags_async(self, request):
        r"""查询项目标签

        查询项目标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRabbitMqProjectTags
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowRabbitMqProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowRabbitMqProjectTagsResponse`
        """
        http_info = self._show_rabbit_mq_project_tags_http_info(request)
        return self._call_api(**http_info)

    def show_rabbit_mq_project_tags_async_invoker(self, request):
        http_info = self._show_rabbit_mq_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rabbit_mq_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/rabbitmq/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRabbitMqProjectTagsResponse"
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

    def show_rabbit_mq_tags_async(self, request):
        r"""查询实例标签

        查询实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRabbitMqTags
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowRabbitMqTagsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowRabbitMqTagsResponse`
        """
        http_info = self._show_rabbit_mq_tags_http_info(request)
        return self._call_api(**http_info)

    def show_rabbit_mq_tags_async_invoker(self, request):
        http_info = self._show_rabbit_mq_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rabbit_mq_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/rabbitmq/{instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRabbitMqTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_instance_async(self, request):
        r"""修改实例信息

        修改实例的名称和描述信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkrabbitmq.v2.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.UpdateInstanceResponse`
        """
        http_info = self._update_instance_http_info(request)
        return self._call_api(**http_info)

    def update_instance_async_invoker(self, request):
        http_info = self._update_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_plugins_async(self, request):
        r"""开启或关闭插件

        开启或关闭插件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlugins
        :type request: :class:`huaweicloudsdkrabbitmq.v2.UpdatePluginsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.UpdatePluginsResponse`
        """
        http_info = self._update_plugins_http_info(request)
        return self._call_api(**http_info)

    def update_plugins_async_invoker(self, request):
        http_info = self._update_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_plugins_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/rabbitmq/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_user_async(self, request):
        r"""修改用户参数

        修改用户参数（仅AMQP版本支持）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkrabbitmq.v2.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_async_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserResponse"
            }

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

    def create_binding_async(self, request):
        r"""添加绑定

        添加绑定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBinding
        :type request: :class:`huaweicloudsdkrabbitmq.v2.CreateBindingRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.CreateBindingResponse`
        """
        http_info = self._create_binding_http_info(request)
        return self._call_api(**http_info)

    def create_binding_async_invoker(self, request):
        http_info = self._create_binding_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_binding_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/exchanges/{exchange}/binding",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBindingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']
        if 'exchange' in local_var_params:
            path_params['exchange'] = local_var_params['exchange']

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

    def delete_binding_async(self, request):
        r"""删除绑定

        删除绑定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBinding
        :type request: :class:`huaweicloudsdkrabbitmq.v2.DeleteBindingRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.DeleteBindingResponse`
        """
        http_info = self._delete_binding_http_info(request)
        return self._call_api(**http_info)

    def delete_binding_async_invoker(self, request):
        http_info = self._delete_binding_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_binding_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/exchanges/{exchange}/destination-type/{destination_type}/destination/{destination}/properties-key/{properties_key}/unbinding",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBindingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']
        if 'exchange' in local_var_params:
            path_params['exchange'] = local_var_params['exchange']
        if 'destination_type' in local_var_params:
            path_params['destination_type'] = local_var_params['destination_type']
        if 'destination' in local_var_params:
            path_params['destination'] = local_var_params['destination']
        if 'properties_key' in local_var_params:
            path_params['properties_key'] = local_var_params['properties_key']

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

    def list_bindings_async(self, request):
        r"""查询Exchange绑定信息列表

        查询Exchange绑定信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBindings
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListBindingsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListBindingsResponse`
        """
        http_info = self._list_bindings_http_info(request)
        return self._call_api(**http_info)

    def list_bindings_async_invoker(self, request):
        http_info = self._list_bindings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bindings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/exchanges/{exchange}/binding",
            "request_type": request.__class__.__name__,
            "response_type": "ListBindingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']
        if 'exchange' in local_var_params:
            path_params['exchange'] = local_var_params['exchange']

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

    def batch_delete_exchanges_async(self, request):
        r"""批量删除指定Exchange

        批量删除指定Exchange。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteExchanges
        :type request: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteExchangesRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteExchangesResponse`
        """
        http_info = self._batch_delete_exchanges_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_exchanges_async_invoker(self, request):
        http_info = self._batch_delete_exchanges_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_exchanges_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/exchanges",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteExchangesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']

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

    def create_exchange_async(self, request):
        r"""创建Exchange

        创建Exchange。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateExchange
        :type request: :class:`huaweicloudsdkrabbitmq.v2.CreateExchangeRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.CreateExchangeResponse`
        """
        http_info = self._create_exchange_http_info(request)
        return self._call_api(**http_info)

    def create_exchange_async_invoker(self, request):
        http_info = self._create_exchange_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_exchange_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/exchanges",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExchangeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']

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

    def list_exchanges_async(self, request):
        r"""查询Exchange列表

        查询Exchange列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExchanges
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListExchangesRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListExchangesResponse`
        """
        http_info = self._list_exchanges_http_info(request)
        return self._call_api(**http_info)

    def list_exchanges_async_invoker(self, request):
        http_info = self._list_exchanges_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_exchanges_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/exchanges",
            "request_type": request.__class__.__name__,
            "response_type": "ListExchangesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']

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

    def batch_delete_queues_async(self, request):
        r"""批量删除指定Queue

        批量删除指定Queue。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteQueues
        :type request: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteQueuesRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteQueuesResponse`
        """
        http_info = self._batch_delete_queues_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_queues_async_invoker(self, request):
        http_info = self._batch_delete_queues_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_queues_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/queues",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteQueuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']

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

    def create_queue_async(self, request):
        r"""创建Queue

        创建Queue。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateQueue
        :type request: :class:`huaweicloudsdkrabbitmq.v2.CreateQueueRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.CreateQueueResponse`
        """
        http_info = self._create_queue_http_info(request)
        return self._call_api(**http_info)

    def create_queue_async_invoker(self, request):
        http_info = self._create_queue_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_queue_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/queues",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']

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

    def delete_queue_info_async(self, request):
        r"""清空Queue消息

        清空Queue消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteQueueInfo
        :type request: :class:`huaweicloudsdkrabbitmq.v2.DeleteQueueInfoRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.DeleteQueueInfoResponse`
        """
        http_info = self._delete_queue_info_http_info(request)
        return self._call_api(**http_info)

    def delete_queue_info_async_invoker(self, request):
        http_info = self._delete_queue_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_queue_info_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/queues/{queue}/contents",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteQueueInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']
        if 'queue' in local_var_params:
            path_params['queue'] = local_var_params['queue']

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

    def list_queues_async(self, request):
        r"""查询所属Vhost下Queue的列表

        查询所属Vhost下Queue的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQueues
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListQueuesRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListQueuesResponse`
        """
        http_info = self._list_queues_http_info(request)
        return self._call_api(**http_info)

    def list_queues_async_invoker(self, request):
        http_info = self._list_queues_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_queues_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/queues",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']

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

    def show_queue_details_async(self, request):
        r"""查询指定Queue详情

        查询指定Queue详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQueueDetails
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ShowQueueDetailsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ShowQueueDetailsResponse`
        """
        http_info = self._show_queue_details_http_info(request)
        return self._call_api(**http_info)

    def show_queue_details_async_invoker(self, request):
        http_info = self._show_queue_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_queue_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts/{vhost}/queues/{queue}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQueueDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vhost' in local_var_params:
            path_params['vhost'] = local_var_params['vhost']
        if 'queue' in local_var_params:
            path_params['queue'] = local_var_params['queue']

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

    def batch_delete_vhosts_async(self, request):
        r"""批量删除指定Vhost

        批量删除指定Vhost。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteVhosts
        :type request: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteVhostsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteVhostsResponse`
        """
        http_info = self._batch_delete_vhosts_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_vhosts_async_invoker(self, request):
        http_info = self._batch_delete_vhosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_vhosts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteVhostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_vhost_async(self, request):
        r"""创建Vhost

        创建Vhost。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVhost
        :type request: :class:`huaweicloudsdkrabbitmq.v2.CreateVhostRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.CreateVhostResponse`
        """
        http_info = self._create_vhost_http_info(request)
        return self._call_api(**http_info)

    def create_vhost_async_invoker(self, request):
        http_info = self._create_vhost_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vhost_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVhostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_vhosts_async(self, request):
        r"""查询Vhost列表

        查询Vhost列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVhosts
        :type request: :class:`huaweicloudsdkrabbitmq.v2.ListVhostsRequest`
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListVhostsResponse`
        """
        http_info = self._list_vhosts_http_info(request)
        return self._call_api(**http_info)

    def list_vhosts_async_invoker(self, request):
        http_info = self._list_vhosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vhosts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rabbitmq/{project_id}/instances/{instance_id}/vhosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListVhostsResponse"
            }

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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkiotda'")


class IoTDAClient(Client):
    def __init__(self):
        super(IoTDAClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiotda.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "BasicCredentials,IoTDACredentials")
        else:
            if clazz.__name__ != "IoTDAClient":
                raise TypeError("client type error, support client type is IoTDAClient")
            client_builder = ClientBuilder(clazz, "BasicCredentials,IoTDACredentials")

        client_builder._with_derived_auth_service_name("iotdm")

        return client_builder

    def create_access_code(self, request):
        r"""生成接入凭证

        接入凭证是用于客户端使用AMQP等协议与平台建链的一个认证凭据。只保留一条记录，如果重复调用只会重置接入凭证，使得之前的失效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccessCode
        :type request: :class:`huaweicloudsdkiotda.v5.CreateAccessCodeRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateAccessCodeResponse`
        """
        http_info = self._create_access_code_http_info(request)
        return self._call_api(**http_info)

    def create_access_code_invoker(self, request):
        http_info = self._create_access_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_access_code_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/auth/accesscode",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccessCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def add_queue(self, request):
        r"""创建AMQP队列

        应用服务器可调用此接口在物联网平台创建一个AMQP队列。每个租户只能创建100个队列，若超过规格，则创建失败，若队列名称与已有的队列名称相同，则创建失败。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddQueue
        :type request: :class:`huaweicloudsdkiotda.v5.AddQueueRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddQueueResponse`
        """
        http_info = self._add_queue_http_info(request)
        return self._call_api(**http_info)

    def add_queue_invoker(self, request):
        http_info = self._add_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_queue_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/amqp-queues",
            "request_type": request.__class__.__name__,
            "response_type": "AddQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def batch_show_queue(self, request):
        r"""查询AMQP列表

        应用服务器可调用此接口查询物联网平台中的AMQP队列信息列表。可通过队列名称作模糊查询，支持分页。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowQueue
        :type request: :class:`huaweicloudsdkiotda.v5.BatchShowQueueRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.BatchShowQueueResponse`
        """
        http_info = self._batch_show_queue_http_info(request)
        return self._call_api(**http_info)

    def batch_show_queue_invoker(self, request):
        http_info = self._batch_show_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_queue_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/amqp-queues",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'queue_name' in local_var_params:
            query_params.append(('queue_name', local_var_params['queue_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_queue(self, request):
        r"""删除AMQP队列

        应用服务器可调用此接口在物联网平台上删除指定AMQP队列。若当前队列正在使用，则会删除失败。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteQueue
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteQueueRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteQueueResponse`
        """
        http_info = self._delete_queue_http_info(request)
        return self._call_api(**http_info)

    def delete_queue_invoker(self, request):
        http_info = self._delete_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_queue_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/amqp-queues/{queue_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_queue(self, request):
        r"""查询单个AMQP队列

        应用服务器可调用此接口查询物联网平台中指定队列的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQueue
        :type request: :class:`huaweicloudsdkiotda.v5.ShowQueueRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowQueueResponse`
        """
        http_info = self._show_queue_http_info(request)
        return self._call_api(**http_info)

    def show_queue_invoker(self, request):
        http_info = self._show_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_queue_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/amqp-queues/{queue_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def add_application(self, request):
        r"""创建资源空间

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口创建资源空间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddApplication
        :type request: :class:`huaweicloudsdkiotda.v5.AddApplicationRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddApplicationResponse`
        """
        http_info = self._add_application_http_info(request)
        return self._call_api(**http_info)

    def add_application_invoker(self, request):
        http_info = self._add_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_application_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "AddApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_application(self, request):
        r"""删除资源空间

        删除指定资源空间。删除资源空间属于高危操作，删除资源空间后，该空间下的产品、设备等资源将不可用，请谨慎操作！
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteApplicationResponse`
        """
        http_info = self._delete_application_http_info(request)
        return self._call_api(**http_info)

    def delete_application_invoker(self, request):
        http_info = self._delete_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_application(self, request):
        r"""查询资源空间

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口查询指定资源空间详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplication
        :type request: :class:`huaweicloudsdkiotda.v5.ShowApplicationRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowApplicationResponse`
        """
        http_info = self._show_application_http_info(request)
        return self._call_api(**http_info)

    def show_application_invoker(self, request):
        http_info = self._show_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_application_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_applications(self, request):
        r"""查询资源空间列表

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口查询资源空间列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplications
        :type request: :class:`huaweicloudsdkiotda.v5.ShowApplicationsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowApplicationsResponse`
        """
        http_info = self._show_applications_http_info(request)
        return self._call_api(**http_info)

    def show_applications_invoker(self, request):
        http_info = self._show_applications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_applications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'default_app' in local_var_params:
            query_params.append(('default_app', local_var_params['default_app']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_application(self, request):
        r"""更新资源空间

        应用服务器可以调用此接口更新资源空间的名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplication
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateApplicationRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateApplicationResponse`
        """
        http_info = self._update_application_http_info(request)
        return self._call_api(**http_info)

    def update_application_invoker(self, request):
        http_info = self._update_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def count_async_history_commands(self, request):
        r"""统计设备下的历史命令总数

        统计设备下的历史命令总数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountAsyncHistoryCommands
        :type request: :class:`huaweicloudsdkiotda.v5.CountAsyncHistoryCommandsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CountAsyncHistoryCommandsResponse`
        """
        http_info = self._count_async_history_commands_http_info(request)
        return self._call_api(**http_info)

    def count_async_history_commands_invoker(self, request):
        http_info = self._count_async_history_commands_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_async_history_commands_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/async-commands-history/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountAsyncHistoryCommandsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'command_name' in local_var_params:
            query_params.append(('command_name', local_var_params['command_name']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_async_command(self, request):
        r"""下发异步设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发异步命令，以实现对设备的控制。平台负责将命令发送给设备，并将设备执行命令结果异步通知应用服务器。 命令执行结果支持灵活的数据流转，应用服务器通过调用物联网平台的创建规则触发条件（Resource:device.command.status，Event:update）、创建规则动作并激活规则后，当命令状态变更时，物联网平台会根据规则将结果发送到规则指定的服务器，如用户自定义的HTTP服务器，AMQP服务器，以及华为云的其他储存服务器等, 详情参考[[设备命令状态变更通知](https://support.huaweicloud.com/api-iothub/iot_06_v5_01212.html)](tag:hws)[[设备命令状态变更通知](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_01212.html)](tag:hws_hk)。
        注意：
        - 此接口适用于NB设备异步命令下发，暂不支持其他协议类型设备命令下发。
        - 此接口仅支持单个设备异步命令下发，如需多个设备异步命令下发，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAsyncCommand
        :type request: :class:`huaweicloudsdkiotda.v5.CreateAsyncCommandRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateAsyncCommandResponse`
        """
        http_info = self._create_async_command_http_info(request)
        return self._call_api(**http_info)

    def create_async_command_invoker(self, request):
        http_info = self._create_async_command_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_async_command_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/async-commands",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAsyncCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_async_commands(self, request):
        r"""查询设备下队列中的命令

        查询设备下队列中的命令（处理中的命令），包含PENDING、SENT、DELIVERED三种状态，注意：DELIVERED状态的命令经过系统设定的一段时间（具体以系统配置为准）仍然没有更新，就会从队列中移除，变为历史命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAsyncCommands
        :type request: :class:`huaweicloudsdkiotda.v5.ListAsyncCommandsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListAsyncCommandsResponse`
        """
        http_info = self._list_async_commands_http_info(request)
        return self._call_api(**http_info)

    def list_async_commands_invoker(self, request):
        http_info = self._list_async_commands_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_async_commands_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/async-commands",
            "request_type": request.__class__.__name__,
            "response_type": "ListAsyncCommandsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'command_name' in local_var_params:
            query_params.append(('command_name', local_var_params['command_name']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_async_history_commands(self, request):
        r"""查询设备下的历史命令

        查询设备下发的历史异步命令，包含EXPIRED、SUCCESSFUL、FAILED、TIMEOUT、DELIVERED五种状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAsyncHistoryCommands
        :type request: :class:`huaweicloudsdkiotda.v5.ListAsyncHistoryCommandsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListAsyncHistoryCommandsResponse`
        """
        http_info = self._list_async_history_commands_http_info(request)
        return self._call_api(**http_info)

    def list_async_history_commands_invoker(self, request):
        http_info = self._list_async_history_commands_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_async_history_commands_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/async-commands-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListAsyncHistoryCommandsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'command_name' in local_var_params:
            query_params.append(('command_name', local_var_params['command_name']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_async_device_command(self, request):
        r"""查询指定id的命令

        物联网平台可查询指定id的命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAsyncDeviceCommand
        :type request: :class:`huaweicloudsdkiotda.v5.ShowAsyncDeviceCommandRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowAsyncDeviceCommandResponse`
        """
        http_info = self._show_async_device_command_http_info(request)
        return self._call_api(**http_info)

    def show_async_device_command_invoker(self, request):
        http_info = self._show_async_device_command_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_async_device_command_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/async-commands/{command_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAsyncDeviceCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_routing_backlog_policy(self, request):
        r"""新建数据流转积压策略

        应用服务器可调用此接口在物联网平台创建数据流转积压策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRoutingBacklogPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.CreateRoutingBacklogPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateRoutingBacklogPolicyResponse`
        """
        http_info = self._create_routing_backlog_policy_http_info(request)
        return self._call_api(**http_info)

    def create_routing_backlog_policy_invoker(self, request):
        http_info = self._create_routing_backlog_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_routing_backlog_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/routing-rule/backlog-policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRoutingBacklogPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_routing_backlog_policy(self, request):
        r"""删除数据流转积压策略

        应用服务器可调用此接口在物联网平台删除指定数据流转积压策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRoutingBacklogPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteRoutingBacklogPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteRoutingBacklogPolicyResponse`
        """
        http_info = self._delete_routing_backlog_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_routing_backlog_policy_invoker(self, request):
        http_info = self._delete_routing_backlog_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_routing_backlog_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/routing-rule/backlog-policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRoutingBacklogPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_routing_backlog_policy(self, request):
        r"""查询数据流转积压策略列表

        应用服务器可调用此接口查询在物联网平台设置的数据流转积压策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRoutingBacklogPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.ListRoutingBacklogPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListRoutingBacklogPolicyResponse`
        """
        http_info = self._list_routing_backlog_policy_http_info(request)
        return self._call_api(**http_info)

    def list_routing_backlog_policy_invoker(self, request):
        http_info = self._list_routing_backlog_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_routing_backlog_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/routing-rule/backlog-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListRoutingBacklogPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_routing_backlog_policy(self, request):
        r"""查询数据流转积压策略

        应用服务器可调用此接口在物联网平台查询指定数据流转积压策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRoutingBacklogPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.ShowRoutingBacklogPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowRoutingBacklogPolicyResponse`
        """
        http_info = self._show_routing_backlog_policy_http_info(request)
        return self._call_api(**http_info)

    def show_routing_backlog_policy_invoker(self, request):
        http_info = self._show_routing_backlog_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_routing_backlog_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/routing-rule/backlog-policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRoutingBacklogPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_routing_backlog_policy(self, request):
        r"""修改数据流转积压策略

        应用服务器可调用此接口在物联网平台修改指定数据流转积压策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRoutingBacklogPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateRoutingBacklogPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRoutingBacklogPolicyResponse`
        """
        http_info = self._update_routing_backlog_policy_http_info(request)
        return self._call_api(**http_info)

    def update_routing_backlog_policy_invoker(self, request):
        http_info = self._update_routing_backlog_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_routing_backlog_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/routing-rule/backlog-policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoutingBacklogPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_batch_task(self, request):
        r"""创建批量任务

        应用服务器可调用此接口为创建批量处理任务，对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结设备、批量解冻设备、批量创建命令、批量创建消息任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.CreateBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateBatchTaskResponse`
        """
        http_info = self._create_batch_task_http_info(request)
        return self._call_api(**http_info)

    def create_batch_task_invoker(self, request):
        http_info = self._create_batch_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_batch_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/batchtasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBatchTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_batch_task(self, request):
        r"""删除批量任务

        应用服务器可调用此接口删除物联网平台中已经完成（状态为成功，失败，部分成功，已停止）的批量任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteBatchTaskResponse`
        """
        http_info = self._delete_batch_task_http_info(request)
        return self._call_api(**http_info)

    def delete_batch_task_invoker(self, request):
        http_info = self._delete_batch_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_batch_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/batchtasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBatchTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_batch_tasks(self, request):
        r"""查询批量任务列表

        应用服务器可调用此接口查询物联网平台中批量任务列表，每一个任务又包括具体的任务内容、任务状态、任务完成情况统计等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBatchTasks
        :type request: :class:`huaweicloudsdkiotda.v5.ListBatchTasksRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListBatchTasksResponse`
        """
        http_info = self._list_batch_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_batch_tasks_invoker(self, request):
        http_info = self._list_batch_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_batch_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/batchtasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListBatchTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def retry_batch_task(self, request):
        r"""重试批量任务

        应用服务器可调用此接口重试批量任务，目前只支持task_type为firmwareUpgrade，softwareUpgrade。如果task_id对应任务已经成功、停止、正在停止、等待中或初始化中，则不可以调用该接口。如果请求Body为{}，则调用该接口后会重新执行所有状态为失败、失败待重试和已停止的子任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.RetryBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.RetryBatchTaskResponse`
        """
        http_info = self._retry_batch_task_http_info(request)
        return self._call_api(**http_info)

    def retry_batch_task_invoker(self, request):
        http_info = self._retry_batch_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_batch_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/batchtasks/{task_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryBatchTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_batch_task(self, request):
        r"""查询批量任务

        应用服务器可调用此接口查询物联网平台中指定批量任务的信息，包括任务内容、任务状态、任务完成情况统计以及子任务列表等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.ShowBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowBatchTaskResponse`
        """
        http_info = self._show_batch_task_http_info(request)
        return self._call_api(**http_info)

    def show_batch_task_invoker(self, request):
        http_info = self._show_batch_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/batchtasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'task_detail_status' in local_var_params:
            query_params.append(('task_detail_status', local_var_params['task_detail_status']))
        if 'target' in local_var_params:
            query_params.append(('target', local_var_params['target']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def stop_batch_task(self, request):
        r"""停止批量任务

        应用服务器可调用此接口停止批量任务，目前只支持task_type为firmwareUpgrade，softwareUpgrade。如果task_id对应任务已经完成（成功、失败、部分成功，已经停止）或正在停止中，则不可以调用该接口。如果请求Body为{}，则调用该接口后会停止所有正在执行中、等待中和失败待重试状态的子任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.StopBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.StopBatchTaskResponse`
        """
        http_info = self._stop_batch_task_http_info(request)
        return self._call_api(**http_info)

    def stop_batch_task_invoker(self, request):
        http_info = self._stop_batch_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_batch_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/batchtasks/{task_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopBatchTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_batch_task_file(self, request):
        r"""删除批量任务文件

        应用服务器可调用此接口删除批量任务文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBatchTaskFile
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteBatchTaskFileRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteBatchTaskFileResponse`
        """
        http_info = self._delete_batch_task_file_http_info(request)
        return self._call_api(**http_info)

    def delete_batch_task_file_invoker(self, request):
        http_info = self._delete_batch_task_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_batch_task_file_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/batchtask-files/{file_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBatchTaskFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_batch_task_files(self, request):
        r"""查询批量任务文件列表

        应用服务器可调用此接口查询批量任务文件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBatchTaskFiles
        :type request: :class:`huaweicloudsdkiotda.v5.ListBatchTaskFilesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListBatchTaskFilesResponse`
        """
        http_info = self._list_batch_task_files_http_info(request)
        return self._call_api(**http_info)

    def list_batch_task_files_invoker(self, request):
        http_info = self._list_batch_task_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_batch_task_files_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/batchtask-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListBatchTaskFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def upload_batch_task_file(self, request):
        r"""上传批量任务文件

        应用服务器可调用此接口上传批量任务文件，用于创建批量任务。当前支持批量创建设备任务、批量删除设备任务、批量冻结设备任务、批量解冻设备任务的文件上传。
        - [批量注册设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchCreateDevices_Template.xlsx)
        
        
        - [批量删除设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchDeleteDevices_Template.xlsx)
        
        
        - [批量冻结设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchFreezeDevices_Template.xlsx)
        
        
        - [批量解冻设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchUnfreezeDevices_Template.xlsx)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadBatchTaskFile
        :type request: :class:`huaweicloudsdkiotda.v5.UploadBatchTaskFileRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UploadBatchTaskFileResponse`
        """
        http_info = self._upload_batch_task_file_http_info(request)
        return self._call_api(**http_info)

    def upload_batch_task_file_invoker(self, request):
        http_info = self._upload_batch_task_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_batch_task_file_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/batchtask-files",
            "request_type": request.__class__.__name__,
            "response_type": "UploadBatchTaskFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def add_bridge(self, request):
        r"""创建网桥

        应用服务器可调用此接口在物联网平台创建一个网桥，仅在创建后的网桥才可以接入物联网平台。
        - 一个实例最多支持20个网桥。
        - 仅**标准版实例、企业版实例**支持该接口调用，基础版不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddBridge
        :type request: :class:`huaweicloudsdkiotda.v5.AddBridgeRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddBridgeResponse`
        """
        http_info = self._add_bridge_http_info(request)
        return self._call_api(**http_info)

    def add_bridge_invoker(self, request):
        http_info = self._add_bridge_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_bridge_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/bridges",
            "request_type": request.__class__.__name__,
            "response_type": "AddBridgeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_bridge(self, request):
        r"""删除网桥

        应用服务器可调用此接口在物联网平台上删除指定网桥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBridge
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteBridgeRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteBridgeResponse`
        """
        http_info = self._delete_bridge_http_info(request)
        return self._call_api(**http_info)

    def delete_bridge_invoker(self, request):
        http_info = self._delete_bridge_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_bridge_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/bridges/{bridge_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBridgeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bridge_id' in local_var_params:
            path_params['bridge_id'] = local_var_params['bridge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_bridges(self, request):
        r"""查询网桥列表

        应用服务器可调用此接口在物联网平台查询网桥列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBridges
        :type request: :class:`huaweicloudsdkiotda.v5.ListBridgesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListBridgesResponse`
        """
        http_info = self._list_bridges_http_info(request)
        return self._call_api(**http_info)

    def list_bridges_invoker(self, request):
        http_info = self._list_bridges_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bridges_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/bridges",
            "request_type": request.__class__.__name__,
            "response_type": "ListBridgesResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def reset_bridge_secret(self, request):
        r"""重置网桥密钥

        应用服务器可调用此接口在物联网平台上重置网桥密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetBridgeSecret
        :type request: :class:`huaweicloudsdkiotda.v5.ResetBridgeSecretRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ResetBridgeSecretResponse`
        """
        http_info = self._reset_bridge_secret_http_info(request)
        return self._call_api(**http_info)

    def reset_bridge_secret_invoker(self, request):
        http_info = self._reset_bridge_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_bridge_secret_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/bridges/{bridge_id}/reset-secret",
            "request_type": request.__class__.__name__,
            "response_type": "ResetBridgeSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bridge_id' in local_var_params:
            path_params['bridge_id'] = local_var_params['bridge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def broadcast_message(self, request):
        r"""下发广播消息

        应用服务器可调用此接口向订阅了指定Topic的所有在线设备发布广播消息。应用将广播消息下发给平台后，平台会先返回应用响应结果，再将消息广播给设备。
        注意：
        - 此接口只适用于使用MQTT协议接入的设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BroadcastMessage
        :type request: :class:`huaweicloudsdkiotda.v5.BroadcastMessageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.BroadcastMessageResponse`
        """
        http_info = self._broadcast_message_http_info(request)
        return self._call_api(**http_info)

    def broadcast_message_invoker(self, request):
        http_info = self._broadcast_message_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _broadcast_message_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/broadcast-messages",
            "request_type": request.__class__.__name__,
            "response_type": "BroadcastMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def add_certificate(self, request):
        r"""上传设备CA证书

        应用服务器可调用此接口在物联网平台上传设备CA证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddCertificate
        :type request: :class:`huaweicloudsdkiotda.v5.AddCertificateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddCertificateResponse`
        """
        http_info = self._add_certificate_http_info(request)
        return self._call_api(**http_info)

    def add_certificate_invoker(self, request):
        http_info = self._add_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "AddCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'sp_auth_token' in local_var_params:
            header_params['Sp-Auth-Token'] = local_var_params['sp_auth_token']
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def check_certificate(self, request):
        r"""验证设备CA证书

        应用服务器可调用此接口在物联网平台验证设备的CA证书，目的是为了验证用户持有设备CA证书的私钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckCertificate
        :type request: :class:`huaweicloudsdkiotda.v5.CheckCertificateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CheckCertificateResponse`
        """
        http_info = self._check_certificate_http_info(request)
        return self._call_api(**http_info)

    def check_certificate_invoker(self, request):
        http_info = self._check_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/certificates/{certificate_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "CheckCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'sp_auth_token' in local_var_params:
            header_params['Sp-Auth-Token'] = local_var_params['sp_auth_token']
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_certificate(self, request):
        r"""删除设备CA证书

        应用服务器可调用此接口在物联网平台删除设备CA证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteCertificateResponse`
        """
        http_info = self._delete_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_invoker(self, request):
        http_info = self._delete_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_certificate_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []

        header_params = {}
        if 'sp_auth_token' in local_var_params:
            header_params['Sp-Auth-Token'] = local_var_params['sp_auth_token']
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_certificates(self, request):
        r"""获取设备CA证书列表

        应用服务器可调用此接口在物联网平台获取设备CA证书列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkiotda.v5.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListCertificatesResponse`
        """
        http_info = self._list_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_invoker(self, request):
        http_info = self._list_certificates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_certificates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'sp_auth_token' in local_var_params:
            header_params['Sp-Auth-Token'] = local_var_params['sp_auth_token']
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_certificate(self, request):
        r"""更新CA证书

        应用服务器可调用此接口在物联网平台上更新CA证书。仅标准版实例、企业版实例支持该接口调用，基础版不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCertificate
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateCertificateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateCertificateResponse`
        """
        http_info = self._update_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_certificate_invoker(self, request):
        http_info = self._update_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_certificate_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_command(self, request):
        r"""下发设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发命令，以实现对设备的同步控制。平台负责将命令以同步方式发送给设备，并将设备执行命令结果同步返回, 如果设备没有响应，平台会返回给应用服务器超时，平台超时时间是20秒。如果命令下发需要超过20秒，建议采用[[消息下发](https://support.huaweicloud.com/api-iothub/iot_06_v5_0059.html)](tag:hws)[[消息下发](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0059.html)](tag:hws_hk)。
        注意：
        - 此接口适用于MQTT设备同步命令下发，暂不支持NB-IoT设备命令下发。
        - 此接口仅支持单个设备同步命令下发，如需多个设备同步命令下发，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCommand
        :type request: :class:`huaweicloudsdkiotda.v5.CreateCommandRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateCommandResponse`
        """
        http_info = self._create_command_http_info(request)
        return self._call_api(**http_info)

    def create_command_invoker(self, request):
        http_info = self._create_command_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_command_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/commands",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_device_authorizer(self, request):
        r"""创建自定义鉴权

        应用服务器可调用此接口在物联网平台创建一个自定义鉴权。自定义鉴权是指用户可以通过函数服务自定义实现鉴权逻辑，以对接入平台的设备进行身份认证。
        - 单个实例最大可配置10个自定义鉴权
        - 仅标准版实例、企业版实例支持该接口调用，基础版不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeviceAuthorizer
        :type request: :class:`huaweicloudsdkiotda.v5.CreateDeviceAuthorizerRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateDeviceAuthorizerResponse`
        """
        http_info = self._create_device_authorizer_http_info(request)
        return self._call_api(**http_info)

    def create_device_authorizer_invoker(self, request):
        http_info = self._create_device_authorizer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_device_authorizer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/device-authorizers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeviceAuthorizerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_device_authorizer(self, request):
        r"""删除自定义鉴权

        应用服务器可调用此接口在物联网平台上删除指定自定义鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeviceAuthorizer
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceAuthorizerRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceAuthorizerResponse`
        """
        http_info = self._delete_device_authorizer_http_info(request)
        return self._call_api(**http_info)

    def delete_device_authorizer_invoker(self, request):
        http_info = self._delete_device_authorizer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_device_authorizer_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/device-authorizers/{authorizer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceAuthorizerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_device_authorizers(self, request):
        r"""查询自定义鉴权列表

        应用服务器可调用此接口在物联网平台查询自定义鉴权列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceAuthorizers
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceAuthorizersRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceAuthorizersResponse`
        """
        http_info = self._list_device_authorizers_http_info(request)
        return self._call_api(**http_info)

    def list_device_authorizers_invoker(self, request):
        http_info = self._list_device_authorizers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_device_authorizers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-authorizers",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeviceAuthorizersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'authorizer_name' in local_var_params:
            query_params.append(('authorizer_name', local_var_params['authorizer_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_device_authorizer(self, request):
        r"""查询自定义鉴权详情

        应用服务器可调用此接口在物联网平台查询指定自定义鉴权ID的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceAuthorizer
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceAuthorizerRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceAuthorizerResponse`
        """
        http_info = self._show_device_authorizer_http_info(request)
        return self._call_api(**http_info)

    def show_device_authorizer_invoker(self, request):
        http_info = self._show_device_authorizer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_authorizer_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-authorizers/{authorizer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceAuthorizerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_device_authorizer(self, request):
        r"""更新指定id的自定义鉴权

        应用服务器可调用此接口在物联网平台更新指定id的自定义鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeviceAuthorizer
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateDeviceAuthorizerRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDeviceAuthorizerResponse`
        """
        http_info = self._update_device_authorizer_http_info(request)
        return self._call_api(**http_info)

    def update_device_authorizer_invoker(self, request):
        http_info = self._update_device_authorizer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_device_authorizer_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/device-authorizers/{authorizer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceAuthorizerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def add_device_group(self, request):
        r"""添加设备组

        应用服务器可调用此接口新建设备组，一个华为云账号下最多可有1,000个设备组，包括父设备组和子设备组。设备组的最大层级关系不超过5层，即群组形成的关系树最大深度不超过5。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDeviceGroup
        :type request: :class:`huaweicloudsdkiotda.v5.AddDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddDeviceGroupResponse`
        """
        http_info = self._add_device_group_http_info(request)
        return self._call_api(**http_info)

    def add_device_group_invoker(self, request):
        http_info = self._add_device_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_device_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/device-group",
            "request_type": request.__class__.__name__,
            "response_type": "AddDeviceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_or_delete_device_in_group(self, request):
        r"""管理设备组中的设备

        应用服务器可调用此接口管理设备组中的设备。单个设备组内最多添加20,000个设备，一个设备最多可以被添加到10个设备组中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrDeleteDeviceInGroup
        :type request: :class:`huaweicloudsdkiotda.v5.CreateOrDeleteDeviceInGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateOrDeleteDeviceInGroupResponse`
        """
        http_info = self._create_or_delete_device_in_group_http_info(request)
        return self._call_api(**http_info)

    def create_or_delete_device_in_group_invoker(self, request):
        http_info = self._create_or_delete_device_in_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_or_delete_device_in_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/device-group/{group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrDeleteDeviceInGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_device_group(self, request):
        r"""删除设备组

        应用服务器可调用此接口删除指定设备组，如果该设备组存在子设备组或者该设备组中存在设备，必须先删除子设备组并将设备从该设备组移除，才能删除该设备组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeviceGroup
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceGroupResponse`
        """
        http_info = self._delete_device_group_http_info(request)
        return self._call_api(**http_info)

    def delete_device_group_invoker(self, request):
        http_info = self._delete_device_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_device_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/device-group/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_device_groups(self, request):
        r"""查询设备组列表

        应用服务器可调用此接口查询物联网平台中的设备组信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceGroups
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceGroupsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceGroupsResponse`
        """
        http_info = self._list_device_groups_http_info(request)
        return self._call_api(**http_info)

    def list_device_groups_invoker(self, request):
        http_info = self._list_device_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_device_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-group",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeviceGroupsResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'last_modified_time' in local_var_params:
            query_params.append(('last_modified_time', local_var_params['last_modified_time']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'group_type' in local_var_params:
            query_params.append(('group_type', local_var_params['group_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_device_group(self, request):
        r"""查询设备组

        应用服务器可调用此接口查询指定设备组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceGroup
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceGroupResponse`
        """
        http_info = self._show_device_group_http_info(request)
        return self._call_api(**http_info)

    def show_device_group_invoker(self, request):
        http_info = self._show_device_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-group/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_devices_in_group(self, request):
        r"""查询设备组设备列表

        应用服务器可调用此接口查询指定设备组下的设备列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDevicesInGroup
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDevicesInGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDevicesInGroupResponse`
        """
        http_info = self._show_devices_in_group_http_info(request)
        return self._call_api(**http_info)

    def show_devices_in_group_invoker(self, request):
        http_info = self._show_devices_in_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_devices_in_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-group/{group_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDevicesInGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_device_group(self, request):
        r"""修改设备组

        应用服务器可调用此接口修改物联网平台中指定设备组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeviceGroup
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDeviceGroupResponse`
        """
        http_info = self._update_device_group_http_info(request)
        return self._call_api(**http_info)

    def update_device_group_invoker(self, request):
        http_info = self._update_device_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_device_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/device-group/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def add_device(self, request):
        r"""创建设备

        应用服务器可调用此接口在物联网平台创建一个设备，仅在创建后设备才可以接入物联网平台。
        
        - 该接口支持使用gateway_id参数指定在父设备下创建一个子设备，并且支持多级子设备，当前最大支持二级子设备。
        - 该接口同时还支持对设备进行初始配置，接口会读取创建设备请求参数product_id对应的产品详情，如果产品的属性有定义默认值，则会将该属性默认值写入该设备的设备影子中。
        - 用户还可以使用创建设备请求参数shadow字段为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以shadow字段中设置的属性值为准写入到设备影子中。
        - 该接口仅支持创建单个设备，如需批量注册设备，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDevice
        :type request: :class:`huaweicloudsdkiotda.v5.AddDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddDeviceResponse`
        """
        http_info = self._add_device_http_info(request)
        return self._call_api(**http_info)

    def add_device_invoker(self, request):
        http_info = self._add_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_device_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "AddDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def change_gateway(self, request):
        r"""修改设备网关

        应用服务器可调用此接口在物联网平台修改子设备网关。
        - 只允许子设备修改网关。
        - 目标网关必须和当前设备在同一个资源空间。
        - 网关id不能和当前子设备网关id相同。
        - 设备如果有下级子设备，则不允许切换网关。
        - 支持多级子设备，当前最大支持二级子设备。
        - 该接口仅支持创建单个设备切换网关，如需批量切换设备网关，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeGateway
        :type request: :class:`huaweicloudsdkiotda.v5.ChangeGatewayRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ChangeGatewayResponse`
        """
        http_info = self._change_gateway_http_info(request)
        return self._call_api(**http_info)

    def change_gateway_invoker(self, request):
        http_info = self._change_gateway_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_gateway_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/change-gateway",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_device(self, request):
        r"""删除设备

        应用服务器可调用此接口在物联网平台上删除指定设备。若设备下连接了非直连设备，则必须把设备下的非直连设备都删除后，才能删除该设备。该接口仅支持删除单个设备，如需批量删除设备，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDevice
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceResponse`
        """
        http_info = self._delete_device_http_info(request)
        return self._call_api(**http_info)

    def delete_device_invoker(self, request):
        http_info = self._delete_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_device_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def freeze_device(self, request):
        r"""冻结设备

        应用服务器可调用此接口冻结设备，设备冻结后不能再连接上线，可以通过解冻设备接口解除设备冻结。注意，当前仅支持冻结与平台直连的设备。该接口仅支持冻结单个设备，如需批量冻结设备，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for FreezeDevice
        :type request: :class:`huaweicloudsdkiotda.v5.FreezeDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.FreezeDeviceResponse`
        """
        http_info = self._freeze_device_http_info(request)
        return self._call_api(**http_info)

    def freeze_device_invoker(self, request):
        http_info = self._freeze_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _freeze_device_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/freeze",
            "request_type": request.__class__.__name__,
            "response_type": "FreezeDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_device_groups_by_device(self, request):
        r"""查询指定设备加入的设备组列表

        应用服务器可调用此接口查询物联网平台中的某个设备加入的设备组信息列表。仅标准版实例、企业版实例支持该接口调用，基础版不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceGroupsByDevice
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceGroupsByDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceGroupsByDeviceResponse`
        """
        http_info = self._list_device_groups_by_device_http_info(request)
        return self._call_api(**http_info)

    def list_device_groups_by_device_invoker(self, request):
        http_info = self._list_device_groups_by_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_device_groups_by_device_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/list-device-group",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeviceGroupsByDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_devices(self, request):
        r"""查询设备列表

        应用服务器可调用此接口查询物联网平台中的设备信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDevices
        :type request: :class:`huaweicloudsdkiotda.v5.ListDevicesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDevicesResponse`
        """
        http_info = self._list_devices_http_info(request)
        return self._call_api(**http_info)

    def list_devices_invoker(self, request):
        http_info = self._list_devices_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_devices_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
        if 'is_cascade_query' in local_var_params:
            query_params.append(('is_cascade_query', local_var_params['is_cascade_query']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def reset_device_secret(self, request):
        r"""重置设备密钥

        应用服务器可调用此接口重置设备密钥，携带指定密钥时平台将设备密钥重置为指定的密钥，不携带密钥时平台将自动生成一个新的随机密钥返回。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetDeviceSecret
        :type request: :class:`huaweicloudsdkiotda.v5.ResetDeviceSecretRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ResetDeviceSecretResponse`
        """
        http_info = self._reset_device_secret_http_info(request)
        return self._call_api(**http_info)

    def reset_device_secret_invoker(self, request):
        http_info = self._reset_device_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_device_secret_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ResetDeviceSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def reset_fingerprint(self, request):
        r"""重置设备指纹

        应用服务器可调用此接口重置设备指纹。携带指定设备指纹时将之重置为指定值；不携带时将之置空，后续设备第一次接入时，该设备指纹的值将设置为第一次接入时的证书指纹。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetFingerprint
        :type request: :class:`huaweicloudsdkiotda.v5.ResetFingerprintRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ResetFingerprintResponse`
        """
        http_info = self._reset_fingerprint_http_info(request)
        return self._call_api(**http_info)

    def reset_fingerprint_invoker(self, request):
        http_info = self._reset_fingerprint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_fingerprint_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/reset-fingerprint",
            "request_type": request.__class__.__name__,
            "response_type": "ResetFingerprintResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def search_devices(self, request):
        r"""灵活搜索设备列表

        #### 接口说明
        
        应用服务器使用SQL语句调用该接口，灵活的搜索所需要的设备资源列表
        
        #### 限制
        
        - 仅**标准版实例、企业版实例**支持该接口调用，基础版不支持。
        - 单账号调用该接口的 TPS 限制最大为1/S(每秒1次请求数)
        
        #### 类SQL语法使用说明
        
        类SQL语句有select、from、where(可选)、order by(可选)、limit子句(可选)组成，长度限制为400个字符。子句里的内容大小写敏感，SQL语句的关键字大小写不敏感。
        
        示例：
        
        &#x60;&#x60;&#x60;
        select * from device where device_id &#x3D; &#39;as********&#39; limit 0,5
        &#x60;&#x60;&#x60;
        
        ##### SELECT子句
        
        &#x60;&#x60;&#x60;
        select [field]/[count(*)/count(1)] from device
        &#x60;&#x60;&#x60;
        
        其中field为需要获取的字段，请参考响应参数字段名称，也可填*，获取所有字段。
        
        如果需要统计搜索的设备个数，请填count(*)或者count(1).
        
        ##### FROM子句
        
        &#x60;&#x60;&#x60;
        from device
        &#x60;&#x60;&#x60;
        
        from后为要查询的资源名，当前支持\&quot;device\&quot;
        
        ##### WHERE子句(可选)
        
        &#x60;&#x60;&#x60;
        WHERE [condition1] AND [condition2]
        &#x60;&#x60;&#x60;
        
        最多支持5个condition，不支持嵌套；支持的检索字段请参见下面的**搜索条件字段说明**和**支持的运算符**章节
        
        连接词支持AND、OR，优先级参考标准SQL语法，默认AND优先级高于OR。
        
        ##### LIMIT子句(可选)
        
        &#x60;&#x60;&#x60;
        limit [offset,] rows
        &#x60;&#x60;&#x60;
        
        offset标识搜索的偏移量，rows标识返回搜索结果的最大行数，例如：
        
        - limit n ;示例(select * from device limit 10)
        
          最大返回n条结果数据
          
        - limit m,n; 示例(select * from device limit 20,10) 
          搜索偏移量为m，最大返回n条结果数据
        
        ###### 限制
        
         offset 最大 500， rows最大50，如果不填写limit子句，默认为limit 10
        
        ##### ORDER BY子句(可选)
        
        用于实现自定义排序，当前支持自定义排序的字段为：\&quot;marker\&quot;。
        
        &#x60;&#x60;&#x60;
        order by marker [asc]/[desc]
        &#x60;&#x60;&#x60;
        
        子句不填写时默认逻辑为随机排序
        
        #### 搜索条件字段说明
        
        | 字段名      | 类型   | 说明             | 取值范围                                                     |
        | :---------- | :----- | :--------------- | :----------------------------------------------------------- |
        | app_id      | string | 资源空间ID       | 长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。 |
        | device_id   | string | 设备ID           | 长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。 |
        | gateway_id  | string | 网关ID           | 长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。 |
        | product_id  | string | 设备关联的产品ID | 长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。 |
        | device_name | string | 设备名称         | 长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合符。 |
        | node_id     | string | 设备标识码       | 长度不超过64，只允许字母、数字、下划线（_）、连接符（-）的组合 |
        | status      | string | 设备的状态       | ONLINE(在线)、OFFLINE(离线)、ABNORMAL(异常)、INACTIVE(未激活)、FROZEN(冻结) |
        | node_type   | string | 设备节点类型     | GATEWAY(直连设备或网关)、ENDPOINT(非直连设备)                |
        | tag_key     | string | 标签键           | 长度不超过64，只允许中文、字母、数字、以及_.-等字符的组合。  |
        | tag_value   | string | 标签值           | 长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。 |
        | sw_version  | string | 软件版本         | 长度不超过64，只允许字母、数字、下划线（_）、连接符（-）、英文点(.)的组合。 |
        | fw_version  | string | 固件版本         | 长度不超过64，只允许字母、数字、下划线（_）、连接符（-）、英文点(.)的组合。 |
        | group_id    | string | 群组Id           | 长度不超过36，十六进制字符串和连接符（-）的组合              |
        | create_time | string | 设备注册时间     | 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;，如：2015-06-06T12:10:10.000Z |
        | marker      | string | 结果记录ID       | 长度为24的十六进制字符串，如ffffffffffffffffffffffff         |
        
        #### 支持的运算符
        
        | 运算符  | 支持的字段                               |
        | ------- | ---------------------------------------- |
        | &#x3D;       | 所有                                     |
        | !&#x3D;      | 所有                                     |
        | &gt;       | create_time、marker                      |
        | &lt;       | create_time、marker                      |
        | like    | device_name、node_id、tag_key、tag_value |
        | in      | 除tag_key、tag_value以外字段             |
        | not  in | 除tag_key、tag_value以外字段             |
        
        #### SQL 限制
        
        - like: 只支持前缀匹配，不支持后缀匹配或者通配符匹配。前缀匹配不得少于4个字符，且不能包含任何特殊字符(只允许中文、字母、数字、下划线（_）、连接符（-）). 前缀后必须跟上\&quot;%\&quot;结尾。
        - 不支持除了count(*)/count(1)以外的其他任何函数。
        - 不支持其他SQL用法，如嵌套SQL、union、join、别名(Alias)等用法
        - SQL长度限制为400个字符，单个请求条件最大支持5个。
        - 不支持\&quot;null\&quot;和空字符串等条件值匹配
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDevices
        :type request: :class:`huaweicloudsdkiotda.v5.SearchDevicesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.SearchDevicesResponse`
        """
        http_info = self._search_devices_http_info(request)
        return self._call_api(**http_info)

    def search_devices_invoker(self, request):
        http_info = self._search_devices_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_devices_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/search/query-devices",
            "request_type": request.__class__.__name__,
            "response_type": "SearchDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_device(self, request):
        r"""查询设备

        应用服务器可调用此接口查询物联网平台中指定设备的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDevice
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceResponse`
        """
        http_info = self._show_device_http_info(request)
        return self._call_api(**http_info)

    def show_device_invoker(self, request):
        http_info = self._show_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def unfreeze_device(self, request):
        r"""解冻设备

        应用服务器可调用此接口解冻设备，解除冻结后，设备可以连接上线。该接口仅支持解冻单个设备，如需批量解冻设备，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnfreezeDevice
        :type request: :class:`huaweicloudsdkiotda.v5.UnfreezeDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UnfreezeDeviceResponse`
        """
        http_info = self._unfreeze_device_http_info(request)
        return self._call_api(**http_info)

    def unfreeze_device_invoker(self, request):
        http_info = self._unfreeze_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unfreeze_device_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/unfreeze",
            "request_type": request.__class__.__name__,
            "response_type": "UnfreezeDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_device(self, request):
        r"""修改设备

        应用服务器可调用此接口修改物联网平台中指定设备的基本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDevice
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDeviceResponse`
        """
        http_info = self._update_device_http_info(request)
        return self._call_api(**http_info)

    def update_device_invoker(self, request):
        http_info = self._update_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_device_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_device_proxy(self, request):
        r"""创建设备代理

        应用服务器可调用此接口在物联网平台创建一个动态设备代理规则，用于子设备自主选择网关设备上线和上报消息，即代理组下的任意网关下的子设备均可以通过代理组里其他设备上线([[网关更新子设备状态](https://support.huaweicloud.com/api-iothub/iot_06_v5_3022.html)](tag:hws) [[网关更新子设备状态](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_3022.html)](tag:hws_hk))然后进行数据上报([[网关批量设备属性上报](https://support.huaweicloud.com/api-iothub/iot_06_v5_3006.html)](tag:hws) [[网关更新子设备状态](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_3006.html)](tag:hws_hk))。
        - 单实例最多可以配置10个设备代理
        - 单账号调用该接口的 TPS 限制最大为1/S(每秒1次请求数)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeviceProxy
        :type request: :class:`huaweicloudsdkiotda.v5.CreateDeviceProxyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateDeviceProxyResponse`
        """
        http_info = self._create_device_proxy_http_info(request)
        return self._call_api(**http_info)

    def create_device_proxy_invoker(self, request):
        http_info = self._create_device_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_device_proxy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/device-proxies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeviceProxyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_device_proxy(self, request):
        r"""删除设备代理

        应用服务器可调用此接口在物联网平台上删除指定设备代理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeviceProxy
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceProxyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceProxyResponse`
        """
        http_info = self._delete_device_proxy_http_info(request)
        return self._call_api(**http_info)

    def delete_device_proxy_invoker(self, request):
        http_info = self._delete_device_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_device_proxy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/device-proxies/{proxy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceProxyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_device_proxies(self, request):
        r"""查询设备代理列表

        应用服务器可调用此接口查询物联网平台中的设备代理列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceProxies
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceProxiesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceProxiesResponse`
        """
        http_info = self._list_device_proxies_http_info(request)
        return self._call_api(**http_info)

    def list_device_proxies_invoker(self, request):
        http_info = self._list_device_proxies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_device_proxies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-proxies",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeviceProxiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'proxy_name' in local_var_params:
            query_params.append(('proxy_name', local_var_params['proxy_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_device_proxy(self, request):
        r"""查询设备代理详情

        应用服务器可调用此接口查询物联网平台中指定设备代理的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceProxy
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceProxyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceProxyResponse`
        """
        http_info = self._show_device_proxy_http_info(request)
        return self._call_api(**http_info)

    def show_device_proxy_invoker(self, request):
        http_info = self._show_device_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_proxy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-proxies/{proxy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceProxyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_device_proxy(self, request):
        r"""修改设备代理

        应用服务器可调用此接口修改物联网平台中指定设备代理的基本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeviceProxy
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateDeviceProxyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDeviceProxyResponse`
        """
        http_info = self._update_device_proxy_http_info(request)
        return self._call_api(**http_info)

    def update_device_proxy_invoker(self, request):
        http_info = self._update_device_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_device_proxy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/device-proxies/{proxy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceProxyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_device_shadow(self, request):
        r"""查询设备影子数据

        应用服务器可调用此接口查询指定设备的设备影子信息，包括对设备的期望属性信息（desired区）和设备最新上报的属性信息（reported区）。
        
        设备影子介绍：
        设备影子是一个用于存储和检索设备当前状态信息的JSON文档。
        - 每个设备有且只有一个设备影子，由设备ID唯一标识
        - 设备影子用于存储设备上报的(状态)属性和应用程序期望的设备(状态)属性
        - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性
        - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发
        
        限制：
        设备影子JSON文档中的key不允许特殊字符：点(.)、dollar符号($)、空char(十六进制的ASCII码为00)。如果包含了以上特殊字符则无法正常刷新影子文档。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceShadow
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceShadowRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceShadowResponse`
        """
        http_info = self._show_device_shadow_http_info(request)
        return self._call_api(**http_info)

    def show_device_shadow_invoker(self, request):
        http_info = self._show_device_shadow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_shadow_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/shadow",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceShadowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_device_shadow_desired_data(self, request):
        r"""配置设备影子预期数据

        应用服务器可调用此接口配置设备影子的预期属性（desired区），当设备上线或者设备上报属性时把属性下发给设备。
        
        设备影子介绍：
        设备影子是一个用于存储和检索设备当前状态信息的JSON文档。
        - 每个设备有且只有一个设备影子，由设备ID唯一标识
        - 设备影子用于存储设备上报的(状态)属性和应用程序期望的设备(状态)属性
        - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性
        - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发
        - 该接口仅支持配置单个设备的设备影子的预期数据，如需多个设备的设备影子配置，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        限制：
        设备影子JSON文档中的key不允许特殊字符：点(.)、dollar符号($)、空char(十六进制的ASCII码为00)。如果包含了以上特殊字符则无法正常刷新影子文档。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeviceShadowDesiredData
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateDeviceShadowDesiredDataRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDeviceShadowDesiredDataResponse`
        """
        http_info = self._update_device_shadow_desired_data_http_info(request)
        return self._call_api(**http_info)

    def update_device_shadow_desired_data_invoker(self, request):
        http_info = self._update_device_shadow_desired_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_device_shadow_desired_data_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/shadow",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceShadowDesiredDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_routing_flow_control_policy(self, request):
        r"""新建数据流转流控策略

        应用服务器可调用此接口在物联网平台创建数据流转流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRoutingFlowControlPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.CreateRoutingFlowControlPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateRoutingFlowControlPolicyResponse`
        """
        http_info = self._create_routing_flow_control_policy_http_info(request)
        return self._call_api(**http_info)

    def create_routing_flow_control_policy_invoker(self, request):
        http_info = self._create_routing_flow_control_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_routing_flow_control_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/routing-rule/flowcontrol-policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRoutingFlowControlPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_routing_flow_control_policy(self, request):
        r"""删除数据流转流控策略

        应用服务器可调用此接口在物联网平台删除指定数据流转流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRoutingFlowControlPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteRoutingFlowControlPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteRoutingFlowControlPolicyResponse`
        """
        http_info = self._delete_routing_flow_control_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_routing_flow_control_policy_invoker(self, request):
        http_info = self._delete_routing_flow_control_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_routing_flow_control_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/routing-rule/flowcontrol-policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRoutingFlowControlPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_routing_flow_control_policy(self, request):
        r"""查询数据流转流控策略列表

        应用服务器可调用此接口查询在物联网平台设置的数据流转流控策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRoutingFlowControlPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.ListRoutingFlowControlPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListRoutingFlowControlPolicyResponse`
        """
        http_info = self._list_routing_flow_control_policy_http_info(request)
        return self._call_api(**http_info)

    def list_routing_flow_control_policy_invoker(self, request):
        http_info = self._list_routing_flow_control_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_routing_flow_control_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/routing-rule/flowcontrol-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListRoutingFlowControlPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'scope_value' in local_var_params:
            query_params.append(('scope_value', local_var_params['scope_value']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_routing_flow_control_policy(self, request):
        r"""查询数据流转流控策略

        应用服务器可调用此接口在物联网平台查询指定数据流转流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRoutingFlowControlPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.ShowRoutingFlowControlPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowRoutingFlowControlPolicyResponse`
        """
        http_info = self._show_routing_flow_control_policy_http_info(request)
        return self._call_api(**http_info)

    def show_routing_flow_control_policy_invoker(self, request):
        http_info = self._show_routing_flow_control_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_routing_flow_control_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/routing-rule/flowcontrol-policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRoutingFlowControlPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_routing_flow_control_policy(self, request):
        r"""修改数据流转流控策略

        应用服务器可调用此接口在物联网平台修改指定数据流转流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRoutingFlowControlPolicy
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateRoutingFlowControlPolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRoutingFlowControlPolicyResponse`
        """
        http_info = self._update_routing_flow_control_policy_http_info(request)
        return self._call_api(**http_info)

    def update_routing_flow_control_policy_invoker(self, request):
        http_info = self._update_routing_flow_control_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_routing_flow_control_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/routing-rule/flowcontrol-policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoutingFlowControlPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def add_functions(self, request):
        r"""创建编解码函数

        提供创建编解码函数的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddFunctions
        :type request: :class:`huaweicloudsdkiotda.v5.AddFunctionsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddFunctionsResponse`
        """
        http_info = self._add_functions_http_info(request)
        return self._call_api(**http_info)

    def add_functions_invoker(self, request):
        http_info = self._add_functions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_functions_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/product-functions",
            "request_type": request.__class__.__name__,
            "response_type": "AddFunctionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_functions(self, request):
        r"""删除编解码函数

        提供删除编解码函数的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFunctions
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteFunctionsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteFunctionsResponse`
        """
        http_info = self._delete_functions_http_info(request)
        return self._call_api(**http_info)

    def delete_functions_invoker(self, request):
        http_info = self._delete_functions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_functions_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/product-functions/{function_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFunctionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_id' in local_var_params:
            path_params['function_id'] = local_var_params['function_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_functions(self, request):
        r"""查询编解码函数

        提供查询编解码函数的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctions
        :type request: :class:`huaweicloudsdkiotda.v5.ListFunctionsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListFunctionsResponse`
        """
        http_info = self._list_functions_http_info(request)
        return self._call_api(**http_info)

    def list_functions_invoker(self, request):
        http_info = self._list_functions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_functions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/product-functions",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_message(self, request):
        r"""下发设备消息

        物联网平台可向设备下发消息，应用服务器可调用此接口向指定设备下发消息，以实现对设备的控制。应用将消息下发给平台后，平台返回应用响应结果，平台再将消息发送给设备。平台返回应用响应结果不一定是设备接收结果，建议用户应用通过订阅[[设备消息状态变更通知](https://support.huaweicloud.com/api-iothub/iot_06_v5_01203.html)](tag:hws)[[设备消息状态变更通知](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_01203.html)](tag:hws_hk)，订阅后平台会将设备接收结果推送给订阅的应用。
        注意：
        - 此接口适用于MQTT设备消息下发，暂不支持其他协议接入的设备消息下发。
        - 此接口仅支持单个设备消息下发，如需多个设备消息下发，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMessage
        :type request: :class:`huaweicloudsdkiotda.v5.CreateMessageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateMessageResponse`
        """
        http_info = self._create_message_http_info(request)
        return self._call_api(**http_info)

    def create_message_invoker(self, request):
        http_info = self._create_message_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_message_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_device_message(self, request):
        r"""删除指定消息id的消息

        应用服务器可调用此接口删除平台下发给设备的指定消息id的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeviceMessage
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceMessageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceMessageResponse`
        """
        http_info = self._delete_device_message_http_info(request)
        return self._call_api(**http_info)

    def delete_device_message_invoker(self, request):
        http_info = self._delete_device_message_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_device_message_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/messages/{message_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_device_messages(self, request):
        r"""查询设备消息

        应用服务器可调用此接口查询平台下发给设备的消息，平台为每个设备默认最多保存20条消息，超过20条后， 后续的消息会替换下发最早的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceMessages
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceMessagesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceMessagesResponse`
        """
        http_info = self._list_device_messages_http_info(request)
        return self._call_api(**http_info)

    def list_device_messages_invoker(self, request):
        http_info = self._list_device_messages_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_device_messages_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeviceMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_device_message(self, request):
        r"""查询指定消息id的消息

        应用服务器可调用此接口查询平台下发给设备的指定消息id的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceMessage
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceMessageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceMessageResponse`
        """
        http_info = self._show_device_message_http_info(request)
        return self._call_api(**http_info)

    def show_device_message_invoker(self, request):
        http_info = self._show_device_message_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_message_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/messages/{message_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_ota_package(self, request):
        r"""创建OTA升级包

        用户可调用此接口创建升级包关联OBS对象
        使用前提：使用该API需要您授权设备接入服务(IoTDA)的实例访问对象存储服务(OBS)以及 密钥管理服务(KMS Administrator)的权限。在“[[统一身份认证服务（IAM）](https://console.huaweicloud.com/iam)](tag:hws)[[统一身份认证服务（IAM）](https://console-intl.huaweicloud.com/iam)](tag:hws_hk) - 委托”中将委托名称为iotda_admin_trust的委托授权KMS Administrator和OBS OperateAccess
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOtaPackage
        :type request: :class:`huaweicloudsdkiotda.v5.CreateOtaPackageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateOtaPackageResponse`
        """
        http_info = self._create_ota_package_http_info(request)
        return self._call_api(**http_info)

    def create_ota_package_invoker(self, request):
        http_info = self._create_ota_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ota_package_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/ota-upgrades/packages",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOtaPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_ota_package(self, request):
        r"""删除OTA升级包

        用户可调用此接口删除关联OBS对象的升级包信息，不会删除OBS上对象
        使用前提：使用该API需要您授权设备接入服务(IoTDA)的实例访问对象存储服务(OBS)以及 密钥管理服务(KMS Administrator)的权限。在“[[统一身份认证服务（IAM）](https://console.huaweicloud.com/iam)](tag:hws)[[统一身份认证服务（IAM）](https://console-intl.huaweicloud.com/iam)](tag:hws_hk) - 委托”中将委托名称为iotda_admin_trust的委托授权KMS Administrator和OBS OperateAccess
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOtaPackage
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteOtaPackageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteOtaPackageResponse`
        """
        http_info = self._delete_ota_package_http_info(request)
        return self._call_api(**http_info)

    def delete_ota_package_invoker(self, request):
        http_info = self._delete_ota_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ota_package_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/ota-upgrades/packages/{package_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOtaPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_ota_package_info(self, request):
        r"""查询OTA升级包列表

        用户可调用此接口查询关联OBS对象的升级包列表
        使用前提：使用该API需要您授权设备接入服务(IoTDA)的实例访问对象存储服务(OBS)以及 密钥管理服务(KMS Administrator)的权限。在“[[统一身份认证服务（IAM）](https://console.huaweicloud.com/iam)](tag:hws)[[统一身份认证服务（IAM）](https://console-intl.huaweicloud.com/iam)](tag:hws_hk) - 委托”中将委托名称为iotda_admin_trust的委托授权KMS Administrator和OBS OperateAccess
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOtaPackageInfo
        :type request: :class:`huaweicloudsdkiotda.v5.ListOtaPackageInfoRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListOtaPackageInfoResponse`
        """
        http_info = self._list_ota_package_info_http_info(request)
        return self._call_api(**http_info)

    def list_ota_package_info_invoker(self, request):
        http_info = self._list_ota_package_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ota_package_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/ota-upgrades/packages",
            "request_type": request.__class__.__name__,
            "response_type": "ListOtaPackageInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'package_type' in local_var_params:
            query_params.append(('package_type', local_var_params['package_type']))
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_ota_package(self, request):
        r"""获取OTA升级包详情

        用户可调用此接口查询关联OBS对象的升级包详情
        使用前提：使用该API需要您授权设备接入服务(IoTDA)的实例访问对象存储服务(OBS)以及 密钥管理服务(KMS Administrator)的权限。在“[[统一身份认证服务（IAM）](https://console.huaweicloud.com/iam)](tag:hws)[[统一身份认证服务（IAM）](https://console-intl.huaweicloud.com/iam)](tag:hws_hk) - 委托”中将委托名称为iotda_admin_trust的委托授权KMS Administrator和OBS OperateAccess
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOtaPackage
        :type request: :class:`huaweicloudsdkiotda.v5.ShowOtaPackageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowOtaPackageResponse`
        """
        http_info = self._show_ota_package_http_info(request)
        return self._call_api(**http_info)

    def show_ota_package_invoker(self, request):
        http_info = self._show_ota_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ota_package_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/ota-upgrades/packages/{package_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOtaPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def bind_device_policy(self, request):
        r"""绑定设备策略

        应用服务器可调用此接口在物联网平台上为批量设备绑定目标策略，目前支持绑定目标类型为：设备、产品，当目标类型为产品时，该产品下所有设备都会生效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BindDevicePolicy
        :type request: :class:`huaweicloudsdkiotda.v5.BindDevicePolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.BindDevicePolicyResponse`
        """
        http_info = self._bind_device_policy_http_info(request)
        return self._call_api(**http_info)

    def bind_device_policy_invoker(self, request):
        http_info = self._bind_device_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _bind_device_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/device-policies/{policy_id}/bind",
            "request_type": request.__class__.__name__,
            "response_type": "BindDevicePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_device_policy(self, request):
        r"""创建设备策略

        应用服务器可调用此接口在物联网平台创建一个策略，该策略需要绑定到设备和产品下才能生效。
        - 一个实例最多能创建50个设备策略。
        - 仅**标准版实例、企业版实例**支持该接口调用，基础版不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDevicePolicy
        :type request: :class:`huaweicloudsdkiotda.v5.CreateDevicePolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateDevicePolicyResponse`
        """
        http_info = self._create_device_policy_http_info(request)
        return self._call_api(**http_info)

    def create_device_policy_invoker(self, request):
        http_info = self._create_device_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_device_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/device-policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDevicePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_device_policy(self, request):
        r"""删除设备策略

        应用服务器可调用此接口在物联网平台上删除指定策略，注意：删除策略同时会解绑该策略下所有绑定对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDevicePolicy
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDevicePolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDevicePolicyResponse`
        """
        http_info = self._delete_device_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_device_policy_invoker(self, request):
        http_info = self._delete_device_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_device_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/device-policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDevicePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_device_policies(self, request):
        r"""查询设备策略列表

        应用服务器可调用此接口在物联网平台查询策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDevicePolicies
        :type request: :class:`huaweicloudsdkiotda.v5.ListDevicePoliciesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDevicePoliciesResponse`
        """
        http_info = self._list_device_policies_http_info(request)
        return self._call_api(**http_info)

    def list_device_policies_invoker(self, request):
        http_info = self._list_device_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_device_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevicePoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_device_policy(self, request):
        r"""查询设备策略详情

        应用服务器可调用此接口在物联网平台查询指定策略ID的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDevicePolicy
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDevicePolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDevicePolicyResponse`
        """
        http_info = self._show_device_policy_http_info(request)
        return self._call_api(**http_info)

    def show_device_policy_invoker(self, request):
        http_info = self._show_device_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/device-policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDevicePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_targets_in_device_policy(self, request):
        r"""查询设备策略绑定的目标列表

        应用服务器可调用此接口在物联网平台上查询指定策略ID下绑定的目标列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTargetsInDevicePolicy
        :type request: :class:`huaweicloudsdkiotda.v5.ShowTargetsInDevicePolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowTargetsInDevicePolicyResponse`
        """
        http_info = self._show_targets_in_device_policy_http_info(request)
        return self._call_api(**http_info)

    def show_targets_in_device_policy_invoker(self, request):
        http_info = self._show_targets_in_device_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_targets_in_device_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/device-policies/{policy_id}/list-targets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTargetsInDevicePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def unbind_device_policy(self, request):
        r"""解绑设备策略

        应用服务器可调用此接口在物联网平台上解除指定策略下绑定的目标对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnbindDevicePolicy
        :type request: :class:`huaweicloudsdkiotda.v5.UnbindDevicePolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UnbindDevicePolicyResponse`
        """
        http_info = self._unbind_device_policy_http_info(request)
        return self._call_api(**http_info)

    def unbind_device_policy_invoker(self, request):
        http_info = self._unbind_device_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unbind_device_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/device-policies/{policy_id}/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "UnbindDevicePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_device_policy(self, request):
        r"""更新设备策略信息

        应用服务器可调用此接口在物联网平台更新策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDevicePolicy
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateDevicePolicyRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDevicePolicyResponse`
        """
        http_info = self._update_device_policy_http_info(request)
        return self._call_api(**http_info)

    def update_device_policy_invoker(self, request):
        http_info = self._update_device_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_device_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/device-policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDevicePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_product(self, request):
        r"""创建产品

        应用服务器可调用此接口创建产品。此接口仅创建了产品，没有创建和安装插件，如果需要对数据进行编解码，还需要在平台开发和安装插件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProduct
        :type request: :class:`huaweicloudsdkiotda.v5.CreateProductRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateProductResponse`
        """
        http_info = self._create_product_http_info(request)
        return self._call_api(**http_info)

    def create_product_invoker(self, request):
        http_info = self._create_product_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_product_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/products",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_product(self, request):
        r"""删除产品

        应用服务器可调用此接口删除已导入物联网平台的指定产品模型。此接口仅删除了产品，未删除关联的插件，在产品下存在设备时，该产品不允许删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProduct
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteProductRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteProductResponse`
        """
        http_info = self._delete_product_http_info(request)
        return self._call_api(**http_info)

    def delete_product_invoker(self, request):
        http_info = self._delete_product_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_product_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_products(self, request):
        r"""查询产品列表

        应用服务器可调用此接口查询已导入物联网平台的产品模型信息列表，了解产品模型的概要信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkiotda.v5.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListProductsResponse`
        """
        http_info = self._list_products_http_info(request)
        return self._call_api(**http_info)

    def list_products_invoker(self, request):
        http_info = self._list_products_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_products_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductsResponse"
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
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'product_name' in local_var_params:
            query_params.append(('product_name', local_var_params['product_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_product(self, request):
        r"""查询产品

        应用服务器可调用此接口查询已导入物联网平台的指定产品模型详细信息，包括产品模型的服务、属性、命令等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProduct
        :type request: :class:`huaweicloudsdkiotda.v5.ShowProductRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowProductResponse`
        """
        http_info = self._show_product_http_info(request)
        return self._call_api(**http_info)

    def show_product_invoker(self, request):
        http_info = self._show_product_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_product_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_product(self, request):
        r"""修改产品

        应用服务器可调用此接口修改已导入物联网平台的指定产品模型，包括产品模型的服务、属性、命令等。此接口仅修改了产品，未修改和安装插件，如果修改了产品中的service定义，且在平台中有对应的插件，请修改并重新安装插件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProduct
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateProductRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateProductResponse`
        """
        http_info = self._update_product_http_info(request)
        return self._call_api(**http_info)

    def update_product_invoker(self, request):
        http_info = self._update_product_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_product_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_properties(self, request):
        r"""查询设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口向设备发送指令用以查询设备的实时属性, 并由设备将属性查询的结果同步返回给应用服务器。
        注意：此接口适用于MQTT设备，暂不支持NB-IoT设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProperties
        :type request: :class:`huaweicloudsdkiotda.v5.ListPropertiesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListPropertiesResponse`
        """
        http_info = self._list_properties_http_info(request)
        return self._call_api(**http_info)

    def list_properties_invoker(self, request):
        http_info = self._list_properties_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_properties_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/properties",
            "request_type": request.__class__.__name__,
            "response_type": "ListPropertiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'service_id' in local_var_params:
            query_params.append(('service_id', local_var_params['service_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_properties(self, request):
        r"""修改设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口向指定设备下发属性。平台负责将属性以同步方式发送给设备，并将设备执行属性结果同步返回。
        注意：此接口适用于MQTT设备，暂不支持NB-IoT设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProperties
        :type request: :class:`huaweicloudsdkiotda.v5.UpdatePropertiesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdatePropertiesResponse`
        """
        http_info = self._update_properties_http_info(request)
        return self._call_api(**http_info)

    def update_properties_invoker(self, request):
        http_info = self._update_properties_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_properties_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/devices/{device_id}/properties",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePropertiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_provisioning_template(self, request):
        r"""创建预调配模板

        应用服务器可调用此接口在物联网平台创建一个预调配模板。用户的设备未在平台注册时，可以通过预调配模板在设备首次接入物联网平台时将设备信息自动注册到物联网平台。
        - 该预调配模板至少需要绑定到一个设备CA证书下才能生效。
        - 一个实例最多可有10个预调配模板。
        - 仅标准版实例、企业版实例支持该接口调用，基础版不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProvisioningTemplate
        :type request: :class:`huaweicloudsdkiotda.v5.CreateProvisioningTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateProvisioningTemplateResponse`
        """
        http_info = self._create_provisioning_template_http_info(request)
        return self._call_api(**http_info)

    def create_provisioning_template_invoker(self, request):
        http_info = self._create_provisioning_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_provisioning_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/provisioning-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProvisioningTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_provisioning_template(self, request):
        r"""删除预调配模板

        应用服务器可调用此接口在物联网平台上删除指定预调配模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProvisioningTemplate
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteProvisioningTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteProvisioningTemplateResponse`
        """
        http_info = self._delete_provisioning_template_http_info(request)
        return self._call_api(**http_info)

    def delete_provisioning_template_invoker(self, request):
        http_info = self._delete_provisioning_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_provisioning_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/provisioning-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProvisioningTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_provisioning_templates(self, request):
        r"""查询预调配模板列表

        应用服务器可调用此接口在物联网平台查询预调配模板列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProvisioningTemplates
        :type request: :class:`huaweicloudsdkiotda.v5.ListProvisioningTemplatesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListProvisioningTemplatesResponse`
        """
        http_info = self._list_provisioning_templates_http_info(request)
        return self._call_api(**http_info)

    def list_provisioning_templates_invoker(self, request):
        http_info = self._list_provisioning_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_provisioning_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/provisioning-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListProvisioningTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_name' in local_var_params:
            query_params.append(('template_name', local_var_params['template_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_provisioning_template(self, request):
        r"""查询预调配模板详情

        应用服务器可调用此接口在物联网平台查询指定预调配模板ID的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProvisioningTemplate
        :type request: :class:`huaweicloudsdkiotda.v5.ShowProvisioningTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowProvisioningTemplateResponse`
        """
        http_info = self._show_provisioning_template_http_info(request)
        return self._call_api(**http_info)

    def show_provisioning_template_invoker(self, request):
        http_info = self._show_provisioning_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_provisioning_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/provisioning-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProvisioningTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_provisioning_template(self, request):
        r"""更新指定id的预调配模板信息

        应用服务器可调用此接口在物联网平台更新指定id的预调配模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProvisioningTemplate
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateProvisioningTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateProvisioningTemplateResponse`
        """
        http_info = self._update_provisioning_template_http_info(request)
        return self._call_api(**http_info)

    def update_provisioning_template_invoker(self, request):
        http_info = self._update_provisioning_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_provisioning_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/provisioning-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProvisioningTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_routing_rule(self, request):
        r"""创建规则触发条件

        应用服务器可调用此接口在物联网平台创建一条规则触发条件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRoutingRule
        :type request: :class:`huaweicloudsdkiotda.v5.CreateRoutingRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateRoutingRuleResponse`
        """
        http_info = self._create_routing_rule_http_info(request)
        return self._call_api(**http_info)

    def create_routing_rule_invoker(self, request):
        http_info = self._create_routing_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_routing_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/routing-rule/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRoutingRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_rule_action(self, request):
        r"""创建规则动作

        应用服务器可调用此接口在物联网平台创建一条规则动作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRuleAction
        :type request: :class:`huaweicloudsdkiotda.v5.CreateRuleActionRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateRuleActionResponse`
        """
        http_info = self._create_rule_action_http_info(request)
        return self._call_api(**http_info)

    def create_rule_action_invoker(self, request):
        http_info = self._create_rule_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_rule_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/routing-rule/actions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRuleActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_routing_rule(self, request):
        r"""删除规则触发条件

        应用服务器可调用此接口删除物联网平台中的指定规则条件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRoutingRule
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteRoutingRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteRoutingRuleResponse`
        """
        http_info = self._delete_routing_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_routing_rule_invoker(self, request):
        http_info = self._delete_routing_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_routing_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/routing-rule/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRoutingRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_rule_action(self, request):
        r"""删除规则动作

        应用服务器可调用此接口删除物联网平台中的指定规则动作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRuleAction
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteRuleActionRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteRuleActionResponse`
        """
        http_info = self._delete_rule_action_http_info(request)
        return self._call_api(**http_info)

    def delete_rule_action_invoker(self, request):
        http_info = self._delete_rule_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_rule_action_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/routing-rule/actions/{action_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRuleActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_routing_rules(self, request):
        r"""查询规则条件列表

        应用服务器可调用此接口查询物联网平台中设置的规则条件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRoutingRules
        :type request: :class:`huaweicloudsdkiotda.v5.ListRoutingRulesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListRoutingRulesResponse`
        """
        http_info = self._list_routing_rules_http_info(request)
        return self._call_api(**http_info)

    def list_routing_rules_invoker(self, request):
        http_info = self._list_routing_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_routing_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/routing-rule/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRoutingRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
        if 'event' in local_var_params:
            query_params.append(('event', local_var_params['event']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'rule_name' in local_var_params:
            query_params.append(('rule_name', local_var_params['rule_name']))
        if 'active' in local_var_params:
            query_params.append(('active', local_var_params['active']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_rule_actions(self, request):
        r"""查询规则动作列表

        应用服务器可调用此接口查询物联网平台中设置的规则动作列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRuleActions
        :type request: :class:`huaweicloudsdkiotda.v5.ListRuleActionsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListRuleActionsResponse`
        """
        http_info = self._list_rule_actions_http_info(request)
        return self._call_api(**http_info)

    def list_rule_actions_invoker(self, request):
        http_info = self._list_rule_actions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rule_actions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/routing-rule/actions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRuleActionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
        if 'channel' in local_var_params:
            query_params.append(('channel', local_var_params['channel']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_routing_rule(self, request):
        r"""查询规则条件

        应用服务器可调用此接口查询物联网平台中指定规则条件的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRoutingRule
        :type request: :class:`huaweicloudsdkiotda.v5.ShowRoutingRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowRoutingRuleResponse`
        """
        http_info = self._show_routing_rule_http_info(request)
        return self._call_api(**http_info)

    def show_routing_rule_invoker(self, request):
        http_info = self._show_routing_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_routing_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/routing-rule/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRoutingRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_rule_action(self, request):
        r"""查询规则动作

        应用服务器可调用此接口查询物联网平台中指定规则动作的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRuleAction
        :type request: :class:`huaweicloudsdkiotda.v5.ShowRuleActionRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowRuleActionResponse`
        """
        http_info = self._show_rule_action_http_info(request)
        return self._call_api(**http_info)

    def show_rule_action_invoker(self, request):
        http_info = self._show_rule_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_rule_action_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/routing-rule/actions/{action_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRuleActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_routing_rule(self, request):
        r"""修改规则触发条件

        应用服务器可调用此接口修改物联网平台中指定规则条件的配置参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRoutingRule
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateRoutingRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRoutingRuleResponse`
        """
        http_info = self._update_routing_rule_http_info(request)
        return self._call_api(**http_info)

    def update_routing_rule_invoker(self, request):
        http_info = self._update_routing_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_routing_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/routing-rule/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoutingRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_rule_action(self, request):
        r"""修改规则动作

        应用服务器可调用此接口修改物联网平台中指定规则动作的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRuleAction
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateRuleActionRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRuleActionResponse`
        """
        http_info = self._update_rule_action_http_info(request)
        return self._call_api(**http_info)

    def update_rule_action_invoker(self, request):
        http_info = self._update_rule_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_rule_action_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/routing-rule/actions/{action_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRuleActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def change_rule_status(self, request):
        r"""修改规则状态

        应用服务器可调用此接口修改物联网平台中指定规则的状态，激活或者去激活规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeRuleStatus
        :type request: :class:`huaweicloudsdkiotda.v5.ChangeRuleStatusRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ChangeRuleStatusResponse`
        """
        http_info = self._change_rule_status_http_info(request)
        return self._call_api(**http_info)

    def change_rule_status_invoker(self, request):
        http_info = self._change_rule_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_rule_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/rules/{rule_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeRuleStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_rule(self, request):
        r"""创建规则

        应用服务器可调用此接口在物联网平台创建一条规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRule
        :type request: :class:`huaweicloudsdkiotda.v5.CreateRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateRuleResponse`
        """
        http_info = self._create_rule_http_info(request)
        return self._call_api(**http_info)

    def create_rule_invoker(self, request):
        http_info = self._create_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_rule(self, request):
        r"""删除规则

        应用服务器可调用此接口删除物联网平台中的指定规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteRuleResponse`
        """
        http_info = self._delete_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_rule_invoker(self, request):
        http_info = self._delete_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_rules(self, request):
        r"""查询规则列表

        应用服务器可调用此接口查询物联网平台中设置的规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRules
        :type request: :class:`huaweicloudsdkiotda.v5.ListRulesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListRulesResponse`
        """
        http_info = self._list_rules_http_info(request)
        return self._call_api(**http_info)

    def list_rules_invoker(self, request):
        http_info = self._list_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'rule_type' in local_var_params:
            query_params.append(('rule_type', local_var_params['rule_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_rule(self, request):
        r"""查询规则

        应用服务器可调用此接口查询物联网平台中指定规则的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRule
        :type request: :class:`huaweicloudsdkiotda.v5.ShowRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowRuleResponse`
        """
        http_info = self._show_rule_http_info(request)
        return self._call_api(**http_info)

    def show_rule_invoker(self, request):
        http_info = self._show_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_rule(self, request):
        r"""修改规则

        应用服务器可调用此接口修改物联网平台中指定规则的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRule
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRuleResponse`
        """
        http_info = self._update_rule_http_info(request)
        return self._call_api(**http_info)

    def update_rule_invoker(self, request):
        http_info = self._update_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_resources_by_tags(self, request):
        r"""按标签查询资源

        应用服务器可调用此接口查询绑定了指定标签的资源。当前支持标签的资源有Device(设备)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourcesByTags
        :type request: :class:`huaweicloudsdkiotda.v5.ListResourcesByTagsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListResourcesByTagsResponse`
        """
        http_info = self._list_resources_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resources_by_tags_invoker(self, request):
        http_info = self._list_resources_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resources_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/tags/query-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesByTagsResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def tag_device(self, request):
        r"""绑定标签

        应用服务器可调用此接口为指定资源绑定标签。当前支持标签的资源有Device(设备)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagDevice
        :type request: :class:`huaweicloudsdkiotda.v5.TagDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.TagDeviceResponse`
        """
        http_info = self._tag_device_http_info(request)
        return self._call_api(**http_info)

    def tag_device_invoker(self, request):
        http_info = self._tag_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _tag_device_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/tags/bind-resource",
            "request_type": request.__class__.__name__,
            "response_type": "TagDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def untag_device(self, request):
        r"""解绑标签

        应用服务器可调用此接口为指定资源解绑标签。当前支持标签的资源有Device(设备)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagDevice
        :type request: :class:`huaweicloudsdkiotda.v5.UntagDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UntagDeviceResponse`
        """
        http_info = self._untag_device_http_info(request)
        return self._call_api(**http_info)

    def untag_device_invoker(self, request):
        http_info = self._untag_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _untag_device_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/tags/unbind-resource",
            "request_type": request.__class__.__name__,
            "response_type": "UntagDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def add_tunnel(self, request):
        r"""创建设备隧道

        用户可以通过该接口创建隧道（WebSocket协议），应用服务器和设备可以通过该隧道进行数据传输。
        
        - 该API接口在基础版不支持。
        - 该API调用后平台会向对应的MQTT/MQTTS设备下发隧道地址及密钥，同时给应用服务器也返回隧道地址及密钥，设备可以通过该地址及密钥创建WebSocket协议连接。
        - 一个设备无法创建多个隧道。
        - 具体应用可见“设备远程登录”功能，请参见[[设备远程登录](https://support.huaweicloud.com/usermanual-iothub/iot_01_00301.html)](tag:hws)[[设备远程登录](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_00301.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddTunnel
        :type request: :class:`huaweicloudsdkiotda.v5.AddTunnelRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddTunnelResponse`
        """
        http_info = self._add_tunnel_http_info(request)
        return self._call_api(**http_info)

    def add_tunnel_invoker(self, request):
        http_info = self._add_tunnel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_tunnel_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/iot/{project_id}/tunnels",
            "request_type": request.__class__.__name__,
            "response_type": "AddTunnelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def close_device_tunnel(self, request):
        r"""关闭设备隧道

        应用服务器可通过该接口关闭某个设备隧道。关闭后可以再次连接。
        - 该API接口在基础版不支持。
        - 具体应用可见“设备远程登录”功能，请参见[[设备远程登录](https://support.huaweicloud.com/usermanual-iothub/iot_01_00301.html)](tag:hws)[[设备远程登录](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_00301.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CloseDeviceTunnel
        :type request: :class:`huaweicloudsdkiotda.v5.CloseDeviceTunnelRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CloseDeviceTunnelResponse`
        """
        http_info = self._close_device_tunnel_http_info(request)
        return self._call_api(**http_info)

    def close_device_tunnel_invoker(self, request):
        http_info = self._close_device_tunnel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _close_device_tunnel_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/iot/{project_id}/tunnels/{tunnel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CloseDeviceTunnelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tunnel_id' in local_var_params:
            path_params['tunnel_id'] = local_var_params['tunnel_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_device_tunnel(self, request):
        r"""删除设备隧道

        用户可通过该接口删除某个设备隧道。删除后该通道不存在，无法再次连接。
        - 该API接口在基础版不支持。
        - 具体应用可见“设备远程登录”功能，请参见[[设备远程登录](https://support.huaweicloud.com/usermanual-iothub/iot_01_00301.html)](tag:hws)[[设备远程登录](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_00301.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeviceTunnel
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceTunnelRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceTunnelResponse`
        """
        http_info = self._delete_device_tunnel_http_info(request)
        return self._call_api(**http_info)

    def delete_device_tunnel_invoker(self, request):
        http_info = self._delete_device_tunnel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_device_tunnel_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/iot/{project_id}/tunnels/{tunnel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceTunnelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tunnel_id' in local_var_params:
            path_params['tunnel_id'] = local_var_params['tunnel_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def list_device_tunnels(self, request):
        r"""查询设备所有隧道

        用户可通过该接口查询某项目下的所有设备隧道，以实现对设备管理。应用服务器可通过此接口向平台查询设备隧道建立的情况。
        - 该API接口在基础版不支持。
        - 具体应用可见“设备远程登录”功能，请参见[[设备远程登录](https://support.huaweicloud.com/usermanual-iothub/iot_01_00301.html)](tag:hws)[[设备远程登录](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_00301.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceTunnels
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceTunnelsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceTunnelsResponse`
        """
        http_info = self._list_device_tunnels_http_info(request)
        return self._call_api(**http_info)

    def list_device_tunnels_invoker(self, request):
        http_info = self._list_device_tunnels_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_device_tunnels_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/tunnels",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeviceTunnelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_device_tunnel(self, request):
        r"""查询设备隧道

        用户可通过该接口查询某项目中的某个设备隧道，查看该设备隧道的信息与连接情况。应用服务器可调用此接口向平台查询设备隧道建立情况。
        - 该API接口在基础版不支持。
        - 具体应用可见“设备远程登录”功能，请参见[[设备远程登录](https://support.huaweicloud.com/usermanual-iothub/iot_01_00301.html)](tag:hws)[[设备远程登录](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_00301.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceTunnel
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceTunnelRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceTunnelResponse`
        """
        http_info = self._show_device_tunnel_http_info(request)
        return self._call_api(**http_info)

    def show_device_tunnel_invoker(self, request):
        http_info = self._show_device_tunnel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_tunnel_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/iot/{project_id}/tunnels/{tunnel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceTunnelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tunnel_id' in local_var_params:
            path_params['tunnel_id'] = local_var_params['tunnel_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

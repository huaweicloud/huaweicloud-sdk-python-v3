# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


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
        """生成接入凭证

        接入凭证是用于客户端使用AMQP等协议与平台建链的一个认证凭据。只保留一条记录，如果重复调用只会重置接入凭证，使得之前的失效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccessCode
        :type request: :class:`huaweicloudsdkiotda.v5.CreateAccessCodeRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateAccessCodeResponse`
        """
        return self._create_access_code_with_http_info(request)

    def _create_access_code_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/auth/accesscode',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAccessCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_queue(self, request):
        """创建AMQP队列

        应用服务器可调用此接口在物联网平台创建一个AMQP队列。每个租户只能创建100个队列，若超过规格，则创建失败，若队列名称与已有的队列名称相同，则创建失败。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddQueue
        :type request: :class:`huaweicloudsdkiotda.v5.AddQueueRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddQueueResponse`
        """
        return self._add_queue_with_http_info(request)

    def _add_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/amqp-queues',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_queue(self, request):
        """查询AMQP列表

        应用服务器可调用此接口查询物联网平台中的AMQP队列信息列表。可通过队列名称作模糊查询，支持分页。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowQueue
        :type request: :class:`huaweicloudsdkiotda.v5.BatchShowQueueRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.BatchShowQueueResponse`
        """
        return self._batch_show_queue_with_http_info(request)

    def _batch_show_queue_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/amqp-queues',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_queue(self, request):
        """删除AMQP队列

        应用服务器可调用此接口在物联网平台上删除指定AMQP队列。若当前队列正在使用，则会删除失败。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteQueue
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteQueueRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteQueueResponse`
        """
        return self._delete_queue_with_http_info(request)

    def _delete_queue_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/amqp-queues/{queue_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_queue(self, request):
        """查询单个AMQP队列

        应用服务器可调用此接口查询物联网平台中指定队列的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQueue
        :type request: :class:`huaweicloudsdkiotda.v5.ShowQueueRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowQueueResponse`
        """
        return self._show_queue_with_http_info(request)

    def _show_queue_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/amqp-queues/{queue_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_application(self, request):
        """创建资源空间

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口创建资源空间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddApplication
        :type request: :class:`huaweicloudsdkiotda.v5.AddApplicationRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddApplicationResponse`
        """
        return self._add_application_with_http_info(request)

    def _add_application_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_application(self, request):
        """删除资源空间

        删除指定资源空间。删除资源空间属于高危操作，删除资源空间后，该空间下的产品、设备等资源将不可用，请谨慎操作！
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteApplicationResponse`
        """
        return self._delete_application_with_http_info(request)

    def _delete_application_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/apps/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_application(self, request):
        """查询资源空间

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口查询指定资源空间详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplication
        :type request: :class:`huaweicloudsdkiotda.v5.ShowApplicationRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowApplicationResponse`
        """
        return self._show_application_with_http_info(request)

    def _show_application_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_applications(self, request):
        """查询资源空间列表

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口查询资源空间列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplications
        :type request: :class:`huaweicloudsdkiotda.v5.ShowApplicationsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowApplicationsResponse`
        """
        return self._show_applications_with_http_info(request)

    def _show_applications_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApplicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_async_command(self, request):
        """下发异步设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发异步命令，以实现对设备的控制。平台负责将命令发送给设备，并将设备执行命令结果异步通知应用服务器。 命令执行结果支持灵活的数据流转，应用服务器通过调用物联网平台的创建规则触发条件（Resource:device.command.status，Event:update）、创建规则动作并激活规则后，当命令状态变更时，物联网平台会根据规则将结果发送到规则指定的服务器，如用户自定义的HTTP服务器，AMQP服务器，以及华为云的其他储存服务器等, 详情参考[[设备命令状态变更通知](https://support.huaweicloud.com/api-iothub/iot_06_v5_01212.html)](tag:hws)[[设备命令状态变更通知](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_01212.html)](tag:hws_hk)。
        注意：
        - 此接口适用于NB设备异步命令下发，暂不支持其他协议类型设备命令下发。
        - 此接口仅支持单个设备异步命令下发，如需多个设备异步命令下发，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAsyncCommand
        :type request: :class:`huaweicloudsdkiotda.v5.CreateAsyncCommandRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateAsyncCommandResponse`
        """
        return self._create_async_command_with_http_info(request)

    def _create_async_command_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/async-commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAsyncCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_async_device_command(self, request):
        """查询指定id的命令

        物联网平台可查询指定id的命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAsyncDeviceCommand
        :type request: :class:`huaweicloudsdkiotda.v5.ShowAsyncDeviceCommandRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowAsyncDeviceCommandResponse`
        """
        return self._show_async_device_command_with_http_info(request)

    def _show_async_device_command_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/async-commands/{command_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAsyncDeviceCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_batch_task(self, request):
        """创建批量任务

        应用服务器可调用此接口为创建批量处理任务，对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结设备、批量解冻设备、批量创建命令、批量创建消息任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.CreateBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateBatchTaskResponse`
        """
        return self._create_batch_task_with_http_info(request)

    def _create_batch_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/batchtasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBatchTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_batch_task(self, request):
        """删除批量任务

        应用服务器可调用此接口删除物联网平台中已经完成（状态为成功，失败，部分成功，已停止）的批量任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteBatchTaskResponse`
        """
        return self._delete_batch_task_with_http_info(request)

    def _delete_batch_task_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBatchTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_batch_tasks(self, request):
        """查询批量任务列表

        应用服务器可调用此接口查询物联网平台中批量任务列表，每一个任务又包括具体的任务内容、任务状态、任务完成情况统计等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBatchTasks
        :type request: :class:`huaweicloudsdkiotda.v5.ListBatchTasksRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListBatchTasksResponse`
        """
        return self._list_batch_tasks_with_http_info(request)

    def _list_batch_tasks_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBatchTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def retry_batch_task(self, request):
        """重试批量任务

        应用服务器可调用此接口重试批量任务，目前只支持task_type为firmwareUpgrade，softwareUpgrade。如果task_id对应任务已经成功、停止、正在停止、等待中或初始化中，则不可以调用该接口。如果请求Body为{}，则调用该接口后会重新执行所有状态为失败、失败待重试和已停止的子任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.RetryBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.RetryBatchTaskResponse`
        """
        return self._retry_batch_task_with_http_info(request)

    def _retry_batch_task_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/batchtasks/{task_id}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RetryBatchTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_batch_task(self, request):
        """查询批量任务

        应用服务器可调用此接口查询物联网平台中指定批量任务的信息，包括任务内容、任务状态、任务完成情况统计以及子任务列表等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.ShowBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowBatchTaskResponse`
        """
        return self._show_batch_task_with_http_info(request)

    def _show_batch_task_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBatchTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_batch_task(self, request):
        """停止批量任务

        应用服务器可调用此接口停止批量任务，目前只支持task_type为firmwareUpgrade，softwareUpgrade。如果task_id对应任务已经完成（成功、失败、部分成功，已经停止）或正在停止中，则不可以调用该接口。如果请求Body为{}，则调用该接口后会停止所有正在执行中、等待中和失败待重试状态的子任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopBatchTask
        :type request: :class:`huaweicloudsdkiotda.v5.StopBatchTaskRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.StopBatchTaskResponse`
        """
        return self._stop_batch_task_with_http_info(request)

    def _stop_batch_task_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/batchtasks/{task_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopBatchTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_batch_task_file(self, request):
        """删除批量任务文件

        应用服务器可调用此接口删除批量任务文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBatchTaskFile
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteBatchTaskFileRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteBatchTaskFileResponse`
        """
        return self._delete_batch_task_file_with_http_info(request)

    def _delete_batch_task_file_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtask-files/{file_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBatchTaskFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_batch_task_files(self, request):
        """查询批量任务文件列表

        应用服务器可调用此接口查询批量任务文件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBatchTaskFiles
        :type request: :class:`huaweicloudsdkiotda.v5.ListBatchTaskFilesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListBatchTaskFilesResponse`
        """
        return self._list_batch_task_files_with_http_info(request)

    def _list_batch_task_files_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtask-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBatchTaskFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_batch_task_file(self, request):
        """上传批量任务文件

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
        return self._upload_batch_task_file_with_http_info(request)

    def _upload_batch_task_file_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtask-files',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadBatchTaskFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def broadcast_message(self, request):
        """下发广播消息

        应用服务器可调用此接口向订阅了指定Topic的所有在线设备发布广播消息。应用将广播消息下发给平台后，平台会先返回应用响应结果，再将消息广播给设备。
        注意：
        - 此接口只适用于使用MQTT协议接入的设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BroadcastMessage
        :type request: :class:`huaweicloudsdkiotda.v5.BroadcastMessageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.BroadcastMessageResponse`
        """
        return self._broadcast_message_with_http_info(request)

    def _broadcast_message_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/broadcast-messages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BroadcastMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_certificate(self, request):
        """上传设备CA证书

        应用服务器可调用此接口在物联网平台上传设备CA证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddCertificate
        :type request: :class:`huaweicloudsdkiotda.v5.AddCertificateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddCertificateResponse`
        """
        return self._add_certificate_with_http_info(request)

    def _add_certificate_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/certificates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_certificate(self, request):
        """验证设备CA证书

        应用服务器可调用此接口在物联网平台验证设备的CA证书，目的是为了验证用户持有设备CA证书的私钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckCertificate
        :type request: :class:`huaweicloudsdkiotda.v5.CheckCertificateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CheckCertificateResponse`
        """
        return self._check_certificate_with_http_info(request)

    def _check_certificate_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/certificates/{certificate_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_certificate(self, request):
        """删除设备CA证书

        应用服务器可调用此接口在物联网平台删除设备CA证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteCertificateResponse`
        """
        return self._delete_certificate_with_http_info(request)

    def _delete_certificate_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/certificates/{certificate_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_certificates(self, request):
        """获取设备CA证书列表

        应用服务器可调用此接口在物联网平台获取设备CA证书列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkiotda.v5.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListCertificatesResponse`
        """
        return self._list_certificates_with_http_info(request)

    def _list_certificates_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/certificates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCertificatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_command(self, request):
        """下发设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发命令，以实现对设备的同步控制。平台负责将命令以同步方式发送给设备，并将设备执行命令结果同步返回, 如果设备没有响应，平台会返回给应用服务器超时，平台超时时间是20秒。如果命令下发需要超过20秒，建议采用[[消息下发](https://support.huaweicloud.com/api-iothub/iot_06_v5_0059.html)](tag:hws)[[消息下发](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0059.html)](tag:hws_hk)。
        注意：
        - 此接口适用于MQTT设备同步命令下发，暂不支持NB-IoT设备命令下发。
        - 此接口仅支持单个设备同步命令下发，如需多个设备同步命令下发，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCommand
        :type request: :class:`huaweicloudsdkiotda.v5.CreateCommandRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateCommandResponse`
        """
        return self._create_command_with_http_info(request)

    def _create_command_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_device_group(self, request):
        """添加设备组

        应用服务器可调用此接口新建设备组，一个华为云账号下最多可有1,000个设备组，包括父设备组和子设备组。设备组的最大层级关系不超过5层，即群组形成的关系树最大深度不超过5。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDeviceGroup
        :type request: :class:`huaweicloudsdkiotda.v5.AddDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddDeviceGroupResponse`
        """
        return self._add_device_group_with_http_info(request)

    def _add_device_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/device-group',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddDeviceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_or_delete_device_in_group(self, request):
        """管理设备组中的设备

        应用服务器可调用此接口管理设备组中的设备。单个设备组内最多添加20,000个设备，一个设备最多可以被添加到10个设备组中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrDeleteDeviceInGroup
        :type request: :class:`huaweicloudsdkiotda.v5.CreateOrDeleteDeviceInGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateOrDeleteDeviceInGroupResponse`
        """
        return self._create_or_delete_device_in_group_with_http_info(request)

    def _create_or_delete_device_in_group_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group/{group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrDeleteDeviceInGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_device_group(self, request):
        """删除设备组

        应用服务器可调用此接口删除指定设备组，如果该设备组存在子设备组或者该设备组中存在设备，必须先删除子设备组并将设备从该设备组移除，才能删除该设备组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeviceGroup
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceGroupResponse`
        """
        return self._delete_device_group_with_http_info(request)

    def _delete_device_group_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDeviceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_device_groups(self, request):
        """查询设备组列表

        应用服务器可调用此接口查询物联网平台中的设备组信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceGroups
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceGroupsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceGroupsResponse`
        """
        return self._list_device_groups_with_http_info(request)

    def _list_device_groups_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDeviceGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_group(self, request):
        """查询设备组

        应用服务器可调用此接口查询指定设备组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceGroup
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceGroupResponse`
        """
        return self._show_device_group_with_http_info(request)

    def _show_device_group_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeviceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_devices_in_group(self, request):
        """查询设备组设备列表

        应用服务器可调用此接口查询指定设备组下的设备列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDevicesInGroup
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDevicesInGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDevicesInGroupResponse`
        """
        return self._show_devices_in_group_with_http_info(request)

    def _show_devices_in_group_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group/{group_id}/devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDevicesInGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_group(self, request):
        """修改设备组

        应用服务器可调用此接口修改物联网平台中指定设备组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeviceGroup
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDeviceGroupResponse`
        """
        return self._update_device_group_with_http_info(request)

    def _update_device_group_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/device-group/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDeviceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_device(self, request):
        """创建设备

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
        return self._add_device_with_http_info(request)

    def _add_device_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_device(self, request):
        """删除设备

        应用服务器可调用此接口在物联网平台上删除指定设备。若设备下连接了非直连设备，则必须把设备下的非直连设备都删除后，才能删除该设备。该接口仅支持删除单个设备，如需批量删除设备，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDevice
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceResponse`
        """
        return self._delete_device_with_http_info(request)

    def _delete_device_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def freeze_device(self, request):
        """冻结设备

        应用服务器可调用此接口冻结设备，设备冻结后不能再连接上线，可以通过解冻设备接口解除设备冻结。注意，当前仅支持冻结与平台直连的设备。该接口仅支持冻结单个设备，如需批量冻结设备，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for FreezeDevice
        :type request: :class:`huaweicloudsdkiotda.v5.FreezeDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.FreezeDeviceResponse`
        """
        return self._freeze_device_with_http_info(request)

    def _freeze_device_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/freeze',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='FreezeDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_devices(self, request):
        """查询设备列表

        应用服务器可调用此接口查询物联网平台中的设备信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDevices
        :type request: :class:`huaweicloudsdkiotda.v5.ListDevicesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDevicesResponse`
        """
        return self._list_devices_with_http_info(request)

    def _list_devices_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_device_secret(self, request):
        """重置设备密钥

        应用服务器可调用此接口重置设备密钥，携带指定密钥时平台将设备密钥重置为指定的密钥，不携带密钥时平台将自动生成一个新的随机密钥返回。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetDeviceSecret
        :type request: :class:`huaweicloudsdkiotda.v5.ResetDeviceSecretRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ResetDeviceSecretResponse`
        """
        return self._reset_device_secret_with_http_info(request)

    def _reset_device_secret_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetDeviceSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_fingerprint(self, request):
        """重置设备指纹

        应用服务器可调用此接口重置设备指纹。携带指定设备指纹时将之重置为指定值；不携带时将之置空，后续设备第一次接入时，该设备指纹的值将设置为第一次接入时的证书指纹。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetFingerprint
        :type request: :class:`huaweicloudsdkiotda.v5.ResetFingerprintRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ResetFingerprintResponse`
        """
        return self._reset_fingerprint_with_http_info(request)

    def _reset_fingerprint_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/reset-fingerprint',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetFingerprintResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_devices(self, request):
        """灵活搜索设备列表

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
        return self._search_devices_with_http_info(request)

    def _search_devices_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/search/query-devices',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device(self, request):
        """查询设备

        应用服务器可调用此接口查询物联网平台中指定设备的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDevice
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceResponse`
        """
        return self._show_device_with_http_info(request)

    def _show_device_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def unfreeze_device(self, request):
        """解冻设备

        应用服务器可调用此接口解冻设备，解除冻结后，设备可以连接上线。该接口仅支持解冻单个设备，如需批量解冻设备，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnfreezeDevice
        :type request: :class:`huaweicloudsdkiotda.v5.UnfreezeDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UnfreezeDeviceResponse`
        """
        return self._unfreeze_device_with_http_info(request)

    def _unfreeze_device_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/unfreeze',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UnfreezeDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device(self, request):
        """修改设备

        应用服务器可调用此接口修改物联网平台中指定设备的基本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDevice
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateDeviceResponse`
        """
        return self._update_device_with_http_info(request)

    def _update_device_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/devices/{device_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_shadow(self, request):
        """查询设备影子数据

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
        return self._show_device_shadow_with_http_info(request)

    def _show_device_shadow_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/shadow',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeviceShadowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_shadow_desired_data(self, request):
        """配置设备影子预期数据

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
        return self._update_device_shadow_desired_data_with_http_info(request)

    def _update_device_shadow_desired_data_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/shadow',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDeviceShadowDesiredDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_message(self, request):
        """下发设备消息

        物联网平台可向设备下发消息，应用服务器可调用此接口向指定设备下发消息，以实现对设备的控制。应用将消息下发给平台后，平台返回应用响应结果，平台再将消息发送给设备。平台返回应用响应结果不一定是设备接收结果，建议用户应用通过订阅[[设备消息状态变更通知](https://support.huaweicloud.com/api-iothub/iot_06_v5_01203.html)](tag:hws)[[设备消息状态变更通知](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_01203.html)](tag:hws_hk)，订阅后平台会将设备接收结果推送给订阅的应用。
        注意：
        - 此接口适用于MQTT设备消息下发，暂不支持其他协议接入的设备消息下发。
        - 此接口仅支持单个设备消息下发，如需多个设备消息下发，请参见 [[创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)](tag:hws)[[创建批量任务](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0045.html)](tag:hws_hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMessage
        :type request: :class:`huaweicloudsdkiotda.v5.CreateMessageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateMessageResponse`
        """
        return self._create_message_with_http_info(request)

    def _create_message_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/messages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_device_messages(self, request):
        """查询设备消息

        应用服务器可调用此接口查询平台下发给设备的消息，平台为每个设备默认最多保存20条消息，超过20条后， 后续的消息会替换下发最早的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceMessages
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceMessagesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceMessagesResponse`
        """
        return self._list_device_messages_with_http_info(request)

    def _list_device_messages_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDeviceMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_message(self, request):
        """查询指定消息id的消息

        应用服务器可调用此接口查询平台下发给设备的指定消息id的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceMessage
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceMessageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceMessageResponse`
        """
        return self._show_device_message_with_http_info(request)

    def _show_device_message_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/messages/{message_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeviceMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_ota_package(self, request):
        """创建OTA升级包

        用户可调用此接口创建升级包关联OBS对象
        使用前提：使用该API需要您授权设备接入服务(IoTDA)的实例访问对象存储服务(OBS)以及 密钥管理服务(KMS Administrator)的权限。在“[[统一身份认证服务（IAM）](https://console.huaweicloud.com/iam)](tag:hws)[[统一身份认证服务（IAM）](https://console-intl.huaweicloud.com/iam)](tag:hws_hk) - 委托”中将委托名称为iotda_admin_trust的委托授权KMS Administrator和OBS OperateAccess
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOtaPackage
        :type request: :class:`huaweicloudsdkiotda.v5.CreateOtaPackageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateOtaPackageResponse`
        """
        return self._create_ota_package_with_http_info(request)

    def _create_ota_package_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/ota-upgrades/packages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOtaPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ota_package(self, request):
        """删除OTA升级包

        用户可调用此接口删除关联OBS对象的升级包信息，不会删除OBS上对象
        使用前提：使用该API需要您授权设备接入服务(IoTDA)的实例访问对象存储服务(OBS)以及 密钥管理服务(KMS Administrator)的权限。在“[[统一身份认证服务（IAM）](https://console.huaweicloud.com/iam)](tag:hws)[[统一身份认证服务（IAM）](https://console-intl.huaweicloud.com/iam)](tag:hws_hk) - 委托”中将委托名称为iotda_admin_trust的委托授权KMS Administrator和OBS OperateAccess
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOtaPackage
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteOtaPackageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteOtaPackageResponse`
        """
        return self._delete_ota_package_with_http_info(request)

    def _delete_ota_package_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/ota-upgrades/packages/{package_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteOtaPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ota_package_info(self, request):
        """查询OTA升级包列表

        用户可调用此接口查询关联OBS对象的升级包列表
        使用前提：使用该API需要您授权设备接入服务(IoTDA)的实例访问对象存储服务(OBS)以及 密钥管理服务(KMS Administrator)的权限。在“[[统一身份认证服务（IAM）](https://console.huaweicloud.com/iam)](tag:hws)[[统一身份认证服务（IAM）](https://console-intl.huaweicloud.com/iam)](tag:hws_hk) - 委托”中将委托名称为iotda_admin_trust的委托授权KMS Administrator和OBS OperateAccess
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOtaPackageInfo
        :type request: :class:`huaweicloudsdkiotda.v5.ListOtaPackageInfoRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListOtaPackageInfoResponse`
        """
        return self._list_ota_package_info_with_http_info(request)

    def _list_ota_package_info_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/ota-upgrades/packages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOtaPackageInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ota_package(self, request):
        """获取OTA升级包详情

        用户可调用此接口查询关联OBS对象的升级包详情
        使用前提：使用该API需要您授权设备接入服务(IoTDA)的实例访问对象存储服务(OBS)以及 密钥管理服务(KMS Administrator)的权限。在“[[统一身份认证服务（IAM）](https://console.huaweicloud.com/iam)](tag:hws)[[统一身份认证服务（IAM）](https://console-intl.huaweicloud.com/iam)](tag:hws_hk) - 委托”中将委托名称为iotda_admin_trust的委托授权KMS Administrator和OBS OperateAccess
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOtaPackage
        :type request: :class:`huaweicloudsdkiotda.v5.ShowOtaPackageRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowOtaPackageResponse`
        """
        return self._show_ota_package_with_http_info(request)

    def _show_ota_package_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/ota-upgrades/packages/{package_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOtaPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_product(self, request):
        """创建产品

        应用服务器可调用此接口创建产品。此接口仅创建了产品，没有创建和安装插件，如果需要对数据进行编解码，还需要在平台开发和安装插件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProduct
        :type request: :class:`huaweicloudsdkiotda.v5.CreateProductRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateProductResponse`
        """
        return self._create_product_with_http_info(request)

    def _create_product_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_product(self, request):
        """删除产品

        应用服务器可调用此接口删除已导入物联网平台的指定产品模型。此接口仅删除了产品，未删除关联的插件，在产品下存在设备时，该产品不允许删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProduct
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteProductRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteProductResponse`
        """
        return self._delete_product_with_http_info(request)

    def _delete_product_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products/{product_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_products(self, request):
        """查询产品列表

        应用服务器可调用此接口查询已导入物联网平台的产品模型信息列表，了解产品模型的概要信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkiotda.v5.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListProductsResponse`
        """
        return self._list_products_with_http_info(request)

    def _list_products_with_http_info(self, request):
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products',
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

    def show_product(self, request):
        """查询产品

        应用服务器可调用此接口查询已导入物联网平台的指定产品模型详细信息，包括产品模型的服务、属性、命令等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProduct
        :type request: :class:`huaweicloudsdkiotda.v5.ShowProductRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowProductResponse`
        """
        return self._show_product_with_http_info(request)

    def _show_product_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products/{product_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_product(self, request):
        """修改产品

        应用服务器可调用此接口修改已导入物联网平台的指定产品模型，包括产品模型的服务、属性、命令等。此接口仅修改了产品，未修改和安装插件，如果修改了产品中的service定义，且在平台中有对应的插件，请修改并重新安装插件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProduct
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateProductRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateProductResponse`
        """
        return self._update_product_with_http_info(request)

    def _update_product_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products/{product_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_properties(self, request):
        """查询设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口向设备发送指令用以查询设备的实时属性, 并由设备将属性查询的结果同步返回给应用服务器。
        注意：此接口适用于MQTT设备，暂不支持NB-IoT设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProperties
        :type request: :class:`huaweicloudsdkiotda.v5.ListPropertiesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListPropertiesResponse`
        """
        return self._list_properties_with_http_info(request)

    def _list_properties_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/properties',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPropertiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_properties(self, request):
        """修改设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口向指定设备下发属性。平台负责将属性以同步方式发送给设备，并将设备执行属性结果同步返回。
        注意：此接口适用于MQTT设备，暂不支持NB-IoT设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProperties
        :type request: :class:`huaweicloudsdkiotda.v5.UpdatePropertiesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdatePropertiesResponse`
        """
        return self._update_properties_with_http_info(request)

    def _update_properties_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/properties',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePropertiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_routing_rule(self, request):
        """创建规则触发条件

        应用服务器可调用此接口在物联网平台创建一条规则触发条件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRoutingRule
        :type request: :class:`huaweicloudsdkiotda.v5.CreateRoutingRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateRoutingRuleResponse`
        """
        return self._create_routing_rule_with_http_info(request)

    def _create_routing_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/routing-rule/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRoutingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_rule_action(self, request):
        """创建规则动作

        应用服务器可调用此接口在物联网平台创建一条规则动作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRuleAction
        :type request: :class:`huaweicloudsdkiotda.v5.CreateRuleActionRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateRuleActionResponse`
        """
        return self._create_rule_action_with_http_info(request)

    def _create_rule_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/routing-rule/actions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRuleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_routing_rule(self, request):
        """删除规则触发条件

        应用服务器可调用此接口删除物联网平台中的指定规则条件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRoutingRule
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteRoutingRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteRoutingRuleResponse`
        """
        return self._delete_routing_rule_with_http_info(request)

    def _delete_routing_rule_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRoutingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rule_action(self, request):
        """删除规则动作

        应用服务器可调用此接口删除物联网平台中的指定规则动作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRuleAction
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteRuleActionRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteRuleActionResponse`
        """
        return self._delete_rule_action_with_http_info(request)

    def _delete_rule_action_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/actions/{action_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRuleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_routing_rules(self, request):
        """查询规则条件列表

        应用服务器可调用此接口查询物联网平台中设置的规则条件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRoutingRules
        :type request: :class:`huaweicloudsdkiotda.v5.ListRoutingRulesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListRoutingRulesResponse`
        """
        return self._list_routing_rules_with_http_info(request)

    def _list_routing_rules_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRoutingRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rule_actions(self, request):
        """查询规则动作列表

        应用服务器可调用此接口查询物联网平台中设置的规则动作列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRuleActions
        :type request: :class:`huaweicloudsdkiotda.v5.ListRuleActionsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListRuleActionsResponse`
        """
        return self._list_rule_actions_with_http_info(request)

    def _list_rule_actions_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/actions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRuleActionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_routing_rule(self, request):
        """查询规则条件

        应用服务器可调用此接口查询物联网平台中指定规则条件的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRoutingRule
        :type request: :class:`huaweicloudsdkiotda.v5.ShowRoutingRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowRoutingRuleResponse`
        """
        return self._show_routing_rule_with_http_info(request)

    def _show_routing_rule_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRoutingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_rule_action(self, request):
        """查询规则动作

        应用服务器可调用此接口查询物联网平台中指定规则动作的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRuleAction
        :type request: :class:`huaweicloudsdkiotda.v5.ShowRuleActionRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowRuleActionResponse`
        """
        return self._show_rule_action_with_http_info(request)

    def _show_rule_action_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/actions/{action_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRuleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_routing_rule(self, request):
        """修改规则触发条件

        应用服务器可调用此接口修改物联网平台中指定规则条件的配置参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRoutingRule
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateRoutingRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRoutingRuleResponse`
        """
        return self._update_routing_rule_with_http_info(request)

    def _update_routing_rule_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/routing-rule/rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRoutingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_rule_action(self, request):
        """修改规则动作

        应用服务器可调用此接口修改物联网平台中指定规则动作的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRuleAction
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateRuleActionRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRuleActionResponse`
        """
        return self._update_rule_action_with_http_info(request)

    def _update_rule_action_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/routing-rule/actions/{action_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRuleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_rule_status(self, request):
        """修改规则状态

        应用服务器可调用此接口修改物联网平台中指定规则的状态，激活或者去激活规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeRuleStatus
        :type request: :class:`huaweicloudsdkiotda.v5.ChangeRuleStatusRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ChangeRuleStatusResponse`
        """
        return self._change_rule_status_with_http_info(request)

    def _change_rule_status_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/rules/{rule_id}/status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeRuleStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_rule(self, request):
        """创建规则

        应用服务器可调用此接口在物联网平台创建一条规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRule
        :type request: :class:`huaweicloudsdkiotda.v5.CreateRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CreateRuleResponse`
        """
        return self._create_rule_with_http_info(request)

    def _create_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rule(self, request):
        """删除规则

        应用服务器可调用此接口删除物联网平台中的指定规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteRuleResponse`
        """
        return self._delete_rule_with_http_info(request)

    def _delete_rule_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rules(self, request):
        """查询规则列表

        应用服务器可调用此接口查询物联网平台中设置的规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRules
        :type request: :class:`huaweicloudsdkiotda.v5.ListRulesRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListRulesResponse`
        """
        return self._list_rules_with_http_info(request)

    def _list_rules_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_rule(self, request):
        """查询规则

        应用服务器可调用此接口查询物联网平台中指定规则的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRule
        :type request: :class:`huaweicloudsdkiotda.v5.ShowRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowRuleResponse`
        """
        return self._show_rule_with_http_info(request)

    def _show_rule_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_rule(self, request):
        """修改规则

        应用服务器可调用此接口修改物联网平台中指定规则的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRule
        :type request: :class:`huaweicloudsdkiotda.v5.UpdateRuleRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRuleResponse`
        """
        return self._update_rule_with_http_info(request)

    def _update_rule_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resources_by_tags(self, request):
        """按标签查询资源

        应用服务器可调用此接口查询绑定了指定标签的资源。当前支持标签的资源有Device(设备)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourcesByTags
        :type request: :class:`huaweicloudsdkiotda.v5.ListResourcesByTagsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListResourcesByTagsResponse`
        """
        return self._list_resources_by_tags_with_http_info(request)

    def _list_resources_by_tags_with_http_info(self, request):
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
            resource_path='/v5/iot/{project_id}/tags/query-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourcesByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_device(self, request):
        """绑定标签

        应用服务器可调用此接口为指定资源绑定标签。当前支持标签的资源有Device(设备)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagDevice
        :type request: :class:`huaweicloudsdkiotda.v5.TagDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.TagDeviceResponse`
        """
        return self._tag_device_with_http_info(request)

    def _tag_device_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/tags/bind-resource',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def untag_device(self, request):
        """解绑标签

        应用服务器可调用此接口为指定资源解绑标签。当前支持标签的资源有Device(设备)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagDevice
        :type request: :class:`huaweicloudsdkiotda.v5.UntagDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.UntagDeviceResponse`
        """
        return self._untag_device_with_http_info(request)

    def _untag_device_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/tags/unbind-resource',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UntagDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_tunnel(self, request):
        """创建设备隧道

        创建设备隧道接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddTunnel
        :type request: :class:`huaweicloudsdkiotda.v5.AddTunnelRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.AddTunnelResponse`
        """
        return self._add_tunnel_with_http_info(request)

    def _add_tunnel_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/tunnels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddTunnelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def close_device_tunnel(self, request):
        """关闭设备隧道

        关闭设备隧道接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CloseDeviceTunnel
        :type request: :class:`huaweicloudsdkiotda.v5.CloseDeviceTunnelRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.CloseDeviceTunnelResponse`
        """
        return self._close_device_tunnel_with_http_info(request)

    def _close_device_tunnel_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/tunnels/{tunnel_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CloseDeviceTunnelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_device_tunnel(self, request):
        """删除设备隧道

        删除设备隧道接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeviceTunnel
        :type request: :class:`huaweicloudsdkiotda.v5.DeleteDeviceTunnelRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.DeleteDeviceTunnelResponse`
        """
        return self._delete_device_tunnel_with_http_info(request)

    def _delete_device_tunnel_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/tunnels/{tunnel_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDeviceTunnelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_device_tunnels(self, request):
        """查询设备所有隧道

        用户可通过该接口查询某项目下的所有设备隧道，以实现对设备管理。应用服务器可通过此接口向平台查询设备隧道建立的情况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeviceTunnels
        :type request: :class:`huaweicloudsdkiotda.v5.ListDeviceTunnelsRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ListDeviceTunnelsResponse`
        """
        return self._list_device_tunnels_with_http_info(request)

    def _list_device_tunnels_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/tunnels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDeviceTunnelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_tunnel(self, request):
        """查询设备隧道

        用户可通过该接口查询某项目中的某个设备隧道，查看该设备隧道的信息与连接情况。应用服务器可调用此接口向平台查询设备隧道建立情况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceTunnel
        :type request: :class:`huaweicloudsdkiotda.v5.ShowDeviceTunnelRequest`
        :rtype: :class:`huaweicloudsdkiotda.v5.ShowDeviceTunnelResponse`
        """
        return self._show_device_tunnel_with_http_info(request)

    def _show_device_tunnel_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/tunnels/{tunnel_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeviceTunnelResponse',
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

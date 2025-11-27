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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkesw'")


class EswAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkesw.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EswAsyncClient":
                raise TypeError("client type error, support client type is EswAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def bind_vport_async(self, request):
        r"""将一个虚拟IP绑定到二层连接上

        当您的二层连接创建成功后，您可以通过调用此接口将一个虚拟IP绑定到二层连接上。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BindVport
        :type request: :class:`huaweicloudsdkesw.v3.BindVportRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.BindVportResponse`
        """
        http_info = self._bind_vport_http_info(request)
        return self._call_api(**http_info)

    def bind_vport_async_invoker(self, request):
        http_info = self._bind_vport_http_info(request)
        return AsyncInvoker(self, http_info)

    def _bind_vport_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/l2cg/connections/{connection_id}/vports/bind",
            "request_type": request.__class__.__name__,
            "response_type": "BindVportResponse"
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""创建二层连接

        当您的ESW实例创建成功后，您可以通过调用此接口在该实例上创建一个二层连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConnection
        :type request: :class:`huaweicloudsdkesw.v3.CreateConnectionRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.CreateConnectionResponse`
        """
        http_info = self._create_connection_http_info(request)
        return self._call_api(**http_info)

    def create_connection_async_invoker(self, request):
        http_info = self._create_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/l2cg/instances/{instance_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectionResponse"
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

    def create_instance_async(self, request):
        r"""创建ESW实例

        您可通过调用本接口创建一个ESW实例。该接口是一个异步接口，当前创建ESW实例的请求下发成功后，会响应job_id以及实例ID等信息，需要通过[调用查询任务的执行状态查询job状态](ListResourceJobs.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkesw.v3.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_async_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/l2cg/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
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

    def delete_connection_async(self, request):
        r"""删除二层连接

        当您已创建的二层连接不再使用时，您可以通过调用该接口删除二层连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConnection
        :type request: :class:`huaweicloudsdkesw.v3.DeleteConnectionRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.DeleteConnectionResponse`
        """
        http_info = self._delete_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_connection_async_invoker(self, request):
        http_info = self._delete_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_connection_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/l2cg/instances/{instance_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']
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

    def delete_instance_async(self, request):
        r"""删除ESW实例

        当您创建的ESW实例不再使用时，您可以通过调用该接口删除ESW实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkesw.v3.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_async_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/l2cg/instances/{instance_id}",
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

    def list_availability_zones_async(self, request):
        r"""查询ESW实例可用区

        当您在创建ESW实例时，需要通过调用本接口获取ESW实例主备节点可分布的可用区列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkesw.v3.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ListAvailabilityZonesResponse`
        """
        http_info = self._list_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zones_async_invoker(self, request):
        http_info = self._list_availability_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_availability_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/availability-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZonesResponse"
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

    def list_connections_async(self, request):
        r"""查询实例下的二层连接列表

        当您的二层连接创建成功后，您可以通过调用此接口查询ESW实例下的二层连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConnections
        :type request: :class:`huaweicloudsdkesw.v3.ListConnectionsRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ListConnectionsResponse`
        """
        http_info = self._list_connections_http_info(request)
        return self._call_api(**http_info)

    def list_connections_async_invoker(self, request):
        http_info = self._list_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_connections_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/instances/{instance_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_connections_all_instances_async(self, request):
        r"""查询二层连接列表

        当您的二层连接创建成功后，您可以通过调用此接口查询租户所有二层连接信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConnectionsAllInstances
        :type request: :class:`huaweicloudsdkesw.v3.ListConnectionsAllInstancesRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ListConnectionsAllInstancesResponse`
        """
        http_info = self._list_connections_all_instances_http_info(request)
        return self._call_api(**http_info)

    def list_connections_all_instances_async_invoker(self, request):
        http_info = self._list_connections_all_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_connections_all_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectionsAllInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_flavors_async(self, request):
        r"""查询ESW实例规格列表

        查询租户可选用的ESW实例规格
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkesw.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_async_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
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

    def list_instances_async(self, request):
        r"""查询ESW实例列表

        当您的ESW实例创建成功后，您可以通过调用此接口查询所有ESW实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkesw.v3.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_async_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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
        r"""查询ESW实例配额

        查询租户的ESW实例配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkesw.v3.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_async_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/quotas",
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

    def list_resource_jobs_async(self, request):
        r"""查询任务的执行状态

        查询租户指定资源相关的任务信息列表，COMPLETED表示任务已成功完成，RUNNING表示任务正在执行中，FAILED表示任务执行失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceJobs
        :type request: :class:`huaweicloudsdkesw.v3.ListResourceJobsRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ListResourceJobsResponse`
        """
        http_info = self._list_resource_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_resource_jobs_async_invoker(self, request):
        http_info = self._list_resource_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/resources/{resource_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def show_connection_async(self, request):
        r"""查询二层连接详情

        当您的二层连接创建成功后，您可以通过调用此接口查询单二层连接的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConnection
        :type request: :class:`huaweicloudsdkesw.v3.ShowConnectionRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ShowConnectionResponse`
        """
        http_info = self._show_connection_http_info(request)
        return self._call_api(**http_info)

    def show_connection_async_invoker(self, request):
        http_info = self._show_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_connection_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/instances/{instance_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']
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

    def show_instance_async(self, request):
        r"""查询ESW实例详情

        当您的ESW实例创建成功后，您可以通过调用此接口查询单个ESW实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkesw.v3.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_async_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/l2cg/instances/{instance_id}",
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

    def unbind_vport_async(self, request):
        r"""将一个虚拟IP从二层连接解绑

        当您的二层连接已经绑定虚拟IP时，您可以通过调用此接口将虚拟IP与二层连接解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnbindVport
        :type request: :class:`huaweicloudsdkesw.v3.UnbindVportRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.UnbindVportResponse`
        """
        http_info = self._unbind_vport_http_info(request)
        return self._call_api(**http_info)

    def unbind_vport_async_invoker(self, request):
        http_info = self._unbind_vport_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unbind_vport_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/l2cg/connections/{connection_id}/vports/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "UnbindVportResponse"
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""更新二层连接

        当您的二层连接创建成功后，您可以通过调用此接口更新一个二层连接的名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConnection
        :type request: :class:`huaweicloudsdkesw.v3.UpdateConnectionRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.UpdateConnectionResponse`
        """
        http_info = self._update_connection_http_info(request)
        return self._call_api(**http_info)

    def update_connection_async_invoker(self, request):
        http_info = self._update_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_connection_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/l2cg/instances/{instance_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']
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

    def update_instance_async(self, request):
        r"""更新ESW实例

        当您的ESW实例创建成功后，您可以通过调用此接口更新一个ESW实例的名称或者描述信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkesw.v3.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkesw.v3.UpdateInstanceResponse`
        """
        http_info = self._update_instance_http_info(request)
        return self._call_api(**http_info)

    def update_instance_async_invoker(self, request):
        http_info = self._update_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/l2cg/instances/{instance_id}",
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

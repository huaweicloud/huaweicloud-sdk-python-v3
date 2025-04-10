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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkga'")


class GaAsyncClient(Client):
    def __init__(self):
        super(GaAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkga.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "GaAsyncClient":
                raise TypeError("client type error, support client type is GaAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_accelerator_async(self, request):
        r"""创建全球加速器

        创建全球加速器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAccelerator
        :type request: :class:`huaweicloudsdkga.v1.CreateAcceleratorRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateAcceleratorResponse`
        """
        http_info = self._create_accelerator_http_info(request)
        return self._call_api(**http_info)

    def create_accelerator_async_invoker(self, request):
        http_info = self._create_accelerator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_accelerator_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/accelerators",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAcceleratorResponse"
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

    def delete_accelerator_async(self, request):
        r"""删除全球加速器

        删除全球加速器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAccelerator
        :type request: :class:`huaweicloudsdkga.v1.DeleteAcceleratorRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteAcceleratorResponse`
        """
        http_info = self._delete_accelerator_http_info(request)
        return self._call_api(**http_info)

    def delete_accelerator_async_invoker(self, request):
        http_info = self._delete_accelerator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_accelerator_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/accelerators/{accelerator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAcceleratorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accelerator_id' in local_var_params:
            path_params['accelerator_id'] = local_var_params['accelerator_id']

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

    def list_accelerators_async(self, request):
        r"""查询全球加速器列表

        查询全球加速器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccelerators
        :type request: :class:`huaweicloudsdkga.v1.ListAcceleratorsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListAcceleratorsResponse`
        """
        http_info = self._list_accelerators_http_info(request)
        return self._call_api(**http_info)

    def list_accelerators_async_invoker(self, request):
        http_info = self._list_accelerators_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_accelerators_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/accelerators",
            "request_type": request.__class__.__name__,
            "response_type": "ListAcceleratorsResponse"
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def show_accelerator_async(self, request):
        r"""查询全球加速器详情

        查询全球加速器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccelerator
        :type request: :class:`huaweicloudsdkga.v1.ShowAcceleratorRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowAcceleratorResponse`
        """
        http_info = self._show_accelerator_http_info(request)
        return self._call_api(**http_info)

    def show_accelerator_async_invoker(self, request):
        http_info = self._show_accelerator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_accelerator_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/accelerators/{accelerator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAcceleratorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accelerator_id' in local_var_params:
            path_params['accelerator_id'] = local_var_params['accelerator_id']

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

    def update_accelerator_async(self, request):
        r"""更新全球加速器

        更新全球加速器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAccelerator
        :type request: :class:`huaweicloudsdkga.v1.UpdateAcceleratorRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateAcceleratorResponse`
        """
        http_info = self._update_accelerator_http_info(request)
        return self._call_api(**http_info)

    def update_accelerator_async_invoker(self, request):
        http_info = self._update_accelerator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_accelerator_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/accelerators/{accelerator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAcceleratorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accelerator_id' in local_var_params:
            path_params['accelerator_id'] = local_var_params['accelerator_id']

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

    def create_endpoint_async(self, request):
        r"""创建终端节点

        创建终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkga.v1.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateEndpointResponse`
        """
        http_info = self._create_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_endpoint_async_invoker(self, request):
        http_info = self._create_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/endpoint-groups/{endpoint_group_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

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

    def delete_endpoint_async(self, request):
        r"""删除终端节点

        删除终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpoint
        :type request: :class:`huaweicloudsdkga.v1.DeleteEndpointRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteEndpointResponse`
        """
        http_info = self._delete_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_async_invoker(self, request):
        http_info = self._delete_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/endpoint-groups/{endpoint_group_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']
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

    def list_endpoints_async(self, request):
        r"""查询终端节点组下终端节点列表

        查询终端节点组下终端节点列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpoints
        :type request: :class:`huaweicloudsdkga.v1.ListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListEndpointsResponse`
        """
        http_info = self._list_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_endpoints_async_invoker(self, request):
        http_info = self._list_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/endpoint-groups/{endpoint_group_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def show_endpoint_async(self, request):
        r"""查询终端节点详情

        查询终端节点详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEndpoint
        :type request: :class:`huaweicloudsdkga.v1.ShowEndpointRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowEndpointResponse`
        """
        http_info = self._show_endpoint_http_info(request)
        return self._call_api(**http_info)

    def show_endpoint_async_invoker(self, request):
        http_info = self._show_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_endpoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/endpoint-groups/{endpoint_group_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']
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

    def update_endpoint_async(self, request):
        r"""更新终端节点

        更新终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpoint
        :type request: :class:`huaweicloudsdkga.v1.UpdateEndpointRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateEndpointResponse`
        """
        http_info = self._update_endpoint_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_async_invoker(self, request):
        http_info = self._update_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/endpoint-groups/{endpoint_group_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']
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

    def create_endpoint_group_async(self, request):
        r"""创建终端节点组

        创建终端节点组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpointGroup
        :type request: :class:`huaweicloudsdkga.v1.CreateEndpointGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateEndpointGroupResponse`
        """
        http_info = self._create_endpoint_group_http_info(request)
        return self._call_api(**http_info)

    def create_endpoint_group_async_invoker(self, request):
        http_info = self._create_endpoint_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_endpoint_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/endpoint-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEndpointGroupResponse"
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

    def delete_endpoint_group_async(self, request):
        r"""删除终端节点组

        删除终端节点组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpointGroup
        :type request: :class:`huaweicloudsdkga.v1.DeleteEndpointGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteEndpointGroupResponse`
        """
        http_info = self._delete_endpoint_group_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_group_async_invoker(self, request):
        http_info = self._delete_endpoint_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/endpoint-groups/{endpoint_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

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

    def list_endpoint_groups_async(self, request):
        r"""查询终端节点组列表

        查询终端节点组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointGroups
        :type request: :class:`huaweicloudsdkga.v1.ListEndpointGroupsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListEndpointGroupsResponse`
        """
        http_info = self._list_endpoint_groups_http_info(request)
        return self._call_api(**http_info)

    def list_endpoint_groups_async_invoker(self, request):
        http_info = self._list_endpoint_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoint_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/endpoint-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointGroupsResponse"
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))

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

    def show_endpoint_group_async(self, request):
        r"""查询终端节点组详情

        查询终端节点组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEndpointGroup
        :type request: :class:`huaweicloudsdkga.v1.ShowEndpointGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowEndpointGroupResponse`
        """
        http_info = self._show_endpoint_group_http_info(request)
        return self._call_api(**http_info)

    def show_endpoint_group_async_invoker(self, request):
        http_info = self._show_endpoint_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_endpoint_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/endpoint-groups/{endpoint_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEndpointGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

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

    def update_endpoint_group_async(self, request):
        r"""更新终端节点组

        更新终端节点组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointGroup
        :type request: :class:`huaweicloudsdkga.v1.UpdateEndpointGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateEndpointGroupResponse`
        """
        http_info = self._update_endpoint_group_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_group_async_invoker(self, request):
        http_info = self._update_endpoint_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/endpoint-groups/{endpoint_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

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

    def create_health_check_async(self, request):
        r"""创建健康检查

        创建健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHealthCheck
        :type request: :class:`huaweicloudsdkga.v1.CreateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateHealthCheckResponse`
        """
        http_info = self._create_health_check_http_info(request)
        return self._call_api(**http_info)

    def create_health_check_async_invoker(self, request):
        http_info = self._create_health_check_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_health_check_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/health-checks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHealthCheckResponse"
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

    def delete_health_check_async(self, request):
        r"""删除健康检查

        删除健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHealthCheck
        :type request: :class:`huaweicloudsdkga.v1.DeleteHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteHealthCheckResponse`
        """
        http_info = self._delete_health_check_http_info(request)
        return self._call_api(**http_info)

    def delete_health_check_async_invoker(self, request):
        http_info = self._delete_health_check_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_health_check_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/health-checks/{health_check_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHealthCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'health_check_id' in local_var_params:
            path_params['health_check_id'] = local_var_params['health_check_id']

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

    def list_health_checks_async(self, request):
        r"""查询健康检查列表

        查询健康检查列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHealthChecks
        :type request: :class:`huaweicloudsdkga.v1.ListHealthChecksRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListHealthChecksResponse`
        """
        http_info = self._list_health_checks_http_info(request)
        return self._call_api(**http_info)

    def list_health_checks_async_invoker(self, request):
        http_info = self._list_health_checks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_health_checks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/health-checks",
            "request_type": request.__class__.__name__,
            "response_type": "ListHealthChecksResponse"
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'endpoint_group_id' in local_var_params:
            query_params.append(('endpoint_group_id', local_var_params['endpoint_group_id']))

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

    def show_health_check_async(self, request):
        r"""查询健康检查详情

        查询健康检查详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHealthCheck
        :type request: :class:`huaweicloudsdkga.v1.ShowHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowHealthCheckResponse`
        """
        http_info = self._show_health_check_http_info(request)
        return self._call_api(**http_info)

    def show_health_check_async_invoker(self, request):
        http_info = self._show_health_check_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_health_check_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/health-checks/{health_check_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHealthCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'health_check_id' in local_var_params:
            path_params['health_check_id'] = local_var_params['health_check_id']

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

    def update_health_check_async(self, request):
        r"""更新健康检查

        更新健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHealthCheck
        :type request: :class:`huaweicloudsdkga.v1.UpdateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateHealthCheckResponse`
        """
        http_info = self._update_health_check_http_info(request)
        return self._call_api(**http_info)

    def update_health_check_async_invoker(self, request):
        http_info = self._update_health_check_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_health_check_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/health-checks/{health_check_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHealthCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'health_check_id' in local_var_params:
            path_params['health_check_id'] = local_var_params['health_check_id']

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

    def add_ip_group_ip_async(self, request):
        r"""添加IP地址组中的IP网段

        添加IP地址组中的IP网段。
        该接口属于异步接口，接口返回后，后台的添加任务仍在执行；可以使用查询IP地址组详情接口查询状态，当IP地址组状态为ACTIVE时，表示条目添加完成。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddIpGroupIp
        :type request: :class:`huaweicloudsdkga.v1.AddIpGroupIpRequest`
        :rtype: :class:`huaweicloudsdkga.v1.AddIpGroupIpResponse`
        """
        http_info = self._add_ip_group_ip_http_info(request)
        return self._call_api(**http_info)

    def add_ip_group_ip_async_invoker(self, request):
        http_info = self._add_ip_group_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_ip_group_ip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ip-groups/{ip_group_id}/add-ips",
            "request_type": request.__class__.__name__,
            "response_type": "AddIpGroupIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def associate_listener_async(self, request):
        r"""绑定IP地址组与监听器

        绑定IP地址组与监听器。
        该接口属于异步接口，接口返回后，后台的绑定任务仍在执行；可以使用查询IP地址组详情接口查询状态，当IP地址组状态为ACTIVE时，表示绑定完成。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateListener
        :type request: :class:`huaweicloudsdkga.v1.AssociateListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.AssociateListenerResponse`
        """
        http_info = self._associate_listener_http_info(request)
        return self._call_api(**http_info)

    def associate_listener_async_invoker(self, request):
        http_info = self._associate_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_listener_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ip-groups/{ip_group_id}/associate-listener",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def create_ip_group_async(self, request):
        r"""创建IP地址组

        创建IP地址组。
        该接口属于异步接口，会先返回一个IP地址组ID，但后台的创建任务仍在执行；可以使用查询IP地址组详情接口查询状态，当IP地址组状态为ACTIVE时，表示IP地址组创建完成。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIpGroup
        :type request: :class:`huaweicloudsdkga.v1.CreateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateIpGroupResponse`
        """
        http_info = self._create_ip_group_http_info(request)
        return self._call_api(**http_info)

    def create_ip_group_async_invoker(self, request):
        http_info = self._create_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ip_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ip-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIpGroupResponse"
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

    def delete_ip_group_async(self, request):
        r"""删除IP地址组

        删除IP地址组。
        该接口属于异步接口，接口返回后，后台的删除任务仍在执行；可以使用查询IP地址组详情接口查询状态，当查询不到该IP地址组时，表示删除完成；删除IP地址组时，若IP地址组已经绑定了监听器，则需要先解绑IP地址组与监听器，再进行删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIpGroup
        :type request: :class:`huaweicloudsdkga.v1.DeleteIpGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteIpGroupResponse`
        """
        http_info = self._delete_ip_group_http_info(request)
        return self._call_api(**http_info)

    def delete_ip_group_async_invoker(self, request):
        http_info = self._delete_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ip_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ip-groups/{ip_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def disassociate_listener_async(self, request):
        r"""解绑IP地址组与监听器

        解绑IP地址组与监听器。
        该接口属于异步接口，接口返回后，后台的解绑任务仍在执行；可以使用查询IP地址组详情接口查询状态，当IP地址组状态为ACTIVE时，表示解绑完成。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateListener
        :type request: :class:`huaweicloudsdkga.v1.DisassociateListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DisassociateListenerResponse`
        """
        http_info = self._disassociate_listener_http_info(request)
        return self._call_api(**http_info)

    def disassociate_listener_async_invoker(self, request):
        http_info = self._disassociate_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_listener_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ip-groups/{ip_group_id}/disassociate-listener",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def list_ip_groups_async(self, request):
        r"""查询IP地址组列表

        查询IP地址组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIpGroups
        :type request: :class:`huaweicloudsdkga.v1.ListIpGroupsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListIpGroupsResponse`
        """
        http_info = self._list_ip_groups_http_info(request)
        return self._call_api(**http_info)

    def list_ip_groups_async_invoker(self, request):
        http_info = self._list_ip_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ip_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ip-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpGroupsResponse"
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
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))

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

    def remove_ip_group_ip_async(self, request):
        r"""删除IP地址组中的IP网段

        删除IP地址组中的IP网段。
        该接口属于异步接口，接口返回后，后台的删除任务仍在执行；可以使用查询IP地址组详情接口查询状态，当IP地址组状态为ACTIVE时，表示条目删除完成。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveIpGroupIp
        :type request: :class:`huaweicloudsdkga.v1.RemoveIpGroupIpRequest`
        :rtype: :class:`huaweicloudsdkga.v1.RemoveIpGroupIpResponse`
        """
        http_info = self._remove_ip_group_ip_http_info(request)
        return self._call_api(**http_info)

    def remove_ip_group_ip_async_invoker(self, request):
        http_info = self._remove_ip_group_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_ip_group_ip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ip-groups/{ip_group_id}/remove-ips",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveIpGroupIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def show_ip_group_async(self, request):
        r"""查询IP地址组详情

        查询IP地址组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIpGroup
        :type request: :class:`huaweicloudsdkga.v1.ShowIpGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowIpGroupResponse`
        """
        http_info = self._show_ip_group_http_info(request)
        return self._call_api(**http_info)

    def show_ip_group_async_invoker(self, request):
        http_info = self._show_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ip_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ip-groups/{ip_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def update_ip_group_async(self, request):
        r"""更新IP地址组

        更新IP地址组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIpGroup
        :type request: :class:`huaweicloudsdkga.v1.UpdateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateIpGroupResponse`
        """
        http_info = self._update_ip_group_http_info(request)
        return self._call_api(**http_info)

    def update_ip_group_async_invoker(self, request):
        http_info = self._update_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ip_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ip-groups/{ip_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def create_listener_async(self, request):
        r"""创建监听器

        创建监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateListener
        :type request: :class:`huaweicloudsdkga.v1.CreateListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateListenerResponse`
        """
        http_info = self._create_listener_http_info(request)
        return self._call_api(**http_info)

    def create_listener_async_invoker(self, request):
        http_info = self._create_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_listener_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/listeners",
            "request_type": request.__class__.__name__,
            "response_type": "CreateListenerResponse"
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

    def delete_listener_async(self, request):
        r"""删除监听器

        删除监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteListener
        :type request: :class:`huaweicloudsdkga.v1.DeleteListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteListenerResponse`
        """
        http_info = self._delete_listener_http_info(request)
        return self._call_api(**http_info)

    def delete_listener_async_invoker(self, request):
        http_info = self._delete_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_listener_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def list_listeners_async(self, request):
        r"""查询监听器列表

        查询监听器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListListeners
        :type request: :class:`huaweicloudsdkga.v1.ListListenersRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListListenersResponse`
        """
        http_info = self._list_listeners_http_info(request)
        return self._call_api(**http_info)

    def list_listeners_async_invoker(self, request):
        http_info = self._list_listeners_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_listeners_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/listeners",
            "request_type": request.__class__.__name__,
            "response_type": "ListListenersResponse"
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'accelerator_id' in local_var_params:
            query_params.append(('accelerator_id', local_var_params['accelerator_id']))

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

    def show_listener_async(self, request):
        r"""查询监听器详情

        查询监听器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListener
        :type request: :class:`huaweicloudsdkga.v1.ShowListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowListenerResponse`
        """
        http_info = self._show_listener_http_info(request)
        return self._call_api(**http_info)

    def show_listener_async_invoker(self, request):
        http_info = self._show_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_listener_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def update_listener_async(self, request):
        r"""更新监听器

        更新监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateListener
        :type request: :class:`huaweicloudsdkga.v1.UpdateListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateListenerResponse`
        """
        http_info = self._update_listener_http_info(request)
        return self._call_api(**http_info)

    def update_listener_async_invoker(self, request):
        http_info = self._update_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_listener_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def create_logtank_async(self, request):
        r"""创建云日志

        创建云日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLogtank
        :type request: :class:`huaweicloudsdkga.v1.CreateLogtankRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateLogtankResponse`
        """
        http_info = self._create_logtank_http_info(request)
        return self._call_api(**http_info)

    def create_logtank_async_invoker(self, request):
        http_info = self._create_logtank_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_logtank_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/logtanks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogtankResponse"
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

    def delete_logtank_async(self, request):
        r"""删除云日志

        删除云日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLogtank
        :type request: :class:`huaweicloudsdkga.v1.DeleteLogtankRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteLogtankResponse`
        """
        http_info = self._delete_logtank_http_info(request)
        return self._call_api(**http_info)

    def delete_logtank_async_invoker(self, request):
        http_info = self._delete_logtank_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_logtank_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/logtanks/{logtank_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_logtanks_async(self, request):
        r"""查询云日志列表

        查询云日志列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogtanks
        :type request: :class:`huaweicloudsdkga.v1.ListLogtanksRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListLogtanksResponse`
        """
        http_info = self._list_logtanks_http_info(request)
        return self._call_api(**http_info)

    def list_logtanks_async_invoker(self, request):
        http_info = self._list_logtanks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_logtanks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/logtanks",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogtanksResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'resource_ids' in local_var_params:
            query_params.append(('resource_ids', local_var_params['resource_ids']))
            collection_formats['resource_ids'] = 'multi'
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

    def show_logtank_async(self, request):
        r"""查询云日志详情

        查询云日志详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLogtank
        :type request: :class:`huaweicloudsdkga.v1.ShowLogtankRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowLogtankResponse`
        """
        http_info = self._show_logtank_http_info(request)
        return self._call_api(**http_info)

    def show_logtank_async_invoker(self, request):
        http_info = self._show_logtank_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_logtank_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/logtanks/{logtank_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def update_logtank_async(self, request):
        r"""更新云日志

        更新云日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLogtank
        :type request: :class:`huaweicloudsdkga.v1.UpdateLogtankRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateLogtankResponse`
        """
        http_info = self._update_logtank_http_info(request)
        return self._call_api(**http_info)

    def update_logtank_async_invoker(self, request):
        http_info = self._update_logtank_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_logtank_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/logtanks/{logtank_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_regions_async(self, request):
        r"""查询区域列表

        查询区域列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRegions
        :type request: :class:`huaweicloudsdkga.v1.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListRegionsResponse`
        """
        http_info = self._list_regions_http_info(request)
        return self._call_api(**http_info)

    def list_regions_async_invoker(self, request):
        http_info = self._list_regions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_regions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegionsResponse"
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

    def count_resources_by_tag_async(self, request):
        r"""通过标签查询资源实例数量

        通过标签查询资源实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountResourcesByTag
        :type request: :class:`huaweicloudsdkga.v1.CountResourcesByTagRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CountResourcesByTagResponse`
        """
        http_info = self._count_resources_by_tag_http_info(request)
        return self._call_api(**http_info)

    def count_resources_by_tag_async_invoker(self, request):
        http_info = self._count_resources_by_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_resources_by_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountResourcesByTagResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_tags_async(self, request):
        r"""创建资源标签

        创建资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTags
        :type request: :class:`huaweicloudsdkga.v1.CreateTagsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateTagsResponse`
        """
        http_info = self._create_tags_http_info(request)
        return self._call_api(**http_info)

    def create_tags_async_invoker(self, request):
        http_info = self._create_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_tags_async(self, request):
        r"""删除资源标签

        删除资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTags
        :type request: :class:`huaweicloudsdkga.v1.DeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteTagsResponse`
        """
        http_info = self._delete_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_tags_async_invoker(self, request):
        http_info = self._delete_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resources_by_tag_async(self, request):
        r"""通过标签查询资源实例列表

        通过标签查询资源实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourcesByTag
        :type request: :class:`huaweicloudsdkga.v1.ListResourcesByTagRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListResourcesByTagResponse`
        """
        http_info = self._list_resources_by_tag_http_info(request)
        return self._call_api(**http_info)

    def list_resources_by_tag_async_invoker(self, request):
        http_info = self._list_resources_by_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resources_by_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesByTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_tags_async(self, request):
        r"""查询标签列表

        查询标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkga.v1.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def show_resource_tags_async(self, request):
        r"""查询特定资源标签

        查询特定资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTags
        :type request: :class:`huaweicloudsdkga.v1.ShowResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowResourceTagsResponse`
        """
        http_info = self._show_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def show_resource_tags_async_invoker(self, request):
        http_info = self._show_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceTagsResponse"
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

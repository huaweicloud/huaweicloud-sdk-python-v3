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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkvpcep'")


class VpcepAsyncClient(Client):
    def __init__(self):
        super(VpcepAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpcep.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "VpcepAsyncClient":
                raise TypeError("client type error, support client type is VpcepAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def accept_or_reject_endpoint_async(self, request):
        """接受或拒绝终端节点的连接

        接受或者拒绝终端节点连接到当前的终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptOrRejectEndpoint
        :type request: :class:`huaweicloudsdkvpcep.v1.AcceptOrRejectEndpointRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.AcceptOrRejectEndpointResponse`
        """
        http_info = self._accept_or_reject_endpoint_http_info(request)
        return self._call_api(**http_info)

    def accept_or_reject_endpoint_async_invoker(self, request):
        http_info = self._accept_or_reject_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _accept_or_reject_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/connections/action",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptOrRejectEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def add_or_remove_service_permissions_async(self, request):
        """批量添加或移除终端节点服务的白名单

        批量添加或移除当前用户下终端节点服务的白名单。
        说明
        本帐号默认在自身用户的终端节点服务的白名单中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddOrRemoveServicePermissions
        :type request: :class:`huaweicloudsdkvpcep.v1.AddOrRemoveServicePermissionsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.AddOrRemoveServicePermissionsResponse`
        """
        http_info = self._add_or_remove_service_permissions_http_info(request)
        return self._call_api(**http_info)

    def add_or_remove_service_permissions_async_invoker(self, request):
        http_info = self._add_or_remove_service_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_or_remove_service_permissions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions/action",
            "request_type": request.__class__.__name__,
            "response_type": "AddOrRemoveServicePermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def batch_add_endpoint_service_permissions_async(self, request):
        """批量添加终端节点服务的白名单

        批量添加当前用户下终端节点服务的白名单，支持添加描述信息。
        说明
        本帐号默认在自身用户的终端节点服务的白名单中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddEndpointServicePermissions
        :type request: :class:`huaweicloudsdkvpcep.v1.BatchAddEndpointServicePermissionsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.BatchAddEndpointServicePermissionsResponse`
        """
        http_info = self._batch_add_endpoint_service_permissions_http_info(request)
        return self._call_api(**http_info)

    def batch_add_endpoint_service_permissions_async_invoker(self, request):
        http_info = self._batch_add_endpoint_service_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_endpoint_service_permissions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddEndpointServicePermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def batch_remove_endpoint_service_permissions_async(self, request):
        """批量删除终端节点服务的白名单

        批量删除当前用户下终端节点服务的白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRemoveEndpointServicePermissions
        :type request: :class:`huaweicloudsdkvpcep.v1.BatchRemoveEndpointServicePermissionsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.BatchRemoveEndpointServicePermissionsResponse`
        """
        http_info = self._batch_remove_endpoint_service_permissions_http_info(request)
        return self._call_api(**http_info)

    def batch_remove_endpoint_service_permissions_async_invoker(self, request):
        http_info = self._batch_remove_endpoint_service_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_remove_endpoint_service_permissions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRemoveEndpointServicePermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def create_endpoint_async(self, request):
        """创建终端节点

        创建终端节点，以便访问终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkvpcep.v1.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.CreateEndpointResponse`
        """
        http_info = self._create_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_endpoint_async_invoker(self, request):
        http_info = self._create_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/vpc-endpoints",
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

    def create_endpoint_service_async(self, request):
        """创建终端节点服务

        创建终端节点服务，允许其他用户创建终端节点连接您创建的终端节点服务，
        使用您所提供的服务。
        说明
        该接口为异步接口，调用成功会返回200状态码，说明请求已正常下发。
        通常创建终端节点服务需要1~2分钟，可以通过查询终端节点服务详情查看创建结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpointService
        :type request: :class:`huaweicloudsdkvpcep.v1.CreateEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.CreateEndpointServiceResponse`
        """
        http_info = self._create_endpoint_service_http_info(request)
        return self._call_api(**http_info)

    def create_endpoint_service_async_invoker(self, request):
        http_info = self._create_endpoint_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_endpoint_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEndpointServiceResponse"
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

    def delete_endpoint_async(self, request):
        """删除终端节点

        删除终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpoint
        :type request: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointResponse`
        """
        http_info = self._delete_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_async_invoker(self, request):
        http_info = self._delete_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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

    def delete_endpoint_policy_async(self, request):
        """删除网关型终端节点policy

        删除网关型终端节点policy。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpointPolicy
        :type request: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointPolicyResponse`
        """
        http_info = self._delete_endpoint_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_policy_async_invoker(self, request):
        http_info = self._delete_endpoint_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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

    def delete_endpoint_service_async(self, request):
        """删除终端节点服务

        删除终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpointService
        :type request: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointServiceResponse`
        """
        http_info = self._delete_endpoint_service_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_service_async_invoker(self, request):
        http_info = self._delete_endpoint_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_service_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def list_endpoint_info_details_async(self, request):
        """查询终端节点详情

        查询终端节点的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointInfoDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListEndpointInfoDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListEndpointInfoDetailsResponse`
        """
        http_info = self._list_endpoint_info_details_http_info(request)
        return self._call_api(**http_info)

    def list_endpoint_info_details_async_invoker(self, request):
        http_info = self._list_endpoint_info_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoint_info_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointInfoDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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

    def list_endpoint_service_async(self, request):
        """查询终端节点服务列表

        查询当前用户下的终端节点服务的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointService
        :type request: :class:`huaweicloudsdkvpcep.v1.ListEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListEndpointServiceResponse`
        """
        http_info = self._list_endpoint_service_http_info(request)
        return self._call_api(**http_info)

    def list_endpoint_service_async_invoker(self, request):
        http_info = self._list_endpoint_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoint_service_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_service_name' in local_var_params:
            query_params.append(('endpoint_service_name', local_var_params['endpoint_service_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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
        """查询终端节点列表

        查询当前用户下的终端节点的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpoints
        :type request: :class:`huaweicloudsdkvpcep.v1.ListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListEndpointsResponse`
        """
        http_info = self._list_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_endpoints_async_invoker(self, request):
        http_info = self._list_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpc-endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_service_name' in local_var_params:
            query_params.append(('endpoint_service_name', local_var_params['endpoint_service_name']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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

    def list_quota_details_async(self, request):
        """查询配额

        查询用户的资源配额，包括终端节点服务和终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotaDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListQuotaDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListQuotaDetailsResponse`
        """
        http_info = self._list_quota_details_http_info(request)
        return self._call_api(**http_info)

    def list_quota_details_async_invoker(self, request):
        http_info = self._list_quota_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quota_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotaDetailsResponse"
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

    def list_service_connections_async(self, request):
        """查询连接终端节点服务的连接列表

        查询连接当前用户下的某一个终端节点服务的连接列表。marker_id是连接的唯一标识。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceConnections
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServiceConnectionsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServiceConnectionsResponse`
        """
        http_info = self._list_service_connections_http_info(request)
        return self._call_api(**http_info)

    def list_service_connections_async_invoker(self, request):
        http_info = self._list_service_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_service_connections_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'marker_id' in local_var_params:
            query_params.append(('marker_id', local_var_params['marker_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
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

    def list_service_describe_details_async(self, request):
        """查询终端节点服务概要

        查询终端节点服务的概要信息， 此接口是供创建终端节点的用户来查询需要连接的终端节点服务信息。 此接口既可以方便其他用户查询到您的终端节点服务概要信息, 又可以避免您的终端节点服务的细节信息暴露给其他用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceDescribeDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServiceDescribeDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServiceDescribeDetailsResponse`
        """
        http_info = self._list_service_describe_details_http_info(request)
        return self._call_api(**http_info)

    def list_service_describe_details_async_invoker(self, request):
        http_info = self._list_service_describe_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_service_describe_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/describe",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceDescribeDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_service_name' in local_var_params:
            query_params.append(('endpoint_service_name', local_var_params['endpoint_service_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def list_service_details_async(self, request):
        """查询终端节点服务详情

        查询终端节点服务的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServiceDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServiceDetailsResponse`
        """
        http_info = self._list_service_details_http_info(request)
        return self._call_api(**http_info)

    def list_service_details_async_invoker(self, request):
        http_info = self._list_service_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_service_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def list_service_permissions_details_async(self, request):
        """查询终端节点服务的白名单列表

        查询当前用户下终端节点服务的白名单列表。
        说明
        本帐号默认在当前用户下终端节点服务的白名单中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServicePermissionsDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServicePermissionsDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServicePermissionsDetailsResponse`
        """
        http_info = self._list_service_permissions_details_http_info(request)
        return self._call_api(**http_info)

    def list_service_permissions_details_async_invoker(self, request):
        http_info = self._list_service_permissions_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_service_permissions_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ListServicePermissionsDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

        query_params = []
        if 'permission' in local_var_params:
            query_params.append(('permission', local_var_params['permission']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_service_public_details_async(self, request):
        """查询公共终端节点服务列表

        查询公共终端节点服务的列表，公共终端节点服务是所有用户可见且可连接的终端节点服务，
        由运维人员创建，用户可直接使用，但无权创建。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServicePublicDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServicePublicDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServicePublicDetailsResponse`
        """
        http_info = self._list_service_public_details_http_info(request)
        return self._call_api(**http_info)

    def list_service_public_details_async_invoker(self, request):
        http_info = self._list_service_public_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_service_public_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/public",
            "request_type": request.__class__.__name__,
            "response_type": "ListServicePublicDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'endpoint_service_name' in local_var_params:
            query_params.append(('endpoint_service_name', local_var_params['endpoint_service_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_specified_version_details_async(self, request):
        """查询指定VPC终端节点接口版本信息

        查询指定VPC终端节点接口版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSpecifiedVersionDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListSpecifiedVersionDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListSpecifiedVersionDetailsResponse`
        """
        http_info = self._list_specified_version_details_http_info(request)
        return self._call_api(**http_info)

    def list_specified_version_details_async_invoker(self, request):
        http_info = self._list_specified_version_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_specified_version_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpecifiedVersionDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def list_version_details_async(self, request):
        """查询VPC终端节点接口版本列表

        查询VPC终端节点接口版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVersionDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListVersionDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListVersionDetailsResponse`
        """
        http_info = self._list_version_details_http_info(request)
        return self._call_api(**http_info)

    def list_version_details_async_invoker(self, request):
        http_info = self._list_version_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_version_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListVersionDetailsResponse"
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

    def update_endpoint_connections_desc_async(self, request):
        """更新终端节点连接描述

        更新终端节点服务连接的终端节点的描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointConnectionsDesc
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointConnectionsDescRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointConnectionsDescResponse`
        """
        http_info = self._update_endpoint_connections_desc_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_connections_desc_async_invoker(self, request):
        http_info = self._update_endpoint_connections_desc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_connections_desc_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/connections/description",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointConnectionsDescResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def update_endpoint_policy_async(self, request):
        """修改网关型终端节点policy

        修改网关型终端节点policy。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointPolicy
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointPolicyResponse`
        """
        http_info = self._update_endpoint_policy_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_policy_async_invoker(self, request):
        http_info = self._update_endpoint_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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

    def update_endpoint_routetable_async(self, request):
        """修改终端节点的路由表

        修改终端节点的路由表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointRoutetable
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointRoutetableRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointRoutetableResponse`
        """
        http_info = self._update_endpoint_routetable_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_routetable_async_invoker(self, request):
        http_info = self._update_endpoint_routetable_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_routetable_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}/routetables",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointRoutetableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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

    def update_endpoint_service_async(self, request):
        """修改终端节点服务

        修改终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointService
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServiceResponse`
        """
        http_info = self._update_endpoint_service_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_service_async_invoker(self, request):
        http_info = self._update_endpoint_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_service_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def update_endpoint_service_name_async(self, request):
        """修改终端节点服务名称

        修改终端节点服务名称
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointServiceName
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServiceNameRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServiceNameResponse`
        """
        http_info = self._update_endpoint_service_name_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_service_name_async_invoker(self, request):
        http_info = self._update_endpoint_service_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_service_name_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointServiceNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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

    def update_endpoint_service_permission_desc_async(self, request):
        """更新终端节点服务白名单描述

        更新当前用户下终端节点服务白名单的描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointServicePermissionDesc
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServicePermissionDescRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServicePermissionDescResponse`
        """
        http_info = self._update_endpoint_service_permission_desc_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_service_permission_desc_async_invoker(self, request):
        http_info = self._update_endpoint_service_permission_desc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_service_permission_desc_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions/{permission_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointServicePermissionDescResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']
        if 'permission_id' in local_var_params:
            path_params['permission_id'] = local_var_params['permission_id']

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

    def update_endpoint_white_async(self, request):
        """更新终端节点

        更新或删除允许访问终端节点的白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointWhite
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointWhiteRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointWhiteResponse`
        """
        http_info = self._update_endpoint_white_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_white_async_invoker(self, request):
        http_info = self._update_endpoint_white_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_white_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointWhiteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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

    def batch_add_or_remove_resource_instance_async(self, request):
        """批量添加或删除资源标签接口

        为指定Endpoint Service或Endpoint批量添加或删除标签。
        ● 一个资源上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddOrRemoveResourceInstance
        :type request: :class:`huaweicloudsdkvpcep.v1.BatchAddOrRemoveResourceInstanceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.BatchAddOrRemoveResourceInstanceResponse`
        """
        http_info = self._batch_add_or_remove_resource_instance_http_info(request)
        return self._call_api(**http_info)

    def batch_add_or_remove_resource_instance_async_invoker(self, request):
        http_info = self._batch_add_or_remove_resource_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_or_remove_resource_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddOrRemoveResourceInstanceResponse"
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

    def list_query_project_resource_tags_async(self, request):
        """查询租户资源标签接口

        根据租户ID和资源类型，获取租户下资源的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQueryProjectResourceTags
        :type request: :class:`huaweicloudsdkvpcep.v1.ListQueryProjectResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListQueryProjectResourceTagsResponse`
        """
        http_info = self._list_query_project_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_query_project_resource_tags_async_invoker(self, request):
        http_info = self._list_query_project_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_query_project_resource_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryProjectResourceTagsResponse"
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
        """查询资源实例接口

        使用标签过滤查询租户下资源的实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkvpcep.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListResourceInstancesResponse`
        """
        http_info = self._list_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instances_async_invoker(self, request):
        http_info = self._list_resource_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/resource_instances/action",
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

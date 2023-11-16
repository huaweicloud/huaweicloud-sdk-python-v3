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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdklakeformation'")


class LakeFormationAsyncClient(Client):
    def __init__(self):
        super(LakeFormationAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklakeformation.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "LakeFormationAsyncClient":
                raise TypeError("client type error, support client type is LakeFormationAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def apply_for_access_async(self, request):
        """申请接入服务

        申请接入服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyForAccess
        :type request: :class:`huaweicloudsdklakeformation.v1.ApplyForAccessRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ApplyForAccessResponse`
        """
        http_info = self._apply_for_access_http_info(request)
        return self._call_api(**http_info)

    def apply_for_access_async_invoker(self, request):
        http_info = self._apply_for_access_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_for_access_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/access",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyForAccessResponse"
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

    def batch_authorize_interface_async(self, request):
        """批量授权

        批量授权接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAuthorizeInterface
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchAuthorizeInterfaceRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchAuthorizeInterfaceResponse`
        """
        http_info = self._batch_authorize_interface_http_info(request)
        return self._call_api(**http_info)

    def batch_authorize_interface_async_invoker(self, request):
        http_info = self._batch_authorize_interface_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_authorize_interface_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/policies/grant",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAuthorizeInterfaceResponse"
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

    def batch_cancel_authorization_interface_async(self, request):
        """取消批量授权

        批量取消授权接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCancelAuthorizationInterface
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchCancelAuthorizationInterfaceRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchCancelAuthorizationInterfaceResponse`
        """
        http_info = self._batch_cancel_authorization_interface_http_info(request)
        return self._call_api(**http_info)

    def batch_cancel_authorization_interface_async_invoker(self, request):
        http_info = self._batch_cancel_authorization_interface_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_cancel_authorization_interface_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/policies/revoke",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCancelAuthorizationInterfaceResponse"
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

    def batch_check_permission_async(self, request):
        """批量鉴权

        批量鉴权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCheckPermission
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchCheckPermissionRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchCheckPermissionResponse`
        """
        http_info = self._batch_check_permission_http_info(request)
        return self._call_api(**http_info)

    def batch_check_permission_async_invoker(self, request):
        http_info = self._batch_check_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_check_permission_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/policies/check-permission",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckPermissionResponse"
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

    def create_access_client_async(self, request):
        """创建服务接入客户端

        创建服务接入客户端。
        其他限制：
          同一个实例下默认最多创建20个接入客户端。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAccessClient
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateAccessClientRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateAccessClientResponse`
        """
        http_info = self._create_access_client_http_info(request)
        return self._call_api(**http_info)

    def create_access_client_async_invoker(self, request):
        http_info = self._create_access_client_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_access_client_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/access-clients",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccessClientResponse"
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

    def delete_access_client_async(self, request):
        """删除服务接入客户端

        根据ID删除服务接入客户端
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAccessClient
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteAccessClientRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteAccessClientResponse`
        """
        http_info = self._delete_access_client_http_info(request)
        return self._call_api(**http_info)

    def delete_access_client_async_invoker(self, request):
        http_info = self._delete_access_client_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_access_client_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/access-clients/{client_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAccessClientResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'client_id' in local_var_params:
            path_params['client_id'] = local_var_params['client_id']

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

    def list_access_client_infos_async(self, request):
        """获取服务接入客户端信息列表

        根据LakeFormation实例获取服务实例相关的接入客户端信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessClientInfos
        :type request: :class:`huaweicloudsdklakeformation.v1.ListAccessClientInfosRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListAccessClientInfosResponse`
        """
        http_info = self._list_access_client_infos_http_info(request)
        return self._call_api(**http_info)

    def list_access_client_infos_async_invoker(self, request):
        http_info = self._list_access_client_infos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_access_client_infos_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/access-clients",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessClientInfosResponse"
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

    def list_access_infos_async(self, request):
        """获取服务接入信息

        根据LakeFormation实例获取服务实例相关的接入信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessInfos
        :type request: :class:`huaweicloudsdklakeformation.v1.ListAccessInfosRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListAccessInfosResponse`
        """
        http_info = self._list_access_infos_http_info(request)
        return self._call_api(**http_info)

    def list_access_infos_async_invoker(self, request):
        http_info = self._list_access_infos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_access_infos_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/access",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessInfosResponse"
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

    def list_interfaces_async(self, request):
        """查询策略

        通过过滤条件查询接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInterfaces
        :type request: :class:`huaweicloudsdklakeformation.v1.ListInterfacesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListInterfacesResponse`
        """
        http_info = self._list_interfaces_http_info(request)
        return self._call_api(**http_info)

    def list_interfaces_async_invoker(self, request):
        http_info = self._list_interfaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_interfaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/policies/show",
            "request_type": request.__class__.__name__,
            "response_type": "ListInterfacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'principal_source' in local_var_params:
            query_params.append(('principal_source', local_var_params['principal_source']))
        if 'principal_type' in local_var_params:
            query_params.append(('principal_type', local_var_params['principal_type']))
        if 'principal_name' in local_var_params:
            query_params.append(('principal_name', local_var_params['principal_name']))
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

    def list_policy_async(self, request):
        """获取同步权限策略

        分页获取同步权限策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicy
        :type request: :class:`huaweicloudsdklakeformation.v1.ListPolicyRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListPolicyResponse`
        """
        http_info = self._list_policy_http_info(request)
        return self._call_api(**http_info)

    def list_policy_async_invoker(self, request):
        http_info = self._list_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def show_access_client_async(self, request):
        """获取服务接入客户端详情

        根据ID获取服务接入客户端详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccessClient
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowAccessClientRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowAccessClientResponse`
        """
        http_info = self._show_access_client_http_info(request)
        return self._call_api(**http_info)

    def show_access_client_async_invoker(self, request):
        http_info = self._show_access_client_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_access_client_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/access-clients/{client_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessClientResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'client_id' in local_var_params:
            path_params['client_id'] = local_var_params['client_id']

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

    def show_sync_policy_async(self, request):
        """获取同步权限策略

        获取同步权限策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSyncPolicy
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowSyncPolicyRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowSyncPolicyResponse`
        """
        http_info = self._show_sync_policy_http_info(request)
        return self._call_api(**http_info)

    def show_sync_policy_async_invoker(self, request):
        http_info = self._show_sync_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sync_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/policies/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSyncPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'last_known_version' in local_var_params:
            query_params.append(('last_known_version', local_var_params['last_known_version']))
        if 'supports_policy_deltas' in local_var_params:
            query_params.append(('supports_policy_deltas', local_var_params['supports_policy_deltas']))
        if 'is_return_policy_data' in local_var_params:
            query_params.append(('is_return_policy_data', local_var_params['is_return_policy_data']))

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

    def update_access_client_async(self, request):
        """更新服务接入客户端

        根据ID更新服务接入客户端
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAccessClient
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateAccessClientRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateAccessClientResponse`
        """
        http_info = self._update_access_client_http_info(request)
        return self._call_api(**http_info)

    def update_access_client_async_invoker(self, request):
        http_info = self._update_access_client_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_access_client_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/access-clients/{client_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccessClientResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'client_id' in local_var_params:
            path_params['client_id'] = local_var_params['client_id']

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

    def create_agency_async(self, request):
        """创建委托

        创建委托
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgency
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateAgencyRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateAgencyResponse`
        """
        http_info = self._create_agency_http_info(request)
        return self._call_api(**http_info)

    def create_agency_async_invoker(self, request):
        http_info = self._create_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agency_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/agency",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyResponse"
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

    def delete_agency_async(self, request):
        """删除委托

        删除委托
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAgency
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteAgencyRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteAgencyResponse`
        """
        http_info = self._delete_agency_http_info(request)
        return self._call_api(**http_info)

    def delete_agency_async_invoker(self, request):
        http_info = self._delete_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_agency_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/agency",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgencyResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_agency_async(self, request):
        """委托查询

        委托查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgency
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowAgencyRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowAgencyResponse`
        """
        http_info = self._show_agency_http_info(request)
        return self._call_api(**http_info)

    def show_agency_async_invoker(self, request):
        http_info = self._show_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agency_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/agency",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'agency_type' in local_var_params:
            query_params.append(('agency_type', local_var_params['agency_type']))

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

    def create_catalog_async(self, request):
        """创建catalog

        创建catalog，会在catalog下创建默认数据库，默认数据库名称为：default
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCatalog
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateCatalogRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateCatalogResponse`
        """
        http_info = self._create_catalog_http_info(request)
        return self._call_api(**http_info)

    def create_catalog_async_invoker(self, request):
        http_info = self._create_catalog_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_catalog_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCatalogResponse"
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

    def delete_catalog_async(self, request):
        """删除catalog对象

        删除空的catalog对象。
        删除前需要保证catalog下只有默认的数据库，且默认数据库下没有表对象，否则删除失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCatalog
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteCatalogRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteCatalogResponse`
        """
        http_info = self._delete_catalog_http_info(request)
        return self._call_api(**http_info)

    def delete_catalog_async_invoker(self, request):
        http_info = self._delete_catalog_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_catalog_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']

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

    def list_catalogs_async(self, request):
        """列举catalog信息

        根据catalog名字的通配符列举catalog的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCatalogs
        :type request: :class:`huaweicloudsdklakeformation.v1.ListCatalogsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListCatalogsResponse`
        """
        http_info = self._list_catalogs_http_info(request)
        return self._call_api(**http_info)

    def list_catalogs_async_invoker(self, request):
        http_info = self._list_catalogs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_catalogs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "ListCatalogsResponse"
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

    def show_catalog_async(self, request):
        """获取catalog信息

        获取catalog信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCatalog
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowCatalogRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowCatalogResponse`
        """
        http_info = self._show_catalog_http_info(request)
        return self._call_api(**http_info)

    def show_catalog_async_invoker(self, request):
        http_info = self._show_catalog_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_catalog_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']

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

    def update_catalog_async(self, request):
        """修改catalog信息

        修改catalog信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCatalog
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateCatalogRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateCatalogResponse`
        """
        http_info = self._update_catalog_http_info(request)
        return self._call_api(**http_info)

    def update_catalog_async_invoker(self, request):
        http_info = self._update_catalog_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_catalog_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']

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

    def list_configs_async(self, request):
        """获取所有用户可见的租户面配置

        获取所有用户可见的租户面配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigs
        :type request: :class:`huaweicloudsdklakeformation.v1.ListConfigsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListConfigsResponse`
        """
        http_info = self._list_configs_http_info(request)
        return self._call_api(**http_info)

    def list_configs_async_invoker(self, request):
        http_info = self._list_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_credential_async(self, request):
        """获取临时密钥和securityToken

        获取临时密钥和securityToken，失效时间大于等于1小时，请在1小时内更新
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCredential
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowCredentialRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowCredentialResponse`
        """
        http_info = self._show_credential_http_info(request)
        return self._call_api(**http_info)

    def show_credential_async_invoker(self, request):
        http_info = self._show_credential_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_credential_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/credential",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCredentialResponse"
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

    def create_database_async(self, request):
        """创建数据库

        创建数据库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatabase
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateDatabaseRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateDatabaseResponse`
        """
        http_info = self._create_database_http_info(request)
        return self._call_api(**http_info)

    def create_database_async_invoker(self, request):
        http_info = self._create_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_database_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']

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

    def delete_database_async(self, request):
        """删除数据库

        删除指定数据库，catalog的默认数据库不允许删除。
        cascade: 指定为true时，删除数据库下的表；指定为false时，只能删除空的数据库
        delete_data: 指定为true时，级联删除会将表的数据放入回收站；指定为false时，不删除表数据
        删除数据库后不支持恢复数据库下的事务表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDatabase
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteDatabaseRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteDatabaseResponse`
        """
        http_info = self._delete_database_http_info(request)
        return self._call_api(**http_info)

    def delete_database_async_invoker(self, request):
        http_info = self._delete_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_database_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'delete_data' in local_var_params:
            query_params.append(('delete_data', local_var_params['delete_data']))
        if 'cascade' in local_var_params:
            query_params.append(('cascade', local_var_params['cascade']))

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

    def list_database_names_async(self, request):
        """列举数据库名称信息

        列举数据库名称信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabaseNames
        :type request: :class:`huaweicloudsdklakeformation.v1.ListDatabaseNamesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListDatabaseNamesResponse`
        """
        http_info = self._list_database_names_http_info(request)
        return self._call_api(**http_info)

    def list_database_names_async_invoker(self, request):
        http_info = self._list_database_names_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_database_names_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/names",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseNamesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']

        query_params = []
        if 'database_pattern' in local_var_params:
            query_params.append(('database_pattern', local_var_params['database_pattern']))

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

    def list_databases_async(self, request):
        """列举数据库信息

        列举数据库信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdklakeformation.v1.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListDatabasesResponse`
        """
        http_info = self._list_databases_http_info(request)
        return self._call_api(**http_info)

    def list_databases_async_invoker(self, request):
        http_info = self._list_databases_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_databases_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']

        query_params = []
        if 'database_name_pattern' in local_var_params:
            query_params.append(('database_name_pattern', local_var_params['database_name_pattern']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def show_database_async(self, request):
        """获取数据库

        获取数据库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDatabase
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowDatabaseRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowDatabaseResponse`
        """
        http_info = self._show_database_http_info(request)
        return self._call_api(**http_info)

    def show_database_async_invoker(self, request):
        http_info = self._show_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_database_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def update_database_async(self, request):
        """修改数据库属性

        修改数据库属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDatabase
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateDatabaseRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateDatabaseResponse`
        """
        http_info = self._update_database_http_info(request)
        return self._call_api(**http_info)

    def update_database_async_invoker(self, request):
        http_info = self._update_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_database_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def create_function_async(self, request):
        """创建函数

        创建函数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFunction
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateFunctionRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateFunctionResponse`
        """
        http_info = self._create_function_http_info(request)
        return self._call_api(**http_info)

    def create_function_async_invoker(self, request):
        http_info = self._create_function_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_function_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/functions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFunctionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def delete_function_async(self, request):
        """删除函数

        删除函数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFunction
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteFunctionRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteFunctionResponse`
        """
        http_info = self._delete_function_http_info(request)
        return self._call_api(**http_info)

    def delete_function_async_invoker(self, request):
        http_info = self._delete_function_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_function_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/functions/{function_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFunctionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'function_name' in local_var_params:
            path_params['function_name'] = local_var_params['function_name']

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

    def list_all_functions_async(self, request):
        """列举catalog下所有的函数

        获取catalog下所有的函数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllFunctions
        :type request: :class:`huaweicloudsdklakeformation.v1.ListAllFunctionsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListAllFunctionsResponse`
        """
        http_info = self._list_all_functions_http_info(request)
        return self._call_api(**http_info)

    def list_all_functions_async_invoker(self, request):
        http_info = self._list_all_functions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_functions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/functions",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllFunctionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def list_function_names_async(self, request):
        """列举库下所有函数名称

        查询数据库下的所有函数名称列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFunctionNames
        :type request: :class:`huaweicloudsdklakeformation.v1.ListFunctionNamesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListFunctionNamesResponse`
        """
        http_info = self._list_function_names_http_info(request)
        return self._call_api(**http_info)

    def list_function_names_async_invoker(self, request):
        http_info = self._list_function_names_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_function_names_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/functions/names",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionNamesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'function_pattern' in local_var_params:
            query_params.append(('function_pattern', local_var_params['function_pattern']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_functions_async(self, request):
        """列举函数

        列举函数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFunctions
        :type request: :class:`huaweicloudsdklakeformation.v1.ListFunctionsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListFunctionsResponse`
        """
        http_info = self._list_functions_http_info(request)
        return self._call_api(**http_info)

    def list_functions_async_invoker(self, request):
        http_info = self._list_functions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_functions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/functions",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'function_name_pattern' in local_var_params:
            query_params.append(('function_name_pattern', local_var_params['function_name_pattern']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def show_function_async(self, request):
        """查询函数

        根据函数名称查询函数信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFunction
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowFunctionRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowFunctionResponse`
        """
        http_info = self._show_function_http_info(request)
        return self._call_api(**http_info)

    def show_function_async_invoker(self, request):
        http_info = self._show_function_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_function_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/functions/{function_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFunctionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'function_name' in local_var_params:
            path_params['function_name'] = local_var_params['function_name']

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

    def update_function_async(self, request):
        """修改函数属性

        修改函数属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFunction
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateFunctionRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateFunctionResponse`
        """
        http_info = self._update_function_http_info(request)
        return self._call_api(**http_info)

    def update_function_async_invoker(self, request):
        http_info = self._update_function_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_function_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/functions/{function_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFunctionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'function_name' in local_var_params:
            path_params['function_name'] = local_var_params['function_name']

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

    def authorize_access_service_async(self, request):
        """接入服务授权

        接入服务授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AuthorizeAccessService
        :type request: :class:`huaweicloudsdklakeformation.v1.AuthorizeAccessServiceRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.AuthorizeAccessServiceResponse`
        """
        http_info = self._authorize_access_service_http_info(request)
        return self._call_api(**http_info)

    def authorize_access_service_async_invoker(self, request):
        http_info = self._authorize_access_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _authorize_access_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/access-service",
            "request_type": request.__class__.__name__,
            "response_type": "AuthorizeAccessServiceResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_agreement_async(self, request):
        """注册租户协议

        用户授权并委托
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgreement
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateAgreementRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateAgreementResponse`
        """
        http_info = self._create_agreement_http_info(request)
        return self._call_api(**http_info)

    def create_agreement_async_invoker(self, request):
        http_info = self._create_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agreement_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgreementResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_agreement_async(self, request):
        """删除租户协议

        用户取消授权，同时有权限用户删除委托
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAgreement
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteAgreementRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteAgreementResponse`
        """
        http_info = self._delete_agreement_http_info(request)
        return self._call_api(**http_info)

    def delete_agreement_async_invoker(self, request):
        http_info = self._delete_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_agreement_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgreementResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_access_service_async(self, request):
        """查询租户当前的接入服务授权

        查询租户当前的接入服务授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccessService
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowAccessServiceRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowAccessServiceResponse`
        """
        http_info = self._show_access_service_http_info(request)
        return self._call_api(**http_info)

    def show_access_service_async_invoker(self, request):
        http_info = self._show_access_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_access_service_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/access-service",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessServiceResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_agreement_async(self, request):
        """查询租户是否注册协议

        查询租户当前协议和委托信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgreement
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowAgreementRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowAgreementResponse`
        """
        http_info = self._show_agreement_http_info(request)
        return self._call_api(**http_info)

    def show_agreement_async_invoker(self, request):
        http_info = self._show_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agreement_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgreementResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_agreement_rule_async(self, request):
        """查询当前系统协议

        查询当前系统协议
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgreementRule
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowAgreementRuleRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowAgreementRuleResponse`
        """
        http_info = self._show_agreement_rule_http_info(request)
        return self._call_api(**http_info)

    def show_agreement_rule_async_invoker(self, request):
        http_info = self._show_agreement_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agreement_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/agreement-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgreementRuleResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_meta_obj_async(self, request):
        """元数据数量统计

        元数据数量统计接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountMetaObj
        :type request: :class:`huaweicloudsdklakeformation.v1.CountMetaObjRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CountMetaObjResponse`
        """
        http_info = self._count_meta_obj_http_info(request)
        return self._call_api(**http_info)

    def count_meta_obj_async_invoker(self, request):
        http_info = self._count_meta_obj_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_meta_obj_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/metaobj/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountMetaObjResponse"
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

    def create_lake_formation_instance_async(self, request):
        """创建实例

        创建一个LakeFormation实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLakeFormationInstance
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateLakeFormationInstanceRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateLakeFormationInstanceResponse`
        """
        http_info = self._create_lake_formation_instance_http_info(request)
        return self._call_api(**http_info)

    def create_lake_formation_instance_async_invoker(self, request):
        http_info = self._create_lake_formation_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_lake_formation_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLakeFormationInstanceResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_lake_formation_instance_async(self, request):
        """删除实例

        根据实例Id删除LakeFormation实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLakeFormationInstance
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteLakeFormationInstanceRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteLakeFormationInstanceResponse`
        """
        http_info = self._delete_lake_formation_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_lake_formation_instance_async_invoker(self, request):
        http_info = self._delete_lake_formation_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_lake_formation_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLakeFormationInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'to_recycle_bin' in local_var_params:
            query_params.append(('to_recycle_bin', local_var_params['to_recycle_bin']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_lake_formation_instances_async(self, request):
        """查询实例列表

        查询用户创建的实例列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLakeFormationInstances
        :type request: :class:`huaweicloudsdklakeformation.v1.ListLakeFormationInstancesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListLakeFormationInstancesResponse`
        """
        http_info = self._list_lake_formation_instances_http_info(request)
        return self._call_api(**http_info)

    def list_lake_formation_instances_async_invoker(self, request):
        http_info = self._list_lake_formation_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_lake_formation_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListLakeFormationInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'in_recycle_bin' in local_var_params:
            query_params.append(('in_recycle_bin', local_var_params['in_recycle_bin']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def move_lake_formation_instance_out_recycle_bin_async(self, request):
        """恢复实例

        从回收站恢复LakeFormation实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for MoveLakeFormationInstanceOutRecycleBin
        :type request: :class:`huaweicloudsdklakeformation.v1.MoveLakeFormationInstanceOutRecycleBinRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.MoveLakeFormationInstanceOutRecycleBinResponse`
        """
        http_info = self._move_lake_formation_instance_out_recycle_bin_http_info(request)
        return self._call_api(**http_info)

    def move_lake_formation_instance_out_recycle_bin_async_invoker(self, request):
        http_info = self._move_lake_formation_instance_out_recycle_bin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _move_lake_formation_instance_out_recycle_bin_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/recover",
            "request_type": request.__class__.__name__,
            "response_type": "MoveLakeFormationInstanceOutRecycleBinResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_lake_formation_instance_async(self, request):
        """查询实例详情

        使用实例Id查询LakeFormation实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLakeFormationInstance
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowLakeFormationInstanceRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowLakeFormationInstanceResponse`
        """
        http_info = self._show_lake_formation_instance_http_info(request)
        return self._call_api(**http_info)

    def show_lake_formation_instance_async_invoker(self, request):
        http_info = self._show_lake_formation_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_lake_formation_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLakeFormationInstanceResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_lake_formation_instance_async(self, request):
        """更新实例

        修改LakeFormation实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLakeFormationInstance
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstanceRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstanceResponse`
        """
        http_info = self._update_lake_formation_instance_http_info(request)
        return self._call_api(**http_info)

    def update_lake_formation_instance_async_invoker(self, request):
        http_info = self._update_lake_formation_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_lake_formation_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLakeFormationInstanceResponse"
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

    def update_lake_formation_instance_default_async(self, request):
        """设为默认实例

        设为默认实例，只有非默认实例可以设置为默认实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLakeFormationInstanceDefault
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstanceDefaultRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstanceDefaultResponse`
        """
        http_info = self._update_lake_formation_instance_default_http_info(request)
        return self._call_api(**http_info)

    def update_lake_formation_instance_default_async_invoker(self, request):
        http_info = self._update_lake_formation_instance_default_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_lake_formation_instance_default_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/default",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLakeFormationInstanceDefaultResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_lake_formation_instance_scale_async(self, request):
        """变更实例规格

        变更LakeFormation实例规格
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLakeFormationInstanceScale
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstanceScaleRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstanceScaleResponse`
        """
        http_info = self._update_lake_formation_instance_scale_http_info(request)
        return self._call_api(**http_info)

    def update_lake_formation_instance_scale_async_invoker(self, request):
        http_info = self._update_lake_formation_instance_scale_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_lake_formation_instance_scale_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/scale",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLakeFormationInstanceScaleResponse"
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        """查询OBS桶列表

        查询OBS桶列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListObsBuckets
        :type request: :class:`huaweicloudsdklakeformation.v1.ListObsBucketsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListObsBucketsResponse`
        """
        http_info = self._list_obs_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_obs_buckets_async_invoker(self, request):
        http_info = self._list_obs_buckets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_obs_buckets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/obs/buckets",
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_obs_object_async(self, request):
        """查询obs桶对象列表

        查询obs桶对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListObsObject
        :type request: :class:`huaweicloudsdklakeformation.v1.ListObsObjectRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListObsObjectResponse`
        """
        http_info = self._list_obs_object_http_info(request)
        return self._call_api(**http_info)

    def list_obs_object_async_invoker(self, request):
        http_info = self._list_obs_object_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_obs_object_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/obs/buckets/{bucket_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListObsObjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bucket_name' in local_var_params:
            path_params['bucket_name'] = local_var_params['bucket_name']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))

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

    def add_partitions_async(self, request):
        """批量添加分区信息

        批量添加分区信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddPartitions
        :type request: :class:`huaweicloudsdklakeformation.v1.AddPartitionsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.AddPartitionsResponse`
        """
        http_info = self._add_partitions_http_info(request)
        return self._call_api(**http_info)

    def add_partitions_async_invoker(self, request):
        http_info = self._add_partitions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_partitions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "AddPartitionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def batch_delete_partition_async(self, request):
        """批量删除分区信息

        非事务表：如果设置删除数据，立刻删除分区数据路径下的数据。
        事务表：如果设置删除数据，保留数据在原路径下但对外不可见，待数据超期后统一删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePartition
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchDeletePartitionRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchDeletePartitionResponse`
        """
        http_info = self._batch_delete_partition_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_partition_async_invoker(self, request):
        http_info = self._batch_delete_partition_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_partition_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/batch-drop",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePartitionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def batch_delete_partitioned_statistics_async(self, request):
        """批量清空列表信息

        删除存在分区的数据及统计信息，保留分区的元数据信息。全部存在、部分存在或都不存在，均返回OK
        非事务表：立刻删除分区路径下的数据。
        事务表：数据保留但不可见，待被删除数据超期后统一删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePartitionedStatistics
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchDeletePartitionedStatisticsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchDeletePartitionedStatisticsResponse`
        """
        http_info = self._batch_delete_partitioned_statistics_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_partitioned_statistics_async_invoker(self, request):
        http_info = self._batch_delete_partitioned_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_partitioned_statistics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/batch-truncate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePartitionedStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def batch_list_partition_by_values_async(self, request):
        """批量获取分区信息

        批量获取分区信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListPartitionByValues
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchListPartitionByValuesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchListPartitionByValuesResponse`
        """
        http_info = self._batch_list_partition_by_values_http_info(request)
        return self._call_api(**http_info)

    def batch_list_partition_by_values_async_invoker(self, request):
        http_info = self._batch_list_partition_by_values_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_partition_by_values_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/batch-get",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListPartitionByValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def batch_update_partition_async(self, request):
        """批量修改分区信息

        所有partition必须要全部存在，如果存在某个partition不存在，就返回失败
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdatePartition
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchUpdatePartitionRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchUpdatePartitionResponse`
        """
        http_info = self._batch_update_partition_http_info(request)
        return self._call_api(**http_info)

    def batch_update_partition_async_invoker(self, request):
        http_info = self._batch_update_partition_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_partition_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/batch-alter",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdatePartitionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def list_partition_names_async(self, request):
        """列举分区值列表

        遍历分区名字列表信息
        对于事务表，支持基于表的特定版本遍历分区名字列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPartitionNames
        :type request: :class:`huaweicloudsdklakeformation.v1.ListPartitionNamesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListPartitionNamesResponse`
        """
        http_info = self._list_partition_names_http_info(request)
        return self._call_api(**http_info)

    def list_partition_names_async_invoker(self, request):
        http_info = self._list_partition_names_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_partition_names_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/partition-names",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartitionNamesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def list_partition_names_without_limit_async(self, request):
        """列举全量分区值列表

        遍历分区名称列表信息,返回全量的数据。
        对于事务表，支持基于表的特定版本遍历分区名称列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPartitionNamesWithoutLimit
        :type request: :class:`huaweicloudsdklakeformation.v1.ListPartitionNamesWithoutLimitRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListPartitionNamesWithoutLimitResponse`
        """
        http_info = self._list_partition_names_without_limit_http_info(request)
        return self._call_api(**http_info)

    def list_partition_names_without_limit_async_invoker(self, request):
        http_info = self._list_partition_names_without_limit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_partition_names_without_limit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/names",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartitionNamesWithoutLimitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
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

    def list_partitions_async(self, request):
        """列举分区信息

        遍历指定数据表下的分区列表，对于事务表，支持基于表的特定版本遍历分区列表。
        当过滤条件不为空时，优先根据过滤条件筛选过滤，
        当过滤条件为空且分区值不为空时，再根据分区值筛选过滤，
        当过滤条件和分区值都为空时，返回指定数据表下所有分区。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPartitions
        :type request: :class:`huaweicloudsdklakeformation.v1.ListPartitionsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListPartitionsResponse`
        """
        http_info = self._list_partitions_http_info(request)
        return self._call_api(**http_info)

    def list_partitions_async_invoker(self, request):
        http_info = self._list_partitions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_partitions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartitionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'partition_values' in local_var_params:
            query_params.append(('partition_values', local_var_params['partition_values']))
            collection_formats['partition_values'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def batch_show_partition_column_statistics_async(self, request):
        """批量获取分区的列统计信息

        批量获取分区的列统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchShowPartitionColumnStatistics
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchShowPartitionColumnStatisticsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchShowPartitionColumnStatisticsResponse`
        """
        http_info = self._batch_show_partition_column_statistics_http_info(request)
        return self._call_api(**http_info)

    def batch_show_partition_column_statistics_async_invoker(self, request):
        http_info = self._batch_show_partition_column_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_show_partition_column_statistics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/column-statistics/batch-get",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowPartitionColumnStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def delete_partition_column_statistics_async(self, request):
        """删除分区列的统计信息

        删除分区列的统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePartitionColumnStatistics
        :type request: :class:`huaweicloudsdklakeformation.v1.DeletePartitionColumnStatisticsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeletePartitionColumnStatisticsResponse`
        """
        http_info = self._delete_partition_column_statistics_http_info(request)
        return self._call_api(**http_info)

    def delete_partition_column_statistics_async_invoker(self, request):
        http_info = self._delete_partition_column_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_partition_column_statistics_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/column-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePartitionColumnStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
        if 'partition_values' in local_var_params:
            query_params.append(('partition_values', local_var_params['partition_values']))
            collection_formats['partition_values'] = 'multi'
        if 'column_name' in local_var_params:
            query_params.append(('column_name', local_var_params['column_name']))

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

    def set_partition_column_statistics_async(self, request):
        """批量设置分区的统计信息

        批量设置分区的统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetPartitionColumnStatistics
        :type request: :class:`huaweicloudsdklakeformation.v1.SetPartitionColumnStatisticsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.SetPartitionColumnStatisticsResponse`
        """
        http_info = self._set_partition_column_statistics_http_info(request)
        return self._call_api(**http_info)

    def set_partition_column_statistics_async_invoker(self, request):
        http_info = self._set_partition_column_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_partition_column_statistics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/partitions/column-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "SetPartitionColumnStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def list_quotas_async(self, request):
        """查询配额

        查询用户的配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdklakeformation.v1.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListQuotasResponse`
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def associate_principals_async(self, request):
        """将一个或者多个用户/用户组加入角色

        将一个或者多个用户/用户组加入角色
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociatePrincipals
        :type request: :class:`huaweicloudsdklakeformation.v1.AssociatePrincipalsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.AssociatePrincipalsResponse`
        """
        http_info = self._associate_principals_http_info(request)
        return self._call_api(**http_info)

    def associate_principals_async_invoker(self, request):
        http_info = self._associate_principals_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_principals_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles/{role_name}/grant-principals",
            "request_type": request.__class__.__name__,
            "response_type": "AssociatePrincipalsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'role_name' in local_var_params:
            path_params['role_name'] = local_var_params['role_name']

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

    def create_role_async(self, request):
        """创建role

        创建role
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRole
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateRoleRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateRoleResponse`
        """
        http_info = self._create_role_http_info(request)
        return self._call_api(**http_info)

    def create_role_async_invoker(self, request):
        http_info = self._create_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_role_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRoleResponse"
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

    def delete_role_async(self, request):
        """删除角色

        删除指定角色
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRole
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteRoleRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteRoleResponse`
        """
        http_info = self._delete_role_http_info(request)
        return self._call_api(**http_info)

    def delete_role_async_invoker(self, request):
        http_info = self._delete_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_role_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles/{role_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'role_name' in local_var_params:
            path_params['role_name'] = local_var_params['role_name']

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

    def list_principals_async(self, request):
        """查询角色下的用户/用户组

        查询角色下的用户/用户组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrincipals
        :type request: :class:`huaweicloudsdklakeformation.v1.ListPrincipalsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListPrincipalsResponse`
        """
        http_info = self._list_principals_http_info(request)
        return self._call_api(**http_info)

    def list_principals_async_invoker(self, request):
        http_info = self._list_principals_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_principals_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles/{role_name}/principals",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrincipalsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'role_name' in local_var_params:
            path_params['role_name'] = local_var_params['role_name']

        query_params = []
        if 'principal_pattern' in local_var_params:
            query_params.append(('principal_pattern', local_var_params['principal_pattern']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def list_role_names_async(self, request):
        """列举所有角色名

        查询所有角色名字列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRoleNames
        :type request: :class:`huaweicloudsdklakeformation.v1.ListRoleNamesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListRoleNamesResponse`
        """
        http_info = self._list_role_names_http_info(request)
        return self._call_api(**http_info)

    def list_role_names_async_invoker(self, request):
        http_info = self._list_role_names_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_role_names_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles/names",
            "request_type": request.__class__.__name__,
            "response_type": "ListRoleNamesResponse"
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

    def list_roles_async(self, request):
        """根据条件分页列举角色

        返回所有角色
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRoles
        :type request: :class:`huaweicloudsdklakeformation.v1.ListRolesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListRolesResponse`
        """
        http_info = self._list_roles_http_info(request)
        return self._call_api(**http_info)

    def list_roles_async_invoker(self, request):
        http_info = self._list_roles_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_roles_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListRolesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'role_pattern' in local_var_params:
            query_params.append(('role_pattern', local_var_params['role_pattern']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def revoke_principals_async(self, request):
        """将一个或者多个用户/用户组从角色移除

        将一个或者多个用户/用户组从角色移除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RevokePrincipals
        :type request: :class:`huaweicloudsdklakeformation.v1.RevokePrincipalsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.RevokePrincipalsResponse`
        """
        http_info = self._revoke_principals_http_info(request)
        return self._call_api(**http_info)

    def revoke_principals_async_invoker(self, request):
        http_info = self._revoke_principals_http_info(request)
        return AsyncInvoker(self, http_info)

    def _revoke_principals_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles/{role_name}/revoke-principals",
            "request_type": request.__class__.__name__,
            "response_type": "RevokePrincipalsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'role_name' in local_var_params:
            path_params['role_name'] = local_var_params['role_name']

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

    def show_role_async(self, request):
        """获取角色

        获取角色
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRole
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowRoleRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowRoleResponse`
        """
        http_info = self._show_role_http_info(request)
        return self._call_api(**http_info)

    def show_role_async_invoker(self, request):
        http_info = self._show_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_role_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles/{role_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'role_name' in local_var_params:
            path_params['role_name'] = local_var_params['role_name']

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

    def update_principals_async(self, request):
        """更新角色中的principals

        更新角色中的principals
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrincipals
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdatePrincipalsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdatePrincipalsResponse`
        """
        http_info = self._update_principals_http_info(request)
        return self._call_api(**http_info)

    def update_principals_async_invoker(self, request):
        http_info = self._update_principals_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_principals_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles/{role_name}/update-principals",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrincipalsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'role_name' in local_var_params:
            path_params['role_name'] = local_var_params['role_name']

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

    def update_role_async(self, request):
        """修改角色信息

        修改角色信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRole
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateRoleRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateRoleResponse`
        """
        http_info = self._update_role_http_info(request)
        return self._call_api(**http_info)

    def update_role_async_invoker(self, request):
        http_info = self._update_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_role_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/roles/{role_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'role_name' in local_var_params:
            path_params['role_name'] = local_var_params['role_name']

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

    def list_specs_async(self, request):
        """list_specs

        查询规格列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSpecs
        :type request: :class:`huaweicloudsdklakeformation.v1.ListSpecsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListSpecsResponse`
        """
        http_info = self._list_specs_http_info(request)
        return self._call_api(**http_info)

    def list_specs_async_invoker(self, request):
        http_info = self._list_specs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_specs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/specs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpecsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
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

    def batch_update_lake_formation_instance_tags_async(self, request):
        """批量更新标签

        为指定实例批量更新标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateLakeFormationInstanceTags
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchUpdateLakeFormationInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchUpdateLakeFormationInstanceTagsResponse`
        """
        http_info = self._batch_update_lake_formation_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_update_lake_formation_instance_tags_async_invoker(self, request):
        http_info = self._batch_update_lake_formation_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_lake_formation_instance_tags_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateLakeFormationInstanceTagsResponse"
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

    def list_lake_formation_instance_tags_async(self, request):
        """查询资源标签集合

        查询租户在指定Project中实例类型的所有资源标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLakeFormationInstanceTags
        :type request: :class:`huaweicloudsdklakeformation.v1.ListLakeFormationInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListLakeFormationInstanceTagsResponse`
        """
        http_info = self._list_lake_formation_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def list_lake_formation_instance_tags_async_invoker(self, request):
        http_info = self._list_lake_formation_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_lake_formation_instance_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/lakeformation-instance/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListLakeFormationInstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'use_predefine_tags' in local_var_params:
            query_params.append(('use_predefine_tags', local_var_params['use_predefine_tags']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_table_async(self, request):
        """创建表

        创建表操作
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTable
        :type request: :class:`huaweicloudsdklakeformation.v1.CreateTableRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.CreateTableResponse`
        """
        http_info = self._create_table_http_info(request)
        return self._call_api(**http_info)

    def create_table_async_invoker(self, request):
        http_info = self._create_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_table_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def delete_all_tables_async(self, request):
        """清空表的数据

        清空表以及表下所有分区的数据及统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAllTables
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteAllTablesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteAllTablesResponse`
        """
        http_info = self._delete_all_tables_http_info(request)
        return self._call_api(**http_info)

    def delete_all_tables_async_invoker(self, request):
        http_info = self._delete_all_tables_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_all_tables_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/truncate",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAllTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def delete_table_async(self, request):
        """删除表

        删除表及表下的分区
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTable
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteTableRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteTableResponse`
        """
        http_info = self._delete_table_http_info(request)
        return self._call_api(**http_info)

    def delete_table_async_invoker(self, request):
        http_info = self._delete_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_table_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
        if 'delete_data' in local_var_params:
            query_params.append(('delete_data', local_var_params['delete_data']))

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

    def list_table_meta_async(self, request):
        """分页获取表的描述信息

        通过数据库通配符和表通配符，找到符合条件的表并返回表的描述信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTableMeta
        :type request: :class:`huaweicloudsdklakeformation.v1.ListTableMetaRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListTableMetaResponse`
        """
        http_info = self._list_table_meta_http_info(request)
        return self._call_api(**http_info)

    def list_table_meta_async_invoker(self, request):
        http_info = self._list_table_meta_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_table_meta_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableMetaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']

        query_params = []
        if 'database_name_pattern' in local_var_params:
            query_params.append(('database_name_pattern', local_var_params['database_name_pattern']))
        if 'table_name_pattern' in local_var_params:
            query_params.append(('table_name_pattern', local_var_params['table_name_pattern']))
        if 'table_types' in local_var_params:
            query_params.append(('table_types', local_var_params['table_types']))
            collection_formats['table_types'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def list_table_names_async(self, request):
        """列举库下所有表名

        查询数据库下的所有表名字列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTableNames
        :type request: :class:`huaweicloudsdklakeformation.v1.ListTableNamesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListTableNamesResponse`
        """
        http_info = self._list_table_names_http_info(request)
        return self._call_api(**http_info)

    def list_table_names_async_invoker(self, request):
        http_info = self._list_table_names_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_table_names_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/names",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableNamesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'table_pattern' in local_var_params:
            query_params.append(('table_pattern', local_var_params['table_pattern']))
        if 'table_type' in local_var_params:
            query_params.append(('table_type', local_var_params['table_type']))

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

    def list_tables_async(self, request):
        """根据条件分页列举表信息

        返回数据库下符合查询条件的表的元数据信息，不支持事务操作
        当表名通配符或表类型不为空时，优先根据表名和类型筛选过滤
        当表名通配符或表类型为空时，再根据属性筛选过滤
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTables
        :type request: :class:`huaweicloudsdklakeformation.v1.ListTablesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListTablesResponse`
        """
        http_info = self._list_tables_http_info(request)
        return self._call_api(**http_info)

    def list_tables_async_invoker(self, request):
        http_info = self._list_tables_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tables_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'table_name_pattern' in local_var_params:
            query_params.append(('table_name_pattern', local_var_params['table_name_pattern']))
        if 'table_type' in local_var_params:
            query_params.append(('table_type', local_var_params['table_type']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def list_tables_by_name_async(self, request):
        """根据表名列举表信息

        根据表名查询数据库下的表信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTablesByName
        :type request: :class:`huaweicloudsdklakeformation.v1.ListTablesByNameRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListTablesByNameResponse`
        """
        http_info = self._list_tables_by_name_http_info(request)
        return self._call_api(**http_info)

    def list_tables_by_name_async_invoker(self, request):
        http_info = self._list_tables_by_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tables_by_name_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/list-by-names",
            "request_type": request.__class__.__name__,
            "response_type": "ListTablesByNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def show_table_async(self, request):
        """获取表信息

        获取表信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTable
        :type request: :class:`huaweicloudsdklakeformation.v1.ShowTableRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ShowTableResponse`
        """
        http_info = self._show_table_http_info(request)
        return self._call_api(**http_info)

    def show_table_async_invoker(self, request):
        http_info = self._show_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_table_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def update_table_async(self, request):
        """修改表信息

        修改表信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTable
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateTableRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateTableResponse`
        """
        http_info = self._update_table_http_info(request)
        return self._call_api(**http_info)

    def update_table_async_invoker(self, request):
        http_info = self._update_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_table_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def delete_table_column_statistics_async(self, request):
        """删除表的指定列统计信息

        删除表的指定列统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTableColumnStatistics
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteTableColumnStatisticsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteTableColumnStatisticsResponse`
        """
        http_info = self._delete_table_column_statistics_http_info(request)
        return self._call_api(**http_info)

    def delete_table_column_statistics_async_invoker(self, request):
        http_info = self._delete_table_column_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_table_column_statistics_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/column-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTableColumnStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
        if 'column_name' in local_var_params:
            query_params.append(('column_name', local_var_params['column_name']))

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

    def list_table_column_statistics_async(self, request):
        """获取表的列统计信息

        获取表的列统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTableColumnStatistics
        :type request: :class:`huaweicloudsdklakeformation.v1.ListTableColumnStatisticsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListTableColumnStatisticsResponse`
        """
        http_info = self._list_table_column_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_table_column_statistics_async_invoker(self, request):
        http_info = self._list_table_column_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_table_column_statistics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/column-statistics/batch-get",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableColumnStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def set_table_column_statistics_async(self, request):
        """更新表的列统计信息

        更新表的列统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetTableColumnStatistics
        :type request: :class:`huaweicloudsdklakeformation.v1.SetTableColumnStatisticsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.SetTableColumnStatisticsResponse`
        """
        http_info = self._set_table_column_statistics_http_info(request)
        return self._call_api(**http_info)

    def set_table_column_statistics_async_invoker(self, request):
        http_info = self._set_table_column_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_table_column_statistics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/column-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "SetTableColumnStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def batch_create_constraint_async(self, request):
        """批量创建列限制条件

        批量创建表的列限制条件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateConstraint
        :type request: :class:`huaweicloudsdklakeformation.v1.BatchCreateConstraintRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.BatchCreateConstraintResponse`
        """
        http_info = self._batch_create_constraint_http_info(request)
        return self._call_api(**http_info)

    def batch_create_constraint_async_invoker(self, request):
        http_info = self._batch_create_constraint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_constraint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/constraints",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateConstraintResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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

    def delete_constraint_async(self, request):
        """删除列限制条件

        删除列限制条件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConstraint
        :type request: :class:`huaweicloudsdklakeformation.v1.DeleteConstraintRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.DeleteConstraintResponse`
        """
        http_info = self._delete_constraint_http_info(request)
        return self._call_api(**http_info)

    def delete_constraint_async_invoker(self, request):
        http_info = self._delete_constraint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_constraint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/constraints/{constraint_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConstraintResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']
        if 'constraint_name' in local_var_params:
            path_params['constraint_name'] = local_var_params['constraint_name']

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

    def list_constraints_async(self, request):
        """获取列限制条件

        若查询外键信息，需要在参数中填写被引用表的数据库名和表名。如：parent_db&#x3D;db1&amp;parent_tbl&#x3D;tbl1
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConstraints
        :type request: :class:`huaweicloudsdklakeformation.v1.ListConstraintsRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListConstraintsResponse`
        """
        http_info = self._list_constraints_http_info(request)
        return self._call_api(**http_info)

    def list_constraints_async_invoker(self, request):
        http_info = self._list_constraints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_constraints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/catalogs/{catalog_name}/databases/{database_name}/tables/{table_name}/constraints",
            "request_type": request.__class__.__name__,
            "response_type": "ListConstraintsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'catalog_name' in local_var_params:
            path_params['catalog_name'] = local_var_params['catalog_name']
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'parent_db' in local_var_params:
            query_params.append(('parent_db', local_var_params['parent_db']))
        if 'parent_tbl' in local_var_params:
            query_params.append(('parent_tbl', local_var_params['parent_tbl']))

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

    def associate_roles_async(self, request):
        """将多个角色授予User

        将多个角色授予User
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRoles
        :type request: :class:`huaweicloudsdklakeformation.v1.AssociateRolesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.AssociateRolesResponse`
        """
        http_info = self._associate_roles_http_info(request)
        return self._call_api(**http_info)

    def associate_roles_async_invoker(self, request):
        http_info = self._associate_roles_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_roles_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users/{user_name}/grant-roles",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRolesResponse"
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

    def list_user_roles_async(self, request):
        """查询用户的角色列表

        查询用户的角色列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserRoles
        :type request: :class:`huaweicloudsdklakeformation.v1.ListUserRolesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListUserRolesResponse`
        """
        http_info = self._list_user_roles_http_info(request)
        return self._call_api(**http_info)

    def list_user_roles_async_invoker(self, request):
        http_info = self._list_user_roles_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_roles_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users/{user_name}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserRolesResponse"
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
        if 'role_pattern' in local_var_params:
            query_params.append(('role_pattern', local_var_params['role_pattern']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

    def list_users_async(self, request):
        """获取用户列表

        获取用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdklakeformation.v1.ListUsersRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_async_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'user_source' in local_var_params:
            query_params.append(('user_source', local_var_params['user_source']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))
        if 'user_name_pattern' in local_var_params:
            query_params.append(('user_name_pattern', local_var_params['user_name_pattern']))

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

    def revoke_roles_async(self, request):
        """将一个或者多个角色从用户移除

        将一个或者多个角色从用户移除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RevokeRoles
        :type request: :class:`huaweicloudsdklakeformation.v1.RevokeRolesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.RevokeRolesResponse`
        """
        http_info = self._revoke_roles_http_info(request)
        return self._call_api(**http_info)

    def revoke_roles_async_invoker(self, request):
        http_info = self._revoke_roles_http_info(request)
        return AsyncInvoker(self, http_info)

    def _revoke_roles_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users/{user_name}/revoke-roles",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeRolesResponse"
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

    def update_roles_async(self, request):
        """更新用户中的角色

        更新用户中的角色
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRoles
        :type request: :class:`huaweicloudsdklakeformation.v1.UpdateRolesRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateRolesResponse`
        """
        http_info = self._update_roles_http_info(request)
        return self._call_api(**http_info)

    def update_roles_async_invoker(self, request):
        http_info = self._update_roles_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_roles_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users/{user_name}/update-roles",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRolesResponse"
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

    def list_groups_for_domain_async(self, request):
        """获取租户的用户组

        获取租户的用户组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupsForDomain
        :type request: :class:`huaweicloudsdklakeformation.v1.ListGroupsForDomainRequest`
        :rtype: :class:`huaweicloudsdklakeformation.v1.ListGroupsForDomainResponse`
        """
        http_info = self._list_groups_for_domain_http_info(request)
        return self._call_api(**http_info)

    def list_groups_for_domain_async_invoker(self, request):
        http_info = self._list_groups_for_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_groups_for_domain_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupsForDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'group_source' in local_var_params:
            query_params.append(('group_source', local_var_params['group_source']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reverse_page' in local_var_params:
            query_params.append(('reverse_page', local_var_params['reverse_page']))

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

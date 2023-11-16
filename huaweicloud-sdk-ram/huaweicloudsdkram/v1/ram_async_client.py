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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkram'")


class RamAsyncClient(Client):
    def __init__(self):
        super(RamAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkram.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "RamAsyncClient":
                raise TypeError("client type error, support client type is RamAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def associate_resource_share_permission_async(self, request):
        """绑定或替换共享资源权限

        为资源共享实例中包含的资源类型绑定或替换共享资源权限。 对于资源共享实例中的每一种资源类型，您可以设置唯一权限。仅当资源共享实例中当前没有该资源类型的资源时，您才能绑定新的共享资源权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateResourceSharePermission
        :type request: :class:`huaweicloudsdkram.v1.AssociateResourceSharePermissionRequest`
        :rtype: :class:`huaweicloudsdkram.v1.AssociateResourceSharePermissionResponse`
        """
        http_info = self._associate_resource_share_permission_http_info(request)
        return self._call_api(**http_info)

    def associate_resource_share_permission_async_invoker(self, request):
        http_info = self._associate_resource_share_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_resource_share_permission_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/{resource_share_id}/associate-permission",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateResourceSharePermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disassociate_resource_share_permission_async(self, request):
        """移除共享资源权限

        移除资源共享实例绑定的共享资源权限。权限更改立即生效。只有当目前资源共享实例中没有绑定相关资源类型时，您才能从资源共享实例中移除共享资源权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateResourceSharePermission
        :type request: :class:`huaweicloudsdkram.v1.DisassociateResourceSharePermissionRequest`
        :rtype: :class:`huaweicloudsdkram.v1.DisassociateResourceSharePermissionResponse`
        """
        http_info = self._disassociate_resource_share_permission_http_info(request)
        return self._call_api(**http_info)

    def disassociate_resource_share_permission_async_invoker(self, request):
        http_info = self._disassociate_resource_share_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_resource_share_permission_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/{resource_share_id}/disassociate-permission",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateResourceSharePermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_share_permissions_async(self, request):
        """检索绑定的共享资源权限

        检索资源共享实例关联的共享资源权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceSharePermissions
        :type request: :class:`huaweicloudsdkram.v1.ListResourceSharePermissionsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListResourceSharePermissionsResponse`
        """
        http_info = self._list_resource_share_permissions_http_info(request)
        return self._call_api(**http_info)

    def list_resource_share_permissions_async_invoker(self, request):
        http_info = self._list_resource_share_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_share_permissions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-shares/{resource_share_id}/associated-permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceSharePermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

        query_params = []
        if 'permission_name' in local_var_params:
            query_params.append(('permission_name', local_var_params['permission_name']))
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_quota_async(self, request):
        """查询资源共享的配额

        查询当前帐号的资源共享配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuota
        :type request: :class:`huaweicloudsdkram.v1.ListQuotaRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListQuotaResponse`
        """
        http_info = self._list_quota_http_info(request)
        return self._call_api(**http_info)

    def list_quota_async_invoker(self, request):
        http_info = self._list_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-shares/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotaResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_types_async(self, request):
        """检索云服务资源类型

        查询已对接云服务的资源类型和区域等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceTypes
        :type request: :class:`huaweicloudsdkram.v1.ListResourceTypesRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListResourceTypesResponse`
        """
        http_info = self._list_resource_types_http_info(request)
        return self._call_api(**http_info)

    def list_resource_types_async_invoker(self, request):
        http_info = self._list_resource_types_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_types_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceTypesResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_organization_share_async(self, request):
        """关闭与组织共享

        关闭与组织共享资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableOrganizationShare
        :type request: :class:`huaweicloudsdkram.v1.DisableOrganizationShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.DisableOrganizationShareResponse`
        """
        http_info = self._disable_organization_share_http_info(request)
        return self._call_api(**http_info)

    def disable_organization_share_async_invoker(self, request):
        http_info = self._disable_organization_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_organization_share_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organization-share/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableOrganizationShareResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_organization_share_async(self, request):
        """启用与组织共享

        启用与组织共享资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableOrganizationShare
        :type request: :class:`huaweicloudsdkram.v1.EnableOrganizationShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.EnableOrganizationShareResponse`
        """
        http_info = self._enable_organization_share_http_info(request)
        return self._call_api(**http_info)

    def enable_organization_share_async_invoker(self, request):
        http_info = self._enable_organization_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_organization_share_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organization-share/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableOrganizationShareResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_organization_share_async(self, request):
        """检索是否启用与组织共享

        检索是否启用与组织共享资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOrganizationShare
        :type request: :class:`huaweicloudsdkram.v1.ShowOrganizationShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ShowOrganizationShareResponse`
        """
        http_info = self._show_organization_share_http_info(request)
        return self._call_api(**http_info)

    def show_organization_share_async_invoker(self, request):
        http_info = self._show_organization_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_organization_share_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organization-share",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrganizationShareResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_permissions_async(self, request):
        """检索共享资源权限列表

        检索指定资源类型的共享资源权限列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermissions
        :type request: :class:`huaweicloudsdkram.v1.ListPermissionsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListPermissionsResponse`
        """
        http_info = self._list_permissions_http_info(request)
        return self._call_api(**http_info)

    def list_permissions_async_invoker(self, request):
        http_info = self._list_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_permissions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermissionsResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_permission_async(self, request):
        """检索资源共享权限内容

        检索指定资源类型的共享资源权限内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPermission
        :type request: :class:`huaweicloudsdkram.v1.ShowPermissionRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ShowPermissionResponse`
        """
        http_info = self._show_permission_http_info(request)
        return self._call_api(**http_info)

    def show_permission_async_invoker(self, request):
        http_info = self._show_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/permissions/{permission_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'permission_id' in local_var_params:
            path_params['permission_id'] = local_var_params['permission_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_shared_principals_async(self, request):
        """检索资源使用者

        检索共享资源的使用者。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchSharedPrincipals
        :type request: :class:`huaweicloudsdkram.v1.SearchSharedPrincipalsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchSharedPrincipalsResponse`
        """
        http_info = self._search_shared_principals_http_info(request)
        return self._call_api(**http_info)

    def search_shared_principals_async_invoker(self, request):
        http_info = self._search_shared_principals_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_shared_principals_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/shared-principals/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchSharedPrincipalsResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_shared_resources_async(self, request):
        """检索共享的资源

        检索您共享的或共享给您的资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchSharedResources
        :type request: :class:`huaweicloudsdkram.v1.SearchSharedResourcesRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchSharedResourcesResponse`
        """
        http_info = self._search_shared_resources_http_info(request)
        return self._call_api(**http_info)

    def search_shared_resources_async_invoker(self, request):
        http_info = self._search_shared_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_shared_resources_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/shared-resources/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchSharedResourcesResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_resource_share_async(self, request):
        """创建资源共享实例

        创建一个资源共享实例。您可以指定需要共享的资源列表，资源使用者列表，以及授予资源使用者的权限列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourceShare
        :type request: :class:`huaweicloudsdkram.v1.CreateResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.CreateResourceShareResponse`
        """
        http_info = self._create_resource_share_http_info(request)
        return self._call_api(**http_info)

    def create_resource_share_async_invoker(self, request):
        http_info = self._create_resource_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_resource_share_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceShareResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_resource_share_async(self, request):
        """删除资源共享实例

        删除指定的资源共享实例。此操作不会删除实体资源，仅停止向其他帐号共享资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceShare
        :type request: :class:`huaweicloudsdkram.v1.DeleteResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.DeleteResourceShareResponse`
        """
        http_info = self._delete_resource_share_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_share_async_invoker(self, request):
        http_info = self._delete_resource_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_resource_share_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-shares/{resource_share_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_resource_shares_async(self, request):
        """检索资源共享实例

        检索您创建的或者共享给您的资源共享实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchResourceShares
        :type request: :class:`huaweicloudsdkram.v1.SearchResourceSharesRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchResourceSharesResponse`
        """
        http_info = self._search_resource_shares_http_info(request)
        return self._call_api(**http_info)

    def search_resource_shares_async_invoker(self, request):
        http_info = self._search_resource_shares_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_resource_shares_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchResourceSharesResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_resource_share_async(self, request):
        """更新资源共享实例

        修改资源共享实例的特定属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResourceShare
        :type request: :class:`huaweicloudsdkram.v1.UpdateResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.UpdateResourceShareResponse`
        """
        http_info = self._update_resource_share_http_info(request)
        return self._call_api(**http_info)

    def update_resource_share_async_invoker(self, request):
        http_info = self._update_resource_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_resource_share_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-shares/{resource_share_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def associate_resource_share_async(self, request):
        """绑定资源使用者和共享资源

        向资源共享实例绑定指定的资源使用者列表或共享资源列表。对于新增的共享资源，有权访问此资源共享实例的资源使用者获得该共享资源的访问权限。对于新增的资源使用者，获得对此资源共享实例中共享资源的访问权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateResourceShare
        :type request: :class:`huaweicloudsdkram.v1.AssociateResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.AssociateResourceShareResponse`
        """
        http_info = self._associate_resource_share_http_info(request)
        return self._call_api(**http_info)

    def associate_resource_share_async_invoker(self, request):
        http_info = self._associate_resource_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_resource_share_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/{resource_share_id}/associate",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateResourceShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disassociate_resource_share_async(self, request):
        """移除资源使用者和共享资源

        将指定的资源使用者或共享资源从指定的资源共享实例中移除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateResourceShare
        :type request: :class:`huaweicloudsdkram.v1.DisassociateResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.DisassociateResourceShareResponse`
        """
        http_info = self._disassociate_resource_share_http_info(request)
        return self._call_api(**http_info)

    def disassociate_resource_share_async_invoker(self, request):
        http_info = self._disassociate_resource_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_resource_share_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/{resource_share_id}/disassociate",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateResourceShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_resource_share_associations_async(self, request):
        """检索绑定的资源使用者和共享资源

        检索您拥有的资源共享实例中绑定的共享资源和资源使用者。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchResourceShareAssociations
        :type request: :class:`huaweicloudsdkram.v1.SearchResourceShareAssociationsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchResourceShareAssociationsResponse`
        """
        http_info = self._search_resource_share_associations_http_info(request)
        return self._call_api(**http_info)

    def search_resource_share_associations_async_invoker(self, request):
        http_info = self._search_resource_share_associations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_resource_share_associations_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-share-associations/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchResourceShareAssociationsResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def accept_resource_share_invitation_async(self, request):
        """接受共享邀请

        接受来自其他帐号的资源共享邀请。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptResourceShareInvitation
        :type request: :class:`huaweicloudsdkram.v1.AcceptResourceShareInvitationRequest`
        :rtype: :class:`huaweicloudsdkram.v1.AcceptResourceShareInvitationResponse`
        """
        http_info = self._accept_resource_share_invitation_http_info(request)
        return self._call_api(**http_info)

    def accept_resource_share_invitation_async_invoker(self, request):
        http_info = self._accept_resource_share_invitation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _accept_resource_share_invitation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-share-invitations/{resource_share_invitation_id}/accept",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptResourceShareInvitationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_invitation_id' in local_var_params:
            path_params['resource_share_invitation_id'] = local_var_params['resource_share_invitation_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reject_resource_share_invitation_async(self, request):
        """拒绝共享邀请

        拒绝来自其他帐号的资源共享邀请。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RejectResourceShareInvitation
        :type request: :class:`huaweicloudsdkram.v1.RejectResourceShareInvitationRequest`
        :rtype: :class:`huaweicloudsdkram.v1.RejectResourceShareInvitationResponse`
        """
        http_info = self._reject_resource_share_invitation_http_info(request)
        return self._call_api(**http_info)

    def reject_resource_share_invitation_async_invoker(self, request):
        http_info = self._reject_resource_share_invitation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reject_resource_share_invitation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-share-invitations/{resource_share_invitation_id}/reject",
            "request_type": request.__class__.__name__,
            "response_type": "RejectResourceShareInvitationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_invitation_id' in local_var_params:
            path_params['resource_share_invitation_id'] = local_var_params['resource_share_invitation_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_resource_share_invitation_async(self, request):
        """检索共享邀请

        通过条件检索资源共享邀请。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchResourceShareInvitation
        :type request: :class:`huaweicloudsdkram.v1.SearchResourceShareInvitationRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchResourceShareInvitationResponse`
        """
        http_info = self._search_resource_share_invitation_http_info(request)
        return self._call_api(**http_info)

    def search_resource_share_invitation_async_invoker(self, request):
        http_info = self._search_resource_share_invitation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_resource_share_invitation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-share-invitations/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchResourceShareInvitationResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_create_resource_share_tags_async(self, request):
        """资源共享实例增加标签

        资源共享实例增加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateResourceShareTags
        :type request: :class:`huaweicloudsdkram.v1.BatchCreateResourceShareTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.BatchCreateResourceShareTagsResponse`
        """
        http_info = self._batch_create_resource_share_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_resource_share_tags_async_invoker(self, request):
        http_info = self._batch_create_resource_share_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_resource_share_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/{resource_share_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateResourceShareTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_resource_share_tags_async(self, request):
        """删除资源共享实例的标签

        删除资源共享实例指定的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteResourceShareTags
        :type request: :class:`huaweicloudsdkram.v1.BatchDeleteResourceShareTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.BatchDeleteResourceShareTagsResponse`
        """
        http_info = self._batch_delete_resource_share_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resource_share_tags_async_invoker(self, request):
        http_info = self._batch_delete_resource_share_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_resource_share_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/{resource_share_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteResourceShareTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_share_tags_async(self, request):
        """查询已使用的标签列表

        查询资源共享实例已使用标签的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceShareTags
        :type request: :class:`huaweicloudsdkram.v1.ListResourceShareTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListResourceShareTagsResponse`
        """
        http_info = self._list_resource_share_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resource_share_tags_async_invoker(self, request):
        http_info = self._list_resource_share_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_share_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-shares/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceShareTagsResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_shares_by_tags_async(self, request):
        """根据标签信息查询实例列表

        根据标签信息查询资源共享实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceSharesByTags
        :type request: :class:`huaweicloudsdkram.v1.ListResourceSharesByTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListResourceSharesByTagsResponse`
        """
        http_info = self._list_resource_shares_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resource_shares_by_tags_async_invoker(self, request):
        http_info = self._list_resource_shares_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_shares_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceSharesByTagsResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_resource_share_count_by_tags_async(self, request):
        """根据标签信息查询实例数量

        根据标签信息查询资源共享实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchResourceShareCountByTags
        :type request: :class:`huaweicloudsdkram.v1.SearchResourceShareCountByTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchResourceShareCountByTagsResponse`
        """
        http_info = self._search_resource_share_count_by_tags_http_info(request)
        return self._call_api(**http_info)

    def search_resource_share_count_by_tags_async_invoker(self, request):
        http_info = self._search_resource_share_count_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_resource_share_count_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-shares/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "SearchResourceShareCountByTagsResponse"
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

        auth_settings = ['AccessKeyAuth']

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

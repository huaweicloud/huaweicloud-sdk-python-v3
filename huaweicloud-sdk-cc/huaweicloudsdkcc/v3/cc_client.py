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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcc'")


class CcClient(Client):
    def __init__(self):
        super(CcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcc.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "CcClient":
                raise TypeError("client type error, support client type is CcClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_authorisation(self, request):
        """创建授权

        网络实例所属租户授予云连接实例所属租户加载其网络实例的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuthorisation
        :type request: :class:`huaweicloudsdkcc.v3.CreateAuthorisationRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateAuthorisationResponse`
        """
        http_info = self._create_authorisation_http_info(request)
        return self._call_api(**http_info)

    def create_authorisation_invoker(self, request):
        http_info = self._create_authorisation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_authorisation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/authorisations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuthorisationResponse"
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

    def delete_authorisation(self, request):
        """删除授权

        网络实例所属租户取消授予云连接实例所属租户加载其网络实例的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuthorisation
        :type request: :class:`huaweicloudsdkcc.v3.DeleteAuthorisationRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteAuthorisationResponse`
        """
        http_info = self._delete_authorisation_http_info(request)
        return self._call_api(**http_info)

    def delete_authorisation_invoker(self, request):
        http_info = self._delete_authorisation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_authorisation_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/ccaas/authorisations/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuthorisationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_authorisations(self, request):
        """查询授权列表

        网络实例所属租户查看其已经授予其他租户的权限。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthorisations
        :type request: :class:`huaweicloudsdkcc.v3.ListAuthorisationsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListAuthorisationsResponse`
        """
        http_info = self._list_authorisations_http_info(request)
        return self._call_api(**http_info)

    def list_authorisations_invoker(self, request):
        http_info = self._list_authorisations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_authorisations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/authorisations",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorisationsResponse"
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
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'

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

    def list_permissions(self, request):
        """查询权限列表

        云连接实例所属租户查询其可加载其他租户的网络实例权限。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPermissions
        :type request: :class:`huaweicloudsdkcc.v3.ListPermissionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListPermissionsResponse`
        """
        http_info = self._list_permissions_http_info(request)
        return self._call_api(**http_info)

    def list_permissions_invoker(self, request):
        http_info = self._list_permissions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_permissions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/permissions",
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'

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

    def update_authorisation(self, request):
        """更新授权

        更新授权实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuthorisation
        :type request: :class:`huaweicloudsdkcc.v3.UpdateAuthorisationRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateAuthorisationResponse`
        """
        http_info = self._update_authorisation_http_info(request)
        return self._call_api(**http_info)

    def update_authorisation_invoker(self, request):
        http_info = self._update_authorisation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_authorisation_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/ccaas/authorisations/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuthorisationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def associate_bandwidth_package(self, request):
        """将带宽包实例绑定到云连接实例

        将带宽包实例绑定到云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.AssociateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.AssociateBandwidthPackageResponse`
        """
        http_info = self._associate_bandwidth_package_http_info(request)
        return self._call_api(**http_info)

    def associate_bandwidth_package_invoker(self, request):
        http_info = self._associate_bandwidth_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_bandwidth_package_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/{id}/associate",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateBandwidthPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def create_bandwidth_package(self, request):
        """创建带宽包实例

        创建带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.CreateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateBandwidthPackageResponse`
        """
        http_info = self._create_bandwidth_package_http_info(request)
        return self._call_api(**http_info)

    def create_bandwidth_package_invoker(self, request):
        http_info = self._create_bandwidth_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_bandwidth_package_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBandwidthPackageResponse"
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

    def delete_bandwidth_package(self, request):
        """删除带宽包实例

        删除带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.DeleteBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteBandwidthPackageResponse`
        """
        http_info = self._delete_bandwidth_package_http_info(request)
        return self._call_api(**http_info)

    def delete_bandwidth_package_invoker(self, request):
        http_info = self._delete_bandwidth_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_bandwidth_package_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBandwidthPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def disassociate_bandwidth_package(self, request):
        """解除带宽包实例与云连接实例的绑定

        解除带宽包实例与云连接实例的绑定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.DisassociateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DisassociateBandwidthPackageResponse`
        """
        http_info = self._disassociate_bandwidth_package_http_info(request)
        return self._call_api(**http_info)

    def disassociate_bandwidth_package_invoker(self, request):
        http_info = self._disassociate_bandwidth_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_bandwidth_package_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/{id}/disassociate",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateBandwidthPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_bandwidth_package_tags(self, request):
        """查询带宽包的标签信息

        查询带宽包的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthPackageTags
        :type request: :class:`huaweicloudsdkcc.v3.ListBandwidthPackageTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListBandwidthPackageTagsResponse`
        """
        http_info = self._list_bandwidth_package_tags_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidth_package_tags_invoker(self, request):
        http_info = self._list_bandwidth_package_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bandwidth_package_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthPackageTagsResponse"
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

    def list_bandwidth_packages(self, request):
        """查询带宽包列表

        查询带宽包列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthPackages
        :type request: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesResponse`
        """
        http_info = self._list_bandwidth_packages_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidth_packages_invoker(self, request):
        http_info = self._list_bandwidth_packages_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bandwidth_packages_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthPackagesResponse"
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
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'billing_mode' in local_var_params:
            query_params.append(('billing_mode', local_var_params['billing_mode']))
            collection_formats['billing_mode'] = 'csv'
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
            collection_formats['resource_id'] = 'csv'

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

    def list_bandwidth_packages_by_tags(self, request):
        """通过标签过滤带宽包实例

        通过标签过滤带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthPackagesByTags
        :type request: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesByTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesByTagsResponse`
        """
        http_info = self._list_bandwidth_packages_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidth_packages_by_tags_invoker(self, request):
        http_info = self._list_bandwidth_packages_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bandwidth_packages_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthPackagesByTagsResponse"
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

    def show_bandwidth_package(self, request):
        """查询带宽包实例

        查询带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.ShowBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowBandwidthPackageResponse`
        """
        http_info = self._show_bandwidth_package_http_info(request)
        return self._call_api(**http_info)

    def show_bandwidth_package_invoker(self, request):
        http_info = self._show_bandwidth_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bandwidth_package_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBandwidthPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def tag_bandwidth_package(self, request):
        """创建带宽包标签

        创建带宽包标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.TagBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.TagBandwidthPackageResponse`
        """
        http_info = self._tag_bandwidth_package_http_info(request)
        return self._call_api(**http_info)

    def tag_bandwidth_package_invoker(self, request):
        http_info = self._tag_bandwidth_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _tag_bandwidth_package_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/{id}/tag",
            "request_type": request.__class__.__name__,
            "response_type": "TagBandwidthPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def untag_bandwidth_package(self, request):
        """删除带宽包标签

        删除带宽包标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.UntagBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UntagBandwidthPackageResponse`
        """
        http_info = self._untag_bandwidth_package_http_info(request)
        return self._call_api(**http_info)

    def untag_bandwidth_package_invoker(self, request):
        http_info = self._untag_bandwidth_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _untag_bandwidth_package_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/{id}/untag",
            "request_type": request.__class__.__name__,
            "response_type": "UntagBandwidthPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_bandwidth_package(self, request):
        """更新带宽包实例

        更新带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.UpdateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateBandwidthPackageResponse`
        """
        http_info = self._update_bandwidth_package_http_info(request)
        return self._call_api(**http_info)

    def update_bandwidth_package_invoker(self, request):
        http_info = self._update_bandwidth_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_bandwidth_package_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/ccaas/bandwidth-packages/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBandwidthPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def apply_central_network_policy(self, request):
        """应用中心网络策略

        应用中心网络策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyCentralNetworkPolicy
        :type request: :class:`huaweicloudsdkcc.v3.ApplyCentralNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ApplyCentralNetworkPolicyResponse`
        """
        http_info = self._apply_central_network_policy_http_info(request)
        return self._call_api(**http_info)

    def apply_central_network_policy_invoker(self, request):
        http_info = self._apply_central_network_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_central_network_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/policies/{policy_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyCentralNetworkPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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

    def create_central_network(self, request):
        """创建中心网络

        创建中心网络。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkResponse`
        """
        http_info = self._create_central_network_http_info(request)
        return self._call_api(**http_info)

    def create_central_network_invoker(self, request):
        http_info = self._create_central_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_central_network_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcn/central-networks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCentralNetworkResponse"
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

    def create_central_network_policy(self, request):
        """创建一个新版本的中心网络策略

        创建一份只读的中心网络的策略。如果您有策略文档内容改动，需要基于此版本重新创建一个新版本的策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCentralNetworkPolicy
        :type request: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkPolicyResponse`
        """
        http_info = self._create_central_network_policy_http_info(request)
        return self._call_api(**http_info)

    def create_central_network_policy_invoker(self, request):
        http_info = self._create_central_network_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_central_network_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCentralNetworkPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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

    def delete_central_network(self, request):
        """删除中心网络

        删除中心网络，请先清除附件后再删除中心网络。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkResponse`
        """
        http_info = self._delete_central_network_http_info(request)
        return self._call_api(**http_info)

    def delete_central_network_invoker(self, request):
        http_info = self._delete_central_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_central_network_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/gcn/central-networks/{central_network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCentralNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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

    def delete_central_network_policy(self, request):
        """删除中心网络策略版本

        删除中心网络策略版本。您无法删除正在被应用的中心策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCentralNetworkPolicy
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkPolicyResponse`
        """
        http_info = self._delete_central_network_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_central_network_policy_invoker(self, request):
        http_info = self._delete_central_network_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_central_network_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCentralNetworkPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_central_network_policies(self, request):
        """查询所有版本的中心网络策略列表

        查询所有版本的中心网络策略列表。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkPolicies
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkPoliciesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkPoliciesResponse`
        """
        http_info = self._list_central_network_policies_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_policies_invoker(self, request):
        http_info = self._list_central_network_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'csv'
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
            collection_formats['version'] = 'csv'
        if 'is_applied' in local_var_params:
            query_params.append(('is_applied', local_var_params['is_applied']))

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

    def list_central_network_policy_change_set(self, request):
        """查询中心网络策略变化集

        查询与当前应用中心网络策略的变化集。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkPolicyChangeSet
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkPolicyChangeSetRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkPolicyChangeSetResponse`
        """
        http_info = self._list_central_network_policy_change_set_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_policy_change_set_invoker(self, request):
        http_info = self._list_central_network_policy_change_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_policy_change_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/policies/{policy_id}/change-set",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkPolicyChangeSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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

    def list_central_network_tags(self, request):
        """查询中心网络的标签信息

        查询中心网络的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkTags
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkTagsResponse`
        """
        http_info = self._list_central_network_tags_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_tags_invoker(self, request):
        http_info = self._list_central_network_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-networks/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkTagsResponse"
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

    def list_central_networks(self, request):
        """查询中心网络列表

        查询中心网络列表。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworks
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworksRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworksResponse`
        """
        http_info = self._list_central_networks_http_info(request)
        return self._call_api(**http_info)

    def list_central_networks_invoker(self, request):
        http_info = self._list_central_networks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_networks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-networks",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworksResponse"
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
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'enterprise_router_id' in local_var_params:
            query_params.append(('enterprise_router_id', local_var_params['enterprise_router_id']))
            collection_formats['enterprise_router_id'] = 'multi'
        if 'attachment_instance_id' in local_var_params:
            query_params.append(('attachment_instance_id', local_var_params['attachment_instance_id']))
            collection_formats['attachment_instance_id'] = 'multi'
        if 'global_connection_bandwidth_id' in local_var_params:
            query_params.append(('global_connection_bandwidth_id', local_var_params['global_connection_bandwidth_id']))
            collection_formats['global_connection_bandwidth_id'] = 'csv'
        if 'connection_id' in local_var_params:
            query_params.append(('connection_id', local_var_params['connection_id']))
            collection_formats['connection_id'] = 'multi'

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

    def list_central_networks_by_tags(self, request):
        """通过标签过滤中心网络实例

        通过标签过滤中心网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworksByTags
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworksByTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworksByTagsResponse`
        """
        http_info = self._list_central_networks_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_central_networks_by_tags_invoker(self, request):
        http_info = self._list_central_networks_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_networks_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcn/central-networks/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworksByTagsResponse"
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

    def show_central_network(self, request):
        """查询中心网络详情

        查询中心网络详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkResponse`
        """
        http_info = self._show_central_network_http_info(request)
        return self._call_api(**http_info)

    def show_central_network_invoker(self, request):
        http_info = self._show_central_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_central_network_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-networks/{central_network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCentralNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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

    def tag_central_network(self, request):
        """创建中心网络标签

        创建中心网络标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.TagCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.TagCentralNetworkResponse`
        """
        http_info = self._tag_central_network_http_info(request)
        return self._call_api(**http_info)

    def tag_central_network_invoker(self, request):
        http_info = self._tag_central_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _tag_central_network_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcn/central-networks/{central_network_id}/tag",
            "request_type": request.__class__.__name__,
            "response_type": "TagCentralNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def untag_central_network(self, request):
        """删除中心网络标签

        删除中心网络标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.UntagCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UntagCentralNetworkResponse`
        """
        http_info = self._untag_central_network_http_info(request)
        return self._call_api(**http_info)

    def untag_central_network_invoker(self, request):
        http_info = self._untag_central_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _untag_central_network_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcn/central-networks/{central_network_id}/untag",
            "request_type": request.__class__.__name__,
            "response_type": "UntagCentralNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_central_network(self, request):
        """更新中心网络详情

        更新中心网络详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkResponse`
        """
        http_info = self._update_central_network_http_info(request)
        return self._call_api(**http_info)

    def update_central_network_invoker(self, request):
        http_info = self._update_central_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_central_network_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/gcn/central-networks/{central_network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCentralNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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

    def create_central_network_er_route_table_attachment(self, request):
        """创建中心网络ER路由表附件

        创建中心网络的路由表附件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCentralNetworkErRouteTableAttachment
        :type request: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkErRouteTableAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkErRouteTableAttachmentResponse`
        """
        http_info = self._create_central_network_er_route_table_attachment_http_info(request)
        return self._call_api(**http_info)

    def create_central_network_er_route_table_attachment_invoker(self, request):
        http_info = self._create_central_network_er_route_table_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_central_network_er_route_table_attachment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/er-route-table-attachments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCentralNetworkErRouteTableAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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

    def create_central_network_gdgw_attachment(self, request):
        """创建中心网络GDGW附件

        创建中心网络的GDGW附件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCentralNetworkGdgwAttachment
        :type request: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkGdgwAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkGdgwAttachmentResponse`
        """
        http_info = self._create_central_network_gdgw_attachment_http_info(request)
        return self._call_api(**http_info)

    def create_central_network_gdgw_attachment_invoker(self, request):
        http_info = self._create_central_network_gdgw_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_central_network_gdgw_attachment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/gdgw-attachments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCentralNetworkGdgwAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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

    def delete_central_network_attachment(self, request):
        """删除中心网络附件

        删除中心网络附件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCentralNetworkAttachment
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkAttachmentResponse`
        """
        http_info = self._delete_central_network_attachment_http_info(request)
        return self._call_api(**http_info)

    def delete_central_network_attachment_invoker(self, request):
        http_info = self._delete_central_network_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_central_network_attachment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/attachments/{attachment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCentralNetworkAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']
        if 'attachment_id' in local_var_params:
            path_params['attachment_id'] = local_var_params['attachment_id']

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

    def list_central_network_attachments(self, request):
        """查询中心网络附件列表

        查询中心网络附件列表，分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkAttachments
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkAttachmentsResponse`
        """
        http_info = self._list_central_network_attachments_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_attachments_invoker(self, request):
        http_info = self._list_central_network_attachments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_attachments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/attachments",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkAttachmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'attachment_instance_type' in local_var_params:
            query_params.append(('attachment_instance_type', local_var_params['attachment_instance_type']))
            collection_formats['attachment_instance_type'] = 'csv'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'csv'
        if 'attachment_instance_id' in local_var_params:
            query_params.append(('attachment_instance_id', local_var_params['attachment_instance_id']))
            collection_formats['attachment_instance_id'] = 'multi'

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

    def list_central_network_er_route_table_attachments(self, request):
        """查询中心网络ER路由表附件列表

        查询中心网络ER路由表附件列表。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkErRouteTableAttachments
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkErRouteTableAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkErRouteTableAttachmentsResponse`
        """
        http_info = self._list_central_network_er_route_table_attachments_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_er_route_table_attachments_invoker(self, request):
        http_info = self._list_central_network_er_route_table_attachments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_er_route_table_attachments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/er-route-table-attachments",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkErRouteTableAttachmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'csv'
        if 'attachment_instance_id' in local_var_params:
            query_params.append(('attachment_instance_id', local_var_params['attachment_instance_id']))
            collection_formats['attachment_instance_id'] = 'multi'

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

    def list_central_network_gdgw_attachments(self, request):
        """查询中心网络GDGW附件列表

        查询中心网络GDGW附件列表。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkGdgwAttachments
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkGdgwAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkGdgwAttachmentsResponse`
        """
        http_info = self._list_central_network_gdgw_attachments_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_gdgw_attachments_invoker(self, request):
        http_info = self._list_central_network_gdgw_attachments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_gdgw_attachments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/gdgw-attachments",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkGdgwAttachmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'csv'
        if 'global_dc_gateway_id' in local_var_params:
            query_params.append(('global_dc_gateway_id', local_var_params['global_dc_gateway_id']))
            collection_formats['global_dc_gateway_id'] = 'multi'

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

    def show_central_network_er_route_table_attachment(self, request):
        """查询中心网络ER路由表附件详情

        查询中心网络ER路由表附件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCentralNetworkErRouteTableAttachment
        :type request: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkErRouteTableAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkErRouteTableAttachmentResponse`
        """
        http_info = self._show_central_network_er_route_table_attachment_http_info(request)
        return self._call_api(**http_info)

    def show_central_network_er_route_table_attachment_invoker(self, request):
        http_info = self._show_central_network_er_route_table_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_central_network_er_route_table_attachment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/er-route-table-attachments/{er_route_table_attachment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCentralNetworkErRouteTableAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']
        if 'er_route_table_attachment_id' in local_var_params:
            path_params['er_route_table_attachment_id'] = local_var_params['er_route_table_attachment_id']

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

    def show_central_network_gdgw_attachment(self, request):
        """查询中心网络GDGW附件详情

        查询中心网络GDGW附件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCentralNetworkGdgwAttachment
        :type request: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkGdgwAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkGdgwAttachmentResponse`
        """
        http_info = self._show_central_network_gdgw_attachment_http_info(request)
        return self._call_api(**http_info)

    def show_central_network_gdgw_attachment_invoker(self, request):
        http_info = self._show_central_network_gdgw_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_central_network_gdgw_attachment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/gdgw-attachments/{gdgw_attachment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCentralNetworkGdgwAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']
        if 'gdgw_attachment_id' in local_var_params:
            path_params['gdgw_attachment_id'] = local_var_params['gdgw_attachment_id']

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

    def update_central_network_er_route_table_attachment(self, request):
        """更新中心网络ER路由表附件

        更新中心网络ER路由表附件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCentralNetworkErRouteTableAttachment
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkErRouteTableAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkErRouteTableAttachmentResponse`
        """
        http_info = self._update_central_network_er_route_table_attachment_http_info(request)
        return self._call_api(**http_info)

    def update_central_network_er_route_table_attachment_invoker(self, request):
        http_info = self._update_central_network_er_route_table_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_central_network_er_route_table_attachment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/er-route-table-attachments/{er_route_table_attachment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCentralNetworkErRouteTableAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']
        if 'er_route_table_attachment_id' in local_var_params:
            path_params['er_route_table_attachment_id'] = local_var_params['er_route_table_attachment_id']

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

    def update_central_network_gdgw_attachment(self, request):
        """更新中心网络GDGW附件

        更新中心网络GDGW附件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCentralNetworkGdgwAttachment
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkGdgwAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkGdgwAttachmentResponse`
        """
        http_info = self._update_central_network_gdgw_attachment_http_info(request)
        return self._call_api(**http_info)

    def update_central_network_gdgw_attachment_invoker(self, request):
        http_info = self._update_central_network_gdgw_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_central_network_gdgw_attachment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/gdgw-attachments/{gdgw_attachment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCentralNetworkGdgwAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']
        if 'gdgw_attachment_id' in local_var_params:
            path_params['gdgw_attachment_id'] = local_var_params['gdgw_attachment_id']

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

    def list_central_network_capabilities(self, request):
        """查询中心网络能力列表

        查询中心网络能力列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkCapabilities
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkCapabilitiesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkCapabilitiesResponse`
        """
        http_info = self._list_central_network_capabilities_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_capabilities_invoker(self, request):
        http_info = self._list_central_network_capabilities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_capabilities_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/capabilities",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkCapabilitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'capability' in local_var_params:
            query_params.append(('capability', local_var_params['capability']))
            collection_formats['capability'] = 'csv'

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

    def list_central_network_connections(self, request):
        """查询中心网络连接列表

        查询中心网络连接列表接口。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkConnections
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkConnectionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkConnectionsResponse`
        """
        http_info = self._list_central_network_connections_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_connections_invoker(self, request):
        http_info = self._list_central_network_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'csv'
        if 'global_connection_bandwidth_id' in local_var_params:
            query_params.append(('global_connection_bandwidth_id', local_var_params['global_connection_bandwidth_id']))
            collection_formats['global_connection_bandwidth_id'] = 'csv'
        if 'bandwidth_type' in local_var_params:
            query_params.append(('bandwidth_type', local_var_params['bandwidth_type']))
        if 'connection_type' in local_var_params:
            query_params.append(('connection_type', local_var_params['connection_type']))
        if 'is_cross_region' in local_var_params:
            query_params.append(('is_cross_region', local_var_params['is_cross_region']))

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

    def update_central_network_connection(self, request):
        """更新中心网络连接接口

        更新中心网络连接接口（仅支持更新带宽）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCentralNetworkConnection
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkConnectionResponse`
        """
        http_info = self._update_central_network_connection_http_info(request)
        return self._call_api(**http_info)

    def update_central_network_connection_invoker(self, request):
        http_info = self._update_central_network_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_central_network_connection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/gcn/central-network/{central_network_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCentralNetworkConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']
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

    def list_central_network_quotas(self, request):
        """查询中心网络配额

        查询中心网络配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkQuotas
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkQuotasRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkQuotasResponse`
        """
        http_info = self._list_central_network_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_central_network_quotas_invoker(self, request):
        http_info = self._list_central_network_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_central_network_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcn/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListCentralNetworkQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'quota_type' in local_var_params:
            query_params.append(('quota_type', local_var_params['quota_type']))
            collection_formats['quota_type'] = 'csv'
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

    def create_cloud_connection(self, request):
        """创建云连接实例

        创建云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.CreateCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCloudConnectionResponse`
        """
        http_info = self._create_cloud_connection_http_info(request)
        return self._call_api(**http_info)

    def create_cloud_connection_invoker(self, request):
        http_info = self._create_cloud_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cloud_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCloudConnectionResponse"
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

    def delete_cloud_connection(self, request):
        """删除云连接实例

        删除云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCloudConnectionResponse`
        """
        http_info = self._delete_cloud_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_cloud_connection_invoker(self, request):
        http_info = self._delete_cloud_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cloud_connection_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCloudConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_cloud_connection_tags(self, request):
        """查询云连接实例的标签信息

        查询云连接实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionTags
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionTagsResponse`
        """
        http_info = self._list_cloud_connection_tags_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_connection_tags_invoker(self, request):
        http_info = self._list_cloud_connection_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_connection_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudConnectionTagsResponse"
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

    def list_cloud_connections(self, request):
        """查询云连接列表

        查询云连接列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnections
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsResponse`
        """
        http_info = self._list_cloud_connections_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_connections_invoker(self, request):
        http_info = self._list_cloud_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudConnectionsResponse"
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
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'used_scene' in local_var_params:
            query_params.append(('used_scene', local_var_params['used_scene']))
            collection_formats['used_scene'] = 'csv'

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

    def list_cloud_connections_by_tags(self, request):
        """通过标签过滤云连接实例

        通过标签过滤云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionsByTags
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsByTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsByTagsResponse`
        """
        http_info = self._list_cloud_connections_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_connections_by_tags_invoker(self, request):
        http_info = self._list_cloud_connections_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_connections_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudConnectionsByTagsResponse"
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

    def show_cloud_connection(self, request):
        """查询云连接实例

        查询云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionResponse`
        """
        http_info = self._show_cloud_connection_http_info(request)
        return self._call_api(**http_info)

    def show_cloud_connection_invoker(self, request):
        http_info = self._show_cloud_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cloud_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCloudConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def tag_cloud_connection(self, request):
        """创建云连接实例标签

        创建云连接实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.TagCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.TagCloudConnectionResponse`
        """
        http_info = self._tag_cloud_connection_http_info(request)
        return self._call_api(**http_info)

    def tag_cloud_connection_invoker(self, request):
        http_info = self._tag_cloud_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _tag_cloud_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections/{id}/tag",
            "request_type": request.__class__.__name__,
            "response_type": "TagCloudConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def untag_cloud_connection(self, request):
        """删除云连接实例标签

        删除云连接实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.UntagCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UntagCloudConnectionResponse`
        """
        http_info = self._untag_cloud_connection_http_info(request)
        return self._call_api(**http_info)

    def untag_cloud_connection_invoker(self, request):
        http_info = self._untag_cloud_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _untag_cloud_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections/{id}/untag",
            "request_type": request.__class__.__name__,
            "response_type": "UntagCloudConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_cloud_connection(self, request):
        """更新云连接实例

        更新云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCloudConnectionResponse`
        """
        http_info = self._update_cloud_connection_http_info(request)
        return self._call_api(**http_info)

    def update_cloud_connection_invoker(self, request):
        http_info = self._update_cloud_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cloud_connection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connections/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCloudConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_cloud_connection_quotas(self, request):
        """查询云连接配额

        查询云连接配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionQuotas
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionQuotasRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionQuotasResponse`
        """
        http_info = self._list_cloud_connection_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_connection_quotas_invoker(self, request):
        http_info = self._list_cloud_connection_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_connection_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudConnectionQuotasResponse"
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
        if 'quota_type' in local_var_params:
            query_params.append(('quota_type', local_var_params['quota_type']))
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))

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

    def list_cloud_connection_routes(self, request):
        """查询云连接路由条目列表

        查询云连接路由条目列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionRoutes
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionRoutesResponse`
        """
        http_info = self._list_cloud_connection_routes_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_connection_routes_invoker(self, request):
        http_info = self._list_cloud_connection_routes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_connection_routes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connection-routes",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudConnectionRoutesResponse"
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
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
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

    def show_cloud_connection_routes(self, request):
        """查询云连接路由条目详情

        查询云连接路由条目列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudConnectionRoutes
        :type request: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRoutesResponse`
        """
        http_info = self._show_cloud_connection_routes_http_info(request)
        return self._call_api(**http_info)

    def show_cloud_connection_routes_invoker(self, request):
        http_info = self._show_cloud_connection_routes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cloud_connection_routes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/cloud-connection-routes/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCloudConnectionRoutesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def associate_global_connection_bandwidth_instance(self, request):
        """全域互联带宽绑定实例

        全域互联带宽绑定实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateGlobalConnectionBandwidthInstance
        :type request: :class:`huaweicloudsdkcc.v3.AssociateGlobalConnectionBandwidthInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.AssociateGlobalConnectionBandwidthInstanceResponse`
        """
        http_info = self._associate_global_connection_bandwidth_instance_http_info(request)
        return self._call_api(**http_info)

    def associate_global_connection_bandwidth_instance_invoker(self, request):
        http_info = self._associate_global_connection_bandwidth_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_global_connection_bandwidth_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcb/gcbandwidths/{id}/associate-instance",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateGlobalConnectionBandwidthInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def create_global_connection_bandwidth(self, request):
        """创建全域互联带宽

        创建全域互联带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGlobalConnectionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.CreateGlobalConnectionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateGlobalConnectionBandwidthResponse`
        """
        http_info = self._create_global_connection_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def create_global_connection_bandwidth_invoker(self, request):
        http_info = self._create_global_connection_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_global_connection_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcb/gcbandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGlobalConnectionBandwidthResponse"
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

    def delete_global_connection_bandwidth(self, request):
        """删除全域互联带宽

        删除全域互联带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGlobalConnectionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.DeleteGlobalConnectionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteGlobalConnectionBandwidthResponse`
        """
        http_info = self._delete_global_connection_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def delete_global_connection_bandwidth_invoker(self, request):
        http_info = self._delete_global_connection_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_global_connection_bandwidth_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/gcb/gcbandwidths/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGlobalConnectionBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def disassociate_global_connection_bandwidth_instance(self, request):
        """全域互联带宽解绑实例

        全域互联带宽解绑实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateGlobalConnectionBandwidthInstance
        :type request: :class:`huaweicloudsdkcc.v3.DisassociateGlobalConnectionBandwidthInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DisassociateGlobalConnectionBandwidthInstanceResponse`
        """
        http_info = self._disassociate_global_connection_bandwidth_instance_http_info(request)
        return self._call_api(**http_info)

    def disassociate_global_connection_bandwidth_instance_invoker(self, request):
        http_info = self._disassociate_global_connection_bandwidth_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_global_connection_bandwidth_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/gcb/gcbandwidths/{id}/disassociate-instance",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateGlobalConnectionBandwidthInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_global_connection_bandwidth_configs(self, request):
        """查询全域互联带宽租户配置信息

        查询全域互联带宽租户配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalConnectionBandwidthConfigs
        :type request: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthConfigsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthConfigsResponse`
        """
        http_info = self._list_global_connection_bandwidth_configs_http_info(request)
        return self._call_api(**http_info)

    def list_global_connection_bandwidth_configs_invoker(self, request):
        http_info = self._list_global_connection_bandwidth_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_connection_bandwidth_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcb/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalConnectionBandwidthConfigsResponse"
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

    def list_global_connection_bandwidth_line_levels(self, request):
        """查询线路等级列表

        查询线路等级列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalConnectionBandwidthLineLevels
        :type request: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthLineLevelsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthLineLevelsResponse`
        """
        http_info = self._list_global_connection_bandwidth_line_levels_http_info(request)
        return self._call_api(**http_info)

    def list_global_connection_bandwidth_line_levels_invoker(self, request):
        http_info = self._list_global_connection_bandwidth_line_levels_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_connection_bandwidth_line_levels_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcb/line-levels",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalConnectionBandwidthLineLevelsResponse"
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
            collection_formats['id'] = 'csv'
        if 'local_area' in local_var_params:
            query_params.append(('local_area', local_var_params['local_area']))
        if 'remote_area' in local_var_params:
            query_params.append(('remote_area', local_var_params['remote_area']))
        if 'levels' in local_var_params:
            query_params.append(('levels', local_var_params['levels']))
            collection_formats['levels'] = 'csv'

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

    def list_global_connection_bandwidth_sites(self, request):
        """查询站点列表

        查询站点列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalConnectionBandwidthSites
        :type request: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthSitesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthSitesResponse`
        """
        http_info = self._list_global_connection_bandwidth_sites_http_info(request)
        return self._call_api(**http_info)

    def list_global_connection_bandwidth_sites_invoker(self, request):
        http_info = self._list_global_connection_bandwidth_sites_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_connection_bandwidth_sites_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcb/sites",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalConnectionBandwidthSitesResponse"
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
            collection_formats['id'] = 'csv'
        if 'site_code' in local_var_params:
            query_params.append(('site_code', local_var_params['site_code']))
        if 'site_type' in local_var_params:
            query_params.append(('site_type', local_var_params['site_type']))

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

    def list_global_connection_bandwidth_spec_codes(self, request):
        """查询线路规格列表

        查询线路规格列表。租户白名单控制，默认为空。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalConnectionBandwidthSpecCodes
        :type request: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthSpecCodesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthSpecCodesResponse`
        """
        http_info = self._list_global_connection_bandwidth_spec_codes_http_info(request)
        return self._call_api(**http_info)

    def list_global_connection_bandwidth_spec_codes_invoker(self, request):
        http_info = self._list_global_connection_bandwidth_spec_codes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_connection_bandwidth_spec_codes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcb/spec-codes",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalConnectionBandwidthSpecCodesResponse"
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
            collection_formats['id'] = 'csv'
        if 'local_area' in local_var_params:
            query_params.append(('local_area', local_var_params['local_area']))
        if 'remote_area' in local_var_params:
            query_params.append(('remote_area', local_var_params['remote_area']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
            collection_formats['level'] = 'csv'

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

    def list_global_connection_bandwidths(self, request):
        """查询全域互联带宽列表

        查询全域互联带宽列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalConnectionBandwidths
        :type request: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthsResponse`
        """
        http_info = self._list_global_connection_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def list_global_connection_bandwidths_invoker(self, request):
        http_info = self._list_global_connection_bandwidths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_connection_bandwidths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcb/gcbandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalConnectionBandwidthsResponse"
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
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'binding_service' in local_var_params:
            query_params.append(('binding_service', local_var_params['binding_service']))
            collection_formats['binding_service'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
            collection_formats['charge_mode'] = 'csv'

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

    def list_support_binding_connection_bandwidths(self, request):
        """查询符合绑定条件的全域互联带宽列表

        查询符合绑定条件的全域互联带宽列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSupportBindingConnectionBandwidths
        :type request: :class:`huaweicloudsdkcc.v3.ListSupportBindingConnectionBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListSupportBindingConnectionBandwidthsResponse`
        """
        http_info = self._list_support_binding_connection_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def list_support_binding_connection_bandwidths_invoker(self, request):
        http_info = self._list_support_binding_connection_bandwidths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_support_binding_connection_bandwidths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcb/gcbandwidths/support-bindings",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportBindingConnectionBandwidthsResponse"
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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'local_area' in local_var_params:
            query_params.append(('local_area', local_var_params['local_area']))
        if 'remote_area' in local_var_params:
            query_params.append(('remote_area', local_var_params['remote_area']))
        if 'binding_service' in local_var_params:
            query_params.append(('binding_service', local_var_params['binding_service']))

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

    def show_global_connection_bandwidth(self, request):
        """查询全域互联带宽详情

        查询全域互联带宽详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGlobalConnectionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.ShowGlobalConnectionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowGlobalConnectionBandwidthResponse`
        """
        http_info = self._show_global_connection_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def show_global_connection_bandwidth_invoker(self, request):
        http_info = self._show_global_connection_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_global_connection_bandwidth_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/gcb/gcbandwidths/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGlobalConnectionBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_global_connection_bandwidth(self, request):
        """更新全域互联带宽详情

        更新全域互联带宽详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGlobalConnectionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.UpdateGlobalConnectionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateGlobalConnectionBandwidthResponse`
        """
        http_info = self._update_global_connection_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_global_connection_bandwidth_invoker(self, request):
        http_info = self._update_global_connection_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_global_connection_bandwidth_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/gcb/gcbandwidths/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGlobalConnectionBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def create_inter_region_bandwidth(self, request):
        """创建域间带宽实例

        创建域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidthResponse`
        """
        http_info = self._create_inter_region_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def create_inter_region_bandwidth_invoker(self, request):
        http_info = self._create_inter_region_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_inter_region_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/inter-region-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInterRegionBandwidthResponse"
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

    def delete_inter_region_bandwidth(self, request):
        """删除域间带宽实例

        删除域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.DeleteInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteInterRegionBandwidthResponse`
        """
        http_info = self._delete_inter_region_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def delete_inter_region_bandwidth_invoker(self, request):
        http_info = self._delete_inter_region_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_inter_region_bandwidth_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/ccaas/inter-region-bandwidths/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInterRegionBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_inter_region_bandwidths(self, request):
        """查询域间带宽列表

        查询域间带宽列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInterRegionBandwidths
        :type request: :class:`huaweicloudsdkcc.v3.ListInterRegionBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListInterRegionBandwidthsResponse`
        """
        http_info = self._list_inter_region_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def list_inter_region_bandwidths_invoker(self, request):
        http_info = self._list_inter_region_bandwidths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_inter_region_bandwidths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/inter-region-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ListInterRegionBandwidthsResponse"
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
            collection_formats['id'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'bandwidth_package_id' in local_var_params:
            query_params.append(('bandwidth_package_id', local_var_params['bandwidth_package_id']))
            collection_formats['bandwidth_package_id'] = 'csv'

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

    def show_inter_region_bandwidth(self, request):
        """查询域间带宽实例

        查询域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.ShowInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowInterRegionBandwidthResponse`
        """
        http_info = self._show_inter_region_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def show_inter_region_bandwidth_invoker(self, request):
        http_info = self._show_inter_region_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_inter_region_bandwidth_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/inter-region-bandwidths/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInterRegionBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_inter_region_bandwidth(self, request):
        """更新域间带宽实例

        更新域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.UpdateInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateInterRegionBandwidthResponse`
        """
        http_info = self._update_inter_region_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_inter_region_bandwidth_invoker(self, request):
        http_info = self._update_inter_region_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_inter_region_bandwidth_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/ccaas/inter-region-bandwidths/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInterRegionBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def create_network_instance(self, request):
        """创建网络实例

        创建网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.CreateNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateNetworkInstanceResponse`
        """
        http_info = self._create_network_instance_http_info(request)
        return self._call_api(**http_info)

    def create_network_instance_invoker(self, request):
        http_info = self._create_network_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_network_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/network-instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNetworkInstanceResponse"
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

    def delete_network_instance(self, request):
        """删除网络实例

        删除网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.DeleteNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteNetworkInstanceResponse`
        """
        http_info = self._delete_network_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_network_instance_invoker(self, request):
        http_info = self._delete_network_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_network_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/ccaas/network-instances/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNetworkInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_network_instances(self, request):
        """查询网络实例列表

        查询云连接列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNetworkInstances
        :type request: :class:`huaweicloudsdkcc.v3.ListNetworkInstancesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListNetworkInstancesResponse`
        """
        http_info = self._list_network_instances_http_info(request)
        return self._call_api(**http_info)

    def list_network_instances_invoker(self, request):
        http_info = self._list_network_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_network_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/network-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListNetworkInstancesResponse"
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
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
            collection_formats['region_id'] = 'csv'

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

    def show_network_instance(self, request):
        """查询网络实例

        查询网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.ShowNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowNetworkInstanceResponse`
        """
        http_info = self._show_network_instance_http_info(request)
        return self._call_api(**http_info)

    def show_network_instance_invoker(self, request):
        http_info = self._show_network_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_network_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/network-instances/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNetworkInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_network_instance(self, request):
        """更新网络实例

        更新网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.UpdateNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateNetworkInstanceResponse`
        """
        http_info = self._update_network_instance_http_info(request)
        return self._call_api(**http_info)

    def update_network_instance_invoker(self, request):
        http_info = self._update_network_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_network_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/ccaas/network-instances/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNetworkInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

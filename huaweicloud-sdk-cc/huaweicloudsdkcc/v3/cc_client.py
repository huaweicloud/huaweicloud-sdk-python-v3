# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


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
        return self._create_authorisation_with_http_info(request)

    def _create_authorisation_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/authorisations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAuthorisationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_authorisation(self, request):
        """删除授权

        网络实例所属租户取消授予云连接实例所属租户加载其网络实例的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuthorisation
        :type request: :class:`huaweicloudsdkcc.v3.DeleteAuthorisationRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteAuthorisationResponse`
        """
        return self._delete_authorisation_with_http_info(request)

    def _delete_authorisation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/authorisations/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAuthorisationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_authorisations(self, request):
        """查询授权列表

        网络实例所属租户查看其已经授予其他租户的权限。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthorisations
        :type request: :class:`huaweicloudsdkcc.v3.ListAuthorisationsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListAuthorisationsResponse`
        """
        return self._list_authorisations_with_http_info(request)

    def _list_authorisations_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/authorisations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuthorisationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_permissions(self, request):
        """查询权限列表

        云连接实例所属租户查询其可加载其他租户的网络实例权限。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPermissions
        :type request: :class:`huaweicloudsdkcc.v3.ListPermissionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListPermissionsResponse`
        """
        return self._list_permissions_with_http_info(request)

    def _list_permissions_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/permissions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPermissionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_authorisation(self, request):
        """更新授权

        更新授权实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuthorisation
        :type request: :class:`huaweicloudsdkcc.v3.UpdateAuthorisationRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateAuthorisationResponse`
        """
        return self._update_authorisation_with_http_info(request)

    def _update_authorisation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/authorisations/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAuthorisationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_bandwidth_package(self, request):
        """将带宽包实例绑定到云连接实例

        将带宽包实例绑定到云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.AssociateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.AssociateBandwidthPackageResponse`
        """
        return self._associate_bandwidth_package_with_http_info(request)

    def _associate_bandwidth_package_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/{id}/associate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateBandwidthPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_bandwidth_package(self, request):
        """创建带宽包实例

        创建带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.CreateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateBandwidthPackageResponse`
        """
        return self._create_bandwidth_package_with_http_info(request)

    def _create_bandwidth_package_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBandwidthPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_bandwidth_package(self, request):
        """删除带宽包实例

        删除带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.DeleteBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteBandwidthPackageResponse`
        """
        return self._delete_bandwidth_package_with_http_info(request)

    def _delete_bandwidth_package_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBandwidthPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_bandwidth_package(self, request):
        """解除带宽包实例与云连接实例的绑定

        解除带宽包实例与云连接实例的绑定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.DisassociateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DisassociateBandwidthPackageResponse`
        """
        return self._disassociate_bandwidth_package_with_http_info(request)

    def _disassociate_bandwidth_package_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/{id}/disassociate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateBandwidthPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidth_package_tags(self, request):
        """查询带宽包的标签信息

        查询带宽包的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthPackageTags
        :type request: :class:`huaweicloudsdkcc.v3.ListBandwidthPackageTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListBandwidthPackageTagsResponse`
        """
        return self._list_bandwidth_package_tags_with_http_info(request)

    def _list_bandwidth_package_tags_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBandwidthPackageTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidth_packages(self, request):
        """查询带宽包列表

        查询带宽包列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthPackages
        :type request: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesResponse`
        """
        return self._list_bandwidth_packages_with_http_info(request)

    def _list_bandwidth_packages_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBandwidthPackagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidth_packages_by_tags(self, request):
        """通过标签过滤带宽包实例

        通过标签过滤带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthPackagesByTags
        :type request: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesByTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesByTagsResponse`
        """
        return self._list_bandwidth_packages_by_tags_with_http_info(request)

    def _list_bandwidth_packages_by_tags_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/filter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBandwidthPackagesByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bandwidth_package(self, request):
        """查询带宽包实例

        查询带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.ShowBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowBandwidthPackageResponse`
        """
        return self._show_bandwidth_package_with_http_info(request)

    def _show_bandwidth_package_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBandwidthPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_bandwidth_package(self, request):
        """创建带宽包标签

        创建带宽包标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.TagBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.TagBandwidthPackageResponse`
        """
        return self._tag_bandwidth_package_with_http_info(request)

    def _tag_bandwidth_package_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/{id}/tag',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagBandwidthPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def untag_bandwidth_package(self, request):
        """删除带宽包标签

        删除带宽包标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.UntagBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UntagBandwidthPackageResponse`
        """
        return self._untag_bandwidth_package_with_http_info(request)

    def _untag_bandwidth_package_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/{id}/untag',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UntagBandwidthPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_bandwidth_package(self, request):
        """更新带宽包实例

        更新带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.UpdateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateBandwidthPackageResponse`
        """
        return self._update_bandwidth_package_with_http_info(request)

    def _update_bandwidth_package_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/bandwidth-packages/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBandwidthPackageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def apply_central_network_policy(self, request):
        """应用中心网络策略

        应用中心网络策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyCentralNetworkPolicy
        :type request: :class:`huaweicloudsdkcc.v3.ApplyCentralNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ApplyCentralNetworkPolicyResponse`
        """
        return self._apply_central_network_policy_with_http_info(request)

    def _apply_central_network_policy_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/policies/{policy_id}/apply',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyCentralNetworkPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_central_network(self, request):
        """创建中心网络

        创建中心网络。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkResponse`
        """
        return self._create_central_network_with_http_info(request)

    def _create_central_network_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-networks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCentralNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_central_network_policy(self, request):
        """创建一个新版本的中心网络策略

        创建一份只读的中心网络的策略。如果您有策略文档内容改动，需要基于此版本重新创建一个新版本的策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCentralNetworkPolicy
        :type request: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkPolicyResponse`
        """
        return self._create_central_network_policy_with_http_info(request)

    def _create_central_network_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/policies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCentralNetworkPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_central_network(self, request):
        """删除中心网络

        删除中心网络，请先清除附件后再删除中心网络。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkResponse`
        """
        return self._delete_central_network_with_http_info(request)

    def _delete_central_network_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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
            resource_path='/v3/{domain_id}/gcn/central-networks/{central_network_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCentralNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_central_network_policy(self, request):
        """删除中心网络策略版本

        删除中心网络策略版本。您无法删除正在被应用的中心策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCentralNetworkPolicy
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkPolicyRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkPolicyResponse`
        """
        return self._delete_central_network_policy_with_http_info(request)

    def _delete_central_network_policy_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/policies/{policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCentralNetworkPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_network_policies(self, request):
        """查询所有版本的中心网络策略列表

        查询所有版本的中心网络策略列表。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkPolicies
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkPoliciesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkPoliciesResponse`
        """
        return self._list_central_network_policies_with_http_info(request)

    def _list_central_network_policies_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworkPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_network_policy_change_set(self, request):
        """查询中心网络策略变化集

        查询与当前应用中心网络策略的变化集。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkPolicyChangeSet
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkPolicyChangeSetRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkPolicyChangeSetResponse`
        """
        return self._list_central_network_policy_change_set_with_http_info(request)

    def _list_central_network_policy_change_set_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/policies/{policy_id}/change-set',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworkPolicyChangeSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_network_tags(self, request):
        """查询中心网络的标签信息

        查询中心网络的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkTags
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkTagsResponse`
        """
        return self._list_central_network_tags_with_http_info(request)

    def _list_central_network_tags_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-networks/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworkTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_networks(self, request):
        """查询中心网络列表

        查询中心网络列表。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworks
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworksRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworksResponse`
        """
        return self._list_central_networks_with_http_info(request)

    def _list_central_networks_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-networks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_central_network(self, request):
        """查询中心网络详情

        查询中心网络详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkResponse`
        """
        return self._show_central_network_with_http_info(request)

    def _show_central_network_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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
            resource_path='/v3/{domain_id}/gcn/central-networks/{central_network_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCentralNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_central_network(self, request):
        """创建中心网络标签

        创建中心网络标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.TagCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.TagCentralNetworkResponse`
        """
        return self._tag_central_network_with_http_info(request)

    def _tag_central_network_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-networks/{central_network_id}/tag',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagCentralNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def untag_central_network(self, request):
        """删除中心网络标签

        删除中心网络标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.UntagCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UntagCentralNetworkResponse`
        """
        return self._untag_central_network_with_http_info(request)

    def _untag_central_network_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-networks/{central_network_id}/untag',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UntagCentralNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_central_network(self, request):
        """更新中心网络详情

        更新中心网络详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCentralNetwork
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkResponse`
        """
        return self._update_central_network_with_http_info(request)

    def _update_central_network_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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
            resource_path='/v3/{domain_id}/gcn/central-networks/{central_network_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCentralNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_central_network_gdgw_attachment(self, request):
        """创建中心网络GDGW附件

        创建中心网络的GDGW附件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCentralNetworkGdgwAttachment
        :type request: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkGdgwAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetworkGdgwAttachmentResponse`
        """
        return self._create_central_network_gdgw_attachment_with_http_info(request)

    def _create_central_network_gdgw_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'central_network_id' in local_var_params:
            path_params['central_network_id'] = local_var_params['central_network_id']

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
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/gdgw-attachments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCentralNetworkGdgwAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_central_network_attachment(self, request):
        """删除中心网络附件

        删除中心网络附件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCentralNetworkAttachment
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCentralNetworkAttachmentResponse`
        """
        return self._delete_central_network_attachment_with_http_info(request)

    def _delete_central_network_attachment_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/attachments/{attachment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCentralNetworkAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_network_attachments(self, request):
        """查询中心网络附件列表

        查询中心网络附件列表，分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkAttachments
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkAttachmentsResponse`
        """
        return self._list_central_network_attachments_with_http_info(request)

    def _list_central_network_attachments_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/attachments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworkAttachmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_network_gdgw_attachments(self, request):
        """查询中心网络GDGW附件列表

        查询中心网络GDGW附件列表。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkGdgwAttachments
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkGdgwAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkGdgwAttachmentsResponse`
        """
        return self._list_central_network_gdgw_attachments_with_http_info(request)

    def _list_central_network_gdgw_attachments_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/gdgw-attachments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworkGdgwAttachmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_central_network_gdgw_attachment(self, request):
        """查询中心网络GDGW附件详情

        查询中心网络GDGW附件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCentralNetworkGdgwAttachment
        :type request: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkGdgwAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCentralNetworkGdgwAttachmentResponse`
        """
        return self._show_central_network_gdgw_attachment_with_http_info(request)

    def _show_central_network_gdgw_attachment_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/gdgw-attachments/{gdgw_attachment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCentralNetworkGdgwAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_central_network_gdgw_attachment(self, request):
        """更新中心网络GDGW附件

        更新中心网络GDGW附件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCentralNetworkGdgwAttachment
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkGdgwAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkGdgwAttachmentResponse`
        """
        return self._update_central_network_gdgw_attachment_with_http_info(request)

    def _update_central_network_gdgw_attachment_with_http_info(self, request):
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
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/gdgw-attachments/{gdgw_attachment_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCentralNetworkGdgwAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_network_capabilities(self, request):
        """查询中心网络能力列表

        查询中心网络能力列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkCapabilities
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkCapabilitiesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkCapabilitiesResponse`
        """
        return self._list_central_network_capabilities_with_http_info(request)

    def _list_central_network_capabilities_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/capabilities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworkCapabilitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_network_connections(self, request):
        """查询中心网络连接列表

        查询中心网络连接列表接口。
        分页查询使用的参数为marker、limit。limit默认值为0，没有指定marker时返回第一条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkConnections
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkConnectionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkConnectionsResponse`
        """
        return self._list_central_network_connections_with_http_info(request)

    def _list_central_network_connections_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworkConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_central_network_connection(self, request):
        """更新中心网络连接接口

        更新中心网络连接接口（仅支持更新带宽）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCentralNetworkConnection
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkConnectionResponse`
        """
        return self._update_central_network_connection_with_http_info(request)

    def _update_central_network_connection_with_http_info(self, request):
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
            resource_path='/v3/{domain_id}/gcn/central-network/{central_network_id}/connections/{connection_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCentralNetworkConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_central_network_quotas(self, request):
        """查询中心网络配额

        查询中心网络配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCentralNetworkQuotas
        :type request: :class:`huaweicloudsdkcc.v3.ListCentralNetworkQuotasRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCentralNetworkQuotasResponse`
        """
        return self._list_central_network_quotas_with_http_info(request)

    def _list_central_network_quotas_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/gcn/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCentralNetworkQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cloud_connection(self, request):
        """创建云连接实例

        创建云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.CreateCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCloudConnectionResponse`
        """
        return self._create_cloud_connection_with_http_info(request)

    def _create_cloud_connection_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/cloud-connections',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_cloud_connection(self, request):
        """删除云连接实例

        删除云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCloudConnectionResponse`
        """
        return self._delete_cloud_connection_with_http_info(request)

    def _delete_cloud_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_connection_tags(self, request):
        """查询云连接实例的标签信息

        查询云连接实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionTags
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionTagsResponse`
        """
        return self._list_cloud_connection_tags_with_http_info(request)

    def _list_cloud_connection_tags_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudConnectionTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_connections(self, request):
        """查询云连接列表

        查询云连接列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnections
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsResponse`
        """
        return self._list_cloud_connections_with_http_info(request)

    def _list_cloud_connections_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/cloud-connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_connections_by_tags(self, request):
        """通过标签过滤云连接实例

        通过标签过滤云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionsByTags
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsByTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsByTagsResponse`
        """
        return self._list_cloud_connections_by_tags_with_http_info(request)

    def _list_cloud_connections_by_tags_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/filter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudConnectionsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cloud_connection(self, request):
        """查询云连接实例

        查询云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionResponse`
        """
        return self._show_cloud_connection_with_http_info(request)

    def _show_cloud_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_cloud_connection(self, request):
        """创建云连接实例标签

        创建云连接实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.TagCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.TagCloudConnectionResponse`
        """
        return self._tag_cloud_connection_with_http_info(request)

    def _tag_cloud_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/{id}/tag',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def untag_cloud_connection(self, request):
        """删除云连接实例标签

        删除云连接实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.UntagCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UntagCloudConnectionResponse`
        """
        return self._untag_cloud_connection_with_http_info(request)

    def _untag_cloud_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/{id}/untag',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UntagCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cloud_connection(self, request):
        """更新云连接实例

        更新云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCloudConnectionResponse`
        """
        return self._update_cloud_connection_with_http_info(request)

    def _update_cloud_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_connection_quotas(self, request):
        """查询云连接配额

        查询云连接配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionQuotas
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionQuotasRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionQuotasResponse`
        """
        return self._list_cloud_connection_quotas_with_http_info(request)

    def _list_cloud_connection_quotas_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudConnectionQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_connection_routes(self, request):
        """查询云连接路由条目列表

        查询云连接路由条目列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionRoutes
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionRoutesResponse`
        """
        return self._list_cloud_connection_routes_with_http_info(request)

    def _list_cloud_connection_routes_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/cloud-connection-routes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudConnectionRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cloud_connection_routes(self, request):
        """查询云连接路由条目详情

        查询云连接路由条目列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudConnectionRoutes
        :type request: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRoutesResponse`
        """
        return self._show_cloud_connection_routes_with_http_info(request)

    def _show_cloud_connection_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/cloud-connection-routes/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCloudConnectionRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_inter_region_bandwidth(self, request):
        """创建域间带宽实例

        创建域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidthResponse`
        """
        return self._create_inter_region_bandwidth_with_http_info(request)

    def _create_inter_region_bandwidth_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/inter-region-bandwidths',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInterRegionBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_inter_region_bandwidth(self, request):
        """删除域间带宽实例

        删除域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.DeleteInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteInterRegionBandwidthResponse`
        """
        return self._delete_inter_region_bandwidth_with_http_info(request)

    def _delete_inter_region_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/inter-region-bandwidths/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteInterRegionBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_inter_region_bandwidths(self, request):
        """查询域间带宽列表

        查询域间带宽列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInterRegionBandwidths
        :type request: :class:`huaweicloudsdkcc.v3.ListInterRegionBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListInterRegionBandwidthsResponse`
        """
        return self._list_inter_region_bandwidths_with_http_info(request)

    def _list_inter_region_bandwidths_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/inter-region-bandwidths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInterRegionBandwidthsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_inter_region_bandwidth(self, request):
        """查询域间带宽实例

        查询域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.ShowInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowInterRegionBandwidthResponse`
        """
        return self._show_inter_region_bandwidth_with_http_info(request)

    def _show_inter_region_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/inter-region-bandwidths/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInterRegionBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_inter_region_bandwidth(self, request):
        """更新域间带宽实例

        更新域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.UpdateInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateInterRegionBandwidthResponse`
        """
        return self._update_inter_region_bandwidth_with_http_info(request)

    def _update_inter_region_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/inter-region-bandwidths/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInterRegionBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_network_instance(self, request):
        """创建网络实例

        创建网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.CreateNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateNetworkInstanceResponse`
        """
        return self._create_network_instance_with_http_info(request)

    def _create_network_instance_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/network-instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNetworkInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_network_instance(self, request):
        """删除网络实例

        删除网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.DeleteNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteNetworkInstanceResponse`
        """
        return self._delete_network_instance_with_http_info(request)

    def _delete_network_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/network-instances/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNetworkInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_network_instances(self, request):
        """查询网络实例列表

        查询云连接列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNetworkInstances
        :type request: :class:`huaweicloudsdkcc.v3.ListNetworkInstancesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListNetworkInstancesResponse`
        """
        return self._list_network_instances_with_http_info(request)

    def _list_network_instances_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/network-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNetworkInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_network_instance(self, request):
        """查询网络实例

        查询网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.ShowNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowNetworkInstanceResponse`
        """
        return self._show_network_instance_with_http_info(request)

    def _show_network_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/network-instances/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNetworkInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_network_instance(self, request):
        """更新网络实例

        更新网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.UpdateNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateNetworkInstanceResponse`
        """
        return self._update_network_instance_with_http_info(request)

    def _update_network_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/{domain_id}/ccaas/network-instances/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNetworkInstanceResponse',
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

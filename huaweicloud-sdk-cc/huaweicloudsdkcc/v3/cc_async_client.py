# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CcAsyncClient(Client):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(CcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcc.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "CcClient":
            raise TypeError("client type error, support client type is CcClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def associate_bandwidth_package_async(self, request):
        """将带宽包实例关联到资源

        将带宽包实例关联到资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.AssociateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.AssociateBandwidthPackageResponse`
        """
        return self.associate_bandwidth_package_with_http_info(request)

    def associate_bandwidth_package_with_http_info(self, request):
        all_params = ['id', 'associate_bandwidth_package_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def batch_create_delete_tags_async(self, request):
        """批量创建和删除资源标签

        批量创建和删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateDeleteTags
        :type request: :class:`huaweicloudsdkcc.v3.BatchCreateDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.BatchCreateDeleteTagsResponse`
        """
        return self.batch_create_delete_tags_with_http_info(request)

    def batch_create_delete_tags_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type', 'batch_create_delete_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{domain_id}/ccaas/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_authorisation_async(self, request):
        """创建授权

        网络实例所属租户授予云连接实例所属租户加载其网络实例的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAuthorisation
        :type request: :class:`huaweicloudsdkcc.v3.CreateAuthorisationRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateAuthorisationResponse`
        """
        return self.create_authorisation_with_http_info(request)

    def create_authorisation_with_http_info(self, request):
        all_params = ['create_authorisation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def create_bandwidth_package_async(self, request):
        """创建带宽包实例

        创建带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.CreateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateBandwidthPackageResponse`
        """
        return self.create_bandwidth_package_with_http_info(request)

    def create_bandwidth_package_with_http_info(self, request):
        all_params = ['create_bandwidth_package_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def create_cloud_connection_async(self, request):
        """创建云连接实例

        创建云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.CreateCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCloudConnectionResponse`
        """
        return self.create_cloud_connection_with_http_info(request)

    def create_cloud_connection_with_http_info(self, request):
        all_params = ['create_cloud_connection_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def create_inter_region_bandwidth_async(self, request):
        """创建域间带宽实例

        创建域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidthResponse`
        """
        return self.create_inter_region_bandwidth_with_http_info(request)

    def create_inter_region_bandwidth_with_http_info(self, request):
        all_params = ['create_inter_region_bandwidth_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def create_network_instance_async(self, request):
        """创建网络实例

        创建网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.CreateNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateNetworkInstanceResponse`
        """
        return self.create_network_instance_with_http_info(request)

    def create_network_instance_with_http_info(self, request):
        all_params = ['create_network_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def create_tag_async(self, request):
        """添加资源标签

        添加资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkcc.v3.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateTagResponse`
        """
        return self.create_tag_with_http_info(request)

    def create_tag_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type', 'create_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{domain_id}/ccaas/{resource_type}/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_authorisation_async(self, request):
        """删除授权

        网络实例所属租户取消授予云连接实例所属租户加载其网络实例的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAuthorisation
        :type request: :class:`huaweicloudsdkcc.v3.DeleteAuthorisationRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteAuthorisationResponse`
        """
        return self.delete_authorisation_with_http_info(request)

    def delete_authorisation_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def delete_bandwidth_package_async(self, request):
        """删除带宽包实例

        删除带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.DeleteBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteBandwidthPackageResponse`
        """
        return self.delete_bandwidth_package_with_http_info(request)

    def delete_bandwidth_package_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def delete_cloud_connection_async(self, request):
        """删除云连接实例

        删除云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCloudConnectionResponse`
        """
        return self.delete_cloud_connection_with_http_info(request)

    def delete_cloud_connection_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def delete_inter_region_bandwidth_async(self, request):
        """删除域间带宽实例

        删除域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.DeleteInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteInterRegionBandwidthResponse`
        """
        return self.delete_inter_region_bandwidth_with_http_info(request)

    def delete_inter_region_bandwidth_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def delete_network_instance_async(self, request):
        """删除网络实例

        删除网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.DeleteNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteNetworkInstanceResponse`
        """
        return self.delete_network_instance_with_http_info(request)

    def delete_network_instance_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def delete_tag_async(self, request):
        """删除资源标签

        删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkcc.v3.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteTagResponse`
        """
        return self.delete_tag_with_http_info(request)

    def delete_tag_with_http_info(self, request):
        all_params = ['resource_id', 'tag_key', 'resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'tag_key' in local_var_params:
            path_params['tag_key'] = local_var_params['tag_key']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{domain_id}/ccaas/{resource_type}/{resource_id}/tags/{tag_key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_bandwidth_package_async(self, request):
        """将带宽包实例与资源解关联

        将带宽包实例与资源解关联。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.DisassociateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DisassociateBandwidthPackageResponse`
        """
        return self.disassociate_bandwidth_package_with_http_info(request)

    def disassociate_bandwidth_package_with_http_info(self, request):
        all_params = ['id', 'disassociate_bandwidth_package_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_authorisations_async(self, request):
        """查询授权列表

        网络实例所属租户查看其已经授予其他租户的权限。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorisations
        :type request: :class:`huaweicloudsdkcc.v3.ListAuthorisationsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListAuthorisationsResponse`
        """
        return self.list_authorisations_with_http_info(request)

    def list_authorisations_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'description', 'cloud_connection_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_bandwidth_packages_async(self, request):
        """查询带宽包列表

        查询带宽包列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBandwidthPackages
        :type request: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListBandwidthPackagesResponse`
        """
        return self.list_bandwidth_packages_with_http_info(request)

    def list_bandwidth_packages_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'status', 'enterprise_project_id', 'billing_mode', 'resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
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

    def list_cloud_connection_routes_async(self, request):
        """查询云连接路由条目列表

        查询云连接路由条目列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudConnectionRoutes
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionRoutesResponse`
        """
        return self.list_cloud_connection_routes_with_http_info(request)

    def list_cloud_connection_routes_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'cloud_connection_id', 'instance_id', 'region_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'
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

    def list_cloud_connections_async(self, request):
        """查询云连接列表

        查询云连接列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudConnections
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsResponse`
        """
        return self.list_cloud_connections_with_http_info(request)

    def list_cloud_connections_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'description', 'status', 'enterprise_project_id', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'

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

    def list_domain_tags_async(self, request):
        """查询账户资源标签

        查询账户资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDomainTags
        :type request: :class:`huaweicloudsdkcc.v3.ListDomainTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListDomainTagsResponse`
        """
        return self.list_domain_tags_with_http_info(request)

    def list_domain_tags_with_http_info(self, request):
        all_params = ['resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{domain_id}/ccaas/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_inter_region_bandwidths_async(self, request):
        """查询域间带宽列表

        查询域间带宽列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInterRegionBandwidths
        :type request: :class:`huaweicloudsdkcc.v3.ListInterRegionBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListInterRegionBandwidthsResponse`
        """
        return self.list_inter_region_bandwidths_with_http_info(request)

    def list_inter_region_bandwidths_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'enterprise_project_id', 'cloud_connection_id', 'bandwidth_package_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_network_instances_async(self, request):
        """查询网络实例列表

        查询云连接列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNetworkInstances
        :type request: :class:`huaweicloudsdkcc.v3.ListNetworkInstancesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListNetworkInstancesResponse`
        """
        return self.list_network_instances_with_http_info(request)

    def list_network_instances_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'description', 'status', 'type', 'cloud_connection_id', 'instance_id', 'region_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
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

    def list_permissions_async(self, request):
        """查询权限列表

        云连接实例所属租户查询其可加载其他租户的网络实例权限。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermissions
        :type request: :class:`huaweicloudsdkcc.v3.ListPermissionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListPermissionsResponse`
        """
        return self.list_permissions_with_http_info(request)

    def list_permissions_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'description', 'cloud_connection_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_quotas_async(self, request):
        """查询配额

        查询配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkcc.v3.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListQuotasResponse`
        """
        return self.list_quotas_with_http_info(request)

    def list_quotas_with_http_info(self, request):
        all_params = ['limit', 'marker', 'quota_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_by_filter_tag_async(self, request):
        """查询资源实例

        查询资源实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceByFilterTag
        :type request: :class:`huaweicloudsdkcc.v3.ListResourceByFilterTagRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListResourceByFilterTagResponse`
        """
        return self.list_resource_by_filter_tag_with_http_info(request)

    def list_resource_by_filter_tag_with_http_info(self, request):
        all_params = ['resource_type', 'list_resource_by_filter_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{domain_id}/ccaas/{resource_type}/resource-instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceByFilterTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_async(self, request):
        """查询资源标签

        查询资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkcc.v3.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListTagsResponse`
        """
        return self.list_tags_with_http_info(request)

    def list_tags_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{domain_id}/ccaas/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bandwidth_package_async(self, request):
        """查询带宽包实例

        查询带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.ShowBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowBandwidthPackageResponse`
        """
        return self.show_bandwidth_package_with_http_info(request)

    def show_bandwidth_package_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def show_cloud_connection_async(self, request):
        """查询云连接实例

        查询云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionResponse`
        """
        return self.show_cloud_connection_with_http_info(request)

    def show_cloud_connection_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def show_cloud_connection_routes_async(self, request):
        """查询云连接路由条目详情

        查询云连接路由条目列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCloudConnectionRoutes
        :type request: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRoutesResponse`
        """
        return self.show_cloud_connection_routes_with_http_info(request)

    def show_cloud_connection_routes_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def show_inter_region_bandwidth_async(self, request):
        """查询域间带宽实例

        查询域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.ShowInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowInterRegionBandwidthResponse`
        """
        return self.show_inter_region_bandwidth_with_http_info(request)

    def show_inter_region_bandwidth_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def show_network_instance_async(self, request):
        """查询网络实例

        查询网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.ShowNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowNetworkInstanceResponse`
        """
        return self.show_network_instance_with_http_info(request)

    def show_network_instance_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_authorisation_async(self, request):
        """更新授权

        更新授权实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAuthorisation
        :type request: :class:`huaweicloudsdkcc.v3.UpdateAuthorisationRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateAuthorisationResponse`
        """
        return self.update_authorisation_with_http_info(request)

    def update_authorisation_with_http_info(self, request):
        all_params = ['id', 'update_authorisation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_bandwidth_package_async(self, request):
        """更新带宽包实例

        更新带宽包实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBandwidthPackage
        :type request: :class:`huaweicloudsdkcc.v3.UpdateBandwidthPackageRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateBandwidthPackageResponse`
        """
        return self.update_bandwidth_package_with_http_info(request)

    def update_bandwidth_package_with_http_info(self, request):
        all_params = ['id', 'update_bandwidth_package_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_cloud_connection_async(self, request):
        """更新云连接实例

        更新云连接实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCloudConnectionResponse`
        """
        return self.update_cloud_connection_with_http_info(request)

    def update_cloud_connection_with_http_info(self, request):
        all_params = ['id', 'update_cloud_connection_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_inter_region_bandwidth_async(self, request):
        """更新域间带宽实例

        更新域间带宽实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInterRegionBandwidth
        :type request: :class:`huaweicloudsdkcc.v3.UpdateInterRegionBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateInterRegionBandwidthResponse`
        """
        return self.update_inter_region_bandwidth_with_http_info(request)

    def update_inter_region_bandwidth_with_http_info(self, request):
        all_params = ['id', 'update_inter_region_bandwidth_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_network_instance_async(self, request):
        """更新网络实例

        更新网络实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.UpdateNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateNetworkInstanceResponse`
        """
        return self.update_network_instance_with_http_info(request)

    def update_network_instance_with_http_info(self, request):
        all_params = ['id', 'update_network_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

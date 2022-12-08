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


class EipAsyncClient(Client):
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
        super(EipAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeip.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EipClient":
            raise TypeError("client type error, support client type is EipClient")

        return ClientBuilder(clazz)

    def list_common_pools_async(self, request):
        """查询公共池列表

        查询公共池列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCommonPools
        :type request: :class:`huaweicloudsdkeip.v3.ListCommonPoolsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListCommonPoolsResponse`
        """
        return self.list_common_pools_with_http_info(request)

    def list_common_pools_with_http_info(self, request):
        all_params = ['fields', 'name', 'public_border_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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
            resource_path='/v3/{project_id}/eip/publicip-pools/common-pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCommonPoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_public_border_groups_async(self, request):
        """查询公共池分组列表

        查询公共池分组列表，包含名称和位置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicBorderGroups
        :type request: :class:`huaweicloudsdkeip.v3.ListPublicBorderGroupsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListPublicBorderGroupsResponse`
        """
        return self.list_public_border_groups_with_http_info(request)

    def list_public_border_groups_with_http_info(self, request):
        all_params = ['fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))

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
            resource_path='/v3/{project_id}/eip/public-border-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPublicBorderGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_publicip_pool_async(self, request):
        """查询公网IP池列表

        全量查询公网IP池列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicipPool
        :type request: :class:`huaweicloudsdkeip.v3.ListPublicipPoolRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListPublicipPoolResponse`
        """
        return self.list_publicip_pool_with_http_info(request)

    def list_publicip_pool_with_http_info(self, request):
        all_params = ['marker', 'limit', 'fields', 'sort_key', 'sort_dir', 'id', 'name', 'size', 'status', 'type', 'description', 'public_border_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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
            resource_path='/v3/{project_id}/eip/publicip-pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPublicipPoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_share_bandwidth_types_async(self, request):
        """查询指定租户下的共享带宽类型列表

        查询指定租户下的共享带宽类型列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListShareBandwidthTypes
        :type request: :class:`huaweicloudsdkeip.v3.ListShareBandwidthTypesRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListShareBandwidthTypesResponse`
        """
        return self.list_share_bandwidth_types_with_http_info(request)

    def list_share_bandwidth_types_with_http_info(self, request):
        all_params = ['fields', 'id', 'bandwidth_type', 'name_en', 'name_zh', 'public_border_group', 'sort_key', 'sort_dir', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'bandwidth_type' in local_var_params:
            query_params.append(('bandwidth_type', local_var_params['bandwidth_type']))
        if 'name_en' in local_var_params:
            query_params.append(('name_en', local_var_params['name_en']))
        if 'name_zh' in local_var_params:
            query_params.append(('name_zh', local_var_params['name_zh']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v3/{project_id}/eip/share-bandwidth-types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListShareBandwidthTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_publicip_pool_async(self, request):
        """查询公网IP池详情

        查询公网IP池详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicipPool
        :type request: :class:`huaweicloudsdkeip.v3.ShowPublicipPoolRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ShowPublicipPoolResponse`
        """
        return self.show_publicip_pool_with_http_info(request)

    def show_publicip_pool_with_http_info(self, request):
        all_params = ['publicip_pool_id', 'fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_pool_id' in local_var_params:
            path_params['publicip_pool_id'] = local_var_params['publicip_pool_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))

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
            resource_path='/v3/{project_id}/eip/publicip-pools/{publicip_pool_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublicipPoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_publicips_async(self, request):
        """绑定弹性公网IP

        绑定弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociatePublicips
        :type request: :class:`huaweicloudsdkeip.v3.AssociatePublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.AssociatePublicipsResponse`
        """
        return self.associate_publicips_with_http_info(request)

    def associate_publicips_with_http_info(self, request):
        all_params = ['publicip_id', 'associate_publicips_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}/associate-instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociatePublicipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_eip_available_resources_async(self, request):
        """查询弹性公网IP可用数

        IP池用于查询公网可用ip个数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountEipAvailableResources
        :type request: :class:`huaweicloudsdkeip.v3.CountEipAvailableResourcesRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.CountEipAvailableResourcesResponse`
        """
        return self.count_eip_available_resources_with_http_info(request)

    def count_eip_available_resources_with_http_info(self, request):
        all_params = ['eip_resources_available_v3_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/eip/resources/available',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountEipAvailableResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_publicips_async(self, request):
        """解绑弹性公网IP

        解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociatePublicips
        :type request: :class:`huaweicloudsdkeip.v3.DisassociatePublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.DisassociatePublicipsResponse`
        """
        return self.disassociate_publicips_with_http_info(request)

    def disassociate_publicips_with_http_info(self, request):
        all_params = ['publicip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}/disassociate-instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociatePublicipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_publicips_async(self, request):
        """全量查询弹性公网IP列表

        查询弹性公网IP列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicips
        :type request: :class:`huaweicloudsdkeip.v3.ListPublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListPublicipsResponse`
        """
        return self.list_publicips_with_http_info(request)

    def list_publicips_with_http_info(self, request):
        all_params = ['marker', 'offset', 'limit', 'fields', 'sort_key', 'sort_dir', 'id', 'ip_version', 'public_ip_address', 'public_ip_address_like', 'public_ipv6_address', 'public_ipv6_address_like', 'type', 'network_type', 'publicip_pool_name', 'status', 'alias_like', 'alias', 'description', 'vnic_private_ip_address', 'vnic_private_ip_address_like', 'vnic_device_id', 'vnic_device_owner', 'vnic_vpc_id', 'vnic_port_id', 'vnic_device_owner_prefixlike', 'vnic_instance_type', 'vnic_instance_id', 'bandwidth_id', 'bandwidth_name', 'bandwidth_name_like', 'bandwidth_size', 'bandwidth_share_type', 'bandwidth_charge_mode', 'billing_info', 'billing_mode', 'associate_instance_type', 'associate_instance_id', 'enterprise_project_id', 'public_border_group', 'allow_share_bandwidth_type_any']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'public_ip_address' in local_var_params:
            query_params.append(('public_ip_address', local_var_params['public_ip_address']))
            collection_formats['public_ip_address'] = 'multi'
        if 'public_ip_address_like' in local_var_params:
            query_params.append(('public_ip_address_like', local_var_params['public_ip_address_like']))
        if 'public_ipv6_address' in local_var_params:
            query_params.append(('public_ipv6_address', local_var_params['public_ipv6_address']))
            collection_formats['public_ipv6_address'] = 'multi'
        if 'public_ipv6_address_like' in local_var_params:
            query_params.append(('public_ipv6_address_like', local_var_params['public_ipv6_address_like']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'network_type' in local_var_params:
            query_params.append(('network_type', local_var_params['network_type']))
            collection_formats['network_type'] = 'multi'
        if 'publicip_pool_name' in local_var_params:
            query_params.append(('publicip_pool_name', local_var_params['publicip_pool_name']))
            collection_formats['publicip_pool_name'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'alias_like' in local_var_params:
            query_params.append(('alias_like', local_var_params['alias_like']))
        if 'alias' in local_var_params:
            query_params.append(('alias', local_var_params['alias']))
            collection_formats['alias'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'vnic_private_ip_address' in local_var_params:
            query_params.append(('vnic.private_ip_address', local_var_params['vnic_private_ip_address']))
            collection_formats['vnic.private_ip_address'] = 'multi'
        if 'vnic_private_ip_address_like' in local_var_params:
            query_params.append(('vnic.private_ip_address_like', local_var_params['vnic_private_ip_address_like']))
        if 'vnic_device_id' in local_var_params:
            query_params.append(('vnic.device_id', local_var_params['vnic_device_id']))
            collection_formats['vnic.device_id'] = 'multi'
        if 'vnic_device_owner' in local_var_params:
            query_params.append(('vnic.device_owner', local_var_params['vnic_device_owner']))
            collection_formats['vnic.device_owner'] = 'multi'
        if 'vnic_vpc_id' in local_var_params:
            query_params.append(('vnic.vpc_id', local_var_params['vnic_vpc_id']))
            collection_formats['vnic.vpc_id'] = 'multi'
        if 'vnic_port_id' in local_var_params:
            query_params.append(('vnic.port_id', local_var_params['vnic_port_id']))
            collection_formats['vnic.port_id'] = 'multi'
        if 'vnic_device_owner_prefixlike' in local_var_params:
            query_params.append(('vnic.device_owner_prefixlike', local_var_params['vnic_device_owner_prefixlike']))
        if 'vnic_instance_type' in local_var_params:
            query_params.append(('vnic.instance_type', local_var_params['vnic_instance_type']))
            collection_formats['vnic.instance_type'] = 'multi'
        if 'vnic_instance_id' in local_var_params:
            query_params.append(('vnic.instance_id', local_var_params['vnic_instance_id']))
            collection_formats['vnic.instance_id'] = 'multi'
        if 'bandwidth_id' in local_var_params:
            query_params.append(('bandwidth.id', local_var_params['bandwidth_id']))
            collection_formats['bandwidth.id'] = 'multi'
        if 'bandwidth_name' in local_var_params:
            query_params.append(('bandwidth.name', local_var_params['bandwidth_name']))
            collection_formats['bandwidth.name'] = 'multi'
        if 'bandwidth_name_like' in local_var_params:
            query_params.append(('bandwidth.name_like', local_var_params['bandwidth_name_like']))
            collection_formats['bandwidth.name_like'] = 'multi'
        if 'bandwidth_size' in local_var_params:
            query_params.append(('bandwidth.size', local_var_params['bandwidth_size']))
            collection_formats['bandwidth.size'] = 'multi'
        if 'bandwidth_share_type' in local_var_params:
            query_params.append(('bandwidth.share_type', local_var_params['bandwidth_share_type']))
            collection_formats['bandwidth.share_type'] = 'multi'
        if 'bandwidth_charge_mode' in local_var_params:
            query_params.append(('bandwidth.charge_mode', local_var_params['bandwidth_charge_mode']))
            collection_formats['bandwidth.charge_mode'] = 'multi'
        if 'billing_info' in local_var_params:
            query_params.append(('billing_info', local_var_params['billing_info']))
            collection_formats['billing_info'] = 'multi'
        if 'billing_mode' in local_var_params:
            query_params.append(('billing_mode', local_var_params['billing_mode']))
        if 'associate_instance_type' in local_var_params:
            query_params.append(('associate_instance_type', local_var_params['associate_instance_type']))
            collection_formats['associate_instance_type'] = 'multi'
        if 'associate_instance_id' in local_var_params:
            query_params.append(('associate_instance_id', local_var_params['associate_instance_id']))
            collection_formats['associate_instance_id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
            collection_formats['public_border_group'] = 'multi'
        if 'allow_share_bandwidth_type_any' in local_var_params:
            query_params.append(('allow_share_bandwidth_type_any', local_var_params['allow_share_bandwidth_type_any']))
            collection_formats['allow_share_bandwidth_type_any'] = 'multi'

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
            resource_path='/v3/{project_id}/eip/publicips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPublicipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_publicip_async(self, request):
        """查询弹性公网IP详情

        查询弹性公网IP详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicip
        :type request: :class:`huaweicloudsdkeip.v3.ShowPublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ShowPublicipResponse`
        """
        return self.show_publicip_with_http_info(request)

    def show_publicip_with_http_info(self, request):
        all_params = ['publicip_id', 'fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'csv'

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
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_associate_publicip_async(self, request):
        """绑定弹性公网IP

        绑定弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAssociatePublicip
        :type request: :class:`huaweicloudsdkeip.v3.UpdateAssociatePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.UpdateAssociatePublicipResponse`
        """
        return self.update_associate_publicip_with_http_info(request)

    def update_associate_publicip_with_http_info(self, request):
        all_params = ['publicip_id', 'associate_publicips_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}/associate-instance',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAssociatePublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_disassociate_publicip_async(self, request):
        """解绑弹性公网IP

        解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDisassociatePublicip
        :type request: :class:`huaweicloudsdkeip.v3.UpdateDisassociatePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.UpdateDisassociatePublicipResponse`
        """
        return self.update_disassociate_publicip_with_http_info(request)

    def update_disassociate_publicip_with_http_info(self, request):
        all_params = ['publicip_id', 'disassociate_publicips_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}/disassociate-instance',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDisassociatePublicipResponse',
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

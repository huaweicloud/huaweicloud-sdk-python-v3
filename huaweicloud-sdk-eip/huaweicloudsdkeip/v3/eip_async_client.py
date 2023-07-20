# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class EipAsyncClient(Client):
    def __init__(self):
        super(EipAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeip.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EipClient":
            raise TypeError("client type error, support client type is EipClient")

        return ClientBuilder(clazz)

    def list_bandwidth_async(self, request):
        """查询带宽列表

        查询带宽列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBandwidth
        :type request: :class:`huaweicloudsdkeip.v3.ListBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListBandwidthResponse`
        """
        return self._list_bandwidth_with_http_info(request)

    def _list_bandwidth_with_http_info(self, request):
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
        if 'bandwidth_type' in local_var_params:
            query_params.append(('bandwidth_type', local_var_params['bandwidth_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'ingress_size' in local_var_params:
            query_params.append(('ingress_size', local_var_params['ingress_size']))
        if 'admin_state' in local_var_params:
            query_params.append(('admin_state', local_var_params['admin_state']))
        if 'billing_info' in local_var_params:
            query_params.append(('billing_info', local_var_params['billing_info']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'enable_bandwidth_rules' in local_var_params:
            query_params.append(('enable_bandwidth_rules', local_var_params['enable_bandwidth_rules']))
        if 'rule_quota' in local_var_params:
            query_params.append(('rule_quota', local_var_params['rule_quota']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v3/{project_id}/eip/bandwidths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_common_pools_async(self, request):
        """查询公共池列表

        查询公共池列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCommonPools
        :type request: :class:`huaweicloudsdkeip.v3.ListCommonPoolsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListCommonPoolsResponse`
        """
        return self._list_common_pools_with_http_info(request)

    def _list_common_pools_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
        return self._list_public_border_groups_with_http_info(request)

    def _list_public_border_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        return self._list_publicip_pool_with_http_info(request)

    def _list_publicip_pool_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        return self._list_share_bandwidth_types_with_http_info(request)

    def _list_share_bandwidth_types_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
        return self._show_publicip_pool_with_http_info(request)

    def _show_publicip_pool_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        return self._associate_publicips_with_http_info(request)

    def _associate_publicips_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def attach_batch_public_ip_async(self, request):
        """共享带宽批量加入弹性公网IP

        共享带宽批量加入弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachBatchPublicIp
        :type request: :class:`huaweicloudsdkeip.v3.AttachBatchPublicIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.AttachBatchPublicIpResponse`
        """
        return self._attach_batch_public_ip_with_http_info(request)

    def _attach_batch_public_ip_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/eip/publicips/attach-share-bandwidth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachBatchPublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_share_bandwidth_async(self, request):
        """共享带宽加入弹性公网IP

        共享带宽加入弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachShareBandwidth
        :type request: :class:`huaweicloudsdkeip.v3.AttachShareBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.AttachShareBandwidthResponse`
        """
        return self._attach_share_bandwidth_with_http_info(request)

    def _attach_share_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}/attach-share-bandwidth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachShareBandwidthResponse',
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
        return self._count_eip_available_resources_with_http_info(request)

    def _count_eip_available_resources_with_http_info(self, request):
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

    def detach_batch_public_ip_async(self, request):
        """共享带宽批量移出弹性公网IP

        共享带宽批量移出弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachBatchPublicIp
        :type request: :class:`huaweicloudsdkeip.v3.DetachBatchPublicIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.DetachBatchPublicIpResponse`
        """
        return self._detach_batch_public_ip_with_http_info(request)

    def _detach_batch_public_ip_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/eip/publicips/detach-share-bandwidth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachBatchPublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_share_bandwidth_async(self, request):
        """共享带宽移出弹性公网IP

        共享带宽移出弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachShareBandwidth
        :type request: :class:`huaweicloudsdkeip.v3.DetachShareBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.DetachShareBandwidthResponse`
        """
        return self._detach_share_bandwidth_with_http_info(request)

    def _detach_share_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}/detach-share-bandwidth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachShareBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_nat64_async(self, request):
        """弹性公网IP关闭NAT64

        弹性公网IP关闭NAT64
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableNat64
        :type request: :class:`huaweicloudsdkeip.v3.DisableNat64Request`
        :rtype: :class:`huaweicloudsdkeip.v3.DisableNat64Response`
        """
        return self._disable_nat64_with_http_info(request)

    def _disable_nat64_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}/disable-nat64',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableNat64Response',
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
        return self._disassociate_publicips_with_http_info(request)

    def _disassociate_publicips_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def enable_nat64_async(self, request):
        """弹性公网IP开启NAT64

        弹性公网IP开启NAT64
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableNat64
        :type request: :class:`huaweicloudsdkeip.v3.EnableNat64Request`
        :rtype: :class:`huaweicloudsdkeip.v3.EnableNat64Response`
        """
        return self._enable_nat64_with_http_info(request)

    def _enable_nat64_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/eip/publicips/{publicip_id}/enable-nat64',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableNat64Response',
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
        return self._list_publicips_with_http_info(request)

    def _list_publicips_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        return self._show_publicip_with_http_info(request)

    def _show_publicip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        return self._update_associate_publicip_with_http_info(request)

    def _update_associate_publicip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        return self._update_disassociate_publicip_with_http_info(request)

    def _update_disassociate_publicip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

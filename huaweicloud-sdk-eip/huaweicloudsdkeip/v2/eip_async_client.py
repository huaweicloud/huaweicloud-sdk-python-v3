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
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

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
        self.model_package = importlib.import_module("huaweicloudsdkeip.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EipClient":
            raise TypeError("client type error, support client type is EipClient")

        return ClientBuilder(clazz)

    def add_publicips_into_shared_bandwidth_async(self, request):
        """共享带宽插入弹性公网IP

        共享带宽插入弹性公网IP。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddPublicipsIntoSharedBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.AddPublicipsIntoSharedBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.AddPublicipsIntoSharedBandwidthResponse`
        """
        return self.add_publicips_into_shared_bandwidth_with_http_info(request)

    def add_publicips_into_shared_bandwidth_with_http_info(self, request):
        all_params = ['bandwidth_id', 'bandwidth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v2.0/{project_id}/bandwidths/{bandwidth_id}/insert',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddPublicipsIntoSharedBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_shared_bandwidths_async(self, request):
        """批量创建共享带宽

        批量创建共享带宽。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchCreateSharedBandwidths
        :type request: :class:`huaweicloudsdkeip.v2.BatchCreateSharedBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchCreateSharedBandwidthsResponse`
        """
        return self.batch_create_shared_bandwidths_with_http_info(request)

    def batch_create_shared_bandwidths_with_http_info(self, request):
        all_params = ['bandwidth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/batch-bandwidths',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateSharedBandwidthsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_shared_bandwidth_async(self, request):
        """创建共享带宽

        创建共享带宽。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateSharedBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.CreateSharedBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CreateSharedBandwidthResponse`
        """
        return self.create_shared_bandwidth_with_http_info(request)

    def create_shared_bandwidth_with_http_info(self, request):
        all_params = ['bandwidth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/bandwidths',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSharedBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_shared_bandwidth_async(self, request):
        """删除共享带宽

        删除共享带宽。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteSharedBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.DeleteSharedBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.DeleteSharedBandwidthResponse`
        """
        return self.delete_shared_bandwidth_with_http_info(request)

    def delete_shared_bandwidth_with_http_info(self, request):
        all_params = ['bandwidth_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v2.0/{project_id}/bandwidths/{bandwidth_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSharedBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidths_async(self, request):
        """查询带宽列表

        查询带宽列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListBandwidths
        :type request: :class:`huaweicloudsdkeip.v2.ListBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListBandwidthsResponse`
        """
        return self.list_bandwidths_with_http_info(request)

    def list_bandwidths_with_http_info(self, request):
        all_params = ['marker', 'limit', 'enterprise_project_id', 'share_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'share_type' in local_var_params:
            query_params.append(('share_type', local_var_params['share_type']))

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
            resource_path='/v1/{project_id}/bandwidths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBandwidthsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas_async(self, request):
        """查询配额接口

        查询配额
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkeip.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListQuotasResponse`
        """
        return self.list_quotas_with_http_info(request)

    def list_quotas_with_http_info(self, request):
        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_publicips_from_shared_bandwidth_async(self, request):
        """共享带宽移除弹性公网IP

        共享带宽移除弹性公网IP。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RemovePublicipsFromSharedBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.RemovePublicipsFromSharedBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.RemovePublicipsFromSharedBandwidthResponse`
        """
        return self.remove_publicips_from_shared_bandwidth_with_http_info(request)

    def remove_publicips_from_shared_bandwidth_with_http_info(self, request):
        all_params = ['bandwidth_id', 'bandwidth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v2.0/{project_id}/bandwidths/{bandwidth_id}/remove',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemovePublicipsFromSharedBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bandwidth_async(self, request):
        """查询带宽

        查询带宽
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.ShowBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowBandwidthResponse`
        """
        return self.show_bandwidth_with_http_info(request)

    def show_bandwidth_with_http_info(self, request):
        all_params = ['bandwidth_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v1/{project_id}/bandwidths/{bandwidth_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_bandwidth_async(self, request):
        """更新带宽

        更新带宽。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.UpdateBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.UpdateBandwidthResponse`
        """
        return self.update_bandwidth_with_http_info(request)

    def update_bandwidth_with_http_info(self, request):
        all_params = ['bandwidth_id', 'bandwidth']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v1/{project_id}/bandwidths/{bandwidth_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_pre_paid_bandwidth_async(self, request):
        """更新包周期带宽

        更新带宽。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePrePaidBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthResponse`
        """
        return self.update_pre_paid_bandwidth_with_http_info(request)

    def update_pre_paid_bandwidth_with_http_info(self, request):
        all_params = ['bandwidth_id', 'update_bandwidth_information']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v2.0/{project_id}/bandwidths/{bandwidth_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePrePaidBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_publicip_tags_async(self, request):
        """批量创建弹性公网IP资源标签

        为指定的弹性公网IP资源实例批量添加标签。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchCreatePublicipTags
        :type request: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipTagsResponse`
        """
        return self.batch_create_publicip_tags_with_http_info(request)

    def batch_create_publicip_tags_with_http_info(self, request):
        all_params = ['publicip_id', 'resource_tag_action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreatePublicipTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_publicip_tags_async(self, request):
        """批量删除弹性公网IP资源标签

        为指定的弹性公网IP资源实例批量删除标签。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeletePublicipTags
        :type request: :class:`huaweicloudsdkeip.v2.BatchDeletePublicipTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchDeletePublicipTagsResponse`
        """
        return self.batch_delete_publicip_tags_with_http_info(request)

    def batch_delete_publicip_tags_with_http_info(self, request):
        all_params = ['publicip_id', 'resource_tag_action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeletePublicipTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_pre_paid_publicip_async(self, request):
        """申请包周期弹性公网IP

        申请包年包月的弹性公网IP。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePrePaidPublicip
        :type request: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipResponse`
        """
        return self.create_pre_paid_publicip_with_http_info(request)

    def create_pre_paid_publicip_with_http_info(self, request):
        all_params = ['create_period_publicip']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/publicips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePrePaidPublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_publicip_async(self, request):
        """申请弹性公网IP

        申请弹性公网IP，支持IPv4和IPv6。
         弹性公网IP（Elastic IP）提供独立的公网IP资源，包括公网IP地址与公网出口带宽服务。可以与弹性云服务器、裸金属服务器、虚拟IP、弹性负载均衡、NAT网关等资源灵活地绑定及解绑。拥有多种灵活的计费方式，可以满足各种业务场景的需要。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePublicip
        :type request: :class:`huaweicloudsdkeip.v2.CreatePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePublicipResponse`
        """
        return self.create_publicip_with_http_info(request)

    def create_publicip_with_http_info(self, request):
        all_params = ['create_publicip']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/publicips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_publicip_tag_async(self, request):
        """创建弹性公网IP资源标签

        给指定弹性IP资源实例增加标签信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePublicipTag
        :type request: :class:`huaweicloudsdkeip.v2.CreatePublicipTagRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePublicipTagResponse`
        """
        return self.create_publicip_tag_with_http_info(request)

    def create_publicip_tag_with_http_info(self, request):
        all_params = ['publicip_id', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePublicipTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_publicip_async(self, request):
        """删除弹性公网IP

        删除弹性公网IP,绑定状态eip不允许直接删除。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeletePublicip
        :type request: :class:`huaweicloudsdkeip.v2.DeletePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.DeletePublicipResponse`
        """
        return self.delete_publicip_with_http_info(request)

    def delete_publicip_with_http_info(self, request):
        all_params = ['publicip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/publicips/{publicip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_publicip_tag_async(self, request):
        """删除弹性公网IP的标签

        删除指定弹性公网IP的标签信息。其中project_id是项目ID，publicip_id 是要操作的弹性公网IP的id。key是要删除标签的键。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeletePublicipTag
        :type request: :class:`huaweicloudsdkeip.v2.DeletePublicipTagRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.DeletePublicipTagResponse`
        """
        return self.delete_publicip_tag_with_http_info(request)

    def delete_publicip_tag_with_http_info(self, request):
        all_params = ['publicip_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePublicipTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_publicip_tags_async(self, request):
        """查询租户的弹性公网IP标签

        查询租户在指定区域和实例类型的所有标签集合。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPublicipTags
        :type request: :class:`huaweicloudsdkeip.v2.ListPublicipTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListPublicipTagsResponse`
        """
        return self.list_publicip_tags_with_http_info(request)

    def list_publicip_tags_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/publicips/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPublicipTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_publicips_async(self, request):
        """查询弹性公网IP列表

        查询弹性公网IP列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPublicips
        :type request: :class:`huaweicloudsdkeip.v2.ListPublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListPublicipsResponse`
        """
        return self.list_publicips_with_http_info(request)

    def list_publicips_with_http_info(self, request):
        all_params = ['marker', 'limit', 'ip_version', 'enterprise_project_id', 'port_id', 'public_ip_address', 'private_ip_address', 'id', 'allow_share_bandwidth_type_any']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))
            collection_formats['port_id'] = 'multi'
        if 'public_ip_address' in local_var_params:
            query_params.append(('public_ip_address', local_var_params['public_ip_address']))
            collection_formats['public_ip_address'] = 'multi'
        if 'private_ip_address' in local_var_params:
            query_params.append(('private_ip_address', local_var_params['private_ip_address']))
            collection_formats['private_ip_address'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
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
            resource_path='/v1/{project_id}/publicips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPublicipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_publicips_by_tags_async(self, request):
        """按标签查询弹性公网IP列表

        使用标签过滤弹性公网IP。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPublicipsByTags
        :type request: :class:`huaweicloudsdkeip.v2.ListPublicipsByTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListPublicipsByTagsResponse`
        """
        return self.list_publicips_by_tags_with_http_info(request)

    def list_publicips_by_tags_with_http_info(self, request):
        all_params = ['show_publicip_resource_instance']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/publicips/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPublicipsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_publicip_async(self, request):
        """查询弹性公网IP

        查询指定的弹性公网IP。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPublicip
        :type request: :class:`huaweicloudsdkeip.v2.ShowPublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowPublicipResponse`
        """
        return self.show_publicip_with_http_info(request)

    def show_publicip_with_http_info(self, request):
        all_params = ['publicip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/publicips/{publicip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_publicip_tags_async(self, request):
        """查询弹性公网IP的标签

        查询指定弹性IP实例的标签信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPublicipTags
        :type request: :class:`huaweicloudsdkeip.v2.ShowPublicipTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowPublicipTagsResponse`
        """
        return self.show_publicip_tags_with_http_info(request)

    def show_publicip_tags_with_http_info(self, request):
        all_params = ['publicip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPublicipTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_publicip_async(self, request):
        """更新弹性公网IP

        更新弹性公网IP，将弹性公网IP跟一个网卡绑定或者解绑定，转换IP地址版本类型。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePublicip
        :type request: :class:`huaweicloudsdkeip.v2.UpdatePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.UpdatePublicipResponse`
        """
        return self.update_publicip_with_http_info(request)

    def update_publicip_with_http_info(self, request):
        all_params = ['publicip_id', 'publicip']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/publicips/{publicip_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_create_floating_ip_async(self, request):
        """创建浮动IP

        创建浮动IP的外部网络UUID，请使用GET /v2.0/networks?router:external&#x3D;True或neutron net-external-list方式获取。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for NeutronCreateFloatingIp
        :type request: :class:`huaweicloudsdkeip.v2.NeutronCreateFloatingIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronCreateFloatingIpResponse`
        """
        return self.neutron_create_floating_ip_with_http_info(request)

    def neutron_create_floating_ip_with_http_info(self, request):
        all_params = ['floatingip']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2.0/floatingips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateFloatingIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_delete_floating_ip_async(self, request):
        """删除浮动IP

        删除指定的浮动IP。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteFloatingIp
        :type request: :class:`huaweicloudsdkeip.v2.NeutronDeleteFloatingIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronDeleteFloatingIpResponse`
        """
        return self.neutron_delete_floating_ip_with_http_info(request)

    def neutron_delete_floating_ip_with_http_info(self, request):
        all_params = ['floatingip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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
            resource_path='/v2.0/floatingips/{floatingip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronDeleteFloatingIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_list_floating_ips_async(self, request):
        """查询浮动IP列表

        查询提交请求的租户有权限操作的所有浮动IP地址。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for NeutronListFloatingIps
        :type request: :class:`huaweicloudsdkeip.v2.NeutronListFloatingIpsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronListFloatingIpsResponse`
        """
        return self.neutron_list_floating_ips_with_http_info(request)

    def neutron_list_floating_ips_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'floating_ip_address', 'router_id', 'port_id', 'fixed_ip_address', 'tenant_id', 'floating_network_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'floating_ip_address' in local_var_params:
            query_params.append(('floating_ip_address', local_var_params['floating_ip_address']))
        if 'router_id' in local_var_params:
            query_params.append(('router_id', local_var_params['router_id']))
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))
        if 'fixed_ip_address' in local_var_params:
            query_params.append(('fixed_ip_address', local_var_params['fixed_ip_address']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'floating_network_id' in local_var_params:
            query_params.append(('floating_network_id', local_var_params['floating_network_id']))

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
            resource_path='/v2.0/floatingips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListFloatingIpsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_show_floating_ip_async(self, request):
        """查询浮动IP

        查询浮动IP详情，包括浮动IP状态，浮动IP所属路由器ID，浮动IP的外部网络ID等等。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for NeutronShowFloatingIp
        :type request: :class:`huaweicloudsdkeip.v2.NeutronShowFloatingIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronShowFloatingIpResponse`
        """
        return self.neutron_show_floating_ip_with_http_info(request)

    def neutron_show_floating_ip_with_http_info(self, request):
        all_params = ['floatingip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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
            resource_path='/v2.0/floatingips/{floatingip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowFloatingIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_update_floating_ip_async(self, request):
        """更新浮动IP

        更新浮动IP。
         更新时需在URL中给出浮动IP地址的ID。
         port_id 为空，则表示浮动IP从端口解绑。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for NeutronUpdateFloatingIp
        :type request: :class:`huaweicloudsdkeip.v2.NeutronUpdateFloatingIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronUpdateFloatingIpResponse`
        """
        return self.neutron_update_floating_ip_with_http_info(request)

    def neutron_update_floating_ip_with_http_info(self, request):
        all_params = ['floatingip_id', 'neutron_update_floating_ip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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
            resource_path='/v2.0/floatingips/{floatingip_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdateFloatingIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)

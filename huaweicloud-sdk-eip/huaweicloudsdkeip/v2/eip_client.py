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


class EipClient(Client):
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
        super(EipClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeip.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EipClient":
            raise TypeError("client type error, support client type is EipClient")

        return ClientBuilder(clazz)

    def add_publicips_into_shared_bandwidth(self, request):
        """共享带宽插入弹性公网IP

        共享带宽插入弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='AddPublicipsIntoSharedBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_shared_bandwidths(self, request):
        """批量创建共享带宽

        批量创建共享带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/batch-bandwidths',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateSharedBandwidthsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_bandwidth_to_period(self, request):
        """按需转包API

        租户按需转包接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeBandwidthToPeriod
        :type request: :class:`huaweicloudsdkeip.v2.ChangeBandwidthToPeriodRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ChangeBandwidthToPeriodResponse`
        """
        return self.change_bandwidth_to_period_with_http_info(request)

    def change_bandwidth_to_period_with_http_info(self, request):
        all_params = ['ip_change_to_period_request_body']
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
            resource_path='/v2.0/{project_id}/bandwidths/change-to-period',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeBandwidthToPeriodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_shared_bandwidth(self, request):
        """创建共享带宽

        创建共享带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/bandwidths',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSharedBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_shared_bandwidth(self, request):
        """删除共享带宽

        删除共享带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='DeleteSharedBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidth_pkg(self, request):
        """查询带宽加油包列表

        查询带宽加油包列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthPkg
        :type request: :class:`huaweicloudsdkeip.v2.ListBandwidthPkgRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListBandwidthPkgResponse`
        """
        return self.list_bandwidth_pkg_with_http_info(request)

    def list_bandwidth_pkg_with_http_info(self, request):
        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/bandwidthpkgs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBandwidthPkgResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidths(self, request):
        """查询带宽列表

        查询带宽列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ListBandwidthsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas(self, request):
        """查询配额接口

        查询配额
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_publicips_from_shared_bandwidth(self, request):
        """共享带宽移除弹性公网IP

        共享带宽移除弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='RemovePublicipsFromSharedBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bandwidth(self, request):
        """查询带宽

        查询带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ShowBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_bandwidth(self, request):
        """更新带宽

        更新带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='UpdateBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_pre_paid_bandwidth(self, request):
        """更新包周期带宽

        更新带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='UpdatePrePaidBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_publicip_tags(self, request):
        """批量创建弹性公网IP资源标签

        为指定的弹性公网IP资源实例批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreatePublicipTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_publicips(self, request):
        """批量创建弹性公网IP

        批量创建弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreatePublicips
        :type request: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipsResponse`
        """
        return self.batch_create_publicips_with_http_info(request)

    def batch_create_publicips_with_http_info(self, request):
        all_params = ['batch_create_publicips_v2_request_body']
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
            resource_path='/v2/{project_id}/batchpublicips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreatePublicipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_public_ip(self, request):
        """批量删除弹性公网IP

        批量删除弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeletePublicIp
        :type request: :class:`huaweicloudsdkeip.v2.BatchDeletePublicIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchDeletePublicIpResponse`
        """
        return self.batch_delete_public_ip_with_http_info(request)

    def batch_delete_public_ip_with_http_info(self, request):
        all_params = ['batch_delete_public_ip_request_body']
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
            resource_path='/v2/{project_id}/batchpublicips',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeletePublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_publicip_tags(self, request):
        """批量删除弹性公网IP资源标签

        为指定的弹性公网IP资源实例批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeletePublicipTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_disassociate_publicips(self, request):
        """批量解绑弹性公网IP

        批量解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDisassociatePublicips
        :type request: :class:`huaweicloudsdkeip.v2.BatchDisassociatePublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchDisassociatePublicipsResponse`
        """
        return self.batch_disassociate_publicips_with_http_info(request)

    def batch_disassociate_publicips_with_http_info(self, request):
        all_params = ['batch_disassociate_publicips_request_body']
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
            resource_path='/v2/{project_id}/batchpublicips',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDisassociatePublicipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_publicip_to_period(self, request):
        """按需转包接口

        租户按需转包接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangePublicipToPeriod
        :type request: :class:`huaweicloudsdkeip.v2.ChangePublicipToPeriodRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ChangePublicipToPeriodResponse`
        """
        return self.change_publicip_to_period_with_http_info(request)

    def change_publicip_to_period_with_http_info(self, request):
        all_params = ['ip_change_to_period_request_body']
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
            resource_path='/v2.0/{project_id}/publicips/change-to-period',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangePublicipToPeriodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_public_ip(self, request):
        """查询PublicIp数量

        查询PublicIp数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountPublicIp
        :type request: :class:`huaweicloudsdkeip.v2.CountPublicIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CountPublicIpResponse`
        """
        return self.count_public_ip_with_http_info(request)

    def count_public_ip_with_http_info(self, request):
        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elasticips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountPublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_public_ip_instance(self, request):
        """查询PublicIp实例数

        查询PublicIp实例数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountPublicIpInstance
        :type request: :class:`huaweicloudsdkeip.v2.CountPublicIpInstanceRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CountPublicIpInstanceResponse`
        """
        return self.count_public_ip_instance_with_http_info(request)

    def count_public_ip_instance_with_http_info(self, request):
        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/publicip/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountPublicIpInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_pre_paid_publicip(self, request):
        """申请包周期弹性公网IP

        申请包年包月的弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/publicips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePrePaidPublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_publicip(self, request):
        """申请弹性公网IP

        申请弹性公网IP，支持IPv4和IPv6。
         弹性公网IP（Elastic IP）提供独立的公网IP资源，包括公网IP地址与公网出口带宽服务。可以与弹性云服务器、裸金属服务器、虚拟IP、弹性负载均衡、NAT网关等资源灵活地绑定及解绑。拥有多种灵活的计费方式，可以满足各种业务场景的需要。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v1/{project_id}/publicips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_publicip_tag(self, request):
        """创建弹性公网IP资源标签

        给指定弹性IP资源实例增加标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePublicipTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_publicip(self, request):
        """删除弹性公网IP

        删除弹性公网IP,绑定状态eip不允许直接删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v1/{project_id}/publicips/{publicip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_publicip_tag(self, request):
        """删除弹性公网IP的标签

        删除指定弹性公网IP的标签信息。其中project_id是项目ID，publicip_id 是要操作的弹性公网IP的id。key是要删除标签的键。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='DeletePublicipTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_publicip_tags(self, request):
        """查询租户的弹性公网IP标签

        查询租户在指定区域和实例类型的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/publicips/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPublicipTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_publicips(self, request):
        """查询弹性公网IP列表

        查询弹性公网IP列表
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ListPublicipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_publicips_by_tags(self, request):
        """按标签查询弹性公网IP列表

        使用标签过滤弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/publicips/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPublicipsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_ip_type(self, request):
        """查询PublicIp类型

        查询PublicIp类型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPublicIpType
        :type request: :class:`huaweicloudsdkeip.v2.ShowPublicIpTypeRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowPublicIpTypeResponse`
        """
        return self.show_public_ip_type_with_http_info(request)

    def show_public_ip_type_with_http_info(self, request):
        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/publicip_types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublicIpTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_publicip(self, request):
        """查询弹性公网IP

        查询指定的弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v1/{project_id}/publicips/{publicip_id}',
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

    def show_publicip_tags(self, request):
        """查询弹性公网IP的标签

        查询指定弹性IP实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/{project_id}/publicips/{publicip_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublicipTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_publicip(self, request):
        """更新弹性公网IP

        更新弹性公网IP，将弹性公网IP跟一个网卡绑定或者解绑定，转换IP地址版本类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v1/{project_id}/publicips/{publicip_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePublicipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resources_job_detail(self, request):
        """查询Job状态接口

        查询Job状态接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourcesJobDetail
        :type request: :class:`huaweicloudsdkeip.v2.ShowResourcesJobDetailRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowResourcesJobDetailResponse`
        """
        return self.show_resources_job_detail_with_http_info(request)

    def show_resources_job_detail_with_http_info(self, request):
        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourcesJobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_create_floating_ip(self, request):
        """创建浮动IP

        创建浮动IP的外部网络UUID，请使用GET /v2.0/networks?router:external&#x3D;True或neutron net-external-list方式获取。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2.0/floatingips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronCreateFloatingIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_delete_floating_ip(self, request):
        """删除浮动IP

        删除指定的浮动IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='NeutronDeleteFloatingIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_list_floating_ips(self, request):
        """查询浮动IP列表

        查询提交请求的租户有权限操作的所有浮动IP地址。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            cname=cname,
            response_type='NeutronListFloatingIpsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_show_floating_ip(self, request):
        """查询浮动IP

        查询浮动IP详情，包括浮动IP状态，浮动IP所属路由器ID，浮动IP的外部网络ID等等。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='NeutronShowFloatingIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_update_floating_ip(self, request):
        """更新浮动IP

        更新浮动IP。
         更新时需在URL中给出浮动IP地址的ID。
         port_id 为空，则表示浮动IP从端口解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='NeutronUpdateFloatingIpResponse',
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

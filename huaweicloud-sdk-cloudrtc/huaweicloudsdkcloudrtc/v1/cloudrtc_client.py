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


class CloudRTCClient(Client):
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
        super(CloudRTCClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudrtc.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CloudRTCClient":
            raise TypeError("client type error, support client type is CloudRTCClient")

        return ClientBuilder(clazz)

    def list_rtc_abnormal_event_dimension(self, request):
        """查询异常事件用户分布

        查询指定APP下指定时间内的通话异常明细数据分布情况。
        
        最大查询跨度1天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcAbnormalEventDimension
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcAbnormalEventDimensionRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcAbnormalEventDimensionResponse`
        """
        return self.list_rtc_abnormal_event_dimension_with_http_info(request)

    def list_rtc_abnormal_event_dimension_with_http_info(self, request):
        all_params = ['app', 'room_id', 'dimension', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'dimension' in local_var_params:
            query_params.append(('dimension', local_var_params['dimension']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/rtc/data/abnormal-event/dimension',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcAbnormalEventDimensionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_abnormal_events(self, request):
        """查询用户异常体验事件

        查询指定APP下通话的异常明细数据。
        
        最大查询跨度1天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcAbnormalEvents
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcAbnormalEventsRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcAbnormalEventsResponse`
        """
        return self.list_rtc_abnormal_events_with_http_info(request)

    def list_rtc_abnormal_events_with_http_info(self, request):
        all_params = ['app', 'room_id', 'uid', 'start_time', 'end_time', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'uid' in local_var_params:
            query_params.append(('uid', local_var_params['uid']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/rtc/data/abnormal-events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcAbnormalEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_client_qos_details(self, request):
        """查询用户通话指标

        查询用户通话质量指标数据。
        
        可查询5天内的数据，mid 不为null，查询实时数据时，查询起止时间不超过24个小时，每次查询单个用户时，支持跨天查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcClientQosDetails
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcClientQosDetailsRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcClientQosDetailsResponse`
        """
        return self.list_rtc_client_qos_details_with_http_info(request)

    def list_rtc_client_qos_details_with_http_info(self, request):
        all_params = ['project_id', 'app_id', 'room_id', 'mid', 'start_time', 'end_time', 'authorization', 'x_sdk_date', 'x_project_id', 'domain', 'user_id', 'peer_id', 'stream_id', 'direction', 'time_type', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))
        if 'peer_id' in local_var_params:
            query_params.append(('peer_id', local_var_params['peer_id']))
        if 'stream_id' in local_var_params:
            query_params.append(('stream_id', local_var_params['stream_id']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'mid' in local_var_params:
            query_params.append(('mid', local_var_params['mid']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_type' in local_var_params:
            query_params.append(('time_type', local_var_params['time_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/client/qos/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcClientQosDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_history_quality(self, request):
        """查询历史质量

        查询质量指标过去每天的体验数据，可查询最近31天的数据。当天未结束，无法查询到当天的体验数据。
        
        最大查询跨度31天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcHistoryQuality
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcHistoryQualityRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcHistoryQualityResponse`
        """
        return self.list_rtc_history_quality_with_http_info(request)

    def list_rtc_history_quality_with_http_info(self, request):
        all_params = ['project_id', 'app', 'metric', 'authorization', 'x_sdk_date', 'x_project_id', 'start_date', 'end_date']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))
            collection_formats['metric'] = 'csv'
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/history/quality',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcHistoryQualityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_history_scale(self, request):
        """查询历史规模

        查询指标过去每天的规模数量，可查询最近31天的数据。当天未结束，无法查到当天的房间数与用户数。
        
        最大查询跨度31天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcHistoryScale
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcHistoryScaleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcHistoryScaleResponse`
        """
        return self.list_rtc_history_scale_with_http_info(request)

    def list_rtc_history_scale_with_http_info(self, request):
        all_params = ['project_id', 'app', 'metric', 'authorization', 'x_sdk_date', 'x_project_id', 'start_date', 'end_date']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))
            collection_formats['metric'] = 'csv'
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/history/scale',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcHistoryScaleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_history_usage(self, request):
        """查询用量

        查询过去的某一时间段内各种业务的用量数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcHistoryUsage
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcHistoryUsageRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcHistoryUsageResponse`
        """
        return self.list_rtc_history_usage_with_http_info(request)

    def list_rtc_history_usage_with_http_info(self, request):
        all_params = ['project_id', 'app', 'metric', 'start_date', 'end_date', 'authorization', 'x_sdk_date', 'x_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/history/usage',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcHistoryUsageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_realtime_network(self, request):
        """查询实时网络

        获取实时网络数据相关指标在某一时间段内每分钟的统计数据。
        
        最大查询跨度1天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcRealtimeNetwork
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRealtimeNetworkRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRealtimeNetworkResponse`
        """
        return self.list_rtc_realtime_network_with_http_info(request)

    def list_rtc_realtime_network_with_http_info(self, request):
        all_params = ['project_id', 'app', 'metric', 'sdk_type', 'authorization', 'x_sdk_date', 'x_project_id', 'room_id', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))
        if 'sdk_type' in local_var_params:
            query_params.append(('sdk_type', local_var_params['sdk_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/realtime/network',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcRealtimeNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_realtime_quality(self, request):
        """查询实时质量数据

        获取实时质量数据的相关指标在某一时间段内每分钟的统计数据。
        
        最大查询跨度1天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcRealtimeQuality
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRealtimeQualityRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRealtimeQualityResponse`
        """
        return self.list_rtc_realtime_quality_with_http_info(request)

    def list_rtc_realtime_quality_with_http_info(self, request):
        all_params = ['project_id', 'app', 'metric', 'sdk_type', 'authorization', 'x_sdk_date', 'x_project_id', 'room_id', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))
        if 'sdk_type' in local_var_params:
            query_params.append(('sdk_type', local_var_params['sdk_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/realtime/quality',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcRealtimeQualityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_realtime_scale(self, request):
        """查询实时规模

        获取规模相关的指标在某一时间段内每分钟的统计数据。
        
        最大查询跨度1天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcRealtimeScale
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRealtimeScaleRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRealtimeScaleResponse`
        """
        return self.list_rtc_realtime_scale_with_http_info(request)

    def list_rtc_realtime_scale_with_http_info(self, request):
        all_params = ['project_id', 'app', 'metric', 'authorization', 'x_sdk_date', 'x_project_id', 'room_id', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/realtime/scale',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcRealtimeScaleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_realtime_scale_dimension(self, request):
        """查询实时规模分布

        对规模相关的数据，根据指定维度按在线用户数排名，获取规模相关的指标在指定维度下的统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcRealtimeScaleDimension
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRealtimeScaleDimensionRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRealtimeScaleDimensionResponse`
        """
        return self.list_rtc_realtime_scale_dimension_with_http_info(request)

    def list_rtc_realtime_scale_dimension_with_http_info(self, request):
        all_params = ['project_id', 'app', 'metric', 'dimension', 'time', 'authorization', 'x_sdk_date', 'x_project_id', 'room_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))
        if 'dimension' in local_var_params:
            query_params.append(('dimension', local_var_params['dimension']))
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/realtime/scale/dimension',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcRealtimeScaleDimensionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_room_list(self, request):
        """查询房间列表

        指定事件范围查询这段期间创建的房间列表。
        
        最大查询跨度90天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcRoomList
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRoomListRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcRoomListResponse`
        """
        return self.list_rtc_room_list_with_http_info(request)

    def list_rtc_room_list_with_http_info(self, request):
        all_params = ['project_id', 'app', 'authorization', 'x_sdk_date', 'x_project_id', 'room_id', 'state', 'start_time', 'end_time', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/rooms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcRoomListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rtc_user_list(self, request):
        """查询用户列表

        指定事件范围查询这段期间加入房间的用户列表。
        
        最大查询跨度90天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRtcUserList
        :type request: :class:`huaweicloudsdkcloudrtc.v1.ListRtcUserListRequest`
        :rtype: :class:`huaweicloudsdkcloudrtc.v1.ListRtcUserListResponse`
        """
        return self.list_rtc_user_list_with_http_info(request)

    def list_rtc_user_list_with_http_info(self, request):
        all_params = ['project_id', 'app', 'authorization', 'x_sdk_date', 'x_project_id', 'room_id', 'uid', 'nickname', 'region', 'isp', 'state', 'start_time', 'end_time', 'limit', 'offset', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'uid' in local_var_params:
            query_params.append(('uid', local_var_params['uid']))
        if 'nickname' in local_var_params:
            query_params.append(('nickname', local_var_params['nickname']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'csv'
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_project_id' in local_var_params:
            header_params['X-Project-Id'] = local_var_params['x_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rtc/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRtcUserListResponse',
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

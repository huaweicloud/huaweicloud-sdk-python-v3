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


class LiveClient(Client):
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
        super(LiveClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklive.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "LiveClient":
            raise TypeError("client type error, support client type is LiveClient")

        return ClientBuilder(clazz)

    def list_area_detail(self, request):
        """查询直播各区域指标分布接口

        查询直播全球区域维度的详细数据接口。
        
        最大查询跨度1天，最大查询周期90天。
        
        支持查询当天，当前数据延时少于5分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAreaDetail
        :type request: :class:`huaweicloudsdklive.v2.ListAreaDetailRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListAreaDetailResponse`
        """
        return self.list_area_detail_with_http_info(request)

    def list_area_detail_with_http_info(self, request):
        all_params = ['start_time', 'end_time', 'play_domains', 'area', 'metric', 'app', 'stream', 'interval', 'isp', 'protocol']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'play_domains' in local_var_params:
            query_params.append(('play_domains', local_var_params['play_domains']))
            collection_formats['play_domains'] = 'csv'
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'area' in local_var_params:
            query_params.append(('area', local_var_params['area']))
            collection_formats['area'] = 'csv'
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/area/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAreaDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidth_detail(self, request):
        """查询播放带宽趋势接口

        查询播放域名带宽数据。
        
        如果不传入域名，则查询租户下所有播放域名的带宽数据。
        
        当查询租户级别带宽数据时，参数app、stream不生效。
        
        最大查询跨度31天，最大查询周期一年。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthDetail
        :type request: :class:`huaweicloudsdklive.v2.ListBandwidthDetailRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListBandwidthDetailResponse`
        """
        return self.list_bandwidth_detail_with_http_info(request)

    def list_bandwidth_detail_with_http_info(self, request):
        all_params = ['play_domains', 'app', 'stream', 'country', 'region', 'isp', 'protocol', 'interval', 'start_time', 'end_time', 'service_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domains' in local_var_params:
            query_params.append(('play_domains', local_var_params['play_domains']))
            collection_formats['play_domains'] = 'csv'
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'country' in local_var_params:
            query_params.append(('country', local_var_params['country']))
            collection_formats['country'] = 'csv'
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/bandwidth/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBandwidthDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_bandwidth_peak(self, request):
        """查询播放带宽峰值接口

        查询指定时间范围内播放带宽峰值。
        
        如果不传入域名，则查询租户下所有播放域名的带宽峰值。
        
        当查询租户级别带宽数据时，参数app、stream不生效。
        
        最大查询跨度31天，最大查询周期一年。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainBandwidthPeak
        :type request: :class:`huaweicloudsdklive.v2.ListDomainBandwidthPeakRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListDomainBandwidthPeakResponse`
        """
        return self.list_domain_bandwidth_peak_with_http_info(request)

    def list_domain_bandwidth_peak_with_http_info(self, request):
        all_params = ['play_domains', 'app', 'stream', 'region', 'isp', 'protocol', 'start_time', 'end_time', 'service_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domains' in local_var_params:
            query_params.append(('play_domains', local_var_params['play_domains']))
            collection_formats['play_domains'] = 'csv'
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/bandwidth/peak',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainBandwidthPeakResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_traffic_detail(self, request):
        """查询播放流量趋势接口

        查询播放域名流量数据。
        
        如果不传入域名，则查询租户下所有播放域名的流量数据。
        
        当查询租户级别流量数据时，参数app、stream不生效。
        
        最大查询跨度31天，最大查询周期一年。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainTrafficDetail
        :type request: :class:`huaweicloudsdklive.v2.ListDomainTrafficDetailRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListDomainTrafficDetailResponse`
        """
        return self.list_domain_traffic_detail_with_http_info(request)

    def list_domain_traffic_detail_with_http_info(self, request):
        all_params = ['play_domains', 'app', 'stream', 'region', 'isp', 'protocol', 'interval', 'start_time', 'end_time', 'service_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domains' in local_var_params:
            query_params.append(('play_domains', local_var_params['play_domains']))
            collection_formats['play_domains'] = 'csv'
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/traffic/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainTrafficDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_traffic_summary(self, request):
        """查询播放流量汇总接口

        查询指定时间范围内流量汇总量。
        
        如果不传入域名，则查询租户下所有播放域名的流量汇总量。
        
        当查询租户级别流量数据时，参数app、stream不生效。
        
        最大查询跨度31天，最大查询周期一年。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainTrafficSummary
        :type request: :class:`huaweicloudsdklive.v2.ListDomainTrafficSummaryRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListDomainTrafficSummaryResponse`
        """
        return self.list_domain_traffic_summary_with_http_info(request)

    def list_domain_traffic_summary_with_http_info(self, request):
        all_params = ['play_domains', 'app', 'stream', 'region', 'isp', 'protocol', 'start_time', 'end_time', 'service_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domains' in local_var_params:
            query_params.append(('play_domains', local_var_params['play_domains']))
            collection_formats['play_domains'] = 'csv'
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/traffic/summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainTrafficSummaryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_history_streams(self, request):
        """查询历史推流列表接口

        查询历史推流列表。
        
        不能查询现推流。
        
        最大查询跨度1天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistoryStreams
        :type request: :class:`huaweicloudsdklive.v2.ListHistoryStreamsRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListHistoryStreamsResponse`
        """
        return self.list_history_streams_with_http_info(request)

    def list_history_streams_with_http_info(self, request):
        all_params = ['domain', 'app', 'stream', 'start_time', 'end_time', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/history/streams',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHistoryStreamsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_query_http_code(self, request):
        """查询直播拉流HTTP状态码接口

        查询直播拉流HTTP状态码接口。  获取加速域名1分钟粒度的HTTP返回码  最大查询跨度不能超过24小时，最大查询周期7天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryHttpCode
        :type request: :class:`huaweicloudsdklive.v2.ListQueryHttpCodeRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListQueryHttpCodeResponse`
        """
        return self.list_query_http_code_with_http_info(request)

    def list_query_http_code_with_http_info(self, request):
        all_params = ['play_domains', 'code', 'region', 'isp', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domains' in local_var_params:
            query_params.append(('play_domains', local_var_params['play_domains']))
            collection_formats['play_domains'] = 'csv'
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))
            collection_formats['code'] = 'csv'
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/httpcodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQueryHttpCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_data(self, request):
        """查询录制用量接口

        查询直播租户每小时录制的最大并发数，计算1小时内每分钟的并发总路数，取最大值做为统计值。  最大查询跨度31天，最大查询周期90天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordData
        :type request: :class:`huaweicloudsdklive.v2.ListRecordDataRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListRecordDataResponse`
        """
        return self.list_record_data_with_http_info(request)

    def list_record_data_with_http_info(self, request):
        all_params = ['publish_domain', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/record',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRecordDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_snapshot_data(self, request):
        """查询截图用量接口

        查询直播域名每小时的截图数量。  最大查询跨度31天，最大查询周期90天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshotData
        :type request: :class:`huaweicloudsdklive.v2.ListSnapshotDataRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListSnapshotDataResponse`
        """
        return self.list_snapshot_data_with_http_info(request)

    def list_snapshot_data_with_http_info(self, request):
        all_params = ['publish_domain', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/snapshot',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSnapshotDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transcode_data(self, request):
        """查询转码用量接口

        查询直播域名每小时的转码时长数据。  最大查询跨度31天，最大查询周期90天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTranscodeData
        :type request: :class:`huaweicloudsdklive.v2.ListTranscodeDataRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListTranscodeDataResponse`
        """
        return self.list_transcode_data_with_http_info(request)

    def list_transcode_data_with_http_info(self, request):
        all_params = ['publish_domain', 'stream', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/transcode',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTranscodeDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_users_of_stream(self, request):
        """查询观众趋势接口

        查询观众趋势。  最大查询跨度31天，最大查询周期一年。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsersOfStream
        :type request: :class:`huaweicloudsdklive.v2.ListUsersOfStreamRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListUsersOfStreamResponse`
        """
        return self.list_users_of_stream_with_http_info(request)

    def list_users_of_stream_with_http_info(self, request):
        all_params = ['play_domain', 'app', 'stream', 'isp', 'country', 'region', 'protocol', 'interval', 'start_time', 'end_time', 'service_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domain' in local_var_params:
            query_params.append(('play_domain', local_var_params['play_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'country' in local_var_params:
            query_params.append(('country', local_var_params['country']))
            collection_formats['country'] = 'csv'
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/user',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUsersOfStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_stream_count(self, request):
        """查询域名维度推流路数接口

        查询域名维度推流路数接口。  最大查询跨度31天，最大查询周期1年。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStreamCount
        :type request: :class:`huaweicloudsdklive.v2.ShowStreamCountRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ShowStreamCountResponse`
        """
        return self.show_stream_count_with_http_info(request)

    def show_stream_count_with_http_info(self, request):
        all_params = ['publish_domains', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domains' in local_var_params:
            query_params.append(('publish_domains', local_var_params['publish_domains']))
            collection_formats['publish_domains'] = 'csv'
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream-count',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStreamCountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_stream_portrait(self, request):
        """查询播放画像信息接口

        查询播放画像信息。  最大查询跨度1天，最大查询周期31天。
        不统计协议为HLS的播放时长（play_duration）信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStreamPortrait
        :type request: :class:`huaweicloudsdklive.v2.ShowStreamPortraitRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ShowStreamPortraitResponse`
        """
        return self.show_stream_portrait_with_http_info(request)

    def show_stream_portrait_with_http_info(self, request):
        all_params = ['play_domain', 'time', 'stream']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domain' in local_var_params:
            query_params.append(('play_domain', local_var_params['play_domain']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream-portraits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStreamPortraitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_up_bandwidth(self, request):
        """查询上行带宽数据接口

        查询上行带宽数据。  最大查询跨度31天，最大查询周期1年。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpBandwidth
        :type request: :class:`huaweicloudsdklive.v2.ShowUpBandwidthRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ShowUpBandwidthResponse`
        """
        return self.show_up_bandwidth_with_http_info(request)

    def show_up_bandwidth_with_http_info(self, request):
        all_params = ['publish_domains', 'app', 'stream', 'region', 'isp', 'interval', 'type', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domains' in local_var_params:
            query_params.append(('publish_domains', local_var_params['publish_domains']))
            collection_formats['publish_domains'] = 'csv'
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'csv'
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/up-bandwidth/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUpBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_single_stream_bitrate(self, request):
        """查询推流码率数据接口

        查询推流监控码率数据接口。
        
        最大查询跨度1天，最大查询周期1个月。
        
        返回的码率数据列表粒度为1秒钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSingleStreamBitrate
        :type request: :class:`huaweicloudsdklive.v2.ListSingleStreamBitrateRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListSingleStreamBitrateResponse`
        """
        return self.list_single_stream_bitrate_with_http_info(request)

    def list_single_stream_bitrate_with_http_info(self, request):
        all_params = ['domain', 'app', 'stream', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream/bitrate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSingleStreamBitrateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_single_stream_detail(self, request):
        """查询流监控数据接口

        查询流监控数据接口，包括帧率码率断流情况。
        
        最大查询跨度1天，最大查询周期1个月。
        
        返回的码率数据列表粒度为1秒钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSingleStreamDetail
        :type request: :class:`huaweicloudsdklive.v2.ListSingleStreamDetailRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListSingleStreamDetailResponse`
        """
        return self.list_single_stream_detail_with_http_info(request)

    def list_single_stream_detail_with_http_info(self, request):
        all_params = ['publish_domain', 'app', 'stream', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSingleStreamDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_single_stream_framerate(self, request):
        """查询推流帧率数据接口

        查询推流帧率数据接口。
        
        最大查询跨度1天，最大查询周期1个月。
        
        返回的帧率数据列表粒度为1秒钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSingleStreamFramerate
        :type request: :class:`huaweicloudsdklive.v2.ListSingleStreamFramerateRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListSingleStreamFramerateResponse`
        """
        return self.list_single_stream_framerate_with_http_info(request)

    def list_single_stream_framerate_with_http_info(self, request):
        all_params = ['domain', 'app', 'stream', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream/framerate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSingleStreamFramerateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_up_stream_detail(self, request):
        """查询CDN上行推流质量数据接口

        查询CDN上行推流质量数据。
        
        最大查询跨度1天，最大查询周期7天。
        
        返回的CDN上行推流质量数据列表粒度为1分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUpStreamDetail
        :type request: :class:`huaweicloudsdklive.v2.ListUpStreamDetailRequest`
        :rtype: :class:`huaweicloudsdklive.v2.ListUpStreamDetailResponse`
        """
        return self.list_up_stream_detail_with_http_info(request)

    def list_up_stream_detail_with_http_info(self, request):
        all_params = ['publish_domain', 'app', 'stream', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/up-stream/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUpStreamDetailResponse',
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

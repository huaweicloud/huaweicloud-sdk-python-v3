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


class LiveAPIAsyncClient(Client):
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
        super(LiveAPIAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklive.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def list_bandwidth_detail_v2_async(self, request):
        """查询播放带宽趋势接口

        查询播放域名带宽数据。  最大查询跨度31天，最大查询周期90天。

        :param ListBandwidthDetailV2Request request
        :return: ListBandwidthDetailV2Response
        """
        return self.list_bandwidth_detail_v2_with_http_info(request)

    def list_bandwidth_detail_v2_with_http_info(self, request):
        """查询播放带宽趋势接口

        查询播放域名带宽数据。  最大查询跨度31天，最大查询周期90天。

        :param ListBandwidthDetailV2Request request
        :return: ListBandwidthDetailV2Response
        """

        all_params = ['play_domains', 'app', 'stream', 'region', 'isp', 'interval', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/bandwidth/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBandwidthDetailV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_domain_bandwidth_summary_v2_async(self, request):
        """查询播放带宽峰值接口

        查询指定时间范围内播放带宽峰值。  最大查询跨度31天，最大查询周期90天。

        :param ListDomainBandwidthSummaryV2Request request
        :return: ListDomainBandwidthSummaryV2Response
        """
        return self.list_domain_bandwidth_summary_v2_with_http_info(request)

    def list_domain_bandwidth_summary_v2_with_http_info(self, request):
        """查询播放带宽峰值接口

        查询指定时间范围内播放带宽峰值。  最大查询跨度31天，最大查询周期90天。

        :param ListDomainBandwidthSummaryV2Request request
        :return: ListDomainBandwidthSummaryV2Response
        """

        all_params = ['play_domains', 'app', 'stream', 'region', 'isp', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/bandwidth/peak',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDomainBandwidthSummaryV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_domain_traffic_detail_v2_async(self, request):
        """查询播放流量趋势接口

        查询播放域名流量数据。  最大查询跨度31天，最大查询周期90天。

        :param ListDomainTrafficDetailV2Request request
        :return: ListDomainTrafficDetailV2Response
        """
        return self.list_domain_traffic_detail_v2_with_http_info(request)

    def list_domain_traffic_detail_v2_with_http_info(self, request):
        """查询播放流量趋势接口

        查询播放域名流量数据。  最大查询跨度31天，最大查询周期90天。

        :param ListDomainTrafficDetailV2Request request
        :return: ListDomainTrafficDetailV2Response
        """

        all_params = ['play_domains', 'app', 'stream', 'region', 'isp', 'interval', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/traffic/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDomainTrafficDetailV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_domain_traffic_summary_v2_async(self, request):
        """查询播放流量汇总接口

        查询指定时间范围内流量汇总量。  最大查询跨度31天，最大查询周期90天。

        :param ListDomainTrafficSummaryV2Request request
        :return: ListDomainTrafficSummaryV2Response
        """
        return self.list_domain_traffic_summary_v2_with_http_info(request)

    def list_domain_traffic_summary_v2_with_http_info(self, request):
        """查询播放流量汇总接口

        查询指定时间范围内流量汇总量。  最大查询跨度31天，最大查询周期90天。

        :param ListDomainTrafficSummaryV2Request request
        :return: ListDomainTrafficSummaryV2Response
        """

        all_params = ['play_domains', 'app', 'stream', 'region', 'isp', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/traffic/summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDomainTrafficSummaryV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_history_streams_v2_async(self, request):
        """查询历史推流列表接口

        查询历史推流列表。  最大查询跨度1天，最大查询周期7天。

        :param ListHistoryStreamsV2Request request
        :return: ListHistoryStreamsV2Response
        """
        return self.list_history_streams_v2_with_http_info(request)

    def list_history_streams_v2_with_http_info(self, request):
        """查询历史推流列表接口

        查询历史推流列表。  最大查询跨度1天，最大查询周期7天。

        :param ListHistoryStreamsV2Request request
        :return: ListHistoryStreamsV2Response
        """

        all_params = ['domain', 'app', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/history/streams',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHistoryStreamsV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_query_http_code_async(self, request):
        """查询直播拉流HTTP状态码接口

        查询直播拉流HTTP状态码接口。  获取加速域名1分钟粒度的HTTP返回码  最大查询跨度不能超过24小时，最大查询周期7天。

        :param ListQueryHttpCodeRequest request
        :return: ListQueryHttpCodeResponse
        """
        return self.list_query_http_code_with_http_info(request)

    def list_query_http_code_with_http_info(self, request):
        """查询直播拉流HTTP状态码接口

        查询直播拉流HTTP状态码接口。  获取加速域名1分钟粒度的HTTP返回码  最大查询跨度不能超过24小时，最大查询周期7天。

        :param ListQueryHttpCodeRequest request
        :return: ListQueryHttpCodeResponse
        """

        all_params = ['play_domains', 'code', 'region', 'isp', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/httpcodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQueryHttpCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_record_data_v2_async(self, request):
        """查询录制用量接口

        查询直播租户每小时录制的最大并发数，计算1小时内每分钟的并发总路数，取最大值做为统计值。  最大查询跨度31天，最大查询周期90天。

        :param ListRecordDataV2Request request
        :return: ListRecordDataV2Response
        """
        return self.list_record_data_v2_with_http_info(request)

    def list_record_data_v2_with_http_info(self, request):
        """查询录制用量接口

        查询直播租户每小时录制的最大并发数，计算1小时内每分钟的并发总路数，取最大值做为统计值。  最大查询跨度31天，最大查询周期90天。

        :param ListRecordDataV2Request request
        :return: ListRecordDataV2Response
        """

        all_params = ['start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/record',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRecordDataV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_single_stream_bitrate_v2_async(self, request):
        """查询推流码率数据接口

        查询推流监控码率数据接口。  最大查询跨度6小时，最大查询周期7天。

        :param ListSingleStreamBitrateV2Request request
        :return: ListSingleStreamBitrateV2Response
        """
        return self.list_single_stream_bitrate_v2_with_http_info(request)

    def list_single_stream_bitrate_v2_with_http_info(self, request):
        """查询推流码率数据接口

        查询推流监控码率数据接口。  最大查询跨度6小时，最大查询周期7天。

        :param ListSingleStreamBitrateV2Request request
        :return: ListSingleStreamBitrateV2Response
        """

        all_params = ['domain', 'app', 'stream', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream/bitrate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSingleStreamBitrateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_single_stream_framerate_v2_async(self, request):
        """查询推流帧率数据接口

        查询推流帧率数据接口。  最大查询跨度6小时，最大查询周期7天。

        :param ListSingleStreamFramerateV2Request request
        :return: ListSingleStreamFramerateV2Response
        """
        return self.list_single_stream_framerate_v2_with_http_info(request)

    def list_single_stream_framerate_v2_with_http_info(self, request):
        """查询推流帧率数据接口

        查询推流帧率数据接口。  最大查询跨度6小时，最大查询周期7天。

        :param ListSingleStreamFramerateV2Request request
        :return: ListSingleStreamFramerateV2Response
        """

        all_params = ['domain', 'app', 'stream', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream/framerate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSingleStreamFramerateV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_snapshot_data_v2_async(self, request):
        """查询截图用量接口

        查询直播域名每小时的截图数量。  最大查询跨度31天，最大查询周期90天。

        :param ListSnapshotDataV2Request request
        :return: ListSnapshotDataV2Response
        """
        return self.list_snapshot_data_v2_with_http_info(request)

    def list_snapshot_data_v2_with_http_info(self, request):
        """查询截图用量接口

        查询直播域名每小时的截图数量。  最大查询跨度31天，最大查询周期90天。

        :param ListSnapshotDataV2Request request
        :return: ListSnapshotDataV2Response
        """

        all_params = ['publish_domain', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/snapshot',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSnapshotDataV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_transcode_data_v2_async(self, request):
        """查询转码用量接口

        查询直播域名每小时的转码时长数据。  最大查询跨度31天，最大查询周期90天。

        :param ListTranscodeDataV2Request request
        :return: ListTranscodeDataV2Response
        """
        return self.list_transcode_data_v2_with_http_info(request)

    def list_transcode_data_v2_with_http_info(self, request):
        """查询转码用量接口

        查询直播域名每小时的转码时长数据。  最大查询跨度31天，最大查询周期90天。

        :param ListTranscodeDataV2Request request
        :return: ListTranscodeDataV2Response
        """

        all_params = ['publish_domain', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/transcode',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTranscodeDataV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_users_of_stream_v2_async(self, request):
        """查询观众趋势接口

        查询观众趋势。  最大查询跨度7天，最大查询周期90天。

        :param ListUsersOfStreamV2Request request
        :return: ListUsersOfStreamV2Response
        """
        return self.list_users_of_stream_v2_with_http_info(request)

    def list_users_of_stream_v2_with_http_info(self, request):
        """查询观众趋势接口

        查询观众趋势。  最大查询跨度7天，最大查询周期90天。

        :param ListUsersOfStreamV2Request request
        :return: ListUsersOfStreamV2Response
        """

        all_params = ['play_domain', 'app', 'stream', 'isp', 'region', 'interval', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
            collection_formats['region'] = 'csv'
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/user',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUsersOfStreamV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_stream_count_v2_async(self, request):
        """查询域名维度推流路数接口

        查询域名维度推流路数接口。  最大查询跨度31天，最大查询周期90天。

        :param ShowStreamCountV2Request request
        :return: ShowStreamCountV2Response
        """
        return self.show_stream_count_v2_with_http_info(request)

    def show_stream_count_v2_with_http_info(self, request):
        """查询域名维度推流路数接口

        查询域名维度推流路数接口。  最大查询跨度31天，最大查询周期90天。

        :param ShowStreamCountV2Request request
        :return: ShowStreamCountV2Response
        """

        all_params = ['publish_domains', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream-count',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowStreamCountV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_stream_portrait_async(self, request):
        """查询播放画像信息接口

        查询播放画像信息。  最大查询跨度1天，最大查询周期31天。

        :param ShowStreamPortraitRequest request
        :return: ShowStreamPortraitResponse
        """
        return self.show_stream_portrait_with_http_info(request)

    def show_stream_portrait_with_http_info(self, request):
        """查询播放画像信息接口

        查询播放画像信息。  最大查询跨度1天，最大查询周期31天。

        :param ShowStreamPortraitRequest request
        :return: ShowStreamPortraitResponse
        """

        all_params = ['play_domain', 'time', 'stream']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/stream-portraits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowStreamPortraitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_up_bandwidth_v2_async(self, request):
        """查询上行带宽数据接口

        查询上行带宽数据。  最大查询跨度31天，最大查询周期90天。

        :param ShowUpBandwidthV2Request request
        :return: ShowUpBandwidthV2Response
        """
        return self.show_up_bandwidth_v2_with_http_info(request)

    def show_up_bandwidth_v2_with_http_info(self, request):
        """查询上行带宽数据接口

        查询上行带宽数据。  最大查询跨度31天，最大查询周期90天。

        :param ShowUpBandwidthV2Request request
        :return: ShowUpBandwidthV2Response
        """

        all_params = ['publish_domains', 'app', 'stream', 'region', 'isp', 'interval', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id"]


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/stats/up-bandwidth/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUpBandwidthV2Response',
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

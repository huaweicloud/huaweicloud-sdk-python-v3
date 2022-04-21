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


class AomClient(Client):
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
        super(AomClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaom.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "AomClient":
            raise TypeError("client type error, support client type is AomClient")

        return ClientBuilder(clazz)

    def add_alarm_rule(self, request):
        """添加阈值规则

        该接口用于添加一条阈值规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.AddAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddAlarmRuleResponse`
        """
        return self.add_alarm_rule_with_http_info(request)

    def add_alarm_rule_with_http_info(self, request):
        all_params = ['add_alarm_rule_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_metric_data(self, request):
        """添加监控数据

        该接口用于向服务端添加一条或多条监控数据。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddMetricData
        :type request: :class:`huaweicloudsdkaom.v2.AddMetricDataRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddMetricDataResponse`
        """
        return self.add_metric_data_with_http_info(request)

    def add_metric_data_with_http_info(self, request):
        all_params = ['metric_data_param']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/ams/report/metricdata',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddMetricDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_or_update_service_discovery_rules(self, request):
        """添加或修改服务发现规则

        该接口用于添加或修改一条或多条服务发现规则。同一projectid下可添加的规则上限为100条。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddOrUpdateServiceDiscoveryRules
        :type request: :class:`huaweicloudsdkaom.v2.AddOrUpdateServiceDiscoveryRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddOrUpdateServiceDiscoveryRulesResponse`
        """
        return self.add_or_update_service_discovery_rules_with_http_info(request)

    def add_or_update_service_discovery_rules_with_http_info(self, request):
        all_params = ['app_rules']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/inv/servicediscoveryrules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddOrUpdateServiceDiscoveryRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_events(self, request):
        """统计事件告警信息

        该接口用于分段统计指定条件下的事件、告警。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CountEvents
        :type request: :class:`huaweicloudsdkaom.v2.CountEventsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.CountEventsResponse`
        """
        return self.count_events_with_http_info(request)

    def count_events_with_http_info(self, request):
        all_params = ['count_events_request_body', 'type']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/events/statistic',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CountEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alarm_rule(self, request):
        """删除阈值规则

        该接口用于删除阈值规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.DeleteAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteAlarmRuleResponse`
        """
        return self.delete_alarm_rule_with_http_info(request)

    def delete_alarm_rule_with_http_info(self, request):
        all_params = ['alarm_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'alarm_rule_id' in local_var_params:
            path_params['alarm_rule_id'] = local_var_params['alarm_rule_id']

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
            resource_path='/v2/{project_id}/alarm-rules/{alarm_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alarm_rules(self, request):
        """批量删除阈值规则

        批量删除阈值规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAlarmRules
        :type request: :class:`huaweicloudsdkaom.v2.DeleteAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteAlarmRulesResponse`
        """
        return self.delete_alarm_rules_with_http_info(request)

    def delete_alarm_rules_with_http_info(self, request):
        all_params = ['alarm_rules']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-rules/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAlarmRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def deleteservice_discovery_rules(self, request):
        """删除服务发现规则

        该接口用于删除服务发现规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteserviceDiscoveryRules
        :type request: :class:`huaweicloudsdkaom.v2.DeleteserviceDiscoveryRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteserviceDiscoveryRulesResponse`
        """
        return self.deleteservice_discovery_rules_with_http_info(request)

    def deleteservice_discovery_rules_with_http_info(self, request):
        all_params = ['app_rules_ids']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_rules_ids' in local_var_params:
            query_params.append(('appRulesIds', local_var_params['app_rules_ids']))
            collection_formats['appRulesIds'] = 'csv'

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
            resource_path='/v1/{project_id}/inv/servicediscoveryrules',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteserviceDiscoveryRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_rule(self, request):
        """查询阈值规则列表

        该接口用于查询阈值规则列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.ListAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListAlarmRuleResponse`
        """
        return self.list_alarm_rule_with_http_info(request)

    def list_alarm_rule_with_http_info(self, request):
        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v2/{project_id}/alarm-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_events(self, request):
        """查询事件告警信息

        该接口用于查询对应用户的事件、告警。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkaom.v2.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListEventsResponse`
        """
        return self.list_events_with_http_info(request)

    def list_events_with_http_info(self, request):
        all_params = ['list_events_request_body', 'type']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_log_items(self, request):
        """查询日志

        该接口用于查询不同维度(例如集群、IP、应用等)下的日志内容，支持分页查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLogItems
        :type request: :class:`huaweicloudsdkaom.v2.ListLogItemsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListLogItemsResponse`
        """
        return self.list_log_items_with_http_info(request)

    def list_log_items_with_http_info(self, request):
        all_params = ['type', 'list_log_items_request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/als/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLogItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_metric_items(self, request):
        """查询指标

        该接口用于查询系统当前可监控的指标列表，可以指定指标命名空间、指标名称、维度、所属资源的编号（格式为：resType_resId），分页查询的起始位置和返回的最大记录条数。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMetricItems
        :type request: :class:`huaweicloudsdkaom.v2.ListMetricItemsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListMetricItemsResponse`
        """
        return self.list_metric_items_with_http_info(request)

    def list_metric_items_with_http_info(self, request):
        all_params = ['query_item_param', 'type', 'limit', 'start']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))

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
            resource_path='/v1/{project_id}/ams/metrics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMetricItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sample(self, request):
        """查询时序数据

        该接口用于查询指定时间范围内的监控时序数据，可以通过参数指定需要查询的数据维度，数据周期等。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSample
        :type request: :class:`huaweicloudsdkaom.v2.ListSampleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListSampleResponse`
        """
        return self.list_sample_with_http_info(request)

    def list_sample_with_http_info(self, request):
        all_params = ['list_sample_request_body', 'fill_value']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fill_value' in local_var_params:
            query_params.append(('fill_value', local_var_params['fill_value']))

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
            resource_path='/v2/{project_id}/samples',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSampleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_series(self, request):
        """查询时间序列

        该接口用于查询系统当前可监控的时间序列列表，可以指定时间序列命名空间、名称、维度、所属资源的编号（格式为：resType_resId），分页查询的起始位置和返回的最大记录条数。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSeries
        :type request: :class:`huaweicloudsdkaom.v2.ListSeriesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListSeriesResponse`
        """
        return self.list_series_with_http_info(request)

    def list_series_with_http_info(self, request):
        all_params = ['list_series_request_body', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v2/{project_id}/series',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSeriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_discovery_rules(self, request):
        """查询系统中已有服务发现规则

        该接口用于查询系统当前已存在的服务发现规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListServiceDiscoveryRules
        :type request: :class:`huaweicloudsdkaom.v2.ListServiceDiscoveryRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListServiceDiscoveryRulesResponse`
        """
        return self.list_service_discovery_rules_with_http_info(request)

    def list_service_discovery_rules_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/inv/servicediscoveryrules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServiceDiscoveryRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def push_events(self, request):
        """上报事件告警信息

        该接口用于上报对应用户的事件、告警。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for PushEvents
        :type request: :class:`huaweicloudsdkaom.v2.PushEventsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.PushEventsResponse`
        """
        return self.push_events_with_http_info(request)

    def push_events_with_http_info(self, request):
        all_params = ['push_events_request_body', 'x_enterprise_prject_id', 'action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}
        if 'x_enterprise_prject_id' in local_var_params:
            header_params['x-enterprise-prject-id'] = local_var_params['x_enterprise_prject_id']

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
            resource_path='/v2/{project_id}/push/events',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='PushEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alarm_rule(self, request):
        """查询单条阈值规则

        该接口用于查询单条阈值规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.ShowAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ShowAlarmRuleResponse`
        """
        return self.show_alarm_rule_with_http_info(request)

    def show_alarm_rule_with_http_info(self, request):
        all_params = ['alarm_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'alarm_rule_id' in local_var_params:
            path_params['alarm_rule_id'] = local_var_params['alarm_rule_id']

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
            resource_path='/v2/{project_id}/alarm-rules/{alarm_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_metrics_data(self, request):
        """查询监控数据

        该接口用于查询指定时间范围内指标的监控数据，可以通过参数指定需要查询的数据维度，数据周期等。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMetricsData
        :type request: :class:`huaweicloudsdkaom.v2.ShowMetricsDataRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ShowMetricsDataResponse`
        """
        return self.show_metrics_data_with_http_info(request)

    def show_metrics_data_with_http_info(self, request):
        all_params = ['query_metric_data_param', 'fill_value']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fill_value' in local_var_params:
            query_params.append(('fillValue', local_var_params['fill_value']))

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
            resource_path='/v1/{project_id}/ams/metricdata',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMetricsDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_rule(self, request):
        """修改阈值规则

        该接口用于修改一条阈值规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.UpdateAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.UpdateAlarmRuleResponse`
        """
        return self.update_alarm_rule_with_http_info(request)

    def update_alarm_rule_with_http_info(self, request):
        all_params = ['update_alarm_rule_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/alarm-rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instant_query_aom_prom_get(self, request):
        """瞬时数据查询

        该接口用于查询PromQL(Prometheus Query Language)。 在特定时间点下的计算结果。（注：接口目前开放的region为：北京四、上海一和广州）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListInstantQueryAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListInstantQueryAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListInstantQueryAomPromGetResponse`
        """
        return self.list_instant_query_aom_prom_get_with_http_info(request)

    def list_instant_query_aom_prom_get_with_http_info(self, request):
        all_params = ['query', 'time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))

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
            resource_path='/v1/{project_id}/aom/api/v1/query',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstantQueryAomPromGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instant_query_aom_prom_post(self, request):
        """瞬时数据查询

        该接口用于查询PromQL(Prometheus Query Language) 在特定时间点下的计算结果。（注：接口目前开放的region为：北京四、上海一和广州）
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListInstantQueryAomPromPost
        :type request: :class:`huaweicloudsdkaom.v2.ListInstantQueryAomPromPostRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListInstantQueryAomPromPostResponse`
        """
        return self.list_instant_query_aom_prom_post_with_http_info(request)

    def list_instant_query_aom_prom_post_with_http_info(self, request):
        all_params = ['query', 'time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))

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
            resource_path='/v1/{project_id}/aom/api/v1/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstantQueryAomPromPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_label_values_aom_prom_get(self, request):
        """查询标签值

        该接口用于查询带有指定标签的时间序列列表。（注：接口目前开放的region为：北京四、上海一和广州）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLabelValuesAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListLabelValuesAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListLabelValuesAomPromGetResponse`
        """
        return self.list_label_values_aom_prom_get_with_http_info(request)

    def list_label_values_aom_prom_get_with_http_info(self, request):
        all_params = ['label_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'label_name' in local_var_params:
            path_params['label_name'] = local_var_params['label_name']

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
            resource_path='/v1/{project_id}/aom/api/v1/label/{label_name}/values',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLabelValuesAomPromGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_labels_aom_prom_get(self, request):
        """获取标签名列表

        该接口用于获取标签名列表。（注：接口目前开放的region为：北京四、上海一和广州）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLabelsAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListLabelsAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListLabelsAomPromGetResponse`
        """
        return self.list_labels_aom_prom_get_with_http_info(request)

    def list_labels_aom_prom_get_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/aom/api/v1/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLabelsAomPromGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_labels_aom_prom_post(self, request):
        """获取标签名列表

        该接口用于获取标签名列表。（注：接口目前开放的region为：北京四、上海一和广州）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLabelsAomPromPost
        :type request: :class:`huaweicloudsdkaom.v2.ListLabelsAomPromPostRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListLabelsAomPromPostResponse`
        """
        return self.list_labels_aom_prom_post_with_http_info(request)

    def list_labels_aom_prom_post_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/aom/api/v1/labels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLabelsAomPromPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_metadata_aom_prom_get(self, request):
        """元数据查询

        该接口用于查询序列及序列标签的元数据。（注：接口目前开放的region为：北京四、上海一和广州）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMetadataAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListMetadataAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListMetadataAomPromGetResponse`
        """
        return self.list_metadata_aom_prom_get_with_http_info(request)

    def list_metadata_aom_prom_get_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/aom/api/v1/metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMetadataAomPromGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_range_query_aom_prom_get(self, request):
        """区间数据查询

        该接口用于查询PromQL(Prometheus Query Language)在一段时间返回内的计算结果。（注：接口目前开放的region为：北京四、上海一和广州）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRangeQueryAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListRangeQueryAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListRangeQueryAomPromGetResponse`
        """
        return self.list_range_query_aom_prom_get_with_http_info(request)

    def list_range_query_aom_prom_get_with_http_info(self, request):
        all_params = ['query', 'start', 'end', 'step']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))
        if 'step' in local_var_params:
            query_params.append(('step', local_var_params['step']))

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
            resource_path='/v1/{project_id}/aom/api/v1/query_range',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRangeQueryAomPromGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_range_query_aom_prom_post(self, request):
        """区间数据查询

        该接口用于查询PromQL(Prometheus Query Language)在一段时间返回内的计算结果。（注：接口目前开放的region为：北京四、上海一和广州）。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRangeQueryAomPromPost
        :type request: :class:`huaweicloudsdkaom.v2.ListRangeQueryAomPromPostRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListRangeQueryAomPromPostResponse`
        """
        return self.list_range_query_aom_prom_post_with_http_info(request)

    def list_range_query_aom_prom_post_with_http_info(self, request):
        all_params = ['query', 'start', 'end', 'step']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))
        if 'step' in local_var_params:
            query_params.append(('step', local_var_params['step']))

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
            resource_path='/v1/{project_id}/aom/api/v1/query_range',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRangeQueryAomPromPostResponse',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)

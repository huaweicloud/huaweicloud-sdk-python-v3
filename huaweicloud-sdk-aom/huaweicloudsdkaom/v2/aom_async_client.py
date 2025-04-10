# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaom'")


class AomAsyncClient(Client):
    def __init__(self):
        super(AomAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaom.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AomAsyncClient":
                raise TypeError("client type error, support client type is AomAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_action_rule_async(self, request):
        r"""新增告警行动规则

        新增告警行动规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddActionRule
        :type request: :class:`huaweicloudsdkaom.v2.AddActionRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddActionRuleResponse`
        """
        http_info = self._add_action_rule_http_info(request)
        return self._call_api(**http_info)

    def add_action_rule_async_invoker(self, request):
        http_info = self._add_action_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_action_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alert/action-rules",
            "request_type": request.__class__.__name__,
            "response_type": "AddActionRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_alarm_rule_async(self, request):
        r"""添加阈值规则

        该接口用于添加一条阈值规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.AddAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddAlarmRuleResponse`
        """
        http_info = self._add_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def add_alarm_rule_async_invoker(self, request):
        http_info = self._add_alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_alarm_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "AddAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_event2alarm_rule_async(self, request):
        r"""新增一条事件类告警规则

        新增一条事件类告警规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddEvent2alarmRule
        :type request: :class:`huaweicloudsdkaom.v2.AddEvent2alarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddEvent2alarmRuleResponse`
        """
        http_info = self._add_event2alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def add_event2alarm_rule_async_invoker(self, request):
        http_info = self._add_event2alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_event2alarm_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/event2alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "AddEvent2alarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_metric_data_async(self, request):
        r"""添加监控数据

        该接口用于向服务端添加一条或多条监控数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddMetricData
        :type request: :class:`huaweicloudsdkaom.v2.AddMetricDataRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddMetricDataResponse`
        """
        http_info = self._add_metric_data_http_info(request)
        return self._call_api(**http_info)

    def add_metric_data_async_invoker(self, request):
        http_info = self._add_metric_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_metric_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ams/report/metricdata",
            "request_type": request.__class__.__name__,
            "response_type": "AddMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_mute_rules_async(self, request):
        r"""新增静默规则

        新增静默规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddMuteRules
        :type request: :class:`huaweicloudsdkaom.v2.AddMuteRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddMuteRulesResponse`
        """
        http_info = self._add_mute_rules_http_info(request)
        return self._call_api(**http_info)

    def add_mute_rules_async_invoker(self, request):
        http_info = self._add_mute_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_mute_rules_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alert/mute-rules",
            "request_type": request.__class__.__name__,
            "response_type": "AddMuteRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_or_update_metric_or_event_alarm_rule_async(self, request):
        r"""添加或修改指标类或事件类告警规则

        添加或修改AOM2.0指标类或事件类告警规则。(注：接口目前开放的region为：华东-上海一)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddOrUpdateMetricOrEventAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.AddOrUpdateMetricOrEventAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddOrUpdateMetricOrEventAlarmRuleResponse`
        """
        http_info = self._add_or_update_metric_or_event_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def add_or_update_metric_or_event_alarm_rule_async_invoker(self, request):
        http_info = self._add_or_update_metric_or_event_alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_or_update_metric_or_event_alarm_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/alarm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "AddOrUpdateMetricOrEventAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_or_update_service_discovery_rules_async(self, request):
        r"""添加或修改服务发现规则

        该接口用于添加或修改一条或多条服务发现规则。同一projectid下可添加的规则上限为100条。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddOrUpdateServiceDiscoveryRules
        :type request: :class:`huaweicloudsdkaom.v2.AddOrUpdateServiceDiscoveryRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.AddOrUpdateServiceDiscoveryRulesResponse`
        """
        http_info = self._add_or_update_service_discovery_rules_http_info(request)
        return self._call_api(**http_info)

    def add_or_update_service_discovery_rules_async_invoker(self, request):
        http_info = self._add_or_update_service_discovery_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_or_update_service_discovery_rules_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/inv/servicediscoveryrules",
            "request_type": request.__class__.__name__,
            "response_type": "AddOrUpdateServiceDiscoveryRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_events_async(self, request):
        r"""统计事件告警信息

        该接口用于分段统计指定条件下的事件、告警。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountEvents
        :type request: :class:`huaweicloudsdkaom.v2.CountEventsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.CountEventsResponse`
        """
        http_info = self._count_events_http_info(request)
        return self._call_api(**http_info)

    def count_events_async_invoker(self, request):
        http_info = self._count_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_events_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/events/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "CountEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_action_rule_async(self, request):
        r"""删除告警行动规则

        删除告警行动规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteActionRule
        :type request: :class:`huaweicloudsdkaom.v2.DeleteActionRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteActionRuleResponse`
        """
        http_info = self._delete_action_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_action_rule_async_invoker(self, request):
        http_info = self._delete_action_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_action_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/alert/action-rules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteActionRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_alarm_rule_async(self, request):
        r"""删除阈值规则

        该接口用于删除阈值规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.DeleteAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteAlarmRuleResponse`
        """
        http_info = self._delete_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_alarm_rule_async_invoker(self, request):
        http_info = self._delete_alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_alarm_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/alarm-rules/{alarm_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_rule_id' in local_var_params:
            path_params['alarm_rule_id'] = local_var_params['alarm_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_alarm_rules_async(self, request):
        r"""批量删除阈值规则

        该接口用于批量删除阈值规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlarmRules
        :type request: :class:`huaweicloudsdkaom.v2.DeleteAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteAlarmRulesResponse`
        """
        http_info = self._delete_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def delete_alarm_rules_async_invoker(self, request):
        http_info = self._delete_alarm_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_alarm_rules_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarm-rules/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlarmRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_event2alarm_rule_async(self, request):
        r"""删除事件类告警规则

        删除一条事件类告警规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEvent2alarmRule
        :type request: :class:`huaweicloudsdkaom.v2.DeleteEvent2alarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteEvent2alarmRuleResponse`
        """
        http_info = self._delete_event2alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_event2alarm_rule_async_invoker(self, request):
        http_info = self._delete_event2alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_event2alarm_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/event2alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEvent2alarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_metric_or_event_alarm_rule_async(self, request):
        r"""删除指标类或事件类告警规则

        删除AOM2.0指标类或事件类告警规则。(注：接口目前开放的region为：华东-上海一)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMetricOrEventAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.DeleteMetricOrEventAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteMetricOrEventAlarmRuleResponse`
        """
        http_info = self._delete_metric_or_event_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_metric_or_event_alarm_rule_async_invoker(self, request):
        http_info = self._delete_metric_or_event_alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_metric_or_event_alarm_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/{project_id}/alarm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMetricOrEventAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_mute_rules_async(self, request):
        r"""删除静默规则

        删除静默规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMuteRules
        :type request: :class:`huaweicloudsdkaom.v2.DeleteMuteRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteMuteRulesResponse`
        """
        http_info = self._delete_mute_rules_http_info(request)
        return self._call_api(**http_info)

    def delete_mute_rules_async_invoker(self, request):
        http_info = self._delete_mute_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_mute_rules_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/alert/mute-rules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMuteRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def deleteservice_discovery_rules_async(self, request):
        r"""删除服务发现规则

        该接口用于删除服务发现规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteserviceDiscoveryRules
        :type request: :class:`huaweicloudsdkaom.v2.DeleteserviceDiscoveryRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeleteserviceDiscoveryRulesResponse`
        """
        http_info = self._deleteservice_discovery_rules_http_info(request)
        return self._call_api(**http_info)

    def deleteservice_discovery_rules_async_invoker(self, request):
        http_info = self._deleteservice_discovery_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _deleteservice_discovery_rules_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/inv/servicediscoveryrules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteserviceDiscoveryRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_rules_ids' in local_var_params:
            query_params.append(('appRulesIds', local_var_params['app_rules_ids']))
            collection_formats['appRulesIds'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_action_rule_async(self, request):
        r"""获取告警行动规则列表

        获取告警行动规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListActionRule
        :type request: :class:`huaweicloudsdkaom.v2.ListActionRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListActionRuleResponse`
        """
        http_info = self._list_action_rule_http_info(request)
        return self._call_api(**http_info)

    def list_action_rule_async_invoker(self, request):
        http_info = self._list_action_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_action_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alert/action-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListActionRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_agents_async(self, request):
        r"""查询主机安装的ICAgent信息

        该接口用于查询集群主机或用户自定义主机安装的ICAgent信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgents
        :type request: :class:`huaweicloudsdkaom.v2.ListAgentsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListAgentsResponse`
        """
        http_info = self._list_agents_http_info(request)
        return self._call_api(**http_info)

    def list_agents_async_invoker(self, request):
        http_info = self._list_agents_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agents_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{cluster_id}/{namespace}/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_alarm_rule_async(self, request):
        r"""查询阈值规则列表

        该接口用于查询阈值规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.ListAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListAlarmRuleResponse`
        """
        http_info = self._list_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_rule_async_invoker(self, request):
        http_info = self._list_alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_event2alarm_rule_async(self, request):
        r"""查询事件类告警规则列表

        查询事件类告警规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvent2alarmRule
        :type request: :class:`huaweicloudsdkaom.v2.ListEvent2alarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListEvent2alarmRuleResponse`
        """
        http_info = self._list_event2alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def list_event2alarm_rule_async_invoker(self, request):
        http_info = self._list_event2alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event2alarm_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/event2alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListEvent2alarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_events_async(self, request):
        r"""查询事件告警信息

        该接口用于查询对应用户的事件、告警。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkaom.v2.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListEventsResponse`
        """
        http_info = self._list_events_http_info(request)
        return self._call_api(**http_info)

    def list_events_async_invoker(self, request):
        http_info = self._list_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_events_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_log_items_async(self, request):
        r"""查询日志

        该接口用于查询不同维度(例如集群、IP、应用等)下的日志内容，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogItems
        :type request: :class:`huaweicloudsdkaom.v2.ListLogItemsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListLogItemsResponse`
        """
        http_info = self._list_log_items_http_info(request)
        return self._call_api(**http_info)

    def list_log_items_async_invoker(self, request):
        http_info = self._list_log_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_log_items_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/als/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_metric_items_async(self, request):
        r"""查询指标

        该接口用于查询系统当前可监控的指标列表，可以指定指标命名空间、指标名称、维度、所属资源的编号（格式为：resType_resId），分页查询的起始位置和返回的最大记录条数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMetricItems
        :type request: :class:`huaweicloudsdkaom.v2.ListMetricItemsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListMetricItemsResponse`
        """
        http_info = self._list_metric_items_http_info(request)
        return self._call_api(**http_info)

    def list_metric_items_async_invoker(self, request):
        http_info = self._list_metric_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_metric_items_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ams/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_metric_or_event_alarm_rule_async(self, request):
        r"""查询指标类或者事件类告警规则列表

        查询AOM2.0指标类或者事件类告警规则列表。(注：接口目前开放的region为：华东-上海一)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMetricOrEventAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.ListMetricOrEventAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListMetricOrEventAlarmRuleResponse`
        """
        http_info = self._list_metric_or_event_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def list_metric_or_event_alarm_rule_async_invoker(self, request):
        http_info = self._list_metric_or_event_alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_metric_or_event_alarm_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{project_id}/alarm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricOrEventAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'event_source' in local_var_params:
            query_params.append(('event_source', local_var_params['event_source']))
        if 'event_severity' in local_var_params:
            query_params.append(('event_severity', local_var_params['event_severity']))
        if 'alarm_rule_status' in local_var_params:
            query_params.append(('alarm_rule_status', local_var_params['alarm_rule_status']))
        if 'alarm_rule_type' in local_var_params:
            query_params.append(('alarm_rule_type', local_var_params['alarm_rule_type']))
        if 'prom_instance_id' in local_var_params:
            query_params.append(('prom_instance_id', local_var_params['prom_instance_id']))
        if 'bind_notification_rule_id' in local_var_params:
            query_params.append(('bind_notification_rule_id', local_var_params['bind_notification_rule_id']))
        if 'related_cce_clusters' in local_var_params:
            query_params.append(('related_cce_clusters', local_var_params['related_cce_clusters']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_mute_rule_async(self, request):
        r"""获取静默规则列表

        获取静默规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMuteRule
        :type request: :class:`huaweicloudsdkaom.v2.ListMuteRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListMuteRuleResponse`
        """
        http_info = self._list_mute_rule_http_info(request)
        return self._call_api(**http_info)

    def list_mute_rule_async_invoker(self, request):
        http_info = self._list_mute_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_mute_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alert/mute-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListMuteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_notified_histories_async(self, request):
        r"""获取告警发送结果

        获取告警发送结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotifiedHistories
        :type request: :class:`huaweicloudsdkaom.v2.ListNotifiedHistoriesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListNotifiedHistoriesResponse`
        """
        http_info = self._list_notified_histories_http_info(request)
        return self._call_api(**http_info)

    def list_notified_histories_async_invoker(self, request):
        http_info = self._list_notified_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notified_histories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-notified-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotifiedHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'event_sn' in local_var_params:
            query_params.append(('event_sn', local_var_params['event_sn']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_permissions_async(self, request):
        r"""查询aom2.0相关云服务授权信息

        该接口用于查询aom2.0相关云服务授权信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermissions
        :type request: :class:`huaweicloudsdkaom.v2.ListPermissionsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListPermissionsResponse`
        """
        http_info = self._list_permissions_http_info(request)
        return self._call_api(**http_info)

    def list_permissions_async_invoker(self, request):
        http_info = self._list_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_permissions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/aom/auth/grant",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_sample_async(self, request):
        r"""查询时序数据

        该接口用于查询指定时间范围内的监控时序数据，可以通过参数指定需要查询的数据维度，数据周期等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSample
        :type request: :class:`huaweicloudsdkaom.v2.ListSampleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListSampleResponse`
        """
        http_info = self._list_sample_http_info(request)
        return self._call_api(**http_info)

    def list_sample_async_invoker(self, request):
        http_info = self._list_sample_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sample_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/samples",
            "request_type": request.__class__.__name__,
            "response_type": "ListSampleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fill_value' in local_var_params:
            query_params.append(('fill_value', local_var_params['fill_value']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_series_async(self, request):
        r"""查询时间序列

        该接口用于查询系统当前可监控的时间序列列表，可以指定时间序列命名空间、名称、维度、所属资源的编号（格式为：resType_resId），分页查询的起始位置和返回的最大记录条数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSeries
        :type request: :class:`huaweicloudsdkaom.v2.ListSeriesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListSeriesResponse`
        """
        http_info = self._list_series_http_info(request)
        return self._call_api(**http_info)

    def list_series_async_invoker(self, request):
        http_info = self._list_series_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_series_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/series",
            "request_type": request.__class__.__name__,
            "response_type": "ListSeriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_service_discovery_rules_async(self, request):
        r"""查询系统中已有服务发现规则

        该接口用于查询系统当前已存在的服务发现规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceDiscoveryRules
        :type request: :class:`huaweicloudsdkaom.v2.ListServiceDiscoveryRulesRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListServiceDiscoveryRulesResponse`
        """
        http_info = self._list_service_discovery_rules_http_info(request)
        return self._call_api(**http_info)

    def list_service_discovery_rules_async_invoker(self, request):
        http_info = self._list_service_discovery_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_service_discovery_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/inv/servicediscoveryrules",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceDiscoveryRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def push_events_async(self, request):
        r"""上报事件告警信息

        该接口用于上报对应用户的事件、告警。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PushEvents
        :type request: :class:`huaweicloudsdkaom.v2.PushEventsRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.PushEventsResponse`
        """
        http_info = self._push_events_http_info(request)
        return self._call_api(**http_info)

    def push_events_async_invoker(self, request):
        http_info = self._push_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _push_events_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/push/events",
            "request_type": request.__class__.__name__,
            "response_type": "PushEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['enterprise-project-id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_action_rule_async(self, request):
        r"""通过规则名称获取告警行动规则

        通过规则名称获取告警行动规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowActionRule
        :type request: :class:`huaweicloudsdkaom.v2.ShowActionRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ShowActionRuleResponse`
        """
        http_info = self._show_action_rule_http_info(request)
        return self._call_api(**http_info)

    def show_action_rule_async_invoker(self, request):
        http_info = self._show_action_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_action_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alert/action-rules/{rule_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowActionRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_name' in local_var_params:
            path_params['rule_name'] = local_var_params['rule_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_alarm_rule_async(self, request):
        r"""查询单条阈值规则

        该接口用于查询单条阈值规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.ShowAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ShowAlarmRuleResponse`
        """
        http_info = self._show_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_rule_async_invoker(self, request):
        http_info = self._show_alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alarm_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-rules/{alarm_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_rule_id' in local_var_params:
            path_params['alarm_rule_id'] = local_var_params['alarm_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_metrics_data_async(self, request):
        r"""查询监控数据

        该接口用于查询指定时间范围内指标的监控数据，可以通过参数指定需要查询的数据维度，数据周期等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMetricsData
        :type request: :class:`huaweicloudsdkaom.v2.ShowMetricsDataRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ShowMetricsDataResponse`
        """
        http_info = self._show_metrics_data_http_info(request)
        return self._call_api(**http_info)

    def show_metrics_data_async_invoker(self, request):
        http_info = self._show_metrics_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_metrics_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ams/metricdata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetricsDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fill_value' in local_var_params:
            query_params.append(('fillValue', local_var_params['fill_value']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_action_rule_async(self, request):
        r"""修改告警行动规则

        修改告警行动规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateActionRule
        :type request: :class:`huaweicloudsdkaom.v2.UpdateActionRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.UpdateActionRuleResponse`
        """
        http_info = self._update_action_rule_http_info(request)
        return self._call_api(**http_info)

    def update_action_rule_async_invoker(self, request):
        http_info = self._update_action_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_action_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/alert/action-rules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateActionRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_alarm_rule_async(self, request):
        r"""修改阈值规则

        该接口用于修改一条阈值规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlarmRule
        :type request: :class:`huaweicloudsdkaom.v2.UpdateAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.UpdateAlarmRuleResponse`
        """
        http_info = self._update_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_rule_async_invoker(self, request):
        http_info = self._update_alarm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_alarm_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/alarm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_event_rule_async(self, request):
        r"""更新事件类告警规则

        更新事件类告警规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEventRule
        :type request: :class:`huaweicloudsdkaom.v2.UpdateEventRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.UpdateEventRuleResponse`
        """
        http_info = self._update_event_rule_http_info(request)
        return self._call_api(**http_info)

    def update_event_rule_async_invoker(self, request):
        http_info = self._update_event_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_event_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/event2alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEventRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_mute_rule_async(self, request):
        r"""修改静默规则

        修改静默规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMuteRule
        :type request: :class:`huaweicloudsdkaom.v2.UpdateMuteRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.UpdateMuteRuleResponse`
        """
        http_info = self._update_mute_rule_http_info(request)
        return self._call_api(**http_info)

    def update_mute_rule_async_invoker(self, request):
        http_info = self._update_mute_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_mute_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/alert/mute-rules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMuteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_prom_instance_async(self, request):
        r"""新增Prometheus实例

        该接口用于新增Prometheus实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePromInstance
        :type request: :class:`huaweicloudsdkaom.v2.CreatePromInstanceRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.CreatePromInstanceResponse`
        """
        http_info = self._create_prom_instance_http_info(request)
        return self._call_api(**http_info)

    def create_prom_instance_async_invoker(self, request):
        http_info = self._create_prom_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_prom_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/aom/prometheus",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePromInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_recording_rule_async(self, request):
        r"""创建Prometheus实例的预聚合规则

        该接口用于给Prometheus实例创建预聚合规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordingRule
        :type request: :class:`huaweicloudsdkaom.v2.CreateRecordingRuleRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.CreateRecordingRuleResponse`
        """
        http_info = self._create_recording_rule_http_info(request)
        return self._call_api(**http_info)

    def create_recording_rule_async_invoker(self, request):
        http_info = self._create_recording_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_recording_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{prometheus_instance}/aom/api/v1/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordingRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'prometheus_instance' in local_var_params:
            path_params['prometheus_instance'] = local_var_params['prometheus_instance']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_prom_instance_async(self, request):
        r"""卸载托管Prometheus实例

        该接口用于卸载托管Prometheus实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePromInstance
        :type request: :class:`huaweicloudsdkaom.v2.DeletePromInstanceRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.DeletePromInstanceResponse`
        """
        http_info = self._delete_prom_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_prom_instance_async_invoker(self, request):
        http_info = self._delete_prom_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_prom_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/aom/prometheus",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePromInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prom_id' in local_var_params:
            query_params.append(('prom_id', local_var_params['prom_id']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_access_code_async(self, request):
        r"""获取Prometheus实例调用凭证

        该接口用于获取Prometheus实例调用凭证。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessCode
        :type request: :class:`huaweicloudsdkaom.v2.ListAccessCodeRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListAccessCodeResponse`
        """
        http_info = self._list_access_code_http_info(request)
        return self._call_api(**http_info)

    def list_access_code_async_invoker(self, request):
        http_info = self._list_access_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_access_code_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/access-code",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_prom_instance_async(self, request):
        r"""查询Prometheus实例

        该接口用于查询Prometheus实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPromInstance
        :type request: :class:`huaweicloudsdkaom.v2.ListPromInstanceRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListPromInstanceResponse`
        """
        http_info = self._list_prom_instance_http_info(request)
        return self._call_api(**http_info)

    def list_prom_instance_async_invoker(self, request):
        http_info = self._list_prom_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_prom_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/aom/prometheus",
            "request_type": request.__class__.__name__,
            "response_type": "ListPromInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prom_id' in local_var_params:
            query_params.append(('prom_id', local_var_params['prom_id']))
        if 'prom_type' in local_var_params:
            query_params.append(('prom_type', local_var_params['prom_type']))
        if 'cce_cluster_enable' in local_var_params:
            query_params.append(('cce_cluster_enable', local_var_params['cce_cluster_enable']))
        if 'prom_status' in local_var_params:
            query_params.append(('prom_status', local_var_params['prom_status']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instant_query_aom_prom_get_async(self, request):
        r"""GET方法查询瞬时数据

        该接口使用GET方法查询PromQL(Prometheus Query Language)在特定时间点下的计算结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstantQueryAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListInstantQueryAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListInstantQueryAomPromGetResponse`
        """
        http_info = self._list_instant_query_aom_prom_get_http_info(request)
        return self._call_api(**http_info)

    def list_instant_query_aom_prom_get_async_invoker(self, request):
        http_info = self._list_instant_query_aom_prom_get_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instant_query_aom_prom_get_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/aom/api/v1/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstantQueryAomPromGetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instant_query_aom_prom_post_async(self, request):
        r"""（推荐）POST方法查询瞬时数据

        该接口使用POST方法查询PromQL(Prometheus Query Language) 在特定时间点下的计算结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstantQueryAomPromPost
        :type request: :class:`huaweicloudsdkaom.v2.ListInstantQueryAomPromPostRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListInstantQueryAomPromPostResponse`
        """
        http_info = self._list_instant_query_aom_prom_post_http_info(request)
        return self._call_api(**http_info)

    def list_instant_query_aom_prom_post_async_invoker(self, request):
        http_info = self._list_instant_query_aom_prom_post_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instant_query_aom_prom_post_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/aom/api/v1/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstantQueryAomPromPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_label_values_aom_prom_get_async(self, request):
        r"""查询标签值

        该接口用于查询带有指定标签的时间序列列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLabelValuesAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListLabelValuesAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListLabelValuesAomPromGetResponse`
        """
        http_info = self._list_label_values_aom_prom_get_http_info(request)
        return self._call_api(**http_info)

    def list_label_values_aom_prom_get_async_invoker(self, request):
        http_info = self._list_label_values_aom_prom_get_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_label_values_aom_prom_get_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/aom/api/v1/label/{label_name}/values",
            "request_type": request.__class__.__name__,
            "response_type": "ListLabelValuesAomPromGetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'label_name' in local_var_params:
            path_params['label_name'] = local_var_params['label_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_labels_aom_prom_get_async(self, request):
        r"""GET方法获取标签名列表

        该接口使用GET方法获取标签名列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLabelsAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListLabelsAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListLabelsAomPromGetResponse`
        """
        http_info = self._list_labels_aom_prom_get_http_info(request)
        return self._call_api(**http_info)

    def list_labels_aom_prom_get_async_invoker(self, request):
        http_info = self._list_labels_aom_prom_get_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_labels_aom_prom_get_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/aom/api/v1/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListLabelsAomPromGetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_labels_aom_prom_post_async(self, request):
        r"""（推荐）POST方法获取标签名列表

        该接口使用POST方法获取标签名列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLabelsAomPromPost
        :type request: :class:`huaweicloudsdkaom.v2.ListLabelsAomPromPostRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListLabelsAomPromPostResponse`
        """
        http_info = self._list_labels_aom_prom_post_http_info(request)
        return self._call_api(**http_info)

    def list_labels_aom_prom_post_async_invoker(self, request):
        http_info = self._list_labels_aom_prom_post_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_labels_aom_prom_post_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/aom/api/v1/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListLabelsAomPromPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_metadata_aom_prom_get_async(self, request):
        r"""元数据查询

        该接口用于查询序列及序列标签的元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMetadataAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListMetadataAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListMetadataAomPromGetResponse`
        """
        http_info = self._list_metadata_aom_prom_get_http_info(request)
        return self._call_api(**http_info)

    def list_metadata_aom_prom_get_async_invoker(self, request):
        http_info = self._list_metadata_aom_prom_get_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_metadata_aom_prom_get_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/aom/api/v1/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetadataAomPromGetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_range_query_aom_prom_get_async(self, request):
        r"""GET方法查询区间数据

        该接口使用GET方法查询PromQL(Prometheus Query Language)在一段时间返回内的计算结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRangeQueryAomPromGet
        :type request: :class:`huaweicloudsdkaom.v2.ListRangeQueryAomPromGetRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListRangeQueryAomPromGetResponse`
        """
        http_info = self._list_range_query_aom_prom_get_http_info(request)
        return self._call_api(**http_info)

    def list_range_query_aom_prom_get_async_invoker(self, request):
        http_info = self._list_range_query_aom_prom_get_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_range_query_aom_prom_get_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/aom/api/v1/query_range",
            "request_type": request.__class__.__name__,
            "response_type": "ListRangeQueryAomPromGetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_range_query_aom_prom_post_async(self, request):
        r"""（推荐）POST方法查询区间数据

        该接口使用POST方法查询PromQL(Prometheus Query Language)在一段时间返回内的计算结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRangeQueryAomPromPost
        :type request: :class:`huaweicloudsdkaom.v2.ListRangeQueryAomPromPostRequest`
        :rtype: :class:`huaweicloudsdkaom.v2.ListRangeQueryAomPromPostResponse`
        """
        http_info = self._list_range_query_aom_prom_post_http_info(request)
        return self._call_api(**http_info)

    def list_range_query_aom_prom_post_async_invoker(self, request):
        http_info = self._list_range_query_aom_prom_post_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_range_query_aom_prom_post_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/aom/api/v1/query_range",
            "request_type": request.__class__.__name__,
            "response_type": "ListRangeQueryAomPromPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

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

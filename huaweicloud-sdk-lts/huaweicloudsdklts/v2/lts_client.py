# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdklts'")


class LtsClient(Client):
    def __init__(self):
        super(LtsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklts.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "LtsClient":
                raise TypeError("client type error, support client type is LtsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_access_config(self, request):
        r"""创建日志接入

        创建日志接入
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccessConfig
        :type request: :class:`huaweicloudsdklts.v2.CreateAccessConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateAccessConfigResponse`
        """
        http_info = self._create_access_config_http_info(request)
        return self._call_api(**http_info)

    def create_access_config_invoker(self, request):
        http_info = self._create_access_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_access_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/lts/access-config",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccessConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_agency_access(self, request):
        r"""新建跨账号日志接入

        新建跨账号日志接入
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAgencyAccess
        :type request: :class:`huaweicloudsdklts.v2.CreateAgencyAccessRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateAgencyAccessResponse`
        """
        http_info = self._create_agency_access_http_info(request)
        return self._call_api(**http_info)

    def create_agency_access_invoker(self, request):
        http_info = self._create_agency_access_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_agency_access_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/lts/createAgencyAccess",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyAccessResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_dash_board(self, request):
        r"""创建仪表盘

        创建仪表盘
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDashBoard
        :type request: :class:`huaweicloudsdklts.v2.CreateDashBoardRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateDashBoardResponse`
        """
        http_info = self._create_dash_board_http_info(request)
        return self._call_api(**http_info)

    def create_dash_board_invoker(self, request):
        http_info = self._create_dash_board_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dash_board_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dashboard",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDashBoardResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_dashboard_group(self, request):
        r"""创建仪表盘分组

        创建仪表盘分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDashboardGroup
        :type request: :class:`huaweicloudsdklts.v2.CreateDashboardGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateDashboardGroupResponse`
        """
        http_info = self._create_dashboard_group_http_info(request)
        return self._call_api(**http_info)

    def create_dashboard_group_invoker(self, request):
        http_info = self._create_dashboard_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dashboard_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/dashboard-group",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDashboardGroupResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_host_group(self, request):
        r"""创建主机组

        创建主机组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHostGroup
        :type request: :class:`huaweicloudsdklts.v2.CreateHostGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateHostGroupResponse`
        """
        http_info = self._create_host_group_http_info(request)
        return self._call_api(**http_info)

    def create_host_group_invoker(self, request):
        http_info = self._create_host_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_host_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/lts/host-group",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHostGroupResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_keywords_alarm_rule(self, request):
        r"""创建关键词告警规则

        该接口用于创建关键词告警，目前每个帐户最多可以创建共200个关键词告警与SQL告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateKeywordsAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.CreateKeywordsAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateKeywordsAlarmRuleResponse`
        """
        http_info = self._create_keywords_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def create_keywords_alarm_rule_invoker(self, request):
        http_info = self._create_keywords_alarm_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_keywords_alarm_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/alarms/keywords-alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKeywordsAlarmRuleResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_log_dump_obs(self, request):
        r"""创建日志转储（旧版）

        该接口用于将指定的一个或多个日志流的日志转储到OBS服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLogDumpObs
        :type request: :class:`huaweicloudsdklts.v2.CreateLogDumpObsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateLogDumpObsResponse`
        """
        http_info = self._create_log_dump_obs_http_info(request)
        return self._call_api(**http_info)

    def create_log_dump_obs_invoker(self, request):
        http_info = self._create_log_dump_obs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_log_dump_obs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/log-dump/obs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogDumpObsResponse"
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

    def create_log_group(self, request):
        r"""创建日志组

        该接口用于创建一个日志组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLogGroup
        :type request: :class:`huaweicloudsdklts.v2.CreateLogGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateLogGroupResponse`
        """
        http_info = self._create_log_group_http_info(request)
        return self._call_api(**http_info)

    def create_log_group_invoker(self, request):
        http_info = self._create_log_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_log_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogGroupResponse"
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

    def create_log_stream(self, request):
        r"""创建日志流

        该接口用于创建某个指定日志组下的日志流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLogStream
        :type request: :class:`huaweicloudsdklts.v2.CreateLogStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateLogStreamResponse`
        """
        http_info = self._create_log_stream_http_info(request)
        return self._call_api(**http_info)

    def create_log_stream_invoker(self, request):
        http_info = self._create_log_stream_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_log_stream_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}/streams",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogStreamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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

    def create_log_stream_index(self, request):
        r"""向指定流创建索引

        向指定流创建索引
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLogStreamIndex
        :type request: :class:`huaweicloudsdklts.v2.CreateLogStreamIndexRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateLogStreamIndexResponse`
        """
        http_info = self._create_log_stream_index_http_info(request)
        return self._call_api(**http_info)

    def create_log_stream_index_invoker(self, request):
        http_info = self._create_log_stream_index_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_log_stream_index_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/stream/{stream_id}/index/config",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogStreamIndexResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_notification_template(self, request):
        r"""创建消息模板

        该接口用于创建通知模板，目前每个帐户最多可以创建共100个通知模板，创建后名称不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.CreateNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateNotificationTemplateResponse`
        """
        http_info = self._create_notification_template_http_info(request)
        return self._call_api(**http_info)

    def create_notification_template_invoker(self, request):
        http_info = self._create_notification_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_notification_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{domain_id}/lts/events/notification/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNotificationTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_search_criterias(self, request):
        r"""添加快速查询

        添加快速查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSearchCriterias
        :type request: :class:`huaweicloudsdklts.v2.CreateSearchCriteriasRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateSearchCriteriasResponse`
        """
        http_info = self._create_search_criterias_http_info(request)
        return self._call_api(**http_info)

    def create_search_criterias_invoker(self, request):
        http_info = self._create_search_criterias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_search_criterias_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/topics/{topic_id}/search-criterias",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSearchCriteriasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'topic_id' in local_var_params:
            path_params['topic_id'] = local_var_params['topic_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_struct_config(self, request):
        r"""通过结构化模板创建结构化配置（新）

        该接口通过结构化模板创建结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStructConfig
        :type request: :class:`huaweicloudsdklts.v2.CreateStructConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateStructConfigResponse`
        """
        http_info = self._create_struct_config_http_info(request)
        return self._call_api(**http_info)

    def create_struct_config_invoker(self, request):
        http_info = self._create_struct_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_struct_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/lts/struct/template",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStructConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_struct_template(self, request):
        r"""创建结构化配置

        该接口用于创建指定日志流下的结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.CreateStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateStructTemplateResponse`
        """
        http_info = self._create_struct_template_http_info(request)
        return self._call_api(**http_info)

    def create_struct_template_invoker(self, request):
        http_info = self._create_struct_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_struct_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/struct/template",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStructTemplateResponse"
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

    def create_tags(self, request):
        r"""create_tags

        添加标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTags
        :type request: :class:`huaweicloudsdklts.v2.CreateTagsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateTagsResponse`
        """
        http_info = self._create_tags_http_info(request)
        return self._call_api(**http_info)

    def create_tags_invoker(self, request):
        http_info = self._create_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_transfer(self, request):
        r"""创建日志转储（新版）

        该接口用于创建OBS转储，DIS转储，DMS转储。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTransfer
        :type request: :class:`huaweicloudsdklts.v2.CreateTransferRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateTransferResponse`
        """
        http_info = self._create_transfer_http_info(request)
        return self._call_api(**http_info)

    def create_transfer_invoker(self, request):
        http_info = self._create_transfer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_transfer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/transfers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTransferResponse"
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
            ['application/json;charset=UTF-8'])

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

    def createfavorite(self, request):
        r"""创建日志收藏

        创建日志收藏
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Createfavorite
        :type request: :class:`huaweicloudsdklts.v2.CreatefavoriteRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreatefavoriteResponse`
        """
        http_info = self._createfavorite_http_info(request)
        return self._call_api(**http_info)

    def createfavorite_invoker(self, request):
        http_info = self._createfavorite_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _createfavorite_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/lts/favorite",
            "request_type": request.__class__.__name__,
            "response_type": "CreatefavoriteResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_access_config(self, request):
        r"""删除日志接入

        删除日志接入
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAccessConfig
        :type request: :class:`huaweicloudsdklts.v2.DeleteAccessConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteAccessConfigResponse`
        """
        http_info = self._delete_access_config_http_info(request)
        return self._call_api(**http_info)

    def delete_access_config_invoker(self, request):
        http_info = self._delete_access_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_access_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/lts/access-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAccessConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_active_alarms(self, request):
        r"""删除活动告警

        该接口用于删除活动告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteActiveAlarms
        :type request: :class:`huaweicloudsdklts.v2.DeleteActiveAlarmsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteActiveAlarmsResponse`
        """
        http_info = self._delete_active_alarms_http_info(request)
        return self._call_api(**http_info)

    def delete_active_alarms_invoker(self, request):
        http_info = self._delete_active_alarms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_active_alarms_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{domain_id}/lts/alarms/sql-alarm/clear",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteActiveAlarmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_dashboard(self, request):
        r"""删除仪表盘

        删除仪表盘
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDashboard
        :type request: :class:`huaweicloudsdklts.v2.DeleteDashboardRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteDashboardResponse`
        """
        http_info = self._delete_dashboard_http_info(request)
        return self._call_api(**http_info)

    def delete_dashboard_invoker(self, request):
        http_info = self._delete_dashboard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dashboard_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/dashboard",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDashboardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'is_delete_charts' in local_var_params:
            query_params.append(('is_delete_charts', local_var_params['is_delete_charts']))

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

    def delete_host_group(self, request):
        r"""删除主机组

        删除主机组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHostGroup
        :type request: :class:`huaweicloudsdklts.v2.DeleteHostGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteHostGroupResponse`
        """
        http_info = self._delete_host_group_http_info(request)
        return self._call_api(**http_info)

    def delete_host_group_invoker(self, request):
        http_info = self._delete_host_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_host_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/lts/host-group",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHostGroupResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_keywords_alarm_rule(self, request):
        r"""删除关键词告警规则

        该接口用于删除关键词告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteKeywordsAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.DeleteKeywordsAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteKeywordsAlarmRuleResponse`
        """
        http_info = self._delete_keywords_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_keywords_alarm_rule_invoker(self, request):
        http_info = self._delete_keywords_alarm_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_keywords_alarm_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/lts/alarms/keywords-alarm-rule/{keywords_alarm_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKeywordsAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keywords_alarm_rule_id' in local_var_params:
            path_params['keywords_alarm_rule_id'] = local_var_params['keywords_alarm_rule_id']

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

    def delete_log_group(self, request):
        r"""删除日志组

        该接口用于删除指定日志组。当日志组中的日志流配置了日志转储，需要取消日志转储后才可删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogGroup
        :type request: :class:`huaweicloudsdklts.v2.DeleteLogGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteLogGroupResponse`
        """
        http_info = self._delete_log_group_http_info(request)
        return self._call_api(**http_info)

    def delete_log_group_invoker(self, request):
        http_info = self._delete_log_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_log_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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

    def delete_log_stream(self, request):
        r"""删除日志流

        该接口用于删除指定日志组下的指定日志流。当该日志流配置了日志转储，需要取消日志转储后才可删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogStream
        :type request: :class:`huaweicloudsdklts.v2.DeleteLogStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteLogStreamResponse`
        """
        http_info = self._delete_log_stream_http_info(request)
        return self._call_api(**http_info)

    def delete_log_stream_invoker(self, request):
        http_info = self._delete_log_stream_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_log_stream_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogStreamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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

    def delete_notification_template(self, request):
        r"""删除消息模板

        该接口用于删除通知模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.DeleteNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteNotificationTemplateResponse`
        """
        http_info = self._delete_notification_template_http_info(request)
        return self._call_api(**http_info)

    def delete_notification_template_invoker(self, request):
        http_info = self._delete_notification_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_notification_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{domain_id}/lts/events/notification/templates",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNotificationTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_search_criterias(self, request):
        r"""删除快速查询

        删除快速查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSearchCriterias
        :type request: :class:`huaweicloudsdklts.v2.DeleteSearchCriteriasRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteSearchCriteriasResponse`
        """
        http_info = self._delete_search_criterias_http_info(request)
        return self._call_api(**http_info)

    def delete_search_criterias_invoker(self, request):
        http_info = self._delete_search_criterias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_search_criterias_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/topics/{topic_id}/search-criterias",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSearchCriteriasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'topic_id' in local_var_params:
            path_params['topic_id'] = local_var_params['topic_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_struct_template(self, request):
        r"""删除结构化配置

        该接口用于删除指定日志流下的结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.DeleteStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteStructTemplateResponse`
        """
        http_info = self._delete_struct_template_http_info(request)
        return self._call_api(**http_info)

    def delete_struct_template_invoker(self, request):
        http_info = self._delete_struct_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_struct_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/lts/struct/template",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStructTemplateResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_transfer(self, request):
        r"""删除日志转储

        该接口用于删除OBS转储，DIS转储，DMS转储。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTransfer
        :type request: :class:`huaweicloudsdklts.v2.DeleteTransferRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteTransferResponse`
        """
        http_info = self._delete_transfer_http_info(request)
        return self._call_api(**http_info)

    def delete_transfer_invoker(self, request):
        http_info = self._delete_transfer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_transfer_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/transfers",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTransferResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_transfer_id' in local_var_params:
            query_params.append(('log_transfer_id', local_var_params['log_transfer_id']))

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

    def deletefavorite(self, request):
        r"""取消收藏

        取消收藏
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Deletefavorite
        :type request: :class:`huaweicloudsdklts.v2.DeletefavoriteRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeletefavoriteResponse`
        """
        http_info = self._deletefavorite_http_info(request)
        return self._call_api(**http_info)

    def deletefavorite_invoker(self, request):
        http_info = self._deletefavorite_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _deletefavorite_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/lts/favorite/{fav_res_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletefavoriteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'fav_res_id' in local_var_params:
            path_params['fav_res_id'] = local_var_params['fav_res_id']

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

    def disable_log_collection(self, request):
        r"""关闭超额采集开关

        该接口用于将超额采集日志功能关闭。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableLogCollection
        :type request: :class:`huaweicloudsdklts.v2.DisableLogCollectionRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DisableLogCollectionResponse`
        """
        http_info = self._disable_log_collection_http_info(request)
        return self._call_api(**http_info)

    def disable_log_collection_invoker(self, request):
        http_info = self._disable_log_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_log_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/collection/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableLogCollectionResponse"
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

    def enable_log_collection(self, request):
        r"""打开超额采集开关

        该接口用于将超额采集日志功能打开。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableLogCollection
        :type request: :class:`huaweicloudsdklts.v2.EnableLogCollectionRequest`
        :rtype: :class:`huaweicloudsdklts.v2.EnableLogCollectionResponse`
        """
        http_info = self._enable_log_collection_http_info(request)
        return self._call_api(**http_info)

    def enable_log_collection_invoker(self, request):
        http_info = self._enable_log_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_log_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/collection/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableLogCollectionResponse"
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

    def list_access_config(self, request):
        r"""查询日志接入

        查询日志接入列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessConfig
        :type request: :class:`huaweicloudsdklts.v2.ListAccessConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListAccessConfigResponse`
        """
        http_info = self._list_access_config_http_info(request)
        return self._call_api(**http_info)

    def list_access_config_invoker(self, request):
        http_info = self._list_access_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_access_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/lts/access-config-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_active_or_history_alarms(self, request):
        r"""查询活动或历史告警列表

        该接口用于查询告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListActiveOrHistoryAlarms
        :type request: :class:`huaweicloudsdklts.v2.ListActiveOrHistoryAlarmsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListActiveOrHistoryAlarmsResponse`
        """
        http_info = self._list_active_or_history_alarms_http_info(request)
        return self._call_api(**http_info)

    def list_active_or_history_alarms_invoker(self, request):
        http_info = self._list_active_or_history_alarms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_active_or_history_alarms_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{domain_id}/lts/alarms/sql-alarm/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListActiveOrHistoryAlarmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def list_breif_struct_template(self, request):
        r"""查询结构化模板简略列表

        该接口用于查询结构化模板简略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBreifStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.ListBreifStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListBreifStructTemplateResponse`
        """
        http_info = self._list_breif_struct_template_http_info(request)
        return self._call_api(**http_info)

    def list_breif_struct_template_invoker(self, request):
        http_info = self._list_breif_struct_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_breif_struct_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/lts/struct/customtemplate/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListBreifStructTemplateResponse"
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

    def list_charts(self, request):
        r"""查询日志流图表

        该接口用于查询日志流图表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCharts
        :type request: :class:`huaweicloudsdklts.v2.ListChartsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListChartsResponse`
        """
        http_info = self._list_charts_http_info(request)
        return self._call_api(**http_info)

    def list_charts_invoker(self, request):
        http_info = self._list_charts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_charts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/charts",
            "request_type": request.__class__.__name__,
            "response_type": "ListChartsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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

    def list_criterias(self, request):
        r"""获取快速查询

        获取快速查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCriterias
        :type request: :class:`huaweicloudsdklts.v2.ListCriteriasRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListCriteriasResponse`
        """
        http_info = self._list_criterias_http_info(request)
        return self._call_api(**http_info)

    def list_criterias_invoker(self, request):
        http_info = self._list_criterias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_criterias_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/topics/{topic_id}/search-criterias",
            "request_type": request.__class__.__name__,
            "response_type": "ListCriteriasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'topic_id' in local_var_params:
            path_params['topic_id'] = local_var_params['topic_id']

        query_params = []
        if 'search_type' in local_var_params:
            query_params.append(('search_type', local_var_params['search_type']))

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

    def list_history_sql(self, request):
        r"""查询用户历史sql

        查询用户历史sql
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistorySql
        :type request: :class:`huaweicloudsdklts.v2.ListHistorySqlRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListHistorySqlResponse`
        """
        http_info = self._list_history_sql_http_info(request)
        return self._call_api(**http_info)

    def list_history_sql_invoker(self, request):
        http_info = self._list_history_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_sql_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/lts/history-sql",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistorySqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_group_id' in local_var_params:
            query_params.append(('log_group_id', local_var_params['log_group_id']))
        if 'log_stream_id' in local_var_params:
            query_params.append(('log_stream_id', local_var_params['log_stream_id']))

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

    def list_host(self, request):
        r"""查询主机信息

        查询主机列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHost
        :type request: :class:`huaweicloudsdklts.v2.ListHostRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListHostResponse`
        """
        http_info = self._list_host_http_info(request)
        return self._call_api(**http_info)

    def list_host_invoker(self, request):
        http_info = self._list_host_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_host_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/lts/host-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_host_group(self, request):
        r"""查询主机组

        查询主机组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostGroup
        :type request: :class:`huaweicloudsdklts.v2.ListHostGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListHostGroupResponse`
        """
        http_info = self._list_host_group_http_info(request)
        return self._call_api(**http_info)

    def list_host_group_invoker(self, request):
        http_info = self._list_host_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_host_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/lts/host-group-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostGroupResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_keywords_alarm_rules(self, request):
        r"""查询关键词告警规则

        该接口用于查询关键词告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListKeywordsAlarmRules
        :type request: :class:`huaweicloudsdklts.v2.ListKeywordsAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListKeywordsAlarmRulesResponse`
        """
        http_info = self._list_keywords_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def list_keywords_alarm_rules_invoker(self, request):
        http_info = self._list_keywords_alarm_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_keywords_alarm_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/lts/alarms/keywords-alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeywordsAlarmRulesResponse"
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

    def list_log_context(self, request):
        r"""查询上下文日志

        查询上下文日志 该接口用于查询指定日志前（上文）后（下文）的若干条日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogContext
        :type request: :class:`huaweicloudsdklts.v2.ListLogContextRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogContextResponse`
        """
        http_info = self._list_log_context_http_info(request)
        return self._call_api(**http_info)

    def list_log_context_invoker(self, request):
        http_info = self._list_log_context_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_log_context_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/context",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogContextResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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
            ['application/json;charset=UTF-8'])

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

    def list_log_groups(self, request):
        r"""查询账号下所有日志组

        该接口用于查询账号下所有日志组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogGroups
        :type request: :class:`huaweicloudsdklts.v2.ListLogGroupsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogGroupsResponse`
        """
        http_info = self._list_log_groups_http_info(request)
        return self._call_api(**http_info)

    def list_log_groups_invoker(self, request):
        http_info = self._list_log_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_log_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogGroupsResponse"
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

    def list_log_histogram(self, request):
        r"""查询日志直方图

        查询关键词搜索条数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogHistogram
        :type request: :class:`huaweicloudsdklts.v2.ListLogHistogramRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogHistogramResponse`
        """
        http_info = self._list_log_histogram_http_info(request)
        return self._call_api(**http_info)

    def list_log_histogram_invoker(self, request):
        http_info = self._list_log_histogram_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_log_histogram_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/keyword-count",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogHistogramResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_log_stream(self, request):
        r"""查询指定日志组下的所有日志流

        该接口用于查询指定日志组下的所有日志流信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogStream
        :type request: :class:`huaweicloudsdklts.v2.ListLogStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogStreamResponse`
        """
        http_info = self._list_log_stream_http_info(request)
        return self._call_api(**http_info)

    def list_log_stream_invoker(self, request):
        http_info = self._list_log_stream_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_log_stream_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}/streams",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogStreamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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

    def list_log_stream_index(self, request):
        r"""查询日志流索引

        查询日志流索引。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogStreamIndex
        :type request: :class:`huaweicloudsdklts.v2.ListLogStreamIndexRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogStreamIndexResponse`
        """
        http_info = self._list_log_stream_index_http_info(request)
        return self._call_api(**http_info)

    def list_log_stream_index_invoker(self, request):
        http_info = self._list_log_stream_index_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_log_stream_index_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/stream/{stream_id}/index/config",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogStreamIndexResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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

    def list_log_streams(self, request):
        r"""查询日志流信息

        该接口用于查询LTS日志流信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogStreams
        :type request: :class:`huaweicloudsdklts.v2.ListLogStreamsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogStreamsResponse`
        """
        http_info = self._list_log_streams_http_info(request)
        return self._call_api(**http_info)

    def list_log_streams_invoker(self, request):
        http_info = self._list_log_streams_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_log_streams_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/log-streams",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogStreamsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_group_name' in local_var_params:
            query_params.append(('log_group_name', local_var_params['log_group_name']))
        if 'log_stream_name' in local_var_params:
            query_params.append(('log_stream_name', local_var_params['log_stream_name']))

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

    def list_logs(self, request):
        r"""查询日志

        该接口用于查询指定日志流下的日志内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogs
        :type request: :class:`huaweicloudsdklts.v2.ListLogsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogsResponse`
        """
        http_info = self._list_logs_http_info(request)
        return self._call_api(**http_info)

    def list_logs_invoker(self, request):
        http_info = self._list_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/content/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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

    def list_notification_template(self, request):
        r"""预览消息模板邮件格式

        该接口用于预览通知模板邮件格式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.ListNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListNotificationTemplateResponse`
        """
        http_info = self._list_notification_template_http_info(request)
        return self._call_api(**http_info)

    def list_notification_template_invoker(self, request):
        http_info = self._list_notification_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notification_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{domain_id}/lts/events/notification/templates/view",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotificationTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def list_notification_templates(self, request):
        r"""查询消息模板

        该接口用于查询通知模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationTemplates
        :type request: :class:`huaweicloudsdklts.v2.ListNotificationTemplatesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListNotificationTemplatesResponse`
        """
        http_info = self._list_notification_templates_http_info(request)
        return self._call_api(**http_info)

    def list_notification_templates_invoker(self, request):
        http_info = self._list_notification_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notification_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{domain_id}/lts/events/notification/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotificationTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def list_notification_topics(self, request):
        r"""查询SMN主题

        该接口用于查询SMN主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationTopics
        :type request: :class:`huaweicloudsdklts.v2.ListNotificationTopicsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListNotificationTopicsResponse`
        """
        http_info = self._list_notification_topics_http_info(request)
        return self._call_api(**http_info)

    def list_notification_topics_invoker(self, request):
        http_info = self._list_notification_topics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notification_topics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/lts/notifications/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotificationTopicsResponse"
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

    def list_query_all_search_criterias(self, request):
        r"""查询日志组下所有快速查询

        查询日志组下所有快速查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryAllSearchCriterias
        :type request: :class:`huaweicloudsdklts.v2.ListQueryAllSearchCriteriasRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListQueryAllSearchCriteriasResponse`
        """
        http_info = self._list_query_all_search_criterias_http_info(request)
        return self._call_api(**http_info)

    def list_query_all_search_criterias_invoker(self, request):
        http_info = self._list_query_all_search_criterias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_all_search_criterias_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/lts/groups/{group_id}/search-criterias",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryAllSearchCriteriasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_query_structured_logs(self, request):
        r"""查询结构化日志

        该接口用于查询指定日志流下的结构化日志内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryStructuredLogs
        :type request: :class:`huaweicloudsdklts.v2.ListQueryStructuredLogsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListQueryStructuredLogsResponse`
        """
        http_info = self._list_query_structured_logs_http_info(request)
        return self._call_api(**http_info)

    def list_query_structured_logs_invoker(self, request):
        http_info = self._list_query_structured_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_structured_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/struct-content/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryStructuredLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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

    def list_struct_template(self, request):
        r"""查询结构化模板

        该接口用于查询结构化模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.ListStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListStructTemplateResponse`
        """
        http_info = self._list_struct_template_http_info(request)
        return self._call_api(**http_info)

    def list_struct_template_invoker(self, request):
        http_info = self._list_struct_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_struct_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/lts/struct/customtemplate",
            "request_type": request.__class__.__name__,
            "response_type": "ListStructTemplateResponse"
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

    def list_structured_logs_with_time_range(self, request):
        r"""查询结构化日志（新版）

        该接口用于查询指定日志流下的结构化日志内容（新版）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStructuredLogsWithTimeRange
        :type request: :class:`huaweicloudsdklts.v2.ListStructuredLogsWithTimeRangeRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListStructuredLogsWithTimeRangeResponse`
        """
        http_info = self._list_structured_logs_with_time_range_http_info(request)
        return self._call_api(**http_info)

    def list_structured_logs_with_time_range_invoker(self, request):
        http_info = self._list_structured_logs_with_time_range_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_structured_logs_with_time_range_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/streams/{log_stream_id}/struct-content/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListStructuredLogsWithTimeRangeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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

    def list_time_line_traffic_statistics(self, request):
        r"""按时间段统计查询资源

        按时间段统计查询资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTimeLineTrafficStatistics
        :type request: :class:`huaweicloudsdklts.v2.ListTimeLineTrafficStatisticsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListTimeLineTrafficStatisticsResponse`
        """
        http_info = self._list_time_line_traffic_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_time_line_traffic_statistics_invoker(self, request):
        http_info = self._list_time_line_traffic_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_time_line_traffic_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/timeline-traffic-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListTimeLineTrafficStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'timezone' in local_var_params:
            query_params.append(('timezone', local_var_params['timezone']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def list_topn_traffic_statistics(self, request):
        r"""统计top n的日志组或日志流流量

        统计top n的日志组或日志流流量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTopnTrafficStatistics
        :type request: :class:`huaweicloudsdklts.v2.ListTopnTrafficStatisticsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListTopnTrafficStatisticsResponse`
        """
        http_info = self._list_topn_traffic_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_topn_traffic_statistics_invoker(self, request):
        http_info = self._list_topn_traffic_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_topn_traffic_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/topn-traffic-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopnTrafficStatisticsResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_transfers(self, request):
        r"""查询日志转储

        该接口用于查询OBS转储，DIS转储，DMS转储配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTransfers
        :type request: :class:`huaweicloudsdklts.v2.ListTransfersRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListTransfersResponse`
        """
        http_info = self._list_transfers_http_info(request)
        return self._call_api(**http_info)

    def list_transfers_invoker(self, request):
        http_info = self._list_transfers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_transfers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/transfers",
            "request_type": request.__class__.__name__,
            "response_type": "ListTransfersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_transfer_type' in local_var_params:
            query_params.append(('log_transfer_type', local_var_params['log_transfer_type']))
        if 'log_group_name' in local_var_params:
            query_params.append(('log_group_name', local_var_params['log_group_name']))
        if 'log_stream_name' in local_var_params:
            query_params.append(('log_stream_name', local_var_params['log_stream_name']))

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

    def register_dms_kafka_instance(self, request):
        r"""注册DMS kafka实例

        该接口用于注册DMS kafka实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterDmsKafkaInstance
        :type request: :class:`huaweicloudsdklts.v2.RegisterDmsKafkaInstanceRequest`
        :rtype: :class:`huaweicloudsdklts.v2.RegisterDmsKafkaInstanceResponse`
        """
        http_info = self._register_dms_kafka_instance_http_info(request)
        return self._call_api(**http_info)

    def register_dms_kafka_instance_invoker(self, request):
        http_info = self._register_dms_kafka_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_dms_kafka_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/dms/kafka-instance",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterDmsKafkaInstanceResponse"
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
            ['application/json;charset=UTF-8'])

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

    def show_admin_config(self, request):
        r"""获取日志汇聚开关

        只能由管理员或者委托管理员调用    获取日志汇聚开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAdminConfig
        :type request: :class:`huaweicloudsdklts.v2.ShowAdminConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowAdminConfigResponse`
        """
        http_info = self._show_admin_config_http_info(request)
        return self._call_api(**http_info)

    def show_admin_config_invoker(self, request):
        http_info = self._show_admin_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_admin_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/lts/log-converge-config/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAdminConfigResponse"
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

    def show_log_converge_config(self, request):
        r"""获取组织成员汇聚配置

        只能由组织管理员或者委托管理员调用    获取组织成员汇聚配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogConvergeConfig
        :type request: :class:`huaweicloudsdklts.v2.ShowLogConvergeConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowLogConvergeConfigResponse`
        """
        http_info = self._show_log_converge_config_http_info(request)
        return self._call_api(**http_info)

    def show_log_converge_config_invoker(self, request):
        http_info = self._show_log_converge_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_log_converge_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/lts/log-converge-config/{member_account_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogConvergeConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'member_account_id' in local_var_params:
            path_params['member_account_id'] = local_var_params['member_account_id']

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

    def show_member_group_and_stream(self, request):
        r"""获取组织成员日志组日志流

        只能由管理员或者委托管理员调用，获取组织成员日志组日志流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMemberGroupAndStream
        :type request: :class:`huaweicloudsdklts.v2.ShowMemberGroupAndStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowMemberGroupAndStreamResponse`
        """
        http_info = self._show_member_group_and_stream_http_info(request)
        return self._call_api(**http_info)

    def show_member_group_and_stream_invoker(self, request):
        http_info = self._show_member_group_and_stream_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_member_group_and_stream_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/lts/{member_account_id}/all-streams",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMemberGroupAndStreamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'member_account_id' in local_var_params:
            path_params['member_account_id'] = local_var_params['member_account_id']

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

    def show_notification_template(self, request):
        r"""查询单个消息模板

        该接口用于查询单个通知模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.ShowNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowNotificationTemplateResponse`
        """
        http_info = self._show_notification_template_http_info(request)
        return self._call_api(**http_info)

    def show_notification_template_invoker(self, request):
        http_info = self._show_notification_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_notification_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{domain_id}/lts/events/notification/template/{template_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNotificationTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

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

    def show_struct_template(self, request):
        r"""查询结构化配置

        该接口用于查询指定日志流下的结构化配置内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.ShowStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowStructTemplateResponse`
        """
        http_info = self._show_struct_template_http_info(request)
        return self._call_api(**http_info)

    def show_struct_template_invoker(self, request):
        http_info = self._show_struct_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_struct_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/lts/struct/template",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStructTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_group_id' in local_var_params:
            query_params.append(('logGroupId', local_var_params['log_group_id']))
        if 'log_stream_id' in local_var_params:
            query_params.append(('logStreamId', local_var_params['log_stream_id']))

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

    def update_access_config(self, request):
        r"""修改日志接入

        修改日志接入
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccessConfig
        :type request: :class:`huaweicloudsdklts.v2.UpdateAccessConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateAccessConfigResponse`
        """
        http_info = self._update_access_config_http_info(request)
        return self._call_api(**http_info)

    def update_access_config_invoker(self, request):
        http_info = self._update_access_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_access_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/lts/access-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccessConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_host_group(self, request):
        r"""修改主机组

        修改主机组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHostGroup
        :type request: :class:`huaweicloudsdklts.v2.UpdateHostGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateHostGroupResponse`
        """
        http_info = self._update_host_group_http_info(request)
        return self._call_api(**http_info)

    def update_host_group_invoker(self, request):
        http_info = self._update_host_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_host_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/lts/host-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHostGroupResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_keywords_alarm_rule(self, request):
        r"""修改关键词告警规则

        该接口用于修改关键词告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateKeywordsAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.UpdateKeywordsAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateKeywordsAlarmRuleResponse`
        """
        http_info = self._update_keywords_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def update_keywords_alarm_rule_invoker(self, request):
        http_info = self._update_keywords_alarm_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_keywords_alarm_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/lts/alarms/keywords-alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKeywordsAlarmRuleResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_log_converge_config(self, request):
        r"""更新汇聚配置

        只能由管理员或者委托管理员 ,更新汇聚配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLogConvergeConfig
        :type request: :class:`huaweicloudsdklts.v2.UpdateLogConvergeConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateLogConvergeConfigResponse`
        """
        http_info = self._update_log_converge_config_http_info(request)
        return self._call_api(**http_info)

    def update_log_converge_config_invoker(self, request):
        http_info = self._update_log_converge_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_log_converge_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/lts/log-converge-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogConvergeConfigResponse"
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

    def update_log_group(self, request):
        r"""修改日志组

        该接口用于修改指定日志组下的日志存储时长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLogGroup
        :type request: :class:`huaweicloudsdklts.v2.UpdateLogGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateLogGroupResponse`
        """
        http_info = self._update_log_group_http_info(request)
        return self._call_api(**http_info)

    def update_log_group_invoker(self, request):
        http_info = self._update_log_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_log_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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

    def update_log_stream(self, request):
        r"""修改日志流

        该接口用于修改指定日志流下的日志存储时长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLogStream
        :type request: :class:`huaweicloudsdklts.v2.UpdateLogStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateLogStreamResponse`
        """
        http_info = self._update_log_stream_http_info(request)
        return self._call_api(**http_info)

    def update_log_stream_invoker(self, request):
        http_info = self._update_log_stream_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_log_stream_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/groups/{log_group_id}/streams-ttl/{log_stream_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogStreamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_notification_template(self, request):
        r"""修改消息模板

        该接口用于修改通知模板,根据名称进行修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.UpdateNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateNotificationTemplateResponse`
        """
        http_info = self._update_notification_template_http_info(request)
        return self._call_api(**http_info)

    def update_notification_template_invoker(self, request):
        http_info = self._update_notification_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_notification_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/{domain_id}/lts/events/notification/templates",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNotificationTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_struct_config(self, request):
        r"""通过结构化模板修改结构化配置（新）

        该接口通过结构化模板修改结构化配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStructConfig
        :type request: :class:`huaweicloudsdklts.v2.UpdateStructConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateStructConfigResponse`
        """
        http_info = self._update_struct_config_http_info(request)
        return self._call_api(**http_info)

    def update_struct_config_invoker(self, request):
        http_info = self._update_struct_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_struct_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/lts/struct/template",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStructConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_struct_template(self, request):
        r"""修改结构化配置

        该接口用于修改指定日志流下的结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.UpdateStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateStructTemplateResponse`
        """
        http_info = self._update_struct_template_http_info(request)
        return self._call_api(**http_info)

    def update_struct_template_invoker(self, request):
        http_info = self._update_struct_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_struct_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/lts/struct/template",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStructTemplateResponse"
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

    def update_switch(self, request):
        r"""修改日志汇聚开关

        只能由管理员或者委托管理员调用     修改日志汇聚开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSwitch
        :type request: :class:`huaweicloudsdklts.v2.UpdateSwitchRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateSwitchResponse`
        """
        http_info = self._update_switch_http_info(request)
        return self._call_api(**http_info)

    def update_switch_invoker(self, request):
        http_info = self._update_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_switch_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/lts/log-converge-config/switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_converge_switch' in local_var_params:
            query_params.append(('log_converge_switch', local_var_params['log_converge_switch']))

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

    def update_transfer(self, request):
        r"""更新日志转储

        该接口用于更新OBS转储，DIS转储，DMS转储。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTransfer
        :type request: :class:`huaweicloudsdklts.v2.UpdateTransferRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateTransferResponse`
        """
        http_info = self._update_transfer_http_info(request)
        return self._call_api(**http_info)

    def update_transfer_invoker(self, request):
        http_info = self._update_transfer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_transfer_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/transfers",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTransferResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_aom_mapping_rules(self, request):
        r"""创建接入规则

        该接口用于创建aom日志接入lts规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAomMappingRules
        :type request: :class:`huaweicloudsdklts.v2.CreateAomMappingRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateAomMappingRulesResponse`
        """
        http_info = self._create_aom_mapping_rules_http_info(request)
        return self._call_api(**http_info)

    def create_aom_mapping_rules_invoker(self, request):
        http_info = self._create_aom_mapping_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_aom_mapping_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/aom-mapping",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAomMappingRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_batch' in local_var_params:
            query_params.append(('isBatch', local_var_params['is_batch']))

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

    def delete_aom_mapping_rules(self, request):
        r"""删除接入规则

        该接口用于删除lts接入规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAomMappingRules
        :type request: :class:`huaweicloudsdklts.v2.DeleteAomMappingRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteAomMappingRulesResponse`
        """
        http_info = self._delete_aom_mapping_rules_http_info(request)
        return self._call_api(**http_info)

    def delete_aom_mapping_rules_invoker(self, request):
        http_info = self._delete_aom_mapping_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_aom_mapping_rules_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/lts/aom-mapping",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAomMappingRulesResponse"
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

    def show_aom_mapping_rule(self, request):
        r"""查询单个接入规则

        该接口用于查询单个aom日志接入lts
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAomMappingRule
        :type request: :class:`huaweicloudsdklts.v2.ShowAomMappingRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowAomMappingRuleResponse`
        """
        http_info = self._show_aom_mapping_rule_http_info(request)
        return self._call_api(**http_info)

    def show_aom_mapping_rule_invoker(self, request):
        http_info = self._show_aom_mapping_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aom_mapping_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/lts/aom-mapping/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAomMappingRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_aom_mapping_rules(self, request):
        r"""查询所有接入规则

        该接口用于查询aom日志所有接入lts规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAomMappingRules
        :type request: :class:`huaweicloudsdklts.v2.ShowAomMappingRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowAomMappingRulesResponse`
        """
        http_info = self._show_aom_mapping_rules_http_info(request)
        return self._call_api(**http_info)

    def show_aom_mapping_rules_invoker(self, request):
        http_info = self._show_aom_mapping_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aom_mapping_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/lts/aom-mapping",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAomMappingRulesResponse"
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

    def update_aom_mapping_rules(self, request):
        r"""修改接入规则

        该接口用于修改接入规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAomMappingRules
        :type request: :class:`huaweicloudsdklts.v2.UpdateAomMappingRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateAomMappingRulesResponse`
        """
        http_info = self._update_aom_mapping_rules_http_info(request)
        return self._call_api(**http_info)

    def update_aom_mapping_rules_invoker(self, request):
        http_info = self._update_aom_mapping_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_aom_mapping_rules_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/lts/aom-mapping",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAomMappingRulesResponse"
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

    def consumer_group_heart_beat(self, request):
        r"""消费者发送心跳到服务端

        消费者发送心跳到服务端
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConsumerGroupHeartBeat
        :type request: :class:`huaweicloudsdklts.v2.ConsumerGroupHeartBeatRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ConsumerGroupHeartBeatResponse`
        """
        http_info = self._consumer_group_heart_beat_http_info(request)
        return self._call_api(**http_info)

    def consumer_group_heart_beat_invoker(self, request):
        http_info = self._consumer_group_heart_beat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _consumer_group_heart_beat_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/consumer-groups/{consumer_group_name}/heartbeat",
            "request_type": request.__class__.__name__,
            "response_type": "ConsumerGroupHeartBeatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']
        if 'consumer_group_name' in local_var_params:
            path_params['consumer_group_name'] = local_var_params['consumer_group_name']

        query_params = []
        if 'consumer_name' in local_var_params:
            query_params.append(('consumer_name', local_var_params['consumer_name']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_consumer_group(self, request):
        r"""创建消费组

        创建消费组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConsumerGroup
        :type request: :class:`huaweicloudsdklts.v2.CreateConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateConsumerGroupResponse`
        """
        http_info = self._create_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def create_consumer_group_invoker(self, request):
        http_info = self._create_consumer_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_consumer_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/consumer-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_consumer_group(self, request):
        r"""删除消费组

        删除消费组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConsumerGroup
        :type request: :class:`huaweicloudsdklts.v2.DeleteConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteConsumerGroupResponse`
        """
        http_info = self._delete_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def delete_consumer_group_invoker(self, request):
        http_info = self._delete_consumer_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_consumer_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/consumer-groups/{consumer_group_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']
        if 'consumer_group_name' in local_var_params:
            path_params['consumer_group_name'] = local_var_params['consumer_group_name']

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

    def list_consumer_group(self, request):
        r"""查询消费组列表

        查询消费组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConsumerGroup
        :type request: :class:`huaweicloudsdklts.v2.ListConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListConsumerGroupResponse`
        """
        http_info = self._list_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def list_consumer_group_invoker(self, request):
        http_info = self._list_consumer_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_consumer_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/consumer-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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

    def list_details_consumer_group(self, request):
        r"""查询消费组详情

        查询消费组详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDetailsConsumerGroup
        :type request: :class:`huaweicloudsdklts.v2.ListDetailsConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListDetailsConsumerGroupResponse`
        """
        http_info = self._list_details_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def list_details_consumer_group_invoker(self, request):
        http_info = self._list_details_consumer_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_details_consumer_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/consumer-groups/{consumer_group_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListDetailsConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']
        if 'consumer_group_name' in local_var_params:
            path_params['consumer_group_name'] = local_var_params['consumer_group_name']

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

    def show_cursor_by_time(self, request):
        r"""通过时间获取消费游标

        通过时间查询cursor
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCursorByTime
        :type request: :class:`huaweicloudsdklts.v2.ShowCursorByTimeRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowCursorByTimeResponse`
        """
        http_info = self._show_cursor_by_time_http_info(request)
        return self._call_api(**http_info)

    def show_cursor_by_time_invoker(self, request):
        http_info = self._show_cursor_by_time_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cursor_by_time_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/shards/{shard_id}/cursor",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCursorByTimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']
        if 'shard_id' in local_var_params:
            path_params['shard_id'] = local_var_params['shard_id']

        query_params = []
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))

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

    def show_cursor_time(self, request):
        r"""通过消费游标获取时间

        通过cursor查询服务端时间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCursorTime
        :type request: :class:`huaweicloudsdklts.v2.ShowCursorTimeRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowCursorTimeResponse`
        """
        http_info = self._show_cursor_time_http_info(request)
        return self._call_api(**http_info)

    def show_cursor_time_invoker(self, request):
        http_info = self._show_cursor_time_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cursor_time_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/shards/{shard_id}/time",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCursorTimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']
        if 'shard_id' in local_var_params:
            path_params['shard_id'] = local_var_params['shard_id']

        query_params = []
        if 'cursor' in local_var_params:
            query_params.append(('cursor', local_var_params['cursor']))

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

    def show_log_stream_shards(self, request):
        r"""流消费获取Shards

        流消费获取所有的query shards
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogStreamShards
        :type request: :class:`huaweicloudsdklts.v2.ShowLogStreamShardsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowLogStreamShardsResponse`
        """
        http_info = self._show_log_stream_shards_http_info(request)
        return self._call_api(**http_info)

    def show_log_stream_shards_invoker(self, request):
        http_info = self._show_log_stream_shards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_log_stream_shards_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/shards",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogStreamShardsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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

    def update_check_point(self, request):
        r"""更新消费组位点

        更新消费组位点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCheckPoint
        :type request: :class:`huaweicloudsdklts.v2.UpdateCheckPointRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateCheckPointResponse`
        """
        http_info = self._update_check_point_http_info(request)
        return self._call_api(**http_info)

    def update_check_point_invoker(self, request):
        http_info = self._update_check_point_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_check_point_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/groups/{group_id}/streams/{stream_id}/consumer-groups/{consumer_group_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCheckPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']
        if 'consumer_group_name' in local_var_params:
            path_params['consumer_group_name'] = local_var_params['consumer_group_name']

        query_params = []
        if 'consumer_name' in local_var_params:
            query_params.append(('consumer_name', local_var_params['consumer_name']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_sql_alarm_rule(self, request):
        r"""创建SQL告警规则

        该接口用于创建SQL告警，目前每个帐户最多可以创建共200个关键词告警与SQL告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.CreateSqlAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateSqlAlarmRuleResponse`
        """
        http_info = self._create_sql_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def create_sql_alarm_rule_invoker(self, request):
        http_info = self._create_sql_alarm_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sql_alarm_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/lts/alarms/sql-alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSqlAlarmRuleResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_sql_alarm_rule(self, request):
        r"""删除SQL告警规则

        该接口用于删除SQL告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.DeleteSqlAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteSqlAlarmRuleResponse`
        """
        http_info = self._delete_sql_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_sql_alarm_rule_invoker(self, request):
        http_info = self._delete_sql_alarm_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sql_alarm_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/lts/alarms/sql-alarm-rule/{sql_alarm_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSqlAlarmRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sql_alarm_rule_id' in local_var_params:
            path_params['sql_alarm_rule_id'] = local_var_params['sql_alarm_rule_id']

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

    def list_sql_alarm_rules(self, request):
        r"""查询SQL告警规则

        该接口用于查询SQL告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlAlarmRules
        :type request: :class:`huaweicloudsdklts.v2.ListSqlAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListSqlAlarmRulesResponse`
        """
        http_info = self._list_sql_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def list_sql_alarm_rules_invoker(self, request):
        http_info = self._list_sql_alarm_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_alarm_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/lts/alarms/sql-alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlAlarmRulesResponse"
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

    def update_alarm_rule_status(self, request):
        r"""切换告警规则状态

        改变告警规则状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmRuleStatus
        :type request: :class:`huaweicloudsdklts.v2.UpdateAlarmRuleStatusRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateAlarmRuleStatusResponse`
        """
        http_info = self._update_alarm_rule_status_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_rule_status_invoker(self, request):
        http_info = self._update_alarm_rule_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_rule_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/lts/alarms/status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmRuleStatusResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_sql_alarm_rule(self, request):
        r"""修改SQL告警规则

        该接口用于修改SQL告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSqlAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.UpdateSqlAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateSqlAlarmRuleResponse`
        """
        http_info = self._update_sql_alarm_rule_http_info(request)
        return self._call_api(**http_info)

    def update_sql_alarm_rule_invoker(self, request):
        http_info = self._update_sql_alarm_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sql_alarm_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/lts/alarms/sql-alarm-rule",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSqlAlarmRuleResponse"
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
            ['application/json;charset=UTF-8'])

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

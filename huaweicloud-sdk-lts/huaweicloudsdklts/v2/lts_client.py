# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


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
        """创建日志接入

        创建日志接入
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccessConfig
        :type request: :class:`huaweicloudsdklts.v2.CreateAccessConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateAccessConfigResponse`
        """
        return self._create_access_config_with_http_info(request)

    def _create_access_config_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/access-config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAccessConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dash_board(self, request):
        """创建仪表盘

        创建仪表盘
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDashBoard
        :type request: :class:`huaweicloudsdklts.v2.CreateDashBoardRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateDashBoardResponse`
        """
        return self._create_dash_board_with_http_info(request)

    def _create_dash_board_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/dashboard',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDashBoardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dashboard_group(self, request):
        """创建仪表盘分组

        创建仪表盘分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDashboardGroup
        :type request: :class:`huaweicloudsdklts.v2.CreateDashboardGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateDashboardGroupResponse`
        """
        return self._create_dashboard_group_with_http_info(request)

    def _create_dashboard_group_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/dashboard-group',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDashboardGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_host_group(self, request):
        """创建主机组

        创建主机组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHostGroup
        :type request: :class:`huaweicloudsdklts.v2.CreateHostGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateHostGroupResponse`
        """
        return self._create_host_group_with_http_info(request)

    def _create_host_group_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/host-group',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateHostGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_keywords_alarm_rule(self, request):
        """创建关键词告警规则

        该接口用于创建关键词告警，目前每个帐户最多可以创建共200个关键词告警与SQL告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateKeywordsAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.CreateKeywordsAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateKeywordsAlarmRuleResponse`
        """
        return self._create_keywords_alarm_rule_with_http_info(request)

    def _create_keywords_alarm_rule_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/alarms/keywords-alarm-rule',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateKeywordsAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_log_dump_obs(self, request):
        """创建日志转储（旧版）

        该接口用于将指定的一个或多个日志流的日志转储到OBS服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLogDumpObs
        :type request: :class:`huaweicloudsdklts.v2.CreateLogDumpObsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateLogDumpObsResponse`
        """
        return self._create_log_dump_obs_with_http_info(request)

    def _create_log_dump_obs_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/log-dump/obs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLogDumpObsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_log_group(self, request):
        """创建日志组

        该接口用于创建一个日志组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLogGroup
        :type request: :class:`huaweicloudsdklts.v2.CreateLogGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateLogGroupResponse`
        """
        return self._create_log_group_with_http_info(request)

    def _create_log_group_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLogGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_log_stream(self, request):
        """创建日志流

        该接口用于创建某个指定日志组下的日志流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLogStream
        :type request: :class:`huaweicloudsdklts.v2.CreateLogStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateLogStreamResponse`
        """
        return self._create_log_stream_with_http_info(request)

    def _create_log_stream_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLogStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_notification_template(self, request):
        """创建消息模板

        该接口用于创建通知模板，目前每个帐户最多可以创建共100个通知模板，创建后名称不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.CreateNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateNotificationTemplateResponse`
        """
        return self._create_notification_template_with_http_info(request)

    def _create_notification_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/{domain_id}/lts/events/notification/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNotificationTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_search_criterias(self, request):
        """添加快速查询

        添加快速查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSearchCriterias
        :type request: :class:`huaweicloudsdklts.v2.CreateSearchCriteriasRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateSearchCriteriasResponse`
        """
        return self._create_search_criterias_with_http_info(request)

    def _create_search_criterias_with_http_info(self, request):
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
            resource_path='/v1.0/{project_id}/groups/{group_id}/topics/{topic_id}/search-criterias',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSearchCriteriasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_struct_config(self, request):
        """通过结构化模板创建结构化配置（新）

        该接口通过结构化模板创建结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStructConfig
        :type request: :class:`huaweicloudsdklts.v2.CreateStructConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateStructConfigResponse`
        """
        return self._create_struct_config_with_http_info(request)

    def _create_struct_config_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/struct/template',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStructConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_struct_template(self, request):
        """创建结构化配置

        该接口用于创建指定日志流下的结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.CreateStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateStructTemplateResponse`
        """
        return self._create_struct_template_with_http_info(request)

    def _create_struct_template_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/lts/struct/template',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStructTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tags(self, request):
        """create_tags

        添加标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTags
        :type request: :class:`huaweicloudsdklts.v2.CreateTagsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateTagsResponse`
        """
        return self._create_tags_with_http_info(request)

    def _create_tags_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_transfer(self, request):
        """创建日志转储（新版）

        该接口用于创建OBS转储，DIS转储，DMS转储。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTransfer
        :type request: :class:`huaweicloudsdklts.v2.CreateTransferRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateTransferResponse`
        """
        return self._create_transfer_with_http_info(request)

    def _create_transfer_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/transfers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTransferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def createfavorite(self, request):
        """查询Demo

        创建日志收藏
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Createfavorite
        :type request: :class:`huaweicloudsdklts.v2.CreatefavoriteRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreatefavoriteResponse`
        """
        return self._createfavorite_with_http_info(request)

    def _createfavorite_with_http_info(self, request):
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
            resource_path='/v1.0/{project_id}/lts/favorite',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatefavoriteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_access_config(self, request):
        """删除日志接入

        删除日志接入
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAccessConfig
        :type request: :class:`huaweicloudsdklts.v2.DeleteAccessConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteAccessConfigResponse`
        """
        return self._delete_access_config_with_http_info(request)

    def _delete_access_config_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/access-config',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAccessConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_active_alarms(self, request):
        """删除活动告警

        该接口用于删除活动告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteActiveAlarms
        :type request: :class:`huaweicloudsdklts.v2.DeleteActiveAlarmsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteActiveAlarmsResponse`
        """
        return self._delete_active_alarms_with_http_info(request)

    def _delete_active_alarms_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/{domain_id}/lts/alarms/sql-alarm/clear',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteActiveAlarmsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_dashboard(self, request):
        """删除仪表盘

        删除仪表盘
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDashboard
        :type request: :class:`huaweicloudsdklts.v2.DeleteDashboardRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteDashboardResponse`
        """
        return self._delete_dashboard_with_http_info(request)

    def _delete_dashboard_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/dashboard',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDashboardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_host_group(self, request):
        """删除主机组

        删除主机组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHostGroup
        :type request: :class:`huaweicloudsdklts.v2.DeleteHostGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteHostGroupResponse`
        """
        return self._delete_host_group_with_http_info(request)

    def _delete_host_group_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/host-group',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteHostGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_keywords_alarm_rule(self, request):
        """删除关键词告警规则

        该接口用于删除关键词告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteKeywordsAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.DeleteKeywordsAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteKeywordsAlarmRuleResponse`
        """
        return self._delete_keywords_alarm_rule_with_http_info(request)

    def _delete_keywords_alarm_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keywords_alarm_rule_id' in local_var_params:
            path_params['keywords_alarm_rule_id'] = local_var_params['keywords_alarm_rule_id']

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
            resource_path='/v2/{project_id}/lts/alarms/keywords-alarm-rule/{keywords_alarm_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteKeywordsAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_log_group(self, request):
        """删除日志组

        该接口用于删除指定日志组。当日志组中的日志流配置了日志转储，需要取消日志转储后才可删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogGroup
        :type request: :class:`huaweicloudsdklts.v2.DeleteLogGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteLogGroupResponse`
        """
        return self._delete_log_group_with_http_info(request)

    def _delete_log_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteLogGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_log_stream(self, request):
        """删除日志流

        该接口用于删除指定日志组下的指定日志流。当该日志流配置了日志转储，需要取消日志转储后才可删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogStream
        :type request: :class:`huaweicloudsdklts.v2.DeleteLogStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteLogStreamResponse`
        """
        return self._delete_log_stream_with_http_info(request)

    def _delete_log_stream_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteLogStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_notification_template(self, request):
        """删除消息模板

        该接口用于删除通知模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.DeleteNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteNotificationTemplateResponse`
        """
        return self._delete_notification_template_with_http_info(request)

    def _delete_notification_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/{domain_id}/lts/events/notification/templates',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNotificationTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_search_criterias(self, request):
        """删除快速查询

        删除快速查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSearchCriterias
        :type request: :class:`huaweicloudsdklts.v2.DeleteSearchCriteriasRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteSearchCriteriasResponse`
        """
        return self._delete_search_criterias_with_http_info(request)

    def _delete_search_criterias_with_http_info(self, request):
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
            resource_path='/v1.0/{project_id}/groups/{group_id}/topics/{topic_id}/search-criterias',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSearchCriteriasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_struct_template(self, request):
        """删除结构化配置

        该接口用于删除指定日志流下的结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.DeleteStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteStructTemplateResponse`
        """
        return self._delete_struct_template_with_http_info(request)

    def _delete_struct_template_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/struct/template',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStructTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_transfer(self, request):
        """删除日志转储

        该接口用于删除OBS转储，DIS转储，DMS转储。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTransfer
        :type request: :class:`huaweicloudsdklts.v2.DeleteTransferRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteTransferResponse`
        """
        return self._delete_transfer_with_http_info(request)

    def _delete_transfer_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_transfer_id' in local_var_params:
            query_params.append(('log_transfer_id', local_var_params['log_transfer_id']))

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
            resource_path='/v2/{project_id}/transfers',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTransferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def deletefavorite(self, request):
        """取消收藏

        取消收藏
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Deletefavorite
        :type request: :class:`huaweicloudsdklts.v2.DeletefavoriteRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeletefavoriteResponse`
        """
        return self._deletefavorite_with_http_info(request)

    def _deletefavorite_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'fav_res_id' in local_var_params:
            path_params['fav_res_id'] = local_var_params['fav_res_id']

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
            resource_path='/v1.0/{project_id}/lts/favorite/{fav_res_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletefavoriteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_log_collection(self, request):
        """关闭超额采集开关

        该接口用于将超额采集日志功能关闭。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableLogCollection
        :type request: :class:`huaweicloudsdklts.v2.DisableLogCollectionRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DisableLogCollectionResponse`
        """
        return self._disable_log_collection_with_http_info(request)

    def _disable_log_collection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/collection/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableLogCollectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_log_collection(self, request):
        """打开超额采集开关

        该接口用于将超额采集日志功能打开。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableLogCollection
        :type request: :class:`huaweicloudsdklts.v2.EnableLogCollectionRequest`
        :rtype: :class:`huaweicloudsdklts.v2.EnableLogCollectionResponse`
        """
        return self._enable_log_collection_with_http_info(request)

    def _enable_log_collection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/collection/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableLogCollectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_access_config(self, request):
        """查询日志接入

        查询日志接入列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessConfig
        :type request: :class:`huaweicloudsdklts.v2.ListAccessConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListAccessConfigResponse`
        """
        return self._list_access_config_with_http_info(request)

    def _list_access_config_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/access-config-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccessConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_active_or_history_alarms(self, request):
        """查询活动或历史告警列表

        该接口用于查询告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListActiveOrHistoryAlarms
        :type request: :class:`huaweicloudsdklts.v2.ListActiveOrHistoryAlarmsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListActiveOrHistoryAlarmsResponse`
        """
        return self._list_active_or_history_alarms_with_http_info(request)

    def _list_active_or_history_alarms_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/{domain_id}/lts/alarms/sql-alarm/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListActiveOrHistoryAlarmsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_breif_struct_template(self, request):
        """查询结构化模板简略列表

        该接口用于查询结构化模板简略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBreifStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.ListBreifStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListBreifStructTemplateResponse`
        """
        return self._list_breif_struct_template_with_http_info(request)

    def _list_breif_struct_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/lts/struct/customtemplate/list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBreifStructTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_charts(self, request):
        """查询日志流图表

        该接口用于查询日志流图表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCharts
        :type request: :class:`huaweicloudsdklts.v2.ListChartsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListChartsResponse`
        """
        return self._list_charts_with_http_info(request)

    def _list_charts_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/charts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListChartsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_criterias(self, request):
        """获取快速查询

        获取快速查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCriterias
        :type request: :class:`huaweicloudsdklts.v2.ListCriteriasRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListCriteriasResponse`
        """
        return self._list_criterias_with_http_info(request)

    def _list_criterias_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/groups/{group_id}/topics/{topic_id}/search-criterias',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCriteriasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_history_sql(self, request):
        """查询用户历史sql

        查询用户历史sql
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistorySql
        :type request: :class:`huaweicloudsdklts.v2.ListHistorySqlRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListHistorySqlResponse`
        """
        return self._list_history_sql_with_http_info(request)

    def _list_history_sql_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/lts/history-sql',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHistorySqlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host(self, request):
        """查询主机信息

        查询主机列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHost
        :type request: :class:`huaweicloudsdklts.v2.ListHostRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListHostResponse`
        """
        return self._list_host_with_http_info(request)

    def _list_host_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/host-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_group(self, request):
        """查询主机组

        查询主机组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostGroup
        :type request: :class:`huaweicloudsdklts.v2.ListHostGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListHostGroupResponse`
        """
        return self._list_host_group_with_http_info(request)

    def _list_host_group_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/host-group-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_keywords_alarm_rules(self, request):
        """查询关键词告警规则

        该接口用于查询关键词告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListKeywordsAlarmRules
        :type request: :class:`huaweicloudsdklts.v2.ListKeywordsAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListKeywordsAlarmRulesResponse`
        """
        return self._list_keywords_alarm_rules_with_http_info(request)

    def _list_keywords_alarm_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/lts/alarms/keywords-alarm-rule',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKeywordsAlarmRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_log_groups(self, request):
        """查询账号下所有日志组

        该接口用于查询账号下所有日志组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogGroups
        :type request: :class:`huaweicloudsdklts.v2.ListLogGroupsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogGroupsResponse`
        """
        return self._list_log_groups_with_http_info(request)

    def _list_log_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLogGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_log_histogram(self, request):
        """查询日志直方图

        查询关键词搜索条数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogHistogram
        :type request: :class:`huaweicloudsdklts.v2.ListLogHistogramRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogHistogramResponse`
        """
        return self._list_log_histogram_with_http_info(request)

    def _list_log_histogram_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/keyword-count',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLogHistogramResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_log_stream(self, request):
        """查询指定日志组下的所有日志流

        该接口用于查询指定日志组下的所有日志流信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogStream
        :type request: :class:`huaweicloudsdklts.v2.ListLogStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogStreamResponse`
        """
        return self._list_log_stream_with_http_info(request)

    def _list_log_stream_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLogStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_log_streams(self, request):
        """查询日志流信息

        该接口用于查询LTS日志流信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogStreams
        :type request: :class:`huaweicloudsdklts.v2.ListLogStreamsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogStreamsResponse`
        """
        return self._list_log_streams_with_http_info(request)

    def _list_log_streams_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_group_name' in local_var_params:
            query_params.append(('log_group_name', local_var_params['log_group_name']))
        if 'log_stream_name' in local_var_params:
            query_params.append(('log_stream_name', local_var_params['log_stream_name']))
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
            resource_path='/v2/{project_id}/log-streams',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLogStreamsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_logs(self, request):
        """查询日志

        该接口用于查询指定日志流下的日志内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogs
        :type request: :class:`huaweicloudsdklts.v2.ListLogsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListLogsResponse`
        """
        return self._list_logs_with_http_info(request)

    def _list_logs_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/content/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notification_template(self, request):
        """预览消息模板邮件格式

        该接口用于预览通知模板邮件格式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.ListNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListNotificationTemplateResponse`
        """
        return self._list_notification_template_with_http_info(request)

    def _list_notification_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/{domain_id}/lts/events/notification/templates/view',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotificationTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notification_templates(self, request):
        """查询消息模板

        该接口用于查询通知模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationTemplates
        :type request: :class:`huaweicloudsdklts.v2.ListNotificationTemplatesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListNotificationTemplatesResponse`
        """
        return self._list_notification_templates_with_http_info(request)

    def _list_notification_templates_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{domain_id}/lts/events/notification/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotificationTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notification_topics(self, request):
        """查询SMN主题

        该接口用于查询SMN主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationTopics
        :type request: :class:`huaweicloudsdklts.v2.ListNotificationTopicsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListNotificationTopicsResponse`
        """
        return self._list_notification_topics_with_http_info(request)

    def _list_notification_topics_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/lts/notifications/topics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotificationTopicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_query_all_search_criterias(self, request):
        """查询日志组下所有快速查询

        查询日志组下所有快速查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryAllSearchCriterias
        :type request: :class:`huaweicloudsdklts.v2.ListQueryAllSearchCriteriasRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListQueryAllSearchCriteriasResponse`
        """
        return self._list_query_all_search_criterias_with_http_info(request)

    def _list_query_all_search_criterias_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v1.0/{project_id}/lts/groups/{group_id}/search-criterias',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQueryAllSearchCriteriasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_query_structured_logs(self, request):
        """查询结构化日志

        该接口用于查询指定日志流下的结构化日志内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryStructuredLogs
        :type request: :class:`huaweicloudsdklts.v2.ListQueryStructuredLogsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListQueryStructuredLogsResponse`
        """
        return self._list_query_structured_logs_with_http_info(request)

    def _list_query_structured_logs_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams/{log_stream_id}/struct-content/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQueryStructuredLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_struct_template(self, request):
        """查询结构化模板

        该接口用于查询结构化模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.ListStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListStructTemplateResponse`
        """
        return self._list_struct_template_with_http_info(request)

    def _list_struct_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v3/{project_id}/lts/struct/customtemplate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStructTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_structured_logs_with_time_range(self, request):
        """查询结构化日志（新版）

        该接口用于查询指定日志流下的结构化日志内容（新版）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStructuredLogsWithTimeRange
        :type request: :class:`huaweicloudsdklts.v2.ListStructuredLogsWithTimeRangeRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListStructuredLogsWithTimeRangeResponse`
        """
        return self._list_structured_logs_with_time_range_with_http_info(request)

    def _list_structured_logs_with_time_range_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_stream_id' in local_var_params:
            path_params['log_stream_id'] = local_var_params['log_stream_id']

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
            resource_path='/v2/{project_id}/streams/{log_stream_id}/struct-content/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStructuredLogsWithTimeRangeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_time_line_traffic_statistics(self, request):
        """按时间段统计查询资源

        按时间段统计查询资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTimeLineTrafficStatistics
        :type request: :class:`huaweicloudsdklts.v2.ListTimeLineTrafficStatisticsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListTimeLineTrafficStatisticsResponse`
        """
        return self._list_time_line_traffic_statistics_with_http_info(request)

    def _list_time_line_traffic_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'timezone' in local_var_params:
            query_params.append(('timezone', local_var_params['timezone']))

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
            resource_path='/v2/{project_id}/lts/timeline-traffic-statistics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTimeLineTrafficStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_topn_traffic_statistics(self, request):
        """统计top n的日志组或日志流流量

        统计top n的日志组或日志流流量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTopnTrafficStatistics
        :type request: :class:`huaweicloudsdklts.v2.ListTopnTrafficStatisticsRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListTopnTrafficStatisticsResponse`
        """
        return self._list_topn_traffic_statistics_with_http_info(request)

    def _list_topn_traffic_statistics_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/topn-traffic-statistics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTopnTrafficStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transfers(self, request):
        """查询日志转储

        该接口用于查询OBS转储，DIS转储，DMS转储配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTransfers
        :type request: :class:`huaweicloudsdklts.v2.ListTransfersRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListTransfersResponse`
        """
        return self._list_transfers_with_http_info(request)

    def _list_transfers_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/transfers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTransfersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_dms_kafka_instance(self, request):
        """注册DMS kafka实例

        该接口用于注册DMS kafka实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterDmsKafkaInstance
        :type request: :class:`huaweicloudsdklts.v2.RegisterDmsKafkaInstanceRequest`
        :rtype: :class:`huaweicloudsdklts.v2.RegisterDmsKafkaInstanceResponse`
        """
        return self._register_dms_kafka_instance_with_http_info(request)

    def _register_dms_kafka_instance_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/dms/kafka-instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterDmsKafkaInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_admin_config(self, request):
        """获取日志汇聚开关

        只能由管理员或者委托管理员调用    获取日志汇聚开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAdminConfig
        :type request: :class:`huaweicloudsdklts.v2.ShowAdminConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowAdminConfigResponse`
        """
        return self._show_admin_config_with_http_info(request)

    def _show_admin_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/lts/log-converge-config/switch',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAdminConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_log_converge_config(self, request):
        """获取组织成员汇聚配置

        只能由组织管理员或者委托管理员调用    获取组织成员汇聚配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogConvergeConfig
        :type request: :class:`huaweicloudsdklts.v2.ShowLogConvergeConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowLogConvergeConfigResponse`
        """
        return self._show_log_converge_config_with_http_info(request)

    def _show_log_converge_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'member_account_id' in local_var_params:
            path_params['member_account_id'] = local_var_params['member_account_id']

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
            resource_path='/v1/{project_id}/lts/log-converge-config/{member_account_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLogConvergeConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_member_group_and_stream(self, request):
        """获取组织成员日志组日志流

        只能由管理员或者委托管理员调用，获取组织成员日志组日志流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMemberGroupAndStream
        :type request: :class:`huaweicloudsdklts.v2.ShowMemberGroupAndStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowMemberGroupAndStreamResponse`
        """
        return self._show_member_group_and_stream_with_http_info(request)

    def _show_member_group_and_stream_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'member_account_id' in local_var_params:
            path_params['member_account_id'] = local_var_params['member_account_id']

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
            resource_path='/v1/{project_id}/lts/{member_account_id}/all-streams',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMemberGroupAndStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_notification_template(self, request):
        """查询单个消息模板

        该接口用于查询单个通知模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.ShowNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowNotificationTemplateResponse`
        """
        return self._show_notification_template_with_http_info(request)

    def _show_notification_template_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{domain_id}/lts/events/notification/template/{template_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNotificationTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_struct_template(self, request):
        """查询结构化配置

        该接口用于查询指定日志流下的结构化配置内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.ShowStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowStructTemplateResponse`
        """
        return self._show_struct_template_with_http_info(request)

    def _show_struct_template_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/lts/struct/template',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStructTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_access_config(self, request):
        """修改日志接入

        修改日志接入
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccessConfig
        :type request: :class:`huaweicloudsdklts.v2.UpdateAccessConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateAccessConfigResponse`
        """
        return self._update_access_config_with_http_info(request)

    def _update_access_config_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/access-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAccessConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_host_group(self, request):
        """修改主机组

        修改主机组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHostGroup
        :type request: :class:`huaweicloudsdklts.v2.UpdateHostGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateHostGroupResponse`
        """
        return self._update_host_group_with_http_info(request)

    def _update_host_group_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/host-group',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateHostGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_keywords_alarm_rule(self, request):
        """修改关键词告警规则

        该接口用于修改关键词告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateKeywordsAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.UpdateKeywordsAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateKeywordsAlarmRuleResponse`
        """
        return self._update_keywords_alarm_rule_with_http_info(request)

    def _update_keywords_alarm_rule_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/alarms/keywords-alarm-rule',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateKeywordsAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_log_converge_config(self, request):
        """更新汇聚配置

        只能由管理员或者委托管理员 ,更新汇聚配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLogConvergeConfig
        :type request: :class:`huaweicloudsdklts.v2.UpdateLogConvergeConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateLogConvergeConfigResponse`
        """
        return self._update_log_converge_config_with_http_info(request)

    def _update_log_converge_config_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/lts/log-converge-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateLogConvergeConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_log_group(self, request):
        """修改日志组

        该接口用于修改指定日志组下的日志存储时长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLogGroup
        :type request: :class:`huaweicloudsdklts.v2.UpdateLogGroupRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateLogGroupResponse`
        """
        return self._update_log_group_with_http_info(request)

    def _update_log_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'log_group_id' in local_var_params:
            path_params['log_group_id'] = local_var_params['log_group_id']

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
            resource_path='/v2/{project_id}/groups/{log_group_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateLogGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_log_stream(self, request):
        """修改日志流

        该接口用于修改指定日志流下的日志存储时长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLogStream
        :type request: :class:`huaweicloudsdklts.v2.UpdateLogStreamRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateLogStreamResponse`
        """
        return self._update_log_stream_with_http_info(request)

    def _update_log_stream_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/groups/{log_group_id}/streams_ttl/{log_stream_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateLogStreamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_notification_template(self, request):
        """修改消息模板

        该接口用于修改通知模板,根据名称进行修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNotificationTemplate
        :type request: :class:`huaweicloudsdklts.v2.UpdateNotificationTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateNotificationTemplateResponse`
        """
        return self._update_notification_template_with_http_info(request)

    def _update_notification_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v2/{project_id}/{domain_id}/lts/events/notification/templates',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNotificationTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_struct_config(self, request):
        """通过结构化模板修改结构化配置（新）

        该接口通过结构化模板修改结构化配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStructConfig
        :type request: :class:`huaweicloudsdklts.v2.UpdateStructConfigRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateStructConfigResponse`
        """
        return self._update_struct_config_with_http_info(request)

    def _update_struct_config_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/lts/struct/template',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStructConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_struct_template(self, request):
        """修改结构化配置

        该接口用于修改指定日志流下的结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStructTemplate
        :type request: :class:`huaweicloudsdklts.v2.UpdateStructTemplateRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateStructTemplateResponse`
        """
        return self._update_struct_template_with_http_info(request)

    def _update_struct_template_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/lts/struct/template',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStructTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_switch(self, request):
        """修改日志汇聚开关

        只能由管理员或者委托管理员调用     修改日志汇聚开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSwitch
        :type request: :class:`huaweicloudsdklts.v2.UpdateSwitchRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateSwitchResponse`
        """
        return self._update_switch_with_http_info(request)

    def _update_switch_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_converge_switch' in local_var_params:
            query_params.append(('log_converge_switch', local_var_params['log_converge_switch']))

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
            resource_path='/v1/{project_id}/lts/log-converge-config/switch',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_transfer(self, request):
        """更新日志转储

        该接口用于更新OBS转储，DIS转储，DMS转储。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTransfer
        :type request: :class:`huaweicloudsdklts.v2.UpdateTransferRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateTransferResponse`
        """
        return self._update_transfer_with_http_info(request)

    def _update_transfer_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/transfers',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTransferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_aom_mapping_rules(self, request):
        """创建接入规则

        该接口用于创建aom日志接入lts规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAomMappingRules
        :type request: :class:`huaweicloudsdklts.v2.CreateAomMappingRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateAomMappingRulesResponse`
        """
        return self._create_aom_mapping_rules_with_http_info(request)

    def _create_aom_mapping_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_batch' in local_var_params:
            query_params.append(('isBatch', local_var_params['is_batch']))

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
            resource_path='/v2/{project_id}/lts/aom-mapping',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAomMappingRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_aom_mapping_rules(self, request):
        """删除接入规则

        该接口用于删除lts接入规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAomMappingRules
        :type request: :class:`huaweicloudsdklts.v2.DeleteAomMappingRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteAomMappingRulesResponse`
        """
        return self._delete_aom_mapping_rules_with_http_info(request)

    def _delete_aom_mapping_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/lts/aom-mapping',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAomMappingRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_aom_mapping_rule(self, request):
        """查询单个接入规则

        该接口用于查询单个aom日志接入lts
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAomMappingRule
        :type request: :class:`huaweicloudsdklts.v2.ShowAomMappingRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowAomMappingRuleResponse`
        """
        return self._show_aom_mapping_rule_with_http_info(request)

    def _show_aom_mapping_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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
            resource_path='/v2/{project_id}/lts/aom-mapping/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAomMappingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_aom_mapping_rules(self, request):
        """查询所有接入规则

        该接口用于查询aom日志所有接入lts规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAomMappingRules
        :type request: :class:`huaweicloudsdklts.v2.ShowAomMappingRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ShowAomMappingRulesResponse`
        """
        return self._show_aom_mapping_rules_with_http_info(request)

    def _show_aom_mapping_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/lts/aom-mapping',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAomMappingRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_aom_mapping_rules(self, request):
        """修改接入规则

        该接口用于修改接入规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAomMappingRules
        :type request: :class:`huaweicloudsdklts.v2.UpdateAomMappingRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateAomMappingRulesResponse`
        """
        return self._update_aom_mapping_rules_with_http_info(request)

    def _update_aom_mapping_rules_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/lts/aom-mapping',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAomMappingRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_sql_alarm_rule(self, request):
        """创建SQL告警规则

        该接口用于创建SQL告警，目前每个帐户最多可以创建共200个关键词告警与SQL告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.CreateSqlAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.CreateSqlAlarmRuleResponse`
        """
        return self._create_sql_alarm_rule_with_http_info(request)

    def _create_sql_alarm_rule_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/alarms/sql-alarm-rule',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSqlAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_sql_alarm_rule(self, request):
        """删除SQL告警规则

        该接口用于删除SQL告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.DeleteSqlAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.DeleteSqlAlarmRuleResponse`
        """
        return self._delete_sql_alarm_rule_with_http_info(request)

    def _delete_sql_alarm_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sql_alarm_rule_id' in local_var_params:
            path_params['sql_alarm_rule_id'] = local_var_params['sql_alarm_rule_id']

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
            resource_path='/v2/{project_id}/lts/alarms/sql-alarm-rule/{sql_alarm_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSqlAlarmRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sql_alarm_rules(self, request):
        """查询SQL告警规则

        该接口用于查询SQL告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlAlarmRules
        :type request: :class:`huaweicloudsdklts.v2.ListSqlAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdklts.v2.ListSqlAlarmRulesResponse`
        """
        return self._list_sql_alarm_rules_with_http_info(request)

    def _list_sql_alarm_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/lts/alarms/sql-alarm-rule',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSqlAlarmRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_rule_status(self, request):
        """切换告警规则状态

        改变告警规则状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmRuleStatus
        :type request: :class:`huaweicloudsdklts.v2.UpdateAlarmRuleStatusRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateAlarmRuleStatusResponse`
        """
        return self._update_alarm_rule_status_with_http_info(request)

    def _update_alarm_rule_status_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/alarms/status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlarmRuleStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_sql_alarm_rule(self, request):
        """修改SQL告警规则

        该接口用于修改SQL告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSqlAlarmRule
        :type request: :class:`huaweicloudsdklts.v2.UpdateSqlAlarmRuleRequest`
        :rtype: :class:`huaweicloudsdklts.v2.UpdateSqlAlarmRuleResponse`
        """
        return self._update_sql_alarm_rule_with_http_info(request)

    def _update_sql_alarm_rule_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/lts/alarms/sql-alarm-rule',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSqlAlarmRuleResponse',
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

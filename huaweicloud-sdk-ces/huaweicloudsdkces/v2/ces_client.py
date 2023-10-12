# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CesClient(Client):
    def __init__(self):
        super(CesClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkces.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CesClient":
            raise TypeError("client type error, support client type is CesClient")

        return ClientBuilder(clazz)

    def add_alarm_rule_resources(self, request):
        """批量增加告警规则资源

        批量增加告警规则资源(资源分组类型的告警规则不支持)，资源分组类型的修改请使用资源分组管理相关接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAlarmRuleResources
        :type request: :class:`huaweicloudsdkces.v2.AddAlarmRuleResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.AddAlarmRuleResourcesResponse`
        """
        return self._add_alarm_rule_resources_with_http_info(request)

    def _add_alarm_rule_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/resources/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddAlarmRuleResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_resources(self, request):
        """自定义资源分组批量增加关联资源

        给自定义资源分组,即类型为手动添加的资源分组,批量增加关联资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateResources
        :type request: :class:`huaweicloudsdkces.v2.BatchCreateResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchCreateResourcesResponse`
        """
        return self._batch_create_resources_with_http_info(request)

    def _batch_create_resources_with_http_info(self, request):
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/resource-groups/{group_id}/resources/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_alarm_rules(self, request):
        """批量删除告警规则

        批量删除告警规则V2接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteAlarmRulesResponse`
        """
        return self._batch_delete_alarm_rules_with_http_info(request)

    def _batch_delete_alarm_rules_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/alarms/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteAlarmRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_alarm_templates(self, request):
        """批量删除自定义告警模板

        批量删除自定义告警模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAlarmTemplates
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteAlarmTemplatesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteAlarmTemplatesResponse`
        """
        return self._batch_delete_alarm_templates_with_http_info(request)

    def _batch_delete_alarm_templates_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/alarm-templates/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteAlarmTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_notification_masks(self, request):
        """批量删除告警通知屏蔽规则

        批量删除告警通知屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteNotificationMasks
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteNotificationMasksRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteNotificationMasksResponse`
        """
        return self._batch_delete_notification_masks_with_http_info(request)

    def _batch_delete_notification_masks_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/notification-masks/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteNotificationMasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_one_click_alarms(self, request):
        """批量删除一键告警

        批量删除一键告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteOneClickAlarms
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteOneClickAlarmsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteOneClickAlarmsResponse`
        """
        return self._batch_delete_one_click_alarms_with_http_info(request)

    def _batch_delete_one_click_alarms_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/one-click-alarms/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteOneClickAlarmsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_resource_groups(self, request):
        """批量删除资源分组

        批量删除资源分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResourceGroups
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteResourceGroupsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteResourceGroupsResponse`
        """
        return self._batch_delete_resource_groups_with_http_info(request)

    def _batch_delete_resource_groups_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/resource-groups/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteResourceGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_resources(self, request):
        """自定义资源分组批量删除关联资源

        给自定义资源分组,即类型为手动添加的资源分组,批量删除关联资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResources
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteResourcesResponse`
        """
        return self._batch_delete_resources_with_http_info(request)

    def _batch_delete_resources_with_http_info(self, request):
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/resource-groups/{group_id}/resources/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_enable_alarm_rules(self, request):
        """批量启停告警规则

        批量启停告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchEnableAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.BatchEnableAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchEnableAlarmRulesResponse`
        """
        return self._batch_enable_alarm_rules_with_http_info(request)

    def _batch_enable_alarm_rules_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/alarms/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchEnableAlarmRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_notification_mask_time(self, request):
        """批量修改告警通知屏蔽规则的屏蔽时间

        批量修改告警通知屏蔽规则的屏蔽时间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateNotificationMaskTime
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateNotificationMaskTimeRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateNotificationMaskTimeResponse`
        """
        return self._batch_update_notification_mask_time_with_http_info(request)

    def _batch_update_notification_mask_time_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/notification-masks/batch-update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateNotificationMaskTimeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_notification_masks(self, request):
        """批量设置告警通知屏蔽规则

        批量设置告警通知屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateNotificationMasks
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateNotificationMasksRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateNotificationMasksResponse`
        """
        return self._batch_update_notification_masks_with_http_info(request)

    def _batch_update_notification_masks_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/notification-masks',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateNotificationMasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_one_click_alarm_policies_enabled_state(self, request):
        """批量修改一键告警关联告警规则策略的启用状态

        批量修改一键告警关联告警规则策略的启用状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateOneClickAlarmPoliciesEnabledState
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateOneClickAlarmPoliciesEnabledStateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateOneClickAlarmPoliciesEnabledStateResponse`
        """
        return self._batch_update_one_click_alarm_policies_enabled_state_with_http_info(request)

    def _batch_update_one_click_alarm_policies_enabled_state_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'one_click_alarm_id' in local_var_params:
            path_params['one_click_alarm_id'] = local_var_params['one_click_alarm_id']
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/one-click-alarms/{one_click_alarm_id}/alarms/{alarm_id}/policies/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateOneClickAlarmPoliciesEnabledStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_one_click_alarms_enabled_state(self, request):
        """批量修改一键告警关联告警规则的启用状态

        批量修改一键告警关联告警规则的启用状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateOneClickAlarmsEnabledState
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateOneClickAlarmsEnabledStateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateOneClickAlarmsEnabledStateResponse`
        """
        return self._batch_update_one_click_alarms_enabled_state_with_http_info(request)

    def _batch_update_one_click_alarms_enabled_state_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'one_click_alarm_id' in local_var_params:
            path_params['one_click_alarm_id'] = local_var_params['one_click_alarm_id']

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
            resource_path='/v2/{project_id}/one-click-alarms/{one_click_alarm_id}/alarm-rules/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateOneClickAlarmsEnabledStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_widgets(self, request):
        """批量更新监控视图

        批量更新监控视图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateWidgets
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateWidgetsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateWidgetsResponse`
        """
        return self._batch_update_widgets_with_http_info(request)

    def _batch_update_widgets_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/widgets/batch-update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateWidgetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alarm_rules(self, request):
        """创建告警规则

        创建告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.CreateAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateAlarmRulesResponse`
        """
        return self._create_alarm_rules_with_http_info(request)

    def _create_alarm_rules_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/alarms',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlarmRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alarm_template(self, request):
        """创建自定义告警模板

        创建自定义告警模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v2.CreateAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateAlarmTemplateResponse`
        """
        return self._create_alarm_template_with_http_info(request)

    def _create_alarm_template_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/alarm-templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlarmTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dashboard_widgets(self, request):
        """创建/复制/批量创建监控视图到指定的监控看板

        创建/复制/批量创建监控视图到指定的监控看板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDashboardWidgets
        :type request: :class:`huaweicloudsdkces.v2.CreateDashboardWidgetsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateDashboardWidgetsResponse`
        """
        return self._create_dashboard_widgets_with_http_info(request)

    def _create_dashboard_widgets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in local_var_params:
            path_params['dashboard_id'] = local_var_params['dashboard_id']

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
            resource_path='/v2/{project_id}/dashboards/{dashboard_id}/widgets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDashboardWidgetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_one_click_alarm(self, request):
        """创建一键告警

        创建一键告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOneClickAlarm
        :type request: :class:`huaweicloudsdkces.v2.CreateOneClickAlarmRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateOneClickAlarmResponse`
        """
        return self._create_one_click_alarm_with_http_info(request)

    def _create_one_click_alarm_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/one-click-alarms',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOneClickAlarmResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_one_dashboard(self, request):
        """创建/复制监控看板

        创建/复制监控看板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOneDashboard
        :type request: :class:`huaweicloudsdkces.v2.CreateOneDashboardRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateOneDashboardResponse`
        """
        return self._create_one_dashboard_with_http_info(request)

    def _create_one_dashboard_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/dashboards',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOneDashboardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resource_group(self, request):
        """创建资源分组

        创建资源分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResourceGroup
        :type request: :class:`huaweicloudsdkces.v2.CreateResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateResourceGroupResponse`
        """
        return self._create_resource_group_with_http_info(request)

    def _create_resource_group_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/resource-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResourceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alarm_rule_resources(self, request):
        """批量删除告警规则资源

        批量删除告警规则资源（资源分组类型的告警规则不支持），资源分组类型的修改请使用资源分组管理相关接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlarmRuleResources
        :type request: :class:`huaweicloudsdkces.v2.DeleteAlarmRuleResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.DeleteAlarmRuleResourcesResponse`
        """
        return self._delete_alarm_rule_resources_with_http_info(request)

    def _delete_alarm_rule_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/resources/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAlarmRuleResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_dashboards(self, request):
        """批量删除监控看板

        批量删除监控看板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDashboards
        :type request: :class:`huaweicloudsdkces.v2.DeleteDashboardsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.DeleteDashboardsResponse`
        """
        return self._delete_dashboards_with_http_info(request)

    def _delete_dashboards_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/dashboards/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDashboardsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_one_widget(self, request):
        """删除指定监控视图

        删除指定监控视图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOneWidget
        :type request: :class:`huaweicloudsdkces.v2.DeleteOneWidgetRequest`
        :rtype: :class:`huaweicloudsdkces.v2.DeleteOneWidgetResponse`
        """
        return self._delete_one_widget_with_http_info(request)

    def _delete_one_widget_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'widget_id' in local_var_params:
            path_params['widget_id'] = local_var_params['widget_id']

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
            resource_path='/v2/{project_id}/widgets/{widget_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteOneWidgetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_agent_dimension_info(self, request):
        """查询主机监控维度指标信息

        根据ECS/BMS资源ID查询磁盘、挂载点、进程、显卡、RAID控制器维度指标信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgentDimensionInfo
        :type request: :class:`huaweicloudsdkces.v2.ListAgentDimensionInfoRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAgentDimensionInfoResponse`
        """
        return self._list_agent_dimension_info_with_http_info(request)

    def _list_agent_dimension_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dim_name' in local_var_params:
            query_params.append(('dim_name', local_var_params['dim_name']))
        if 'dim_value' in local_var_params:
            query_params.append(('dim_value', local_var_params['dim_value']))
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
            resource_path='/v2/{project_id}/instances/{instance_id}/agent-dimensions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAgentDimensionInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_histories(self, request):
        """查询告警记录列表

        查询告警记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmHistories
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmHistoriesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmHistoriesResponse`
        """
        return self._list_alarm_histories_with_http_info(request)

    def _list_alarm_histories_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alarm_id' in local_var_params:
            query_params.append(('alarm_id', local_var_params['alarm_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
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
            resource_path='/v2/{project_id}/alarm-histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_rule_policies(self, request):
        """查询告警规则策略列表

        根据告警规则ID查询策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmRulePolicies
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmRulePoliciesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmRulePoliciesResponse`
        """
        return self._list_alarm_rule_policies_with_http_info(request)

    def _list_alarm_rule_policies_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmRulePoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_rule_resources(self, request):
        """查询告警规则资源列表

        根据告警规则ID查询告警规则资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmRuleResources
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmRuleResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmRuleResourcesResponse`
        """
        return self._list_alarm_rule_resources_with_http_info(request)

    def _list_alarm_rule_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmRuleResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_rules(self, request):
        """查询告警规则列表

        查询告警规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmRulesResponse`
        """
        return self._list_alarm_rules_with_http_info(request)

    def _list_alarm_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alarm_id' in local_var_params:
            query_params.append(('alarm_id', local_var_params['alarm_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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
            resource_path='/v2/{project_id}/alarms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_template_association_alarms(self, request):
        """查询告警模板关联的告警规则列表

        查询告警模板关联的告警规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmTemplateAssociationAlarms
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmTemplateAssociationAlarmsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmTemplateAssociationAlarmsResponse`
        """
        return self._list_alarm_template_association_alarms_with_http_info(request)

    def _list_alarm_template_association_alarms_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v2/{project_id}/alarm-templates/{template_id}/association-alarms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmTemplateAssociationAlarmsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_templates(self, request):
        """查询告警模板列表

        查询告警模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmTemplates
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmTemplatesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmTemplatesResponse`
        """
        return self._list_alarm_templates_with_http_info(request)

    def _list_alarm_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'dim_name' in local_var_params:
            query_params.append(('dim_name', local_var_params['dim_name']))
        if 'template_type' in local_var_params:
            query_params.append(('template_type', local_var_params['template_type']))
        if 'template_name' in local_var_params:
            query_params.append(('template_name', local_var_params['template_name']))

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
            resource_path='/v2/{project_id}/alarm-templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ces_target_project_tags(self, request):
        """查询CES指定项目指定资源类型标签列表

        查询CES指定项目指定资源类型标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCesTargetProjectTags
        :type request: :class:`huaweicloudsdkces.v2.ListCesTargetProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListCesTargetProjectTagsResponse`
        """
        return self._list_ces_target_project_tags_with_http_info(request)

    def _list_ces_target_project_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v2/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCesTargetProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dashboard_infos(self, request):
        """查询监控看板列表

        查询监控看板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDashboardInfos
        :type request: :class:`huaweicloudsdkces.v2.ListDashboardInfosRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListDashboardInfosResponse`
        """
        return self._list_dashboard_infos_with_http_info(request)

    def _list_dashboard_infos_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_id' in local_var_params:
            query_params.append(('enterprise_id', local_var_params['enterprise_id']))
        if 'is_favorite' in local_var_params:
            query_params.append(('is_favorite', local_var_params['is_favorite']))
        if 'dashboard_name' in local_var_params:
            query_params.append(('dashboard_name', local_var_params['dashboard_name']))
        if 'dashboard_id' in local_var_params:
            query_params.append(('dashboard_id', local_var_params['dashboard_id']))

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
            resource_path='/v2/{project_id}/dashboards',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDashboardInfosResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dashboard_widgets(self, request):
        """查询指定监控看板下的监控视图列表

        查询指定监控看板下的监控视图列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDashboardWidgets
        :type request: :class:`huaweicloudsdkces.v2.ListDashboardWidgetsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListDashboardWidgetsResponse`
        """
        return self._list_dashboard_widgets_with_http_info(request)

    def _list_dashboard_widgets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in local_var_params:
            path_params['dashboard_id'] = local_var_params['dashboard_id']

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
            resource_path='/v2/{project_id}/dashboards/{dashboard_id}/widgets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDashboardWidgetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notification_mask_resources(self, request):
        """查询告警通知屏蔽资源列表

        查询告警通知屏蔽资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationMaskResources
        :type request: :class:`huaweicloudsdkces.v2.ListNotificationMaskResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListNotificationMaskResourcesResponse`
        """
        return self._list_notification_mask_resources_with_http_info(request)

    def _list_notification_mask_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'notification_mask_id' in local_var_params:
            path_params['notification_mask_id'] = local_var_params['notification_mask_id']

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
            resource_path='/v2/{project_id}/notification-masks/{notification_mask_id}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotificationMaskResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notification_masks(self, request):
        """查询告警通知屏蔽列表

        批量查询指定类型的通知屏蔽规则，目前最多支持100个通知屏蔽规则的批量查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationMasks
        :type request: :class:`huaweicloudsdkces.v2.ListNotificationMasksRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListNotificationMasksResponse`
        """
        return self._list_notification_masks_with_http_info(request)

    def _list_notification_masks_with_http_info(self, request):
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/notification-masks/batch-query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotificationMasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_one_click_alarm_rules(self, request):
        """查询一键告警关联告警规则列表

        查询一键告警关联告警规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOneClickAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.ListOneClickAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListOneClickAlarmRulesResponse`
        """
        return self._list_one_click_alarm_rules_with_http_info(request)

    def _list_one_click_alarm_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'one_click_alarm_id' in local_var_params:
            path_params['one_click_alarm_id'] = local_var_params['one_click_alarm_id']

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
            resource_path='/v2/{project_id}/one-click-alarms/{one_click_alarm_id}/alarms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOneClickAlarmRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_one_click_alarms(self, request):
        """查询一键告警列表

        查询一键告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOneClickAlarms
        :type request: :class:`huaweicloudsdkces.v2.ListOneClickAlarmsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListOneClickAlarmsResponse`
        """
        return self._list_one_click_alarms_with_http_info(request)

    def _list_one_click_alarms_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/one-click-alarms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOneClickAlarmsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_groups(self, request):
        """查询资源分组列表

        查询资源分组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceGroups
        :type request: :class:`huaweicloudsdkces.v2.ListResourceGroupsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListResourceGroupsResponse`
        """
        return self._list_resource_groups_with_http_info(request)

    def _list_resource_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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
            resource_path='/v2/{project_id}/resource-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_groups_services_resources(self, request):
        """查询资源分组下指定服务类别特定维度的资源列表

        查询资源分组下指定服务类别特定维度的资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceGroupsServicesResources
        :type request: :class:`huaweicloudsdkces.v2.ListResourceGroupsServicesResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListResourceGroupsServicesResourcesResponse`
        """
        return self._list_resource_groups_services_resources_with_http_info(request)

    def _list_resource_groups_services_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']

        query_params = []
        if 'dim_name' in local_var_params:
            query_params.append(('dim_name', local_var_params['dim_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'dim_value' in local_var_params:
            query_params.append(('dim_value', local_var_params['dim_value']))

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
            resource_path='/v2/{project_id}/resource-groups/{group_id}/services/{service}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceGroupsServicesResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alarm_template(self, request):
        """查询告警模板详情

        查询告警模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v2.ShowAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ShowAlarmTemplateResponse`
        """
        return self._show_alarm_template_with_http_info(request)

    def _show_alarm_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v2/{project_id}/alarm-templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAlarmTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_group(self, request):
        """查询指定资源分组详情

        查询指定资源分组详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceGroup
        :type request: :class:`huaweicloudsdkces.v2.ShowResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ShowResourceGroupResponse`
        """
        return self._show_resource_group_with_http_info(request)

    def _show_resource_group_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/resource-groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_widget(self, request):
        """查询指定监控视图信息

        查询指定监控视图信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWidget
        :type request: :class:`huaweicloudsdkces.v2.ShowWidgetRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ShowWidgetResponse`
        """
        return self._show_widget_with_http_info(request)

    def _show_widget_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'widget_id' in local_var_params:
            path_params['widget_id'] = local_var_params['widget_id']

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
            resource_path='/v2/{project_id}/widgets/{widget_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWidgetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_notifications(self, request):
        """修改告警规则告警通知信息

        修改告警规则告警通知信息，告警策略&amp;资源请使用对应接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmNotifications
        :type request: :class:`huaweicloudsdkces.v2.UpdateAlarmNotificationsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateAlarmNotificationsResponse`
        """
        return self._update_alarm_notifications_with_http_info(request)

    def _update_alarm_notifications_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/notifications',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlarmNotificationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_rule_policies(self, request):
        """修改告警规则策略(全量修改)

        修改告警规则策略(全量修改)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmRulePolicies
        :type request: :class:`huaweicloudsdkces.v2.UpdateAlarmRulePoliciesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateAlarmRulePoliciesResponse`
        """
        return self._update_alarm_rule_policies_with_http_info(request)

    def _update_alarm_rule_policies_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/v2/{project_id}/alarms/{alarm_id}/policies',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlarmRulePoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_template(self, request):
        """修改自定义告警模板

        修改自定义告警模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v2.UpdateAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateAlarmTemplateResponse`
        """
        return self._update_alarm_template_with_http_info(request)

    def _update_alarm_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v2/{project_id}/alarm-templates/{template_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlarmTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_dashboard(self, request):
        """修改监控看板

        修改监控看板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDashboard
        :type request: :class:`huaweicloudsdkces.v2.UpdateDashboardRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateDashboardResponse`
        """
        return self._update_dashboard_with_http_info(request)

    def _update_dashboard_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in local_var_params:
            path_params['dashboard_id'] = local_var_params['dashboard_id']

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
            resource_path='/v2/{project_id}/dashboards/{dashboard_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDashboardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_notification_masks(self, request):
        """修改告警通知屏蔽规则

        修改告警通知屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNotificationMasks
        :type request: :class:`huaweicloudsdkces.v2.UpdateNotificationMasksRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateNotificationMasksResponse`
        """
        return self._update_notification_masks_with_http_info(request)

    def _update_notification_masks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'notification_mask_id' in local_var_params:
            path_params['notification_mask_id'] = local_var_params['notification_mask_id']

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
            resource_path='/v2/{project_id}/notification-masks/{notification_mask_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNotificationMasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_one_click_alarm_notifications(self, request):
        """批量修改开启状态的一键告警关联告警规则的告警通知

        批量修改开启状态的一键告警关联告警规则的告警通知
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOneClickAlarmNotifications
        :type request: :class:`huaweicloudsdkces.v2.UpdateOneClickAlarmNotificationsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateOneClickAlarmNotificationsResponse`
        """
        return self._update_one_click_alarm_notifications_with_http_info(request)

    def _update_one_click_alarm_notifications_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'one_click_alarm_id' in local_var_params:
            path_params['one_click_alarm_id'] = local_var_params['one_click_alarm_id']

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
            resource_path='/v2/{project_id}/one-click-alarms/{one_click_alarm_id}/notifications',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateOneClickAlarmNotificationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_resource_group(self, request):
        """修改资源分组

        修改资源分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResourceGroup
        :type request: :class:`huaweicloudsdkces.v2.UpdateResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateResourceGroupResponse`
        """
        return self._update_resource_group_with_http_info(request)

    def _update_resource_group_with_http_info(self, request):
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/resource-groups/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateResourceGroupResponse',
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

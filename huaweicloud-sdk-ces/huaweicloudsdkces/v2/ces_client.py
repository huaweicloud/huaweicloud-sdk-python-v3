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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkces'")


class CesClient(Client):
    def __init__(self):
        super(CesClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkces.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CesClient":
                raise TypeError("client type error, support client type is CesClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_alarm_rule_resources(self, request):
        r"""批量增加告警规则资源

        批量增加告警规则资源(资源分组类型的告警规则不支持)，资源分组类型的修改请使用资源分组管理相关接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAlarmRuleResources
        :type request: :class:`huaweicloudsdkces.v2.AddAlarmRuleResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.AddAlarmRuleResourcesResponse`
        """
        http_info = self._add_alarm_rule_resources_http_info(request)
        return self._call_api(**http_info)

    def add_alarm_rule_resources_invoker(self, request):
        http_info = self._add_alarm_rule_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_alarm_rule_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarms/{alarm_id}/resources/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "AddAlarmRuleResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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

    def batch_create_resources(self, request):
        r"""自定义资源分组批量增加关联资源

        给自定义资源分组,即类型为手动添加的资源分组,批量增加关联资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateResources
        :type request: :class:`huaweicloudsdkces.v2.BatchCreateResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchCreateResourcesResponse`
        """
        http_info = self._batch_create_resources_http_info(request)
        return self._call_api(**http_info)

    def batch_create_resources_invoker(self, request):
        http_info = self._batch_create_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/resource-groups/{group_id}/resources/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateResourcesResponse"
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

    def batch_delete_alarm_rules(self, request):
        r"""批量删除告警规则

        批量删除告警规则V2接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteAlarmRulesResponse`
        """
        http_info = self._batch_delete_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_alarm_rules_invoker(self, request):
        http_info = self._batch_delete_alarm_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_alarm_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarms/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAlarmRulesResponse"
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

    def batch_delete_alarm_templates(self, request):
        r"""批量删除自定义告警模板

        批量删除自定义告警模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAlarmTemplates
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteAlarmTemplatesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteAlarmTemplatesResponse`
        """
        http_info = self._batch_delete_alarm_templates_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_alarm_templates_invoker(self, request):
        http_info = self._batch_delete_alarm_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_alarm_templates_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarm-templates/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAlarmTemplatesResponse"
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

    def batch_delete_notification_masks(self, request):
        r"""批量删除告警通知屏蔽规则

        批量删除告警通知屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteNotificationMasks
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteNotificationMasksRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteNotificationMasksResponse`
        """
        http_info = self._batch_delete_notification_masks_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_notification_masks_invoker(self, request):
        http_info = self._batch_delete_notification_masks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_notification_masks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notification-masks/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteNotificationMasksResponse"
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

    def batch_delete_one_click_alarms(self, request):
        r"""批量删除一键告警

        批量删除一键告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteOneClickAlarms
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteOneClickAlarmsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteOneClickAlarmsResponse`
        """
        http_info = self._batch_delete_one_click_alarms_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_one_click_alarms_invoker(self, request):
        http_info = self._batch_delete_one_click_alarms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_one_click_alarms_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/one-click-alarms/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteOneClickAlarmsResponse"
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

    def batch_delete_resource_groups(self, request):
        r"""批量删除资源分组

        批量删除资源分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResourceGroups
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteResourceGroupsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteResourceGroupsResponse`
        """
        http_info = self._batch_delete_resource_groups_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resource_groups_invoker(self, request):
        http_info = self._batch_delete_resource_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_resource_groups_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/resource-groups/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteResourceGroupsResponse"
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

    def batch_delete_resources(self, request):
        r"""自定义资源分组批量删除关联资源

        给自定义资源分组,即类型为手动添加的资源分组,批量删除关联资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResources
        :type request: :class:`huaweicloudsdkces.v2.BatchDeleteResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchDeleteResourcesResponse`
        """
        http_info = self._batch_delete_resources_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resources_invoker(self, request):
        http_info = self._batch_delete_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/resource-groups/{group_id}/resources/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteResourcesResponse"
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

    def batch_enable_alarm_rules(self, request):
        r"""批量启停告警规则

        批量启停告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchEnableAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.BatchEnableAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchEnableAlarmRulesResponse`
        """
        http_info = self._batch_enable_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def batch_enable_alarm_rules_invoker(self, request):
        http_info = self._batch_enable_alarm_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_enable_alarm_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarms/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchEnableAlarmRulesResponse"
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

    def batch_update_notification_mask_time(self, request):
        r"""批量修改告警通知屏蔽规则的屏蔽时间

        批量修改告警通知屏蔽规则的屏蔽时间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateNotificationMaskTime
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateNotificationMaskTimeRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateNotificationMaskTimeResponse`
        """
        http_info = self._batch_update_notification_mask_time_http_info(request)
        return self._call_api(**http_info)

    def batch_update_notification_mask_time_invoker(self, request):
        http_info = self._batch_update_notification_mask_time_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_notification_mask_time_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notification-masks/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateNotificationMaskTimeResponse"
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

    def batch_update_notification_masks(self, request):
        r"""批量设置告警通知屏蔽规则

        批量设置告警通知屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateNotificationMasks
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateNotificationMasksRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateNotificationMasksResponse`
        """
        http_info = self._batch_update_notification_masks_http_info(request)
        return self._call_api(**http_info)

    def batch_update_notification_masks_invoker(self, request):
        http_info = self._batch_update_notification_masks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_notification_masks_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notification-masks",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateNotificationMasksResponse"
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

    def batch_update_one_click_alarm_policies_enabled_state(self, request):
        r"""批量修改一键告警关联告警规则策略的启用状态

        批量修改一键告警关联告警规则策略的启用状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateOneClickAlarmPoliciesEnabledState
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateOneClickAlarmPoliciesEnabledStateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateOneClickAlarmPoliciesEnabledStateResponse`
        """
        http_info = self._batch_update_one_click_alarm_policies_enabled_state_http_info(request)
        return self._call_api(**http_info)

    def batch_update_one_click_alarm_policies_enabled_state_invoker(self, request):
        http_info = self._batch_update_one_click_alarm_policies_enabled_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_one_click_alarm_policies_enabled_state_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/one-click-alarms/{one_click_alarm_id}/alarms/{alarm_id}/policies/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateOneClickAlarmPoliciesEnabledStateResponse"
            }

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

    def batch_update_one_click_alarms_enabled_state(self, request):
        r"""批量修改一键告警关联告警规则的启用状态

        批量修改一键告警关联告警规则的启用状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateOneClickAlarmsEnabledState
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateOneClickAlarmsEnabledStateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateOneClickAlarmsEnabledStateResponse`
        """
        http_info = self._batch_update_one_click_alarms_enabled_state_http_info(request)
        return self._call_api(**http_info)

    def batch_update_one_click_alarms_enabled_state_invoker(self, request):
        http_info = self._batch_update_one_click_alarms_enabled_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_one_click_alarms_enabled_state_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/one-click-alarms/{one_click_alarm_id}/alarm-rules/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateOneClickAlarmsEnabledStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'one_click_alarm_id' in local_var_params:
            path_params['one_click_alarm_id'] = local_var_params['one_click_alarm_id']

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

    def batch_update_widgets(self, request):
        r"""批量更新监控视图

        批量更新监控视图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateWidgets
        :type request: :class:`huaweicloudsdkces.v2.BatchUpdateWidgetsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.BatchUpdateWidgetsResponse`
        """
        http_info = self._batch_update_widgets_http_info(request)
        return self._call_api(**http_info)

    def batch_update_widgets_invoker(self, request):
        http_info = self._batch_update_widgets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_widgets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/widgets/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateWidgetsResponse"
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

    def create_alarm_rules(self, request):
        r"""创建告警规则（推荐）

        创建告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.CreateAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateAlarmRulesResponse`
        """
        http_info = self._create_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def create_alarm_rules_invoker(self, request):
        http_info = self._create_alarm_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_alarm_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlarmRulesResponse"
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

    def create_alarm_template(self, request):
        r"""创建自定义告警模板

        创建自定义告警模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v2.CreateAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateAlarmTemplateResponse`
        """
        http_info = self._create_alarm_template_http_info(request)
        return self._call_api(**http_info)

    def create_alarm_template_invoker(self, request):
        http_info = self._create_alarm_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_alarm_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarm-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlarmTemplateResponse"
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

    def create_dashboard_widgets(self, request):
        r"""创建/复制/批量创建监控视图到指定的监控看板

        创建/复制/批量创建监控视图到指定的监控看板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDashboardWidgets
        :type request: :class:`huaweicloudsdkces.v2.CreateDashboardWidgetsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateDashboardWidgetsResponse`
        """
        http_info = self._create_dashboard_widgets_http_info(request)
        return self._call_api(**http_info)

    def create_dashboard_widgets_invoker(self, request):
        http_info = self._create_dashboard_widgets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dashboard_widgets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dashboards/{dashboard_id}/widgets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDashboardWidgetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in local_var_params:
            path_params['dashboard_id'] = local_var_params['dashboard_id']

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

    def create_one_click_alarm(self, request):
        r"""创建一键告警

        创建一键告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOneClickAlarm
        :type request: :class:`huaweicloudsdkces.v2.CreateOneClickAlarmRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateOneClickAlarmResponse`
        """
        http_info = self._create_one_click_alarm_http_info(request)
        return self._call_api(**http_info)

    def create_one_click_alarm_invoker(self, request):
        http_info = self._create_one_click_alarm_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_one_click_alarm_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/one-click-alarms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOneClickAlarmResponse"
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

    def create_one_dashboard(self, request):
        r"""创建/复制监控看板

        创建/复制监控看板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOneDashboard
        :type request: :class:`huaweicloudsdkces.v2.CreateOneDashboardRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateOneDashboardResponse`
        """
        http_info = self._create_one_dashboard_http_info(request)
        return self._call_api(**http_info)

    def create_one_dashboard_invoker(self, request):
        http_info = self._create_one_dashboard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_one_dashboard_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dashboards",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOneDashboardResponse"
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

    def create_resource_group(self, request):
        r"""创建资源分组（推荐）

        创建资源分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResourceGroup
        :type request: :class:`huaweicloudsdkces.v2.CreateResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v2.CreateResourceGroupResponse`
        """
        http_info = self._create_resource_group_http_info(request)
        return self._call_api(**http_info)

    def create_resource_group_invoker(self, request):
        http_info = self._create_resource_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_resource_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/resource-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceGroupResponse"
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

    def delete_alarm_rule_resources(self, request):
        r"""批量删除告警规则资源

        批量删除告警规则资源（资源分组类型的告警规则不支持），资源分组类型的修改请使用资源分组管理相关接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlarmRuleResources
        :type request: :class:`huaweicloudsdkces.v2.DeleteAlarmRuleResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.DeleteAlarmRuleResourcesResponse`
        """
        http_info = self._delete_alarm_rule_resources_http_info(request)
        return self._call_api(**http_info)

    def delete_alarm_rule_resources_invoker(self, request):
        http_info = self._delete_alarm_rule_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_alarm_rule_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarms/{alarm_id}/resources/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlarmRuleResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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

    def delete_dashboards(self, request):
        r"""批量删除监控看板

        批量删除监控看板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDashboards
        :type request: :class:`huaweicloudsdkces.v2.DeleteDashboardsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.DeleteDashboardsResponse`
        """
        http_info = self._delete_dashboards_http_info(request)
        return self._call_api(**http_info)

    def delete_dashboards_invoker(self, request):
        http_info = self._delete_dashboards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dashboards_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dashboards/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDashboardsResponse"
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

    def delete_one_widget(self, request):
        r"""删除指定监控视图

        删除指定监控视图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOneWidget
        :type request: :class:`huaweicloudsdkces.v2.DeleteOneWidgetRequest`
        :rtype: :class:`huaweicloudsdkces.v2.DeleteOneWidgetResponse`
        """
        http_info = self._delete_one_widget_http_info(request)
        return self._call_api(**http_info)

    def delete_one_widget_invoker(self, request):
        http_info = self._delete_one_widget_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_one_widget_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/widgets/{widget_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOneWidgetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'widget_id' in local_var_params:
            path_params['widget_id'] = local_var_params['widget_id']

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

    def list_agent_dimension_info(self, request):
        r"""查询主机监控维度指标信息

        根据ECS/BMS资源ID查询磁盘、挂载点、进程、显卡、RAID控制器维度指标信息；维度NPU已经为原始值，不需要调用该接口进行额外查询获取指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgentDimensionInfo
        :type request: :class:`huaweicloudsdkces.v2.ListAgentDimensionInfoRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAgentDimensionInfoResponse`
        """
        http_info = self._list_agent_dimension_info_http_info(request)
        return self._call_api(**http_info)

    def list_agent_dimension_info_invoker(self, request):
        http_info = self._list_agent_dimension_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_agent_dimension_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/agent-dimensions",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentDimensionInfoResponse"
            }

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

    def list_alarm_histories(self, request):
        r"""查询告警记录列表

        查询告警记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmHistories
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmHistoriesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmHistoriesResponse`
        """
        http_info = self._list_alarm_histories_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_histories_invoker(self, request):
        http_info = self._list_alarm_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alarm_id' in local_var_params:
            query_params.append(('alarm_id', local_var_params['alarm_id']))
            collection_formats['alarm_id'] = 'csv'
        if 'record_id' in local_var_params:
            query_params.append(('record_id', local_var_params['record_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
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
        if 'alarm_type' in local_var_params:
            query_params.append(('alarm_type', local_var_params['alarm_type']))
        if 'create_time_from' in local_var_params:
            query_params.append(('create_time_from', local_var_params['create_time_from']))
        if 'create_time_to' in local_var_params:
            query_params.append(('create_time_to', local_var_params['create_time_to']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))

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

    def list_alarm_rule_policies(self, request):
        r"""查询告警规则策略列表

        根据告警规则ID查询策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmRulePolicies
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmRulePoliciesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmRulePoliciesResponse`
        """
        http_info = self._list_alarm_rule_policies_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_rule_policies_invoker(self, request):
        http_info = self._list_alarm_rule_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_rule_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarms/{alarm_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmRulePoliciesResponse"
            }

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

    def list_alarm_rule_resources(self, request):
        r"""查询告警规则资源列表

        根据告警规则ID查询告警规则资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmRuleResources
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmRuleResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmRuleResourcesResponse`
        """
        http_info = self._list_alarm_rule_resources_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_rule_resources_invoker(self, request):
        http_info = self._list_alarm_rule_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_rule_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarms/{alarm_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmRuleResourcesResponse"
            }

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

    def list_alarm_rules(self, request):
        r"""查询告警规则列表（推荐）

        查询告警规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmRulesResponse`
        """
        http_info = self._list_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_rules_invoker(self, request):
        http_info = self._list_alarm_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmRulesResponse"
            }

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
        if 'product_name' in local_var_params:
            query_params.append(('product_name', local_var_params['product_name']))
        if 'resource_level' in local_var_params:
            query_params.append(('resource_level', local_var_params['resource_level']))
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

    def list_alarm_template_association_alarms(self, request):
        r"""查询告警模板关联的告警规则列表

        查询告警模板关联的告警规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmTemplateAssociationAlarms
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmTemplateAssociationAlarmsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmTemplateAssociationAlarmsResponse`
        """
        http_info = self._list_alarm_template_association_alarms_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_template_association_alarms_invoker(self, request):
        http_info = self._list_alarm_template_association_alarms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_template_association_alarms_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-templates/{template_id}/association-alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmTemplateAssociationAlarmsResponse"
            }

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

    def list_alarm_templates(self, request):
        r"""查询告警模板列表

        查询告警模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmTemplates
        :type request: :class:`huaweicloudsdkces.v2.ListAlarmTemplatesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListAlarmTemplatesResponse`
        """
        http_info = self._list_alarm_templates_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_templates_invoker(self, request):
        http_info = self._list_alarm_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmTemplatesResponse"
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

    def list_ces_target_project_tags(self, request):
        r"""查询CES指定项目指定资源类型标签列表

        查询CES指定项目指定资源类型标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCesTargetProjectTags
        :type request: :class:`huaweicloudsdkces.v2.ListCesTargetProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListCesTargetProjectTagsResponse`
        """
        http_info = self._list_ces_target_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_ces_target_project_tags_invoker(self, request):
        http_info = self._list_ces_target_project_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ces_target_project_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListCesTargetProjectTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_dashboard_infos(self, request):
        r"""查询监控看板列表

        查询监控看板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDashboardInfos
        :type request: :class:`huaweicloudsdkces.v2.ListDashboardInfosRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListDashboardInfosResponse`
        """
        http_info = self._list_dashboard_infos_http_info(request)
        return self._call_api(**http_info)

    def list_dashboard_infos_invoker(self, request):
        http_info = self._list_dashboard_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dashboard_infos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dashboards",
            "request_type": request.__class__.__name__,
            "response_type": "ListDashboardInfosResponse"
            }

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
        if 'dashboard_type' in local_var_params:
            query_params.append(('dashboard_type', local_var_params['dashboard_type']))

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

    def list_dashboard_widgets(self, request):
        r"""查询指定监控看板下的监控视图列表

        查询指定监控看板下的监控视图列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDashboardWidgets
        :type request: :class:`huaweicloudsdkces.v2.ListDashboardWidgetsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListDashboardWidgetsResponse`
        """
        http_info = self._list_dashboard_widgets_http_info(request)
        return self._call_api(**http_info)

    def list_dashboard_widgets_invoker(self, request):
        http_info = self._list_dashboard_widgets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dashboard_widgets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dashboards/{dashboard_id}/widgets",
            "request_type": request.__class__.__name__,
            "response_type": "ListDashboardWidgetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in local_var_params:
            path_params['dashboard_id'] = local_var_params['dashboard_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def list_notification_mask_resources(self, request):
        r"""查询告警通知屏蔽资源列表

        查询告警通知屏蔽资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationMaskResources
        :type request: :class:`huaweicloudsdkces.v2.ListNotificationMaskResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListNotificationMaskResourcesResponse`
        """
        http_info = self._list_notification_mask_resources_http_info(request)
        return self._call_api(**http_info)

    def list_notification_mask_resources_invoker(self, request):
        http_info = self._list_notification_mask_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notification_mask_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notification-masks/{notification_mask_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotificationMaskResourcesResponse"
            }

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

    def list_notification_masks(self, request):
        r"""查询告警通知屏蔽列表

        批量查询指定类型的通知屏蔽规则，目前最多支持100个通知屏蔽规则的批量查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationMasks
        :type request: :class:`huaweicloudsdkces.v2.ListNotificationMasksRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListNotificationMasksResponse`
        """
        http_info = self._list_notification_masks_http_info(request)
        return self._call_api(**http_info)

    def list_notification_masks_invoker(self, request):
        http_info = self._list_notification_masks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notification_masks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notification-masks/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotificationMasksResponse"
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
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_one_click_alarm_rules(self, request):
        r"""查询一键告警关联告警规则列表

        查询一键告警关联告警规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOneClickAlarmRules
        :type request: :class:`huaweicloudsdkces.v2.ListOneClickAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListOneClickAlarmRulesResponse`
        """
        http_info = self._list_one_click_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def list_one_click_alarm_rules_invoker(self, request):
        http_info = self._list_one_click_alarm_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_one_click_alarm_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/one-click-alarms/{one_click_alarm_id}/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListOneClickAlarmRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'one_click_alarm_id' in local_var_params:
            path_params['one_click_alarm_id'] = local_var_params['one_click_alarm_id']

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

    def list_one_click_alarms(self, request):
        r"""查询一键告警列表

        查询一键告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOneClickAlarms
        :type request: :class:`huaweicloudsdkces.v2.ListOneClickAlarmsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListOneClickAlarmsResponse`
        """
        http_info = self._list_one_click_alarms_http_info(request)
        return self._call_api(**http_info)

    def list_one_click_alarms_invoker(self, request):
        http_info = self._list_one_click_alarms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_one_click_alarms_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/one-click-alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListOneClickAlarmsResponse"
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

    def list_resource_groups(self, request):
        r"""查询资源分组列表

        查询资源分组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceGroups
        :type request: :class:`huaweicloudsdkces.v2.ListResourceGroupsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListResourceGroupsResponse`
        """
        http_info = self._list_resource_groups_http_info(request)
        return self._call_api(**http_info)

    def list_resource_groups_invoker(self, request):
        http_info = self._list_resource_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/resource-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceGroupsResponse"
            }

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

    def list_resource_groups_services_resources(self, request):
        r"""查询资源分组下指定服务类别特定维度的资源列表

        查询资源分组下指定服务类别特定维度的资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceGroupsServicesResources
        :type request: :class:`huaweicloudsdkces.v2.ListResourceGroupsServicesResourcesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ListResourceGroupsServicesResourcesResponse`
        """
        http_info = self._list_resource_groups_services_resources_http_info(request)
        return self._call_api(**http_info)

    def list_resource_groups_services_resources_invoker(self, request):
        http_info = self._list_resource_groups_services_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_groups_services_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/resource-groups/{group_id}/services/{service}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceGroupsServicesResourcesResponse"
            }

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
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'extend_relation_id' in local_var_params:
            query_params.append(('extend_relation_id', local_var_params['extend_relation_id']))
        if 'product_name' in local_var_params:
            query_params.append(('product_name', local_var_params['product_name']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'event_status' in local_var_params:
            query_params.append(('event_status', local_var_params['event_status']))

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

    def show_alarm_template(self, request):
        r"""查询告警模板详情

        查询告警模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v2.ShowAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ShowAlarmTemplateResponse`
        """
        http_info = self._show_alarm_template_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_template_invoker(self, request):
        http_info = self._show_alarm_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alarm_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def show_resource_group(self, request):
        r"""查询指定资源分组详情

        查询指定资源分组详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceGroup
        :type request: :class:`huaweicloudsdkces.v2.ShowResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ShowResourceGroupResponse`
        """
        http_info = self._show_resource_group_http_info(request)
        return self._call_api(**http_info)

    def show_resource_group_invoker(self, request):
        http_info = self._show_resource_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/resource-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceGroupResponse"
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

    def show_widget(self, request):
        r"""查询指定监控视图信息

        查询指定监控视图信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWidget
        :type request: :class:`huaweicloudsdkces.v2.ShowWidgetRequest`
        :rtype: :class:`huaweicloudsdkces.v2.ShowWidgetResponse`
        """
        http_info = self._show_widget_http_info(request)
        return self._call_api(**http_info)

    def show_widget_invoker(self, request):
        http_info = self._show_widget_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_widget_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/widgets/{widget_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWidgetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'widget_id' in local_var_params:
            path_params['widget_id'] = local_var_params['widget_id']

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

    def update_alarm_notifications(self, request):
        r"""修改告警规则告警通知信息

        修改告警规则告警通知信息，告警策略&amp;资源请使用对应接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmNotifications
        :type request: :class:`huaweicloudsdkces.v2.UpdateAlarmNotificationsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateAlarmNotificationsResponse`
        """
        http_info = self._update_alarm_notifications_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_notifications_invoker(self, request):
        http_info = self._update_alarm_notifications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_notifications_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/alarms/{alarm_id}/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmNotificationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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

    def update_alarm_rule_policies(self, request):
        r"""修改告警规则策略(全量修改)

        修改告警规则策略(全量修改)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmRulePolicies
        :type request: :class:`huaweicloudsdkces.v2.UpdateAlarmRulePoliciesRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateAlarmRulePoliciesResponse`
        """
        http_info = self._update_alarm_rule_policies_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_rule_policies_invoker(self, request):
        http_info = self._update_alarm_rule_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_rule_policies_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/alarms/{alarm_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmRulePoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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

    def update_alarm_template(self, request):
        r"""修改自定义告警模板

        修改自定义告警模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v2.UpdateAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateAlarmTemplateResponse`
        """
        http_info = self._update_alarm_template_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_template_invoker(self, request):
        http_info = self._update_alarm_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/alarm-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def update_dashboard(self, request):
        r"""修改监控看板

        修改监控看板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDashboard
        :type request: :class:`huaweicloudsdkces.v2.UpdateDashboardRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateDashboardResponse`
        """
        http_info = self._update_dashboard_http_info(request)
        return self._call_api(**http_info)

    def update_dashboard_invoker(self, request):
        http_info = self._update_dashboard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_dashboard_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/dashboards/{dashboard_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDashboardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in local_var_params:
            path_params['dashboard_id'] = local_var_params['dashboard_id']

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

    def update_notification_mask(self, request):
        r"""修改告警通知屏蔽规则

        修改告警通知屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNotificationMask
        :type request: :class:`huaweicloudsdkces.v2.UpdateNotificationMaskRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateNotificationMaskResponse`
        """
        http_info = self._update_notification_mask_http_info(request)
        return self._call_api(**http_info)

    def update_notification_mask_invoker(self, request):
        http_info = self._update_notification_mask_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_notification_mask_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notification-masks/{notification_mask_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNotificationMaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'notification_mask_id' in local_var_params:
            path_params['notification_mask_id'] = local_var_params['notification_mask_id']

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

    def update_one_click_alarm_notifications(self, request):
        r"""批量修改开启状态的一键告警关联告警规则的告警通知

        批量修改开启状态的一键告警关联告警规则的告警通知
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOneClickAlarmNotifications
        :type request: :class:`huaweicloudsdkces.v2.UpdateOneClickAlarmNotificationsRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateOneClickAlarmNotificationsResponse`
        """
        http_info = self._update_one_click_alarm_notifications_http_info(request)
        return self._call_api(**http_info)

    def update_one_click_alarm_notifications_invoker(self, request):
        http_info = self._update_one_click_alarm_notifications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_one_click_alarm_notifications_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/one-click-alarms/{one_click_alarm_id}/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOneClickAlarmNotificationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'one_click_alarm_id' in local_var_params:
            path_params['one_click_alarm_id'] = local_var_params['one_click_alarm_id']

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

    def update_resource_group(self, request):
        r"""修改资源分组

        修改资源分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResourceGroup
        :type request: :class:`huaweicloudsdkces.v2.UpdateResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateResourceGroupResponse`
        """
        http_info = self._update_resource_group_http_info(request)
        return self._call_api(**http_info)

    def update_resource_group_invoker(self, request):
        http_info = self._update_resource_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_resource_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/resource-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceGroupResponse"
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

    def update_resource_group_association_alarm_template(self, request):
        r"""资源分组异步关联自定义告警模板

        提交资源分组批量关联自定义告警模板异步任务，由异步任务覆盖性创建告警规则。每个用户创建处于待执行状态的异步任务数量上限为100个，单个资源分组仅可有1个未完成的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResourceGroupAssociationAlarmTemplate
        :type request: :class:`huaweicloudsdkces.v2.UpdateResourceGroupAssociationAlarmTemplateRequest`
        :rtype: :class:`huaweicloudsdkces.v2.UpdateResourceGroupAssociationAlarmTemplateResponse`
        """
        http_info = self._update_resource_group_association_alarm_template_http_info(request)
        return self._call_api(**http_info)

    def update_resource_group_association_alarm_template_invoker(self, request):
        http_info = self._update_resource_group_association_alarm_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_resource_group_association_alarm_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/resource-groups/{group_id}/alarm-templates/async-association",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceGroupAssociationAlarmTemplateResponse"
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

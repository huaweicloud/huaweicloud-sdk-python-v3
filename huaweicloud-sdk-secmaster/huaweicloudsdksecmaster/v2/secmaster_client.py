# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class SecMasterClient(Client):
    def __init__(self):
        super(SecMasterClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksecmaster.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SecMasterClient":
                raise TypeError("client type error, support client type is SecMasterClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def change_alert(self, request):
        """更新告警

        编辑告警，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeAlert
        :type request: :class:`huaweicloudsdksecmaster.v2.ChangeAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ChangeAlertResponse`
        """
        return self._change_alert_with_http_info(request)

    def _change_alert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_id' in local_var_params:
            path_params['alert_id'] = local_var_params['alert_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/{alert_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeAlertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_incident(self, request):
        """更新事件

        编辑事件，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIncident
        :type request: :class:`huaweicloudsdksecmaster.v2.ChangeIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ChangeIncidentResponse`
        """
        return self._change_incident_with_http_info(request)

    def _change_incident_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/{incident_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeIncidentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_playbook_instance(self, request):
        """操作剧本实例

        操作剧本实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangePlaybookInstance
        :type request: :class:`huaweicloudsdksecmaster.v2.ChangePlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ChangePlaybookInstanceResponse`
        """
        return self._change_playbook_instance_with_http_info(request)

    def _change_playbook_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}/operation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangePlaybookInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_playbook_version(self, request):
        """克隆剧本及版本

        克隆剧本及版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyPlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.CopyPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CopyPlaybookVersionResponse`
        """
        return self._copy_playbook_version_with_http_info(request)

    def _copy_playbook_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/clone',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CopyPlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alert(self, request):
        """创建告警

        创建告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlert
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAlertResponse`
        """
        return self._create_alert_with_http_info(request)

    def _create_alert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alert_rule(self, request):
        """创建告警规则

        Create alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleResponse`
        """
        return self._create_alert_rule_with_http_info(request)

    def _create_alert_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alert_rule_simulation(self, request):
        """模拟告警规则

        Simulate alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlertRuleSimulation
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleSimulationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleSimulationResponse`
        """
        return self._create_alert_rule_simulation_with_http_info(request)

    def _create_alert_rule_simulation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/simulation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlertRuleSimulationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_batch_order_alerts(self, request):
        """告警转事件

        告警转事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBatchOrderAlerts
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateBatchOrderAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateBatchOrderAlertsResponse`
        """
        return self._create_batch_order_alerts_with_http_info(request)

    def _create_batch_order_alerts_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/batch-order',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBatchOrderAlertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dataobject_relations(self, request):
        """关联Dataobject

        关联Dataobject
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataobjectRelations
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateDataobjectRelationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateDataobjectRelationsResponse`
        """
        return self._create_dataobject_relations_with_http_info(request)

    def _create_dataobject_relations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_type' in local_var_params:
            path_params['dataclass_type'] = local_var_params['dataclass_type']
        if 'data_object_id' in local_var_params:
            path_params['data_object_id'] = local_var_params['data_object_id']
        if 'related_dataclass_type' in local_var_params:
            path_params['related_dataclass_type'] = local_var_params['related_dataclass_type']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDataobjectRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_incident(self, request):
        """创建事件

        创建事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIncident
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateIncidentResponse`
        """
        return self._create_incident_with_http_info(request)

    def _create_incident_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIncidentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_indicator(self, request):
        """创建指标

        创建指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIndicator
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorResponse`
        """
        return self._create_indicator_with_http_info(request)

    def _create_indicator_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIndicatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook(self, request):
        """创建剧本

        创建剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookResponse`
        """
        return self._create_playbook_with_http_info(request)

    def _create_playbook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_action(self, request):
        """创建剧本动作

        创建剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookActionResponse`
        """
        return self._create_playbook_action_with_http_info(request)

    def _create_playbook_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_approve(self, request):
        """审核剧本

        审核剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookApprove
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookApproveRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookApproveResponse`
        """
        return self._create_playbook_approve_with_http_info(request)

    def _create_playbook_approve_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/approval',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookApproveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_rule(self, request):
        """创建剧本规则

        创建剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookRuleResponse`
        """
        return self._create_playbook_rule_with_http_info(request)

    def _create_playbook_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_version(self, request):
        """创建剧本版本

        创建剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookVersionResponse`
        """
        return self._create_playbook_version_with_http_info(request)

    def _create_playbook_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/versions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alert(self, request):
        """删除告警

        删除告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlert
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteAlertResponse`
        """
        return self._delete_alert_with_http_info(request)

    def _delete_alert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAlertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alert_rule(self, request):
        """删除告警规则

        Delete alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteAlertRuleResponse`
        """
        return self._delete_alert_rule_with_http_info(request)

    def _delete_alert_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_dataobject_relations(self, request):
        """取消关联Dataobject

        取消关联Dataobject
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataobjectRelations
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteDataobjectRelationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteDataobjectRelationsResponse`
        """
        return self._delete_dataobject_relations_with_http_info(request)

    def _delete_dataobject_relations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_type' in local_var_params:
            path_params['dataclass_type'] = local_var_params['dataclass_type']
        if 'data_object_id' in local_var_params:
            path_params['data_object_id'] = local_var_params['data_object_id']
        if 'related_dataclass_type' in local_var_params:
            path_params['related_dataclass_type'] = local_var_params['related_dataclass_type']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDataobjectRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_incident(self, request):
        """删除事件

        删除事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIncident
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteIncidentResponse`
        """
        return self._delete_incident_with_http_info(request)

    def _delete_incident_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIncidentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_indicator(self, request):
        """删除指标

        删除指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIndicator
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteIndicatorResponse`
        """
        return self._delete_indicator_with_http_info(request)

    def _delete_indicator_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIndicatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_playbook(self, request):
        """删除剧本

        删除剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookResponse`
        """
        return self._delete_playbook_with_http_info(request)

    def _delete_playbook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePlaybookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_playbook_action(self, request):
        """删除剧本动作

        删除剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookActionResponse`
        """
        return self._delete_playbook_action_with_http_info(request)

    def _delete_playbook_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions/{action_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePlaybookActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_playbook_rule(self, request):
        """删除剧本规则

        删除剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookRuleResponse`
        """
        return self._delete_playbook_rule_with_http_info(request)

    def _delete_playbook_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePlaybookRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_playbook_version(self, request):
        """删除剧本版本

        删除剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookVersionResponse`
        """
        return self._delete_playbook_version_with_http_info(request)

    def _delete_playbook_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_alert_rule(self, request):
        """停用告警规则

        Disable alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.DisableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DisableAlertRuleResponse`
        """
        return self._disable_alert_rule_with_http_info(request)

    def _disable_alert_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_alert_rule(self, request):
        """启用告警规则

        Enable alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.EnableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.EnableAlertRuleResponse`
        """
        return self._enable_alert_rule_with_http_info(request)

    def _enable_alert_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alert_rule_metrics(self, request):
        """告警规则总览

        List alert rule metrics
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRuleMetrics
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleMetricsResponse`
        """
        return self._list_alert_rule_metrics_with_http_info(request)

    def _list_alert_rule_metrics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/metrics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlertRuleMetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alert_rule_templates(self, request):
        """列出告警规则模板

        List alert rule templates
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRuleTemplates
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplatesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplatesResponse`
        """
        return self._list_alert_rule_templates_with_http_info(request)

    def _list_alert_rule_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
            collection_formats['severity'] = 'csv'

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlertRuleTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alert_rules(self, request):
        """列出告警规则

        List alert rules
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRules
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRulesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRulesResponse`
        """
        return self._list_alert_rules_with_http_info(request)

    def _list_alert_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'pipe_id' in local_var_params:
            query_params.append(('pipe_id', local_var_params['pipe_id']))
        if 'rule_name' in local_var_params:
            query_params.append(('rule_name', local_var_params['rule_name']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
            collection_formats['severity'] = 'csv'

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlertRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alerts(self, request):
        """搜索告警列表

        搜索告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlerts
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertsResponse`
        """
        return self._list_alerts_with_http_info(request)

    def _list_alerts_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dataobject_relations(self, request):
        """查询关联Dataobject列表

        查询关联Dataobject列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataobjectRelations
        :type request: :class:`huaweicloudsdksecmaster.v2.ListDataobjectRelationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListDataobjectRelationsResponse`
        """
        return self._list_dataobject_relations_with_http_info(request)

    def _list_dataobject_relations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_type' in local_var_params:
            path_params['dataclass_type'] = local_var_params['dataclass_type']
        if 'data_object_id' in local_var_params:
            path_params['data_object_id'] = local_var_params['data_object_id']
        if 'related_dataclass_type' in local_var_params:
            path_params['related_dataclass_type'] = local_var_params['related_dataclass_type']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataobjectRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_incidents(self, request):
        """搜索事件列表

        搜索事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIncidents
        :type request: :class:`huaweicloudsdksecmaster.v2.ListIncidentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListIncidentsResponse`
        """
        return self._list_incidents_with_http_info(request)

    def _list_incidents_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIncidentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_indicators(self, request):
        """查询指标列表

        查询指标列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIndicators
        :type request: :class:`huaweicloudsdksecmaster.v2.ListIndicatorsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListIndicatorsResponse`
        """
        return self._list_indicators_with_http_info(request)

    def _list_indicators_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIndicatorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_actions(self, request):
        """查询剧本动作

        查询剧本动作列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookActions
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookActionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookActionsResponse`
        """
        return self._list_playbook_actions_with_http_info(request)

    def _list_playbook_actions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []
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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookActionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_approves(self, request):
        """查询剧本审核结果

        查询剧本审核结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookApproves
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookApprovesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookApprovesResponse`
        """
        return self._list_playbook_approves_with_http_info(request)

    def _list_playbook_approves_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'approve_type' in local_var_params:
            query_params.append(('approve_type', local_var_params['approve_type']))

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/approval',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookApprovesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_audit_logs(self, request):
        """查询剧本实例审计日志

        查询剧本实例审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookAuditLogs
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookAuditLogsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookAuditLogsResponse`
        """
        return self._list_playbook_audit_logs_with_http_info(request)

    def _list_playbook_audit_logs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/auditlogs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookAuditLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_instances(self, request):
        """查询剧本实例列表

        查询剧本实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookInstances
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookInstancesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookInstancesResponse`
        """
        return self._list_playbook_instances_with_http_info(request)

    def _list_playbook_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'playbook_name' in local_var_params:
            query_params.append(('playbook_name', local_var_params['playbook_name']))
        if 'dataclass_name' in local_var_params:
            query_params.append(('dataclass_name', local_var_params['dataclass_name']))
        if 'dataobject_name' in local_var_params:
            query_params.append(('dataobject_name', local_var_params['dataobject_name']))
        if 'trigger_type' in local_var_params:
            query_params.append(('trigger_type', local_var_params['trigger_type']))
        if 'from_date' in local_var_params:
            query_params.append(('from_date', local_var_params['from_date']))
        if 'to_date' in local_var_params:
            query_params.append(('to_date', local_var_params['to_date']))
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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_versions(self, request):
        """查询剧本版本列表

        查询剧本版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookVersions
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookVersionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookVersionsResponse`
        """
        return self._list_playbook_versions_with_http_info(request)

    def _list_playbook_versions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'version_type' in local_var_params:
            query_params.append(('version_type', local_var_params['version_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbooks(self, request):
        """查询剧本列表

        查询剧本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybooks
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybooksRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybooksResponse`
        """
        return self._list_playbooks_with_http_info(request)

    def _list_playbooks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'search_txt' in local_var_params:
            query_params.append(('search_txt', local_var_params['search_txt']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'dataclass_name' in local_var_params:
            query_params.append(('dataclass_name', local_var_params['dataclass_name']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alert(self, request):
        """获取告警详情

        获取告警详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlert
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertResponse`
        """
        return self._show_alert_with_http_info(request)

    def _show_alert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_id' in local_var_params:
            path_params['alert_id'] = local_var_params['alert_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/{alert_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAlertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alert_rule(self, request):
        """查看告警规则

        查看告警规则 Get alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleResponse`
        """
        return self._show_alert_rule_with_http_info(request)

    def _show_alert_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alert_rule_template(self, request):
        """查看告警规则模板

        List alert rule templates
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlertRuleTemplate
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleTemplateResponse`
        """
        return self._show_alert_rule_template_with_http_info(request)

    def _show_alert_rule_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAlertRuleTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_incident(self, request):
        """获取事件详情

        获取事件详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIncident
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowIncidentResponse`
        """
        return self._show_incident_with_http_info(request)

    def _show_incident_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/{incident_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIncidentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_indicator_detail(self, request):
        """查询指标详情

        查询指标详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIndicatorDetail
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowIndicatorDetailRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowIndicatorDetailResponse`
        """
        return self._show_indicator_detail_with_http_info(request)

    def _show_indicator_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'indicator_id' in local_var_params:
            path_params['indicator_id'] = local_var_params['indicator_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/{indicator_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIndicatorDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook(self, request):
        """查询剧本详情

        查询剧本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybook
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookResponse`
        """
        return self._show_playbook_with_http_info(request)

    def _show_playbook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_instance(self, request):
        """查询剧本实例详情

        Show playbook instance
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookInstance
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookInstanceResponse`
        """
        return self._show_playbook_instance_with_http_info(request)

    def _show_playbook_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_monitors(self, request):
        """剧本运行监控

        剧本运行监控
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookMonitors
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookMonitorsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookMonitorsResponse`
        """
        return self._show_playbook_monitors_with_http_info(request)

    def _show_playbook_monitors_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'version_query_type' in local_var_params:
            query_params.append(('version_query_type', local_var_params['version_query_type']))
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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/monitor',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookMonitorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_rule(self, request):
        """查询剧本规则详情

        查询剧本规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookRuleResponse`
        """
        return self._show_playbook_rule_with_http_info(request)

    def _show_playbook_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_statistics(self, request):
        """剧本数据统计

        剧本统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookStatistics
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookStatisticsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookStatisticsResponse`
        """
        return self._show_playbook_statistics_with_http_info(request)

    def _show_playbook_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_topology(self, request):
        """查询剧本拓扑关系

        查询剧本拓扑关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookTopology
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookTopologyRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookTopologyResponse`
        """
        return self._show_playbook_topology_with_http_info(request)

    def _show_playbook_topology_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}/topology',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookTopologyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_version(self, request):
        """查询剧本版本详情

        Show playbook version version
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookVersionResponse`
        """
        return self._show_playbook_version_with_http_info(request)

    def _show_playbook_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

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
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alert_rule(self, request):
        """更新告警规则

        Update alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleResponse`
        """
        return self._update_alert_rule_with_http_info(request)

    def _update_alert_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_indicator(self, request):
        """更新指标

        更新指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIndicator
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateIndicatorResponse`
        """
        return self._update_indicator_with_http_info(request)

    def _update_indicator_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'indicator_id' in local_var_params:
            path_params['indicator_id'] = local_var_params['indicator_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/{indicator_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIndicatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_playbook(self, request):
        """修改剧本

        修改剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookResponse`
        """
        return self._update_playbook_with_http_info(request)

    def _update_playbook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePlaybookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_playbook_action(self, request):
        """更新剧本动作

        更新剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookActionResponse`
        """
        return self._update_playbook_action_with_http_info(request)

    def _update_playbook_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions/{action_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePlaybookActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_playbook_rule(self, request):
        """更新剧本规则

        更新剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookRuleResponse`
        """
        return self._update_playbook_rule_with_http_info(request)

    def _update_playbook_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePlaybookRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_playbook_version(self, request):
        """更新剧本版本

        更新剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookVersionResponse`
        """
        return self._update_playbook_version_with_http_info(request)

    def _update_playbook_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePlaybookVersionResponse',
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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksecmaster'")


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
        http_info = self._change_alert_http_info(request)
        return self._call_api(**http_info)

    def change_alert_invoker(self, request):
        http_info = self._change_alert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_alert_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/{alert_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAlertResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def change_incident(self, request):
        """更新事件

        编辑事件，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIncident
        :type request: :class:`huaweicloudsdksecmaster.v2.ChangeIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ChangeIncidentResponse`
        """
        http_info = self._change_incident_http_info(request)
        return self._call_api(**http_info)

    def change_incident_invoker(self, request):
        http_info = self._change_incident_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_incident_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/{incident_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeIncidentResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def change_playbook_instance(self, request):
        """操作剧本实例

        操作剧本实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangePlaybookInstance
        :type request: :class:`huaweicloudsdksecmaster.v2.ChangePlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ChangePlaybookInstanceResponse`
        """
        http_info = self._change_playbook_instance_http_info(request)
        return self._call_api(**http_info)

    def change_playbook_instance_invoker(self, request):
        http_info = self._change_playbook_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_playbook_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}/operation",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePlaybookInstanceResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def copy_playbook_version(self, request):
        """克隆剧本及版本

        克隆剧本及版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyPlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.CopyPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CopyPlaybookVersionResponse`
        """
        http_info = self._copy_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def copy_playbook_version_invoker(self, request):
        http_info = self._copy_playbook_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_playbook_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/clone",
            "request_type": request.__class__.__name__,
            "response_type": "CopyPlaybookVersionResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_alert(self, request):
        """创建告警

        创建告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlert
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAlertResponse`
        """
        http_info = self._create_alert_http_info(request)
        return self._call_api(**http_info)

    def create_alert_invoker(self, request):
        http_info = self._create_alert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_alert_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlertResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_alert_rule(self, request):
        """创建告警规则

        Create alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleResponse`
        """
        http_info = self._create_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def create_alert_rule_invoker(self, request):
        http_info = self._create_alert_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_alert_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlertRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_alert_rule_simulation(self, request):
        """模拟告警规则

        Simulate alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlertRuleSimulation
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleSimulationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateAlertRuleSimulationResponse`
        """
        http_info = self._create_alert_rule_simulation_http_info(request)
        return self._call_api(**http_info)

    def create_alert_rule_simulation_invoker(self, request):
        http_info = self._create_alert_rule_simulation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_alert_rule_simulation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/simulation",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlertRuleSimulationResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_batch_order_alerts(self, request):
        """告警转事件

        告警转事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBatchOrderAlerts
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateBatchOrderAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateBatchOrderAlertsResponse`
        """
        http_info = self._create_batch_order_alerts_http_info(request)
        return self._call_api(**http_info)

    def create_batch_order_alerts_invoker(self, request):
        http_info = self._create_batch_order_alerts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_batch_order_alerts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/batch-order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBatchOrderAlertsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_dataobject_relations(self, request):
        """关联Dataobject

        关联Dataobject
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataobjectRelations
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateDataobjectRelationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateDataobjectRelationsResponse`
        """
        http_info = self._create_dataobject_relations_http_info(request)
        return self._call_api(**http_info)

    def create_dataobject_relations_invoker(self, request):
        http_info = self._create_dataobject_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dataobject_relations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataobjectRelationsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_dataspace(self, request):
        """create dataspace (创建数据空间)

        create dataspace
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataspace
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateDataspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateDataspaceResponse`
        """
        http_info = self._create_dataspace_http_info(request)
        return self._call_api(**http_info)

    def create_dataspace_invoker(self, request):
        http_info = self._create_dataspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dataspace_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/dataspaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataspaceResponse"
            }

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

    def create_incident(self, request):
        """创建事件

        创建事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIncident
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateIncidentResponse`
        """
        http_info = self._create_incident_http_info(request)
        return self._call_api(**http_info)

    def create_incident_invoker(self, request):
        http_info = self._create_incident_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_incident_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIncidentResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_indicator(self, request):
        """创建指标

        创建指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIndicator
        :type request: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorResponse`
        """
        http_info = self._create_indicator_http_info(request)
        return self._call_api(**http_info)

    def create_indicator_invoker(self, request):
        http_info = self._create_indicator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_indicator_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIndicatorResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_pipe(self, request):
        """create pipe (创建数据管道)

        create pipe
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipe
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePipeResponse`
        """
        http_info = self._create_pipe_http_info(request)
        return self._call_api(**http_info)

    def create_pipe_invoker(self, request):
        http_info = self._create_pipe_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pipe_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePipeResponse"
            }

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

    def create_playbook(self, request):
        """创建剧本

        创建剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookResponse`
        """
        http_info = self._create_playbook_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_invoker(self, request):
        http_info = self._create_playbook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_playbook_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_action(self, request):
        """创建剧本动作

        创建剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookActionResponse`
        """
        http_info = self._create_playbook_action_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_action_invoker(self, request):
        http_info = self._create_playbook_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_playbook_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookActionResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_approve(self, request):
        """审核剧本

        审核剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookApprove
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookApproveRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookApproveResponse`
        """
        http_info = self._create_playbook_approve_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_approve_invoker(self, request):
        http_info = self._create_playbook_approve_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_playbook_approve_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/approval",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookApproveResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_rule(self, request):
        """创建剧本规则

        创建剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookRuleResponse`
        """
        http_info = self._create_playbook_rule_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_rule_invoker(self, request):
        http_info = self._create_playbook_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_playbook_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_version(self, request):
        """创建剧本版本

        创建剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreatePlaybookVersionResponse`
        """
        http_info = self._create_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_version_invoker(self, request):
        http_info = self._create_playbook_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_playbook_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookVersionResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_alert(self, request):
        """删除告警

        删除告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlert
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteAlertResponse`
        """
        http_info = self._delete_alert_http_info(request)
        return self._call_api(**http_info)

    def delete_alert_invoker(self, request):
        http_info = self._delete_alert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_alert_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlertResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_alert_rule(self, request):
        """删除告警规则

        Delete alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteAlertRuleResponse`
        """
        http_info = self._delete_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_alert_rule_invoker(self, request):
        http_info = self._delete_alert_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_alert_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlertRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_dataobject_relations(self, request):
        """取消关联Dataobject

        取消关联Dataobject
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataobjectRelations
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteDataobjectRelationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteDataobjectRelationsResponse`
        """
        http_info = self._delete_dataobject_relations_http_info(request)
        return self._call_api(**http_info)

    def delete_dataobject_relations_invoker(self, request):
        http_info = self._delete_dataobject_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dataobject_relations_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataobjectRelationsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_incident(self, request):
        """删除事件

        删除事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIncident
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteIncidentResponse`
        """
        http_info = self._delete_incident_http_info(request)
        return self._call_api(**http_info)

    def delete_incident_invoker(self, request):
        http_info = self._delete_incident_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_incident_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIncidentResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_indicator(self, request):
        """删除指标

        删除指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIndicator
        :type request: :class:`huaweicloudsdksecmaster.v2.DeleteIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeleteIndicatorResponse`
        """
        http_info = self._delete_indicator_http_info(request)
        return self._call_api(**http_info)

    def delete_indicator_invoker(self, request):
        http_info = self._delete_indicator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_indicator_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIndicatorResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_playbook(self, request):
        """删除剧本

        删除剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookResponse`
        """
        http_info = self._delete_playbook_http_info(request)
        return self._call_api(**http_info)

    def delete_playbook_invoker(self, request):
        http_info = self._delete_playbook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_playbook_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePlaybookResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_playbook_action(self, request):
        """删除剧本动作

        删除剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookActionResponse`
        """
        http_info = self._delete_playbook_action_http_info(request)
        return self._call_api(**http_info)

    def delete_playbook_action_invoker(self, request):
        http_info = self._delete_playbook_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_playbook_action_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions/{action_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePlaybookActionResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_playbook_rule(self, request):
        """删除剧本规则

        删除剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookRuleResponse`
        """
        http_info = self._delete_playbook_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_playbook_rule_invoker(self, request):
        http_info = self._delete_playbook_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_playbook_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePlaybookRuleResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_playbook_version(self, request):
        """删除剧本版本

        删除剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DeletePlaybookVersionResponse`
        """
        http_info = self._delete_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def delete_playbook_version_invoker(self, request):
        http_info = self._delete_playbook_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_playbook_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePlaybookVersionResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def disable_alert_rule(self, request):
        """停用告警规则

        Disable alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.DisableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.DisableAlertRuleResponse`
        """
        http_info = self._disable_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def disable_alert_rule_invoker(self, request):
        http_info = self._disable_alert_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_alert_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableAlertRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def enable_alert_rule(self, request):
        """启用告警规则

        Enable alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.EnableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.EnableAlertRuleResponse`
        """
        http_info = self._enable_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def enable_alert_rule_invoker(self, request):
        http_info = self._enable_alert_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_alert_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableAlertRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_alert_rule_metrics(self, request):
        """告警规则总览

        List alert rule metrics
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRuleMetrics
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleMetricsResponse`
        """
        http_info = self._list_alert_rule_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rule_metrics_invoker(self, request):
        http_info = self._list_alert_rule_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alert_rule_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRuleMetricsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_alert_rule_templates(self, request):
        """列出告警规则模板

        List alert rule templates
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRuleTemplates
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplatesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplatesResponse`
        """
        http_info = self._list_alert_rule_templates_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rule_templates_invoker(self, request):
        http_info = self._list_alert_rule_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alert_rule_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRuleTemplatesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_alert_rules(self, request):
        """列出告警规则

        List alert rules
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRules
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertRulesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRulesResponse`
        """
        http_info = self._list_alert_rules_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rules_invoker(self, request):
        http_info = self._list_alert_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alert_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRulesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_alerts(self, request):
        """搜索告警列表

        搜索告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlerts
        :type request: :class:`huaweicloudsdksecmaster.v2.ListAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertsResponse`
        """
        http_info = self._list_alerts_http_info(request)
        return self._call_api(**http_info)

    def list_alerts_invoker(self, request):
        http_info = self._list_alerts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alerts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_dataclass(self, request):
        """查询数据类列表

        查询数据类列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataclass
        :type request: :class:`huaweicloudsdksecmaster.v2.ListDataclassRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListDataclassResponse`
        """
        http_info = self._list_dataclass_http_info(request)
        return self._call_api(**http_info)

    def list_dataclass_invoker(self, request):
        http_info = self._list_dataclass_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dataclass_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/dataclasses",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataclassResponse"
            }

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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'business_code' in local_var_params:
            query_params.append(('business_code', local_var_params['business_code']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'is_built_in' in local_var_params:
            query_params.append(('is_built_in', local_var_params['is_built_in']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_dataclass_fields(self, request):
        """查询字段列表

        查询字段列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataclassFields
        :type request: :class:`huaweicloudsdksecmaster.v2.ListDataclassFieldsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListDataclassFieldsResponse`
        """
        http_info = self._list_dataclass_fields_http_info(request)
        return self._call_api(**http_info)

    def list_dataclass_fields_invoker(self, request):
        http_info = self._list_dataclass_fields_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dataclass_fields_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/dataclasses/{dataclass_id}/fields",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataclassFieldsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_id' in local_var_params:
            path_params['dataclass_id'] = local_var_params['dataclass_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'is_built_in' in local_var_params:
            query_params.append(('is_built_in', local_var_params['is_built_in']))
        if 'field_category' in local_var_params:
            query_params.append(('field_category', local_var_params['field_category']))
        if 'mapping' in local_var_params:
            query_params.append(('mapping', local_var_params['mapping']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_dataobject_relations(self, request):
        """查询关联Dataobject列表

        查询关联Dataobject列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataobjectRelations
        :type request: :class:`huaweicloudsdksecmaster.v2.ListDataobjectRelationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListDataobjectRelationsResponse`
        """
        http_info = self._list_dataobject_relations_http_info(request)
        return self._call_api(**http_info)

    def list_dataobject_relations_invoker(self, request):
        http_info = self._list_dataobject_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dataobject_relations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataobjectRelationsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_incidents(self, request):
        """搜索事件列表

        搜索事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIncidents
        :type request: :class:`huaweicloudsdksecmaster.v2.ListIncidentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListIncidentsResponse`
        """
        http_info = self._list_incidents_http_info(request)
        return self._call_api(**http_info)

    def list_incidents_invoker(self, request):
        http_info = self._list_incidents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_incidents_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListIncidentsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_indicators(self, request):
        """查询指标列表

        查询指标列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIndicators
        :type request: :class:`huaweicloudsdksecmaster.v2.ListIndicatorsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListIndicatorsResponse`
        """
        http_info = self._list_indicators_http_info(request)
        return self._call_api(**http_info)

    def list_indicators_invoker(self, request):
        http_info = self._list_indicators_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_indicators_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListIndicatorsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_actions(self, request):
        """查询剧本动作

        查询剧本动作列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookActions
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookActionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookActionsResponse`
        """
        http_info = self._list_playbook_actions_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_actions_invoker(self, request):
        http_info = self._list_playbook_actions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_playbook_actions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookActionsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_approves(self, request):
        """查询剧本审核结果

        查询剧本审核结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookApproves
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookApprovesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookApprovesResponse`
        """
        http_info = self._list_playbook_approves_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_approves_invoker(self, request):
        http_info = self._list_playbook_approves_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_playbook_approves_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/approval",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookApprovesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_audit_logs(self, request):
        """查询剧本实例审计日志

        查询剧本实例审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookAuditLogs
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookAuditLogsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookAuditLogsResponse`
        """
        http_info = self._list_playbook_audit_logs_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_audit_logs_invoker(self, request):
        http_info = self._list_playbook_audit_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_playbook_audit_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/auditlogs",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookAuditLogsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_instances(self, request):
        """查询剧本实例列表

        查询剧本实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookInstances
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookInstancesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookInstancesResponse`
        """
        http_info = self._list_playbook_instances_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_instances_invoker(self, request):
        http_info = self._list_playbook_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_playbook_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookInstancesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_versions(self, request):
        """查询剧本版本列表

        查询剧本版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookVersions
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybookVersionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybookVersionsResponse`
        """
        http_info = self._list_playbook_versions_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_versions_invoker(self, request):
        http_info = self._list_playbook_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_playbook_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookVersionsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbooks(self, request):
        """查询剧本列表

        查询剧本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybooks
        :type request: :class:`huaweicloudsdksecmaster.v2.ListPlaybooksRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListPlaybooksResponse`
        """
        http_info = self._list_playbooks_http_info(request)
        return self._call_api(**http_info)

    def list_playbooks_invoker(self, request):
        http_info = self._list_playbooks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_playbooks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybooksResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_workflows(self, request):
        """查询流程列表

        查询流程列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflows
        :type request: :class:`huaweicloudsdksecmaster.v2.ListWorkflowsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListWorkflowsResponse`
        """
        http_info = self._list_workflows_http_info(request)
        return self._call_api(**http_info)

    def list_workflows_invoker(self, request):
        http_info = self._list_workflows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workflows_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowsResponse"
            }

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
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'sortby' in local_var_params:
            query_params.append(('sortby', local_var_params['sortby']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'last_version' in local_var_params:
            query_params.append(('last_version', local_var_params['last_version']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'dataclass_id' in local_var_params:
            query_params.append(('dataclass_id', local_var_params['dataclass_id']))
        if 'dataclass_name' in local_var_params:
            query_params.append(('dataclass_name', local_var_params['dataclass_name']))
        if 'aop_type' in local_var_params:
            query_params.append(('aop_type', local_var_params['aop_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_alert(self, request):
        """获取告警详情

        获取告警详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlert
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertResponse`
        """
        http_info = self._show_alert_http_info(request)
        return self._call_api(**http_info)

    def show_alert_invoker(self, request):
        http_info = self._show_alert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alert_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/{alert_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_alert_rule(self, request):
        """查看告警规则

        查看告警规则 Get alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleResponse`
        """
        http_info = self._show_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def show_alert_rule_invoker(self, request):
        http_info = self._show_alert_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alert_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertRuleResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_alert_rule_template(self, request):
        """查看告警规则模板

        List alert rule templates
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlertRuleTemplate
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertRuleTemplateResponse`
        """
        http_info = self._show_alert_rule_template_http_info(request)
        return self._call_api(**http_info)

    def show_alert_rule_template_invoker(self, request):
        http_info = self._show_alert_rule_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alert_rule_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertRuleTemplateResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_incident(self, request):
        """获取事件详情

        获取事件详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIncident
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowIncidentResponse`
        """
        http_info = self._show_incident_http_info(request)
        return self._call_api(**http_info)

    def show_incident_invoker(self, request):
        http_info = self._show_incident_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_incident_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/{incident_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIncidentResponse"
            }

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

    def show_indicator_detail(self, request):
        """查询指标详情

        查询指标详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIndicatorDetail
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowIndicatorDetailRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowIndicatorDetailResponse`
        """
        http_info = self._show_indicator_detail_http_info(request)
        return self._call_api(**http_info)

    def show_indicator_detail_invoker(self, request):
        http_info = self._show_indicator_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_indicator_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/{indicator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIndicatorDetailResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook(self, request):
        """查询剧本详情

        查询剧本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybook
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookResponse`
        """
        http_info = self._show_playbook_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_invoker(self, request):
        http_info = self._show_playbook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_playbook_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_instance(self, request):
        """查询剧本实例详情

        Show playbook instance
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookInstance
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookInstanceResponse`
        """
        http_info = self._show_playbook_instance_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_instance_invoker(self, request):
        http_info = self._show_playbook_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_playbook_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookInstanceResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_monitors(self, request):
        """剧本运行监控

        剧本运行监控
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookMonitors
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookMonitorsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookMonitorsResponse`
        """
        http_info = self._show_playbook_monitors_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_monitors_invoker(self, request):
        http_info = self._show_playbook_monitors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_playbook_monitors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/monitor",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookMonitorsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_rule(self, request):
        """查询剧本规则详情

        查询剧本规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookRuleResponse`
        """
        http_info = self._show_playbook_rule_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_rule_invoker(self, request):
        http_info = self._show_playbook_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_playbook_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookRuleResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_statistics(self, request):
        """剧本数据统计

        剧本统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookStatistics
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookStatisticsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookStatisticsResponse`
        """
        http_info = self._show_playbook_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_statistics_invoker(self, request):
        http_info = self._show_playbook_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_playbook_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookStatisticsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_topology(self, request):
        """查询剧本拓扑关系

        查询剧本拓扑关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookTopology
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookTopologyRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookTopologyResponse`
        """
        http_info = self._show_playbook_topology_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_topology_invoker(self, request):
        http_info = self._show_playbook_topology_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_playbook_topology_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}/topology",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookTopologyResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_version(self, request):
        """查询剧本版本详情

        Show playbook version version
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowPlaybookVersionResponse`
        """
        http_info = self._show_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_version_invoker(self, request):
        http_info = self._show_playbook_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_playbook_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookVersionResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_alert_rule(self, request):
        """更新告警规则

        Update alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleResponse`
        """
        http_info = self._update_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def update_alert_rule_invoker(self, request):
        http_info = self._update_alert_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alert_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlertRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_indicator(self, request):
        """更新指标

        更新指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIndicator
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateIndicatorResponse`
        """
        http_info = self._update_indicator_http_info(request)
        return self._call_api(**http_info)

    def update_indicator_invoker(self, request):
        http_info = self._update_indicator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_indicator_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/{indicator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIndicatorResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_playbook(self, request):
        """修改剧本

        修改剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookResponse`
        """
        http_info = self._update_playbook_http_info(request)
        return self._call_api(**http_info)

    def update_playbook_invoker(self, request):
        http_info = self._update_playbook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_playbook_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePlaybookResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_playbook_action(self, request):
        """更新剧本动作

        更新剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookActionResponse`
        """
        http_info = self._update_playbook_action_http_info(request)
        return self._call_api(**http_info)

    def update_playbook_action_invoker(self, request):
        http_info = self._update_playbook_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_playbook_action_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions/{action_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePlaybookActionResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_playbook_rule(self, request):
        """更新剧本规则

        更新剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookRuleResponse`
        """
        http_info = self._update_playbook_rule_http_info(request)
        return self._call_api(**http_info)

    def update_playbook_rule_invoker(self, request):
        http_info = self._update_playbook_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_playbook_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePlaybookRuleResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_playbook_version(self, request):
        """更新剧本版本

        更新剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdatePlaybookVersionResponse`
        """
        http_info = self._update_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def update_playbook_version_invoker(self, request):
        http_info = self._update_playbook_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_playbook_version_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePlaybookVersionResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

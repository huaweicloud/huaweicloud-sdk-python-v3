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
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdksecmaster.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SecMasterClient":
                raise TypeError("client type error, support client type is SecMasterClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_dataobject_relations(self, request):
        r"""批量关联数据对象

        批量关联数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateDataobjectRelations
        :type request: :class:`huaweicloudsdksecmaster.v1.BatchCreateDataobjectRelationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.BatchCreateDataobjectRelationsResponse`
        """
        http_info = self._batch_create_dataobject_relations_http_info(request)
        return self._call_api(**http_info)

    def batch_create_dataobject_relations_invoker(self, request):
        http_info = self._batch_create_dataobject_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_dataobject_relations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{related_dataclass_type}/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateDataobjectRelationsResponse"
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

    def batch_create_datapanel_objects(self, request):
        r"""批量创建数据对象

        数据面批量创建数据类纳管的数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateDatapanelObjects
        :type request: :class:`huaweicloudsdksecmaster.v1.BatchCreateDatapanelObjectsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.BatchCreateDatapanelObjectsResponse`
        """
        http_info = self._batch_create_datapanel_objects_http_info(request)
        return self._call_api(**http_info)

    def batch_create_datapanel_objects_invoker(self, request):
        http_info = self._batch_create_datapanel_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_datapanel_objects_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/datapanel/{dataclass}/data-objects/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateDatapanelObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass' in local_var_params:
            path_params['dataclass'] = local_var_params['dataclass']

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

    def batch_search_metric_hits(self, request):
        r"""批量查询指标结果

        批量查询指标结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSearchMetricHits
        :type request: :class:`huaweicloudsdksecmaster.v1.BatchSearchMetricHitsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.BatchSearchMetricHitsResponse`
        """
        http_info = self._batch_search_metric_hits_http_info(request)
        return self._call_api(**http_info)

    def batch_search_metric_hits_invoker(self, request):
        http_info = self._batch_search_metric_hits_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_search_metric_hits_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/metrics/hits",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSearchMetricHitsResponse"
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
        if 'timespan' in local_var_params:
            query_params.append(('timespan', local_var_params['timespan']))
        if 'cache' in local_var_params:
            query_params.append(('cache', local_var_params['cache']))

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

    def batch_tag_resources(self, request):
        r"""批量添加资源标签

        为指定实例批量添加标签
        标签管理服务需要使用该接口批量管理实例的标签。
        一个资源上最多有20个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchTagResources
        :type request: :class:`huaweicloudsdksecmaster.v1.BatchTagResourcesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.BatchTagResourcesResponse`
        """
        http_info = self._batch_tag_resources_http_info(request)
        return self._call_api(**http_info)

    def batch_tag_resources_invoker(self, request):
        http_info = self._batch_tag_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_tag_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchTagResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def batch_untag_resources(self, request):
        r"""批量删除资源标签

        为指定实例批量删除标签
        标签管理服务需要使用该接口批量管理实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUntagResources
        :type request: :class:`huaweicloudsdksecmaster.v1.BatchUntagResourcesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.BatchUntagResourcesResponse`
        """
        http_info = self._batch_untag_resources_http_info(request)
        return self._call_api(**http_info)

    def batch_untag_resources_invoker(self, request):
        http_info = self._batch_untag_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_untag_resources_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUntagResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def batch_update_catalogue(self, request):
        r"""批量修改目录

        批量修改自定义目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateCatalogue
        :type request: :class:`huaweicloudsdksecmaster.v1.BatchUpdateCatalogueRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.BatchUpdateCatalogueResponse`
        """
        http_info = self._batch_update_catalogue_http_info(request)
        return self._call_api(**http_info)

    def batch_update_catalogue_invoker(self, request):
        http_info = self._batch_update_catalogue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_catalogue_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/catalogues/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateCatalogueResponse"
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

    def change_alert(self, request):
        r"""更新告警

        编辑告警，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeAlert
        :type request: :class:`huaweicloudsdksecmaster.v1.ChangeAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ChangeAlertResponse`
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

    def change_alerts(self, request):
        r"""批量更新告警

        批量更新告警，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeAlerts
        :type request: :class:`huaweicloudsdksecmaster.v1.ChangeAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ChangeAlertsResponse`
        """
        http_info = self._change_alerts_http_info(request)
        return self._call_api(**http_info)

    def change_alerts_invoker(self, request):
        http_info = self._change_alerts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_alerts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAlertsResponse"
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

    def change_incident(self, request):
        r"""更新事件

        编辑事件，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIncident
        :type request: :class:`huaweicloudsdksecmaster.v1.ChangeIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ChangeIncidentResponse`
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

    def change_incidents(self, request):
        r"""批量更新事件

        更新事件，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIncidents
        :type request: :class:`huaweicloudsdksecmaster.v1.ChangeIncidentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ChangeIncidentsResponse`
        """
        http_info = self._change_incidents_http_info(request)
        return self._call_api(**http_info)

    def change_incidents_invoker(self, request):
        http_info = self._change_incidents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_incidents_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeIncidentsResponse"
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

    def change_playbook_instance(self, request):
        r"""操作剧本实例

        操作剧本实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangePlaybookInstance
        :type request: :class:`huaweicloudsdksecmaster.v1.ChangePlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ChangePlaybookInstanceResponse`
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

    def change_resource(self, request):
        r"""更新资产信息

        编辑资产，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeResource
        :type request: :class:`huaweicloudsdksecmaster.v1.ChangeResourceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ChangeResourceResponse`
        """
        http_info = self._change_resource_http_info(request)
        return self._call_api(**http_info)

    def change_resource_invoker(self, request):
        http_info = self._change_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_resource_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/resources/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def copy_mapping(self, request):
        r"""复制映射

        复制映射
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyMapping
        :type request: :class:`huaweicloudsdksecmaster.v1.CopyMappingRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CopyMappingResponse`
        """
        http_info = self._copy_mapping_http_info(request)
        return self._call_api(**http_info)

    def copy_mapping_invoker(self, request):
        http_info = self._copy_mapping_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_mapping_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/{mapping_id}/clone",
            "request_type": request.__class__.__name__,
            "response_type": "CopyMappingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mapping_id' in local_var_params:
            path_params['mapping_id'] = local_var_params['mapping_id']
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

    def copy_playbook_version(self, request):
        r"""克隆剧本及版本

        克隆剧本及版本（待下线）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyPlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.CopyPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CopyPlaybookVersionResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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

    def count_resource_instance(self, request):
        r"""查询资源实例数量

        使用标签过滤实例，查询资源实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountResourceInstance
        :type request: :class:`huaweicloudsdksecmaster.v1.CountResourceInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CountResourceInstanceResponse`
        """
        http_info = self._count_resource_instance_http_info(request)
        return self._call_api(**http_info)

    def count_resource_instance_invoker(self, request):
        http_info = self._count_resource_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_resource_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountResourceInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def create_alert(self, request):
        r"""创建告警

        创建告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlert
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateAlertResponse`
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
        r"""创建告警规则

        创建告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateAlertRuleResponse`
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
        r"""模拟告警规则

        模拟告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlertRuleSimulation
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateAlertRuleSimulationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateAlertRuleSimulationResponse`
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

    def create_aop_workflow(self, request):
        r"""创建流程

        创建流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAopWorkflow
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateAopWorkflowRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateAopWorkflowResponse`
        """
        http_info = self._create_aop_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_aop_workflow_invoker(self, request):
        http_info = self._create_aop_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_aop_workflow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAopWorkflowResponse"
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

    def create_aop_workflow_version(self, request):
        r"""创建流程版本

        创建流程版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAopWorkflowVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateAopWorkflowVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateAopWorkflowVersionResponse`
        """
        http_info = self._create_aop_workflow_version_http_info(request)
        return self._call_api(**http_info)

    def create_aop_workflow_version_invoker(self, request):
        http_info = self._create_aop_workflow_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_aop_workflow_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/{workflow_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAopWorkflowVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def create_aop_workflow_version_approvel(self, request):
        r"""审核流程版本的发布

        审核流程版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAopWorkflowVersionApprovel
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateAopWorkflowVersionApprovelRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateAopWorkflowVersionApprovelResponse`
        """
        http_info = self._create_aop_workflow_version_approvel_http_info(request)
        return self._call_api(**http_info)

    def create_aop_workflow_version_approvel_invoker(self, request):
        http_info = self._create_aop_workflow_version_approvel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_aop_workflow_version_approvel_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/versions/{version_id}/approval",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAopWorkflowVersionApprovelResponse"
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

    def create_batch_order_alerts(self, request):
        r"""告警转事件

        告警转事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBatchOrderAlerts
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateBatchOrderAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateBatchOrderAlertsResponse`
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

    def create_catalogue(self, request):
        r"""创建自定义目录

        新增自定义目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCatalogue
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateCatalogueRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateCatalogueResponse`
        """
        http_info = self._create_catalogue_http_info(request)
        return self._call_api(**http_info)

    def create_catalogue_invoker(self, request):
        http_info = self._create_catalogue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_catalogue_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/catalogues",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCatalogueResponse"
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

    def create_classifier(self, request):
        r"""新增分类

        新增分类
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClassifier
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateClassifierRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateClassifierResponse`
        """
        http_info = self._create_classifier_http_info(request)
        return self._call_api(**http_info)

    def create_classifier_invoker(self, request):
        http_info = self._create_classifier_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_classifier_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/classifiers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClassifierResponse"
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

    def create_collect_config(self, request):
        r"""保存云服务采集配置

        保存云服务采集配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCollectConfig
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateCollectConfigRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateCollectConfigResponse`
        """
        http_info = self._create_collect_config_http_info(request)
        return self._call_api(**http_info)

    def create_collect_config_invoker(self, request):
        http_info = self._create_collect_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_collect_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/collector/cloudlogs/config",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCollectConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))

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

    def create_collector_channel(self, request):
        r"""创建采集通道

        创建采集通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCollectorChannel
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateCollectorChannelRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateCollectorChannelResponse`
        """
        http_info = self._create_collector_channel_http_info(request)
        return self._call_api(**http_info)

    def create_collector_channel_invoker(self, request):
        http_info = self._create_collector_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_collector_channel_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCollectorChannelResponse"
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

    def create_collector_channel_group(self, request):
        r"""创建采集通道分组

        创建采集通道分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCollectorChannelGroup
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateCollectorChannelGroupRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateCollectorChannelGroupResponse`
        """
        http_info = self._create_collector_channel_group_http_info(request)
        return self._call_api(**http_info)

    def create_collector_channel_group_invoker(self, request):
        http_info = self._create_collector_channel_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_collector_channel_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCollectorChannelGroupResponse"
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

    def create_collector_channel_operation(self, request):
        r"""执行采集通道操作

        执行采集通道操作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCollectorChannelOperation
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateCollectorChannelOperationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateCollectorChannelOperationResponse`
        """
        http_info = self._create_collector_channel_operation_http_info(request)
        return self._call_api(**http_info)

    def create_collector_channel_operation_invoker(self, request):
        http_info = self._create_collector_channel_operation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_collector_channel_operation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/{channel_id}/operation",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCollectorChannelOperationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

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

    def create_collector_connection(self, request):
        r"""创建采集连接

        创建采集连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCollectorConnection
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateCollectorConnectionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateCollectorConnectionResponse`
        """
        http_info = self._create_collector_connection_http_info(request)
        return self._call_api(**http_info)

    def create_collector_connection_invoker(self, request):
        http_info = self._create_collector_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_collector_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/connections",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCollectorConnectionResponse"
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

    def create_collector_files(self, request):
        r"""安装采集通道文件

        安装采集通道文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCollectorFiles
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateCollectorFilesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateCollectorFilesResponse`
        """
        http_info = self._create_collector_files_http_info(request)
        return self._call_api(**http_info)

    def create_collector_files_invoker(self, request):
        http_info = self._create_collector_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_collector_files_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/files",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCollectorFilesResponse"
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
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def create_collector_parser(self, request):
        r"""创建采集解析器

        创建采集解析器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCollectorParser
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateCollectorParserRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateCollectorParserResponse`
        """
        http_info = self._create_collector_parser_http_info(request)
        return self._call_api(**http_info)

    def create_collector_parser_invoker(self, request):
        http_info = self._create_collector_parser_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_collector_parser_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/logstash/parsers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCollectorParserResponse"
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

    def create_component_template(self, request):
        r"""创建插件配置模板

        创建在配置流程时的插件配置模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateComponentTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateComponentTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateComponentTemplateResponse`
        """
        http_info = self._create_component_template_http_info(request)
        return self._call_api(**http_info)

    def create_component_template_invoker(self, request):
        http_info = self._create_component_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_component_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components/template",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComponentTemplateResponse"
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

    def create_configuration_application(self, request):
        r"""创建配置应用

        创建配置应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfigurationApplication
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateConfigurationApplicationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateConfigurationApplicationResponse`
        """
        http_info = self._create_configuration_application_http_info(request)
        return self._call_api(**http_info)

    def create_configuration_application_invoker(self, request):
        http_info = self._create_configuration_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_configuration_application_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/components/{component_id}/configurations/application",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConfigurationApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

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

    def create_configuration_dictionaries(self, request):
        r"""创建字典

        创建字典数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfigurationDictionaries
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateConfigurationDictionariesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateConfigurationDictionariesResponse`
        """
        http_info = self._create_configuration_dictionaries_http_info(request)
        return self._call_api(**http_info)

    def create_configuration_dictionaries_invoker(self, request):
        http_info = self._create_configuration_dictionaries_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_configuration_dictionaries_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/configurations/dictionaries",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConfigurationDictionariesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_connection(self, request):
        r"""新建操作连接

        新建操作连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnection
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateConnectionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateConnectionResponse`
        """
        http_info = self._create_connection_http_info(request)
        return self._call_api(**http_info)

    def create_connection_invoker(self, request):
        http_info = self._create_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/assetcredentials",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectionResponse"
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

    def create_dataclass_type(self, request):
        r"""数据类类型新增

        新增数据类类型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataclassType
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateDataclassTypeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateDataclassTypeResponse`
        """
        http_info = self._create_dataclass_type_http_info(request)
        return self._call_api(**http_info)

    def create_dataclass_type_invoker(self, request):
        http_info = self._create_dataclass_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dataclass_type_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/dataclasses/{dataclass_id}/types",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataclassTypeResponse"
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

    def create_dataobject(self, request):
        r"""创建数据对象

        创建数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataobject
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateDataobjectRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateDataobjectResponse`
        """
        http_info = self._create_dataobject_http_info(request)
        return self._call_api(**http_info)

    def create_dataobject_invoker(self, request):
        http_info = self._create_dataobject_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dataobject_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_name}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataobjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_name' in local_var_params:
            path_params['dataclass_name'] = local_var_params['dataclass_name']

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

    def create_dataobject_relation(self, request):
        r"""关联数据对象

        关联数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataobjectRelation
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateDataobjectRelationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateDataobjectRelationResponse`
        """
        http_info = self._create_dataobject_relation_http_info(request)
        return self._call_api(**http_info)

    def create_dataobject_relation_invoker(self, request):
        http_info = self._create_dataobject_relation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dataobject_relation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataobjectRelationResponse"
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
        r"""创建数据空间

        创建数据空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataspace
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateDataspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateDataspaceResponse`
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

    def create_generic_action(self, request):
        r"""agent-action接口

        根据type字段执行不同的agent-action，例如回答质量人工反馈。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGenericAction
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateGenericActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateGenericActionResponse`
        """
        http_info = self._create_generic_action_http_info(request)
        return self._call_api(**http_info)

    def create_generic_action_invoker(self, request):
        http_info = self._create_generic_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_generic_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/security-llm-conductor/agent/actions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGenericActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
        r"""创建事件

        创建事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIncident
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateIncidentResponse`
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
        r"""创建威胁情报

        创建威胁情报
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIndicator
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateIndicatorResponse`
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

    def create_layout(self, request):
        r"""创建布局

        创建布局
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLayout
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateLayoutRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateLayoutResponse`
        """
        http_info = self._create_layout_http_info(request)
        return self._call_api(**http_info)

    def create_layout_invoker(self, request):
        http_info = self._create_layout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_layout_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLayoutResponse"
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

    def create_layout_wizard(self, request):
        r"""新建布局页面

        创建页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLayoutWizard
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateLayoutWizardRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateLayoutWizardResponse`
        """
        http_info = self._create_layout_wizard_http_info(request)
        return self._call_api(**http_info)

    def create_layout_wizard_invoker(self, request):
        http_info = self._create_layout_wizard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_layout_wizard_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/{layout_id}/wizards",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLayoutWizardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'layout_id' in local_var_params:
            path_params['layout_id'] = local_var_params['layout_id']

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

    def create_mapper(self, request):
        r"""新增映射

        新增映射
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMapper
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateMapperRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateMapperResponse`
        """
        http_info = self._create_mapper_http_info(request)
        return self._call_api(**http_info)

    def create_mapper_invoker(self, request):
        http_info = self._create_mapper_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_mapper_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/mappers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMapperResponse"
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

    def create_metric(self, request):
        r"""创建指标

        创建指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMetric
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateMetricRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateMetricResponse`
        """
        http_info = self._create_metric_http_info(request)
        return self._call_api(**http_info)

    def create_metric_invoker(self, request):
        http_info = self._create_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_metric_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMetricResponse"
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

    def create_module(self, request):
        r"""新建模块

        创建模块.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateModule
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateModuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateModuleResponse`
        """
        http_info = self._create_module_http_info(request)
        return self._call_api(**http_info)

    def create_module_invoker(self, request):
        http_info = self._create_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_module_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/modules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateModuleResponse"
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

    def create_note(self, request):
        r"""创建评论

        创建评论
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNote
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateNoteRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateNoteResponse`
        """
        http_info = self._create_note_http_info(request)
        return self._call_api(**http_info)

    def create_note_invoker(self, request):
        http_info = self._create_note_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_note_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/notes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNoteResponse"
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
            ['application/json;charset=utf-8'])

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
        r"""创建数据管道

        创建数据管道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipe
        :type request: :class:`huaweicloudsdksecmaster.v1.CreatePipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreatePipeResponse`
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

    def create_pipe_consumption(self, request):
        r"""开启实时消费

        开启实时消费
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipeConsumption
        :type request: :class:`huaweicloudsdksecmaster.v1.CreatePipeConsumptionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreatePipeConsumptionResponse`
        """
        http_info = self._create_pipe_consumption_http_info(request)
        return self._call_api(**http_info)

    def create_pipe_consumption_invoker(self, request):
        http_info = self._create_pipe_consumption_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pipe_consumption_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}/consumption",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePipeConsumptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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
        r"""创建剧本

        创建剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookResponse`
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
        r"""创建剧本动作

        创建剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookActionResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""审核剧本

        审核剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookApprove
        :type request: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookApproveRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookApproveResponse`
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
        r"""创建剧本规则

        创建剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookRuleResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""创建剧本版本

        创建剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreatePlaybookVersionResponse`
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

    def create_pre_process_rules(self, request):
        r"""创建预处理规则

        创建预处理规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePreProcessRules
        :type request: :class:`huaweicloudsdksecmaster.v1.CreatePreProcessRulesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreatePreProcessRulesResponse`
        """
        http_info = self._create_pre_process_rules_http_info(request)
        return self._call_api(**http_info)

    def create_pre_process_rules_invoker(self, request):
        http_info = self._create_pre_process_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pre_process_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/preprocess-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePreProcessRulesResponse"
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

    def create_report(self, request):
        r"""创建安全报告

        创建安全报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateReport
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateReportRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateReportResponse`
        """
        http_info = self._create_report_http_info(request)
        return self._call_api(**http_info)

    def create_report_invoker(self, request):
        http_info = self._create_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_report_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/reports",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReportResponse"
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
        if 'region' in local_var_params:
            header_params['Region'] = local_var_params['region']

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

    def create_resource_config(self, request):
        r"""创建云日志资源

        创建云日志资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResourceConfig
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateResourceConfigRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateResourceConfigResponse`
        """
        http_info = self._create_resource_config_http_info(request)
        return self._call_api(**http_info)

    def create_resource_config_invoker(self, request):
        http_info = self._create_resource_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_resource_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/cloud-logs/resource",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceConfigResponse"
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

    def create_retry_policy(self, request):
        r"""创建重试应急策略

        创建重试应急策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRetryPolicy
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateRetryPolicyResponse`
        """
        http_info = self._create_retry_policy_http_info(request)
        return self._call_api(**http_info)

    def create_retry_policy_invoker(self, request):
        http_info = self._create_retry_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_retry_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/policys",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRetryPolicyResponse"
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
        if 'action_type' in local_var_params:
            query_params.append(('action_type', local_var_params['action_type']))

        header_params = {}
        if 'x_secmaster_version' in local_var_params:
            header_params['X-Secmaster-Version'] = local_var_params['x_secmaster_version']

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

    def create_search_condition(self, request):
        r"""创建检索条件

        创建检索条件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSearchCondition
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateSearchConditionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateSearchConditionResponse`
        """
        http_info = self._create_search_condition_http_info(request)
        return self._call_api(**http_info)

    def create_search_condition_invoker(self, request):
        http_info = self._create_search_condition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_search_condition_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/search/conditions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSearchConditionResponse"
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

    def create_service_agency(self, request):
        r"""创建委托并授权

        根据body体中的角色和作用范围，创建委托，并将策略赋予给委托
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateServiceAgency
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateServiceAgencyRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateServiceAgencyResponse`
        """
        http_info = self._create_service_agency_http_info(request)
        return self._call_api(**http_info)

    def create_service_agency_invoker(self, request):
        http_info = self._create_service_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_service_agency_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/agency",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServiceAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_shipper(self, request):
        r"""创建数据投递

        创建数据投递
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateShipper
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateShipperRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateShipperResponse`
        """
        http_info = self._create_shipper_http_info(request)
        return self._call_api(**http_info)

    def create_shipper_invoker(self, request):
        http_info = self._create_shipper_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_shipper_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateShipperResponse"
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

    def create_shipper_delegate_auth(self, request):
        r"""创建委托权限

        创建委托权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateShipperDelegateAuth
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateShipperDelegateAuthRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateShipperDelegateAuthResponse`
        """
        http_info = self._create_shipper_delegate_auth_http_info(request)
        return self._call_api(**http_info)

    def create_shipper_delegate_auth_invoker(self, request):
        http_info = self._create_shipper_delegate_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_shipper_delegate_auth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/delegate/auth/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateShipperDelegateAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
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

    def create_workflow_instance(self, request):
        r"""创建流程实例

        创建流程实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkflowInstance
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateWorkflowInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateWorkflowInstanceResponse`
        """
        http_info = self._create_workflow_instance_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_instance_invoker(self, request):
        http_info = self._create_workflow_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_workflow_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/{workflow_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def create_workspace(self, request):
        r"""新建工作空间

        在使用安全云脑的基线检查、告警管理、安全分析、安全编排等功能前，需要创建工作空间，它可以将资源划分为各个不同的工作场景，避免资源冗余查找不便，影响日常使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkspace
        :type request: :class:`huaweicloudsdksecmaster.v1.CreateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateWorkspaceResponse`
        """
        http_info = self._create_workspace_http_info(request)
        return self._call_api(**http_info)

    def create_workspace_invoker(self, request):
        http_info = self._create_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_workspace_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def delete_alert(self, request):
        r"""删除告警

        删除告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlert
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteAlertResponse`
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
        r"""删除告警规则

        删除告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteAlertRuleResponse`
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

    def delete_alerts(self, request):
        r"""批量删除告警

        批量删除告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlerts
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteAlertsResponse`
        """
        http_info = self._delete_alerts_http_info(request)
        return self._call_api(**http_info)

    def delete_alerts_invoker(self, request):
        http_info = self._delete_alerts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_alerts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlertsResponse"
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

    def delete_aop_workflow(self, request):
        r"""删除流程

        删除流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAopWorkflow
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteAopWorkflowRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteAopWorkflowResponse`
        """
        http_info = self._delete_aop_workflow_http_info(request)
        return self._call_api(**http_info)

    def delete_aop_workflow_invoker(self, request):
        http_info = self._delete_aop_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_aop_workflow_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAopWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def delete_aop_workflow_version(self, request):
        r"""删除流程版本

        删除流程版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAopWorkflowVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteAopWorkflowVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteAopWorkflowVersionResponse`
        """
        http_info = self._delete_aop_workflow_version_http_info(request)
        return self._call_api(**http_info)

    def delete_aop_workflow_version_invoker(self, request):
        http_info = self._delete_aop_workflow_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_aop_workflow_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAopWorkflowVersionResponse"
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

    def delete_catalogue(self, request):
        r"""批量删除目录

        批量删除目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCatalogue
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteCatalogueRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteCatalogueResponse`
        """
        http_info = self._delete_catalogue_http_info(request)
        return self._call_api(**http_info)

    def delete_catalogue_invoker(self, request):
        http_info = self._delete_catalogue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_catalogue_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/catalogues",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCatalogueResponse"
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

    def delete_collector_channel(self, request):
        r"""删除采集通道

        删除采集通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCollectorChannel
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteCollectorChannelRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteCollectorChannelResponse`
        """
        http_info = self._delete_collector_channel_http_info(request)
        return self._call_api(**http_info)

    def delete_collector_channel_invoker(self, request):
        http_info = self._delete_collector_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_collector_channel_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/{channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCollectorChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

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

    def delete_collector_channel_group(self, request):
        r"""删除采集通道分组

        删除采集通道分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCollectorChannelGroup
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteCollectorChannelGroupRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteCollectorChannelGroupResponse`
        """
        http_info = self._delete_collector_channel_group_http_info(request)
        return self._call_api(**http_info)

    def delete_collector_channel_group_invoker(self, request):
        http_info = self._delete_collector_channel_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_collector_channel_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCollectorChannelGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
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

    def delete_collector_connection(self, request):
        r"""删除采集连接

        删除采集连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCollectorConnection
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteCollectorConnectionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteCollectorConnectionResponse`
        """
        http_info = self._delete_collector_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_collector_connection_invoker(self, request):
        http_info = self._delete_collector_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_collector_connection_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCollectorConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def delete_collector_parser(self, request):
        r"""删除采集解析器

        删除采集解析器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCollectorParser
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteCollectorParserRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteCollectorParserResponse`
        """
        http_info = self._delete_collector_parser_http_info(request)
        return self._call_api(**http_info)

    def delete_collector_parser_invoker(self, request):
        http_info = self._delete_collector_parser_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_collector_parser_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/logstash/parsers/{parser_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCollectorParserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'parser_id' in local_var_params:
            path_params['parser_id'] = local_var_params['parser_id']

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

    def delete_component_template(self, request):
        r"""删除插件配置模板

        删除某个在配置流程时的插件配置模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteComponentTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteComponentTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteComponentTemplateResponse`
        """
        http_info = self._delete_component_template_http_info(request)
        return self._call_api(**http_info)

    def delete_component_template_invoker(self, request):
        http_info = self._delete_component_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_component_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components/template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComponentTemplateResponse"
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

    def delete_configuration_dictionaries(self, request):
        r"""删除字典

        删除字典数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfigurationDictionaries
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteConfigurationDictionariesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteConfigurationDictionariesResponse`
        """
        http_info = self._delete_configuration_dictionaries_http_info(request)
        return self._call_api(**http_info)

    def delete_configuration_dictionaries_invoker(self, request):
        http_info = self._delete_configuration_dictionaries_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_configuration_dictionaries_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/configurations/dictionaries",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfigurationDictionariesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def delete_connection(self, request):
        r"""删除操作连接

        删除操作连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConnection
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteConnectionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteConnectionResponse`
        """
        http_info = self._delete_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_connection_invoker(self, request):
        http_info = self._delete_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_connection_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/assetcredentials/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def delete_dataclass_type(self, request):
        r"""数据类类型删除

        删除数据类类型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataclassType
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteDataclassTypeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteDataclassTypeResponse`
        """
        http_info = self._delete_dataclass_type_http_info(request)
        return self._call_api(**http_info)

    def delete_dataclass_type_invoker(self, request):
        http_info = self._delete_dataclass_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dataclass_type_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/dataclasses/{dataclass_id}/types",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataclassTypeResponse"
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

    def delete_dataobject_relation(self, request):
        r"""取消关联数据对象

        取消关联数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataobjectRelation
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteDataobjectRelationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteDataobjectRelationResponse`
        """
        http_info = self._delete_dataobject_relation_http_info(request)
        return self._call_api(**http_info)

    def delete_dataobject_relation_invoker(self, request):
        http_info = self._delete_dataobject_relation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dataobject_relation_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataobjectRelationResponse"
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

    def delete_dataobjects(self, request):
        r"""批量删除数据对象

        批量删除数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataobjects
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteDataobjectsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteDataobjectsResponse`
        """
        http_info = self._delete_dataobjects_http_info(request)
        return self._call_api(**http_info)

    def delete_dataobjects_invoker(self, request):
        http_info = self._delete_dataobjects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dataobjects_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataobjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_name' in local_var_params:
            path_params['dataclass_name'] = local_var_params['dataclass_name']

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

    def delete_dataspace(self, request):
        r"""删除数据空间

        删除数据空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataspace
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteDataspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteDataspaceResponse`
        """
        http_info = self._delete_dataspace_http_info(request)
        return self._call_api(**http_info)

    def delete_dataspace_invoker(self, request):
        http_info = self._delete_dataspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dataspace_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/dataspaces/{dataspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataspace_id' in local_var_params:
            path_params['dataspace_id'] = local_var_params['dataspace_id']

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

    def delete_incident(self, request):
        r"""删除事件

        删除事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIncident
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteIncidentResponse`
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

    def delete_incidents(self, request):
        r"""批量删除事件

        批量删除事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIncidents
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteIncidentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteIncidentsResponse`
        """
        http_info = self._delete_incidents_http_info(request)
        return self._call_api(**http_info)

    def delete_incidents_invoker(self, request):
        http_info = self._delete_incidents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_incidents_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIncidentsResponse"
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

    def delete_indicator(self, request):
        r"""删除威胁情报

        删除威胁情报
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIndicator
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteIndicatorResponse`
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

    def delete_layout_wizard(self, request):
        r"""删除布局页面

        删除页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLayoutWizard
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteLayoutWizardRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteLayoutWizardResponse`
        """
        http_info = self._delete_layout_wizard_http_info(request)
        return self._call_api(**http_info)

    def delete_layout_wizard_invoker(self, request):
        http_info = self._delete_layout_wizard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_layout_wizard_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/wizards/{wizard_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLayoutWizardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'wizard_id' in local_var_params:
            path_params['wizard_id'] = local_var_params['wizard_id']

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

    def delete_layouts(self, request):
        r"""删除布局

        删除布局
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLayouts
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteLayoutsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteLayoutsResponse`
        """
        http_info = self._delete_layouts_http_info(request)
        return self._call_api(**http_info)

    def delete_layouts_invoker(self, request):
        http_info = self._delete_layouts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_layouts_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLayoutsResponse"
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

    def delete_lts_cloud_log(self, request):
        r"""删除lts日志订阅

        删除云日志资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLtsCloudLog
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteLtsCloudLogRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteLtsCloudLogResponse`
        """
        http_info = self._delete_lts_cloud_log_http_info(request)
        return self._call_api(**http_info)

    def delete_lts_cloud_log_invoker(self, request):
        http_info = self._delete_lts_cloud_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_lts_cloud_log_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/collector/cloudlogs/config/{csvc}/{source_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLtsCloudLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'csvc' in local_var_params:
            path_params['csvc'] = local_var_params['csvc']
        if 'source_name' in local_var_params:
            path_params['source_name'] = local_var_params['source_name']

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

    def delete_mapping_info(self, request):
        r"""删除映射信息

        删除映射信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMappingInfo
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteMappingInfoRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteMappingInfoResponse`
        """
        http_info = self._delete_mapping_info_http_info(request)
        return self._call_api(**http_info)

    def delete_mapping_info_invoker(self, request):
        http_info = self._delete_mapping_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_mapping_info_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/{mapping_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMappingInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mapping_id' in local_var_params:
            path_params['mapping_id'] = local_var_params['mapping_id']
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

    def delete_metrics(self, request):
        r"""删除指标

        删除指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMetrics
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteMetricsResponse`
        """
        http_info = self._delete_metrics_http_info(request)
        return self._call_api(**http_info)

    def delete_metrics_invoker(self, request):
        http_info = self._delete_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_metrics_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/metrics/{metric_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'metric_id' in local_var_params:
            path_params['metric_id'] = local_var_params['metric_id']

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

    def delete_module(self, request):
        r"""删除模块

        删除模块
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteModule
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteModuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteModuleResponse`
        """
        http_info = self._delete_module_http_info(request)
        return self._call_api(**http_info)

    def delete_module_invoker(self, request):
        http_info = self._delete_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_module_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/modules/{module_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def delete_node(self, request):
        r"""通过节点id删除节点

        删除节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNode
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteNodeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteNodeResponse`
        """
        http_info = self._delete_node_http_info(request)
        return self._call_api(**http_info)

    def delete_node_invoker(self, request):
        http_info = self._delete_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_node_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNodeResponse"
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

    def delete_notes(self, request):
        r"""删除评论

        删除评论
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNotes
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteNotesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteNotesResponse`
        """
        http_info = self._delete_notes_http_info(request)
        return self._call_api(**http_info)

    def delete_notes_invoker(self, request):
        http_info = self._delete_notes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_notes_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/notes",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNotesResponse"
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
            ['application/json;charset=utf-8'])

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

    def delete_pipe(self, request):
        r"""删除数据管道

        删除数据管道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePipe
        :type request: :class:`huaweicloudsdksecmaster.v1.DeletePipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeletePipeResponse`
        """
        http_info = self._delete_pipe_http_info(request)
        return self._call_api(**http_info)

    def delete_pipe_invoker(self, request):
        http_info = self._delete_pipe_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_pipe_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePipeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def delete_pipe_consumption(self, request):
        r"""关闭实时消费

        关闭实时消费
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePipeConsumption
        :type request: :class:`huaweicloudsdksecmaster.v1.DeletePipeConsumptionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeletePipeConsumptionResponse`
        """
        http_info = self._delete_pipe_consumption_http_info(request)
        return self._call_api(**http_info)

    def delete_pipe_consumption_invoker(self, request):
        http_info = self._delete_pipe_consumption_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_pipe_consumption_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}/consumption",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePipeConsumptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def delete_playbook(self, request):
        r"""删除剧本

        删除剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v1.DeletePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeletePlaybookResponse`
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
        r"""删除剧本动作

        删除剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v1.DeletePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeletePlaybookActionResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""删除剧本规则

        删除剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v1.DeletePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeletePlaybookRuleResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""删除剧本版本

        删除剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.DeletePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeletePlaybookVersionResponse`
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

    def delete_policies(self, request):
        r"""批量删除应急策略

        批量删除应急策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicies
        :type request: :class:`huaweicloudsdksecmaster.v1.DeletePoliciesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeletePoliciesResponse`
        """
        http_info = self._delete_policies_http_info(request)
        return self._call_api(**http_info)

    def delete_policies_invoker(self, request):
        http_info = self._delete_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policies_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/policys/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePoliciesResponse"
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
        if 'x_secmaster_version' in local_var_params:
            header_params['X-Secmaster-Version'] = local_var_params['x_secmaster_version']

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

    def delete_report(self, request):
        r"""删除报告

        删除报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteReport
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteReportRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteReportResponse`
        """
        http_info = self._delete_report_http_info(request)
        return self._call_api(**http_info)

    def delete_report_invoker(self, request):
        http_info = self._delete_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_report_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/reports/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

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

    def delete_resource(self, request):
        r"""删除资产

        删除资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResource
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteResourceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteResourceResponse`
        """
        http_info = self._delete_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_invoker(self, request):
        http_info = self._delete_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_resource_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/resources",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_search_condition(self, request):
        r"""删除检索条件

        删除检索条件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSearchCondition
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteSearchConditionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteSearchConditionResponse`
        """
        http_info = self._delete_search_condition_http_info(request)
        return self._call_api(**http_info)

    def delete_search_condition_invoker(self, request):
        http_info = self._delete_search_condition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_search_condition_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/search/conditions/{condition_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSearchConditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'condition_id' in local_var_params:
            path_params['condition_id'] = local_var_params['condition_id']

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

    def delete_shipper(self, request):
        r"""删除投递信息

        删除投递信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteShipper
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteShipperRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteShipperResponse`
        """
        http_info = self._delete_shipper_http_info(request)
        return self._call_api(**http_info)

    def delete_shipper_invoker(self, request):
        http_info = self._delete_shipper_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_shipper_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteShipperResponse"
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

    def delete_single_mapper(self, request):
        r"""删除单个映射

        删除单个映射
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSingleMapper
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteSingleMapperRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteSingleMapperResponse`
        """
        http_info = self._delete_single_mapper_http_info(request)
        return self._call_api(**http_info)

    def delete_single_mapper_invoker(self, request):
        http_info = self._delete_single_mapper_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_single_mapper_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/mappers/{mapper_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSingleMapperResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'mapper_id' in local_var_params:
            path_params['mapper_id'] = local_var_params['mapper_id']

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

    def delete_tags(self, request):
        r"""删除资源标签

        为指定实例批量删除标签
        标签管理服务需要使用该接口批量管理实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTags
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteTagsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteTagsResponse`
        """
        http_info = self._delete_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_tags_invoker(self, request):
        http_info = self._delete_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def delete_workspace(self, request):
        r"""删除工作空间

        删除工作空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkspace
        :type request: :class:`huaweicloudsdksecmaster.v1.DeleteWorkspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DeleteWorkspaceResponse`
        """
        http_info = self._delete_workspace_http_info(request)
        return self._call_api(**http_info)

    def delete_workspace_invoker(self, request):
        http_info = self._delete_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_workspace_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkspaceResponse"
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
        if 'permanent_delete' in local_var_params:
            query_params.append(('permanent_delete', local_var_params['permanent_delete']))

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

    def disable_alert_rule(self, request):
        r"""停用告警规则

        停用告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v1.DisableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DisableAlertRuleResponse`
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

    def download_alert_template(self, request):
        r"""下载告警导入模板

        下载告警导入模板，模板根据标准的dataclass字段属性来组织，下载时需要实现默认的告警样例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAlertTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.DownloadAlertTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DownloadAlertTemplateResponse`
        """
        http_info = self._download_alert_template_http_info(request)
        return self._call_api(**http_info)

    def download_alert_template_invoker(self, request):
        http_info = self._download_alert_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_alert_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/template/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAlertTemplateResponse"
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

    def download_attachment(self, request):
        r"""下载附件

        从OBS下载附件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAttachment
        :type request: :class:`huaweicloudsdksecmaster.v1.DownloadAttachmentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DownloadAttachmentResponse`
        """
        http_info = self._download_attachment_http_info(request)
        return self._call_api(**http_info)

    def download_attachment_invoker(self, request):
        http_info = self._download_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_attachment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/attachment/{attach_id}/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'attach_id' in local_var_params:
            path_params['attach_id'] = local_var_params['attach_id']

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

    def download_incident_template(self, request):
        r"""下载事件导入模板

        下载事件导入模板，模板根据标准的dataclass字段属性来组织，下载时需要实现默认的事件样例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadIncidentTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.DownloadIncidentTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DownloadIncidentTemplateResponse`
        """
        http_info = self._download_incident_template_http_info(request)
        return self._call_api(**http_info)

    def download_incident_template_invoker(self, request):
        http_info = self._download_incident_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_incident_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/template/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadIncidentTemplateResponse"
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

    def download_indicator_template(self, request):
        r"""下载情报模板

        下载情报导入模板，模板根据标准的dataclass字段属性来组织，下载时需要实现默认的情报样例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadIndicatorTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.DownloadIndicatorTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DownloadIndicatorTemplateResponse`
        """
        http_info = self._download_indicator_template_http_info(request)
        return self._call_api(**http_info)

    def download_indicator_template_invoker(self, request):
        http_info = self._download_indicator_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_indicator_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/template/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadIndicatorTemplateResponse"
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

    def download_resource_template(self, request):
        r"""下载资产导入模板

        下载资产导入模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadResourceTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.DownloadResourceTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DownloadResourceTemplateResponse`
        """
        http_info = self._download_resource_template_http_info(request)
        return self._call_api(**http_info)

    def download_resource_template_invoker(self, request):
        http_info = self._download_resource_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_resource_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/resources/template/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadResourceTemplateResponse"
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
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def download_vulnerability_template(self, request):
        r"""下载漏洞导入模板

        下载漏洞导入模板，模板根据标准的dataclass字段属性来组织
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadVulnerabilityTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.DownloadVulnerabilityTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.DownloadVulnerabilityTemplateResponse`
        """
        http_info = self._download_vulnerability_template_http_info(request)
        return self._call_api(**http_info)

    def download_vulnerability_template_invoker(self, request):
        http_info = self._download_vulnerability_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_vulnerability_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/vulnerability/template/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadVulnerabilityTemplateResponse"
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

    def enable_alert_rule(self, request):
        r"""启用告警规则

        启用告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v1.EnableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.EnableAlertRuleResponse`
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

    def enable_dataclass_type(self, request):
        r"""数据类类型启用/禁用

        禁用/启用数据类类型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableDataclassType
        :type request: :class:`huaweicloudsdksecmaster.v1.EnableDataclassTypeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.EnableDataclassTypeResponse`
        """
        http_info = self._enable_dataclass_type_http_info(request)
        return self._call_api(**http_info)

    def enable_dataclass_type_invoker(self, request):
        http_info = self._enable_dataclass_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_dataclass_type_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/dataclasses/{dataclass_id}/types/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDataclassTypeResponse"
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

    def execute_report_action(self, request):
        r"""操作安全报告

        操作安全报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteReportAction
        :type request: :class:`huaweicloudsdksecmaster.v1.ExecuteReportActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExecuteReportActionResponse`
        """
        http_info = self._execute_report_action_http_info(request)
        return self._call_api(**http_info)

    def execute_report_action_invoker(self, request):
        http_info = self._execute_report_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_report_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/reports/{report_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteReportActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

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

    def export_alerts(self, request):
        r"""导出告警

        导出告警,若字段是object类型，则将整个子对象的内容导出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportAlerts
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportAlertsResponse`
        """
        http_info = self._export_alerts_http_info(request)
        return self._call_api(**http_info)

    def export_alerts_invoker(self, request):
        http_info = self._export_alerts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_alerts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportAlertsResponse"
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

    def export_aopworkflow(self, request):
        r"""导出流程

        导出流程信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportAopworkflow
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportAopworkflowRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportAopworkflowResponse`
        """
        http_info = self._export_aopworkflow_http_info(request)
        return self._call_api(**http_info)

    def export_aopworkflow_invoker(self, request):
        http_info = self._export_aopworkflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_aopworkflow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportAopworkflowResponse"
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

    def export_collector_parser(self, request):
        r"""导出采集解析器

        导出采集解析器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportCollectorParser
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportCollectorParserRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportCollectorParserResponse`
        """
        http_info = self._export_collector_parser_http_info(request)
        return self._call_api(**http_info)

    def export_collector_parser_invoker(self, request):
        http_info = self._export_collector_parser_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_collector_parser_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/logstash/parsers/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportCollectorParserResponse"
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

    def export_dataobjects(self, request):
        r"""导出数据对象

        导出数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportDataobjects
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportDataobjectsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportDataobjectsResponse`
        """
        http_info = self._export_dataobjects_http_info(request)
        return self._call_api(**http_info)

    def export_dataobjects_invoker(self, request):
        http_info = self._export_dataobjects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_dataobjects_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_name}/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportDataobjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_name' in local_var_params:
            path_params['dataclass_name'] = local_var_params['dataclass_name']

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

    def export_incidents(self, request):
        r"""导出事件

        导出事件列表,若字段是object类型，需要将整个子对象的内容导出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportIncidents
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportIncidentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportIncidentsResponse`
        """
        http_info = self._export_incidents_http_info(request)
        return self._call_api(**http_info)

    def export_incidents_invoker(self, request):
        http_info = self._export_incidents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_incidents_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportIncidentsResponse"
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

    def export_indicators(self, request):
        r"""导出情报

        导出情报,若字段是object类型，则将整个子对象的内容导出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportIndicators
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportIndicatorsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportIndicatorsResponse`
        """
        http_info = self._export_indicators_http_info(request)
        return self._call_api(**http_info)

    def export_indicators_invoker(self, request):
        http_info = self._export_indicators_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_indicators_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportIndicatorsResponse"
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

    def export_playbook(self, request):
        r"""导出剧本信息

        导出剧本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportPlaybook
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportPlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportPlaybookResponse`
        """
        http_info = self._export_playbook_http_info(request)
        return self._call_api(**http_info)

    def export_playbook_invoker(self, request):
        http_info = self._export_playbook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_playbook_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportPlaybookResponse"
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

    def export_resources(self, request):
        r"""导出资产列表

        导出资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportResources
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportResourcesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportResourcesResponse`
        """
        http_info = self._export_resources_http_info(request)
        return self._call_api(**http_info)

    def export_resources_invoker(self, request):
        http_info = self._export_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/resources/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportResourcesResponse"
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
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def export_vulnerabilities(self, request):
        r"""导出漏洞

        导出详细漏洞信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportVulnerabilities
        :type request: :class:`huaweicloudsdksecmaster.v1.ExportVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ExportVulnerabilitiesResponse`
        """
        http_info = self._export_vulnerabilities_http_info(request)
        return self._call_api(**http_info)

    def export_vulnerabilities_invoker(self, request):
        http_info = self._export_vulnerabilities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_vulnerabilities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/vulnerability/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportVulnerabilitiesResponse"
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

    def handle_shipper_authorization(self, request):
        r"""授权处理

        授权处理
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HandleShipperAuthorization
        :type request: :class:`huaweicloudsdksecmaster.v1.HandleShipperAuthorizationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.HandleShipperAuthorizationResponse`
        """
        http_info = self._handle_shipper_authorization_http_info(request)
        return self._call_api(**http_info)

    def handle_shipper_authorization_invoker(self, request):
        http_info = self._handle_shipper_authorization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _handle_shipper_authorization_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/authorizations/handle",
            "request_type": request.__class__.__name__,
            "response_type": "HandleShipperAuthorizationResponse"
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

    def import_alerts(self, request):
        r"""导入告警

        批量导入告警，根据template下载的模板填写告警，告警的所有字段根据是否必填来限制，参照:安全事件数据对象定义中的类型和说明来确定, 后台实现时需要校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportAlerts
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportAlertsResponse`
        """
        http_info = self._import_alerts_http_info(request)
        return self._call_api(**http_info)

    def import_alerts_invoker(self, request):
        http_info = self._import_alerts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_alerts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportAlertsResponse"
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
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def import_aopworkflow(self, request):
        r"""导入流程信息

        导入流程信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportAopworkflow
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportAopworkflowRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportAopworkflowResponse`
        """
        http_info = self._import_aopworkflow_http_info(request)
        return self._call_api(**http_info)

    def import_aopworkflow_invoker(self, request):
        http_info = self._import_aopworkflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_aopworkflow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportAopworkflowResponse"
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
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def import_collector_parser(self, request):
        r"""导入采集解析器

        导入采集解析器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportCollectorParser
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportCollectorParserRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportCollectorParserResponse`
        """
        http_info = self._import_collector_parser_http_info(request)
        return self._call_api(**http_info)

    def import_collector_parser_invoker(self, request):
        http_info = self._import_collector_parser_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_collector_parser_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/logstash/parsers/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportCollectorParserResponse"
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
        if 'files' in local_var_params:
            form_params['files'] = local_var_params['files']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def import_dataobjects(self, request):
        r"""导入数据对象

        导入数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportDataobjects
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportDataobjectsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportDataobjectsResponse`
        """
        http_info = self._import_dataobjects_http_info(request)
        return self._call_api(**http_info)

    def import_dataobjects_invoker(self, request):
        http_info = self._import_dataobjects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_dataobjects_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_name}/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportDataobjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_name' in local_var_params:
            path_params['dataclass_name'] = local_var_params['dataclass_name']

        query_params = []

        header_params = {}

        form_params = {}
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def import_incidents(self, request):
        r"""导入事件

        导入事件，根据template下载的模板填写事件，事件的所有字段根据是否必填来限制，参照:安全事件数据对象定义中的类型和说明来确定, 后台实现时需要校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportIncidents
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportIncidentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportIncidentsResponse`
        """
        http_info = self._import_incidents_http_info(request)
        return self._call_api(**http_info)

    def import_incidents_invoker(self, request):
        http_info = self._import_incidents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_incidents_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportIncidentsResponse"
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
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def import_indicators(self, request):
        r"""导入情报

        批量导入情报，根据template下载的模板填写情报，告警的所有字段根据是否必填来限制，参照:安全事件数据对象定义中的类型和说明来确定, 后台实现时需要校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportIndicators
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportIndicatorsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportIndicatorsResponse`
        """
        http_info = self._import_indicators_http_info(request)
        return self._call_api(**http_info)

    def import_indicators_invoker(self, request):
        http_info = self._import_indicators_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_indicators_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportIndicatorsResponse"
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
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def import_playbook(self, request):
        r"""导入剧本信息

        导入剧本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportPlaybook
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportPlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportPlaybookResponse`
        """
        http_info = self._import_playbook_http_info(request)
        return self._call_api(**http_info)

    def import_playbook_invoker(self, request):
        http_info = self._import_playbook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_playbook_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportPlaybookResponse"
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
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']
        if 'upload_model' in local_var_params:
            form_params['upload_model'] = local_var_params['upload_model']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def import_resource(self, request):
        r"""导入资产

        导入资产，根据下载的模板填写资产，资产的所有字段根据是否必填来限制，参照:资产对象定义中的类型和说明来确定, 后台实现时需要校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportResource
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportResourceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportResourceResponse`
        """
        http_info = self._import_resource_http_info(request)
        return self._call_api(**http_info)

    def import_resource_invoker(self, request):
        http_info = self._import_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/resources/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportResourceResponse"
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
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def import_vulnerabilities(self, request):
        r"""导入漏洞

        批量导入漏洞，根据template下载的模板填写漏洞，漏洞的所有字段根据是否必填来限制，参照:安全事件数据对象定义中的类型和说明来确定, 后台实现时需要校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportVulnerabilities
        :type request: :class:`huaweicloudsdksecmaster.v1.ImportVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ImportVulnerabilitiesResponse`
        """
        http_info = self._import_vulnerabilities_http_info(request)
        return self._call_api(**http_info)

    def import_vulnerabilities_invoker(self, request):
        http_info = self._import_vulnerabilities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_vulnerabilities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/vulnerability/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportVulnerabilitiesResponse"
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
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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
        r"""告警规则总览

        告警规则总览
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRuleMetrics
        :type request: :class:`huaweicloudsdksecmaster.v1.ListAlertRuleMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListAlertRuleMetricsResponse`
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

    def list_alert_rule_template_metrics(self, request):
        r"""告警模板总览

        告警模板总览
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRuleTemplateMetrics
        :type request: :class:`huaweicloudsdksecmaster.v1.ListAlertRuleTemplateMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListAlertRuleTemplateMetricsResponse`
        """
        http_info = self._list_alert_rule_template_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rule_template_metrics_invoker(self, request):
        http_info = self._list_alert_rule_template_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alert_rule_template_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRuleTemplateMetricsResponse"
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

    def list_alert_rule_templates(self, request):
        r"""列出告警规则模板

        列出告警规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRuleTemplates
        :type request: :class:`huaweicloudsdksecmaster.v1.ListAlertRuleTemplatesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListAlertRuleTemplatesResponse`
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
        r"""列出告警规则

        列出告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlertRules
        :type request: :class:`huaweicloudsdksecmaster.v1.ListAlertRulesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListAlertRulesResponse`
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
        r"""搜索告警列表

        搜索告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlerts
        :type request: :class:`huaweicloudsdksecmaster.v1.ListAlertsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListAlertsResponse`
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

    def list_all_second_catalogue(self, request):
        r"""获取目录全量列表

        获取目录全量列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllSecondCatalogue
        :type request: :class:`huaweicloudsdksecmaster.v1.ListAllSecondCatalogueRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListAllSecondCatalogueResponse`
        """
        http_info = self._list_all_second_catalogue_http_info(request)
        return self._call_api(**http_info)

    def list_all_second_catalogue_invoker(self, request):
        http_info = self._list_all_second_catalogue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_second_catalogue_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/catalogues",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllSecondCatalogueResponse"
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
        if 'catalogue_type' in local_var_params:
            query_params.append(('catalogue_type', local_var_params['catalogue_type']))
        if 'catalogue_code' in local_var_params:
            query_params.append(('catalogue_code', local_var_params['catalogue_code']))

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

    def list_aop_workflow_instance(self, request):
        r"""查询流程实例的列表

        查询流程实例的列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAopWorkflowInstance
        :type request: :class:`huaweicloudsdksecmaster.v1.ListAopWorkflowInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListAopWorkflowInstanceResponse`
        """
        http_info = self._list_aop_workflow_instance_http_info(request)
        return self._call_api(**http_info)

    def list_aop_workflow_instance_invoker(self, request):
        http_info = self._list_aop_workflow_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aop_workflow_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListAopWorkflowInstanceResponse"
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
        if 'from_date' in local_var_params:
            query_params.append(('from_date', local_var_params['from_date']))
        if 'to_date' in local_var_params:
            query_params.append(('to_date', local_var_params['to_date']))
        if 'workflow_id' in local_var_params:
            query_params.append(('workflow_id', local_var_params['workflow_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'dataobject_id' in local_var_params:
            query_params.append(('dataobject_id', local_var_params['dataobject_id']))
        if 'dataclass_id' in local_var_params:
            query_params.append(('dataclass_id', local_var_params['dataclass_id']))
        if 'playbook_id' in local_var_params:
            query_params.append(('playbook_id', local_var_params['playbook_id']))
        if 'defence_id' in local_var_params:
            query_params.append(('defence_id', local_var_params['defence_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'trigger_type' in local_var_params:
            query_params.append(('trigger_type', local_var_params['trigger_type']))

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

    def list_aop_workflow_versions(self, request):
        r"""查询流程版本列表

        查询流程版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAopWorkflowVersions
        :type request: :class:`huaweicloudsdksecmaster.v1.ListAopWorkflowVersionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListAopWorkflowVersionsResponse`
        """
        http_info = self._list_aop_workflow_versions_http_info(request)
        return self._call_api(**http_info)

    def list_aop_workflow_versions_invoker(self, request):
        http_info = self._list_aop_workflow_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aop_workflow_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/{workflow_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListAopWorkflowVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_catalogue(self, request):
        r"""目录列表查询

        目录列表查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCatalogue
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCatalogueRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCatalogueResponse`
        """
        http_info = self._list_catalogue_http_info(request)
        return self._call_api(**http_info)

    def list_catalogue_invoker(self, request):
        http_info = self._list_catalogue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_catalogue_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/catalogues/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListCatalogueResponse"
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

    def list_cloud_log_alias(self, request):
        r"""列出管道alias

        列出云日志资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudLogAlias
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCloudLogAliasRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCloudLogAliasResponse`
        """
        http_info = self._list_cloud_log_alias_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_log_alias_invoker(self, request):
        http_info = self._list_cloud_log_alias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_log_alias_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/collector/cloudlogs/alias",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudLogAliasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def list_cloud_log_manages(self, request):
        r"""列出行管账户信息

        列出云日志资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudLogManages
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCloudLogManagesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCloudLogManagesResponse`
        """
        http_info = self._list_cloud_log_manages_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_log_manages_invoker(self, request):
        http_info = self._list_cloud_log_manages_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_log_manages_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/collector/cloudlogs/managers",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudLogManagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def list_cloud_log_platform(self, request):
        r"""列出平台行管账户信息

        列出云日志资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudLogPlatform
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCloudLogPlatformRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCloudLogPlatformResponse`
        """
        http_info = self._list_cloud_log_platform_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_log_platform_invoker(self, request):
        http_info = self._list_cloud_log_platform_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_log_platform_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/cloud-logs/platform",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudLogPlatformResponse"
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

    def list_cloud_log_resources(self, request):
        r"""列出云日志资源

        列出云日志资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudLogResources
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCloudLogResourcesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCloudLogResourcesResponse`
        """
        http_info = self._list_cloud_log_resources_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_log_resources_invoker(self, request):
        http_info = self._list_cloud_log_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_log_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/cloud-logs/resource",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudLogResourcesResponse"
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
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
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

    def list_collect_config(self, request):
        r"""获取云服务采集配置

        获取云服务采集配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectConfig
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponse`
        """
        http_info = self._list_collect_config_http_info(request)
        return self._call_api(**http_info)

    def list_collect_config_invoker(self, request):
        http_info = self._list_collect_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collect_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/collector/cloudlogs/config",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'csvc' in local_var_params:
            query_params.append(('csvc', local_var_params['csvc']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'query_statistics' in local_var_params:
            query_params.append(('query_statistics', local_var_params['query_statistics']))

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

    def list_collector_channel_group(self, request):
        r"""列出采集通道分组

        列出采集通道分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorChannelGroup
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorChannelGroupRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorChannelGroupResponse`
        """
        http_info = self._list_collector_channel_group_http_info(request)
        return self._call_api(**http_info)

    def list_collector_channel_group_invoker(self, request):
        http_info = self._list_collector_channel_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_channel_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorChannelGroupResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_collector_channels(self, request):
        r"""列出采集通道列表

        列出采集通道列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorChannels
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorChannelsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorChannelsResponse`
        """
        http_info = self._list_collector_channels_http_info(request)
        return self._call_api(**http_info)

    def list_collector_channels_invoker(self, request):
        http_info = self._list_collector_channels_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_channels_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorChannelsResponse"
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
        if 'title' in local_var_params:
            query_params.append(('title', local_var_params['title']))
        if 'connection_module_id' in local_var_params:
            query_params.append(('connection_module_id', local_var_params['connection_module_id']))
        if 'parser_id' in local_var_params:
            query_params.append(('parser_id', local_var_params['parser_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
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

    def list_collector_connections(self, request):
        r"""列表采集连接

        列表采集连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorConnections
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorConnectionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorConnectionsResponse`
        """
        http_info = self._list_collector_connections_http_info(request)
        return self._call_api(**http_info)

    def list_collector_connections_invoker(self, request):
        http_info = self._list_collector_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorConnectionsResponse"
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
        if 'connection_type' in local_var_params:
            query_params.append(('connection_type', local_var_params['connection_type']))
        if 'title' in local_var_params:
            query_params.append(('title', local_var_params['title']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
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

    def list_collector_instances(self, request):
        r"""列出采集通道实例

        列出采集通道实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorInstances
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorInstancesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorInstancesResponse`
        """
        http_info = self._list_collector_instances_http_info(request)
        return self._call_api(**http_info)

    def list_collector_instances_invoker(self, request):
        http_info = self._list_collector_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorInstancesResponse"
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
        if 'channel_id' in local_var_params:
            query_params.append(('channel_id', local_var_params['channel_id']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'node_name' in local_var_params:
            query_params.append(('node_name', local_var_params['node_name']))
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

    def list_collector_module_restrictions(self, request):
        r"""列出采集模块规则

        列出采集模块规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorModuleRestrictions
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorModuleRestrictionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorModuleRestrictionsResponse`
        """
        http_info = self._list_collector_module_restrictions_http_info(request)
        return self._call_api(**http_info)

    def list_collector_module_restrictions_invoker(self, request):
        http_info = self._list_collector_module_restrictions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_module_restrictions_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/module-templates/restriction",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorModuleRestrictionsResponse"
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

    def list_collector_module_template(self, request):
        r"""列出采集模块

        列出采集模块
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorModuleTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorModuleTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorModuleTemplateResponse`
        """
        http_info = self._list_collector_module_template_http_info(request)
        return self._call_api(**http_info)

    def list_collector_module_template_invoker(self, request):
        http_info = self._list_collector_module_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_module_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/module-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorModuleTemplateResponse"
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
        if 'parser_type' in local_var_params:
            query_params.append(('parser_type', local_var_params['parser_type']))

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

    def list_collector_node(self, request):
        r"""列出采集节点

        列出采集节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorNode
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorNodeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorNodeResponse`
        """
        http_info = self._list_collector_node_http_info(request)
        return self._call_api(**http_info)

    def list_collector_node_invoker(self, request):
        http_info = self._list_collector_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_node_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorNodeResponse"
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
        if 'health_status' in local_var_params:
            query_params.append(('health_status', local_var_params['health_status']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'node_name' in local_var_params:
            query_params.append(('node_name', local_var_params['node_name']))
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
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

    def list_collector_parser_template(self, request):
        r"""列出采集解析器模板

        列出采集解析器模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorParserTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorParserTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorParserTemplateResponse`
        """
        http_info = self._list_collector_parser_template_http_info(request)
        return self._call_api(**http_info)

    def list_collector_parser_template_invoker(self, request):
        http_info = self._list_collector_parser_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_parser_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/logstash/parsers/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorParserTemplateResponse"
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
        if 'title' in local_var_params:
            query_params.append(('title', local_var_params['title']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
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

    def list_collector_parsers(self, request):
        r"""列出采集解析器

        列出采集解析器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollectorParsers
        :type request: :class:`huaweicloudsdksecmaster.v1.ListCollectorParsersRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListCollectorParsersResponse`
        """
        http_info = self._list_collector_parsers_http_info(request)
        return self._call_api(**http_info)

    def list_collector_parsers_invoker(self, request):
        http_info = self._list_collector_parsers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collector_parsers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/logstash/parsers",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectorParsersResponse"
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
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))
        if 'title' in local_var_params:
            query_params.append(('title', local_var_params['title']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
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

    def list_component_actions(self, request):
        r"""查询插件Action列表

        查询插件的函数、连接器和管理器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComponentActions
        :type request: :class:`huaweicloudsdksecmaster.v1.ListComponentActionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListComponentActionsResponse`
        """
        http_info = self._list_component_actions_http_info(request)
        return self._call_api(**http_info)

    def list_component_actions_invoker(self, request):
        http_info = self._list_component_actions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_component_actions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components/{component_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentActionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))

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

    def list_component_configuration(self, request):
        r"""列出组件配置

        列出组件配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComponentConfiguration
        :type request: :class:`huaweicloudsdksecmaster.v1.ListComponentConfigurationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListComponentConfigurationResponse`
        """
        http_info = self._list_component_configuration_http_info(request)
        return self._call_api(**http_info)

    def list_component_configuration_invoker(self, request):
        http_info = self._list_component_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_component_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/components/{component_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_component_template(self, request):
        r"""列出组件模板

        列出组件模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComponentTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.ListComponentTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListComponentTemplateResponse`
        """
        http_info = self._list_component_template_http_info(request)
        return self._call_api(**http_info)

    def list_component_template_invoker(self, request):
        http_info = self._list_component_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_component_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/components/{component_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []
        if 'file_type' in local_var_params:
            query_params.append(('file_type', local_var_params['file_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_component_templates(self, request):
        r"""查询插件配置模板列表

        查询在配置流程时的插件配置模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComponentTemplates
        :type request: :class:`huaweicloudsdksecmaster.v1.ListComponentTemplatesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListComponentTemplatesResponse`
        """
        http_info = self._list_component_templates_http_info(request)
        return self._call_api(**http_info)

    def list_component_templates_invoker(self, request):
        http_info = self._list_component_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_component_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components/template",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentTemplatesResponse"
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
        if 'search_value' in local_var_params:
            query_params.append(('search_value', local_var_params['search_value']))
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

    def list_components(self, request):
        r"""查询插件定义列表

        查询插件定义列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComponents
        :type request: :class:`huaweicloudsdksecmaster.v1.ListComponentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListComponentsResponse`
        """
        http_info = self._list_components_http_info(request)
        return self._call_api(**http_info)

    def list_components_invoker(self, request):
        http_info = self._list_components_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_components_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentsResponse"
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

    def list_configuration_dictionaries(self, request):
        r"""获取字典信息

        获取字典信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurationDictionaries
        :type request: :class:`huaweicloudsdksecmaster.v1.ListConfigurationDictionariesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListConfigurationDictionariesResponse`
        """
        http_info = self._list_configuration_dictionaries_http_info(request)
        return self._call_api(**http_info)

    def list_configuration_dictionaries_invoker(self, request):
        http_info = self._list_configuration_dictionaries_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_configuration_dictionaries_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/configurations/dictionaries",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationDictionariesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'scene' in local_var_params:
            query_params.append(('scene', local_var_params['scene']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'dict_key' in local_var_params:
            query_params.append(('dict_key', local_var_params['dict_key']))
        if 'is_built_in' in local_var_params:
            query_params.append(('is_built_in', local_var_params['is_built_in']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_connections(self, request):
        r"""操作连接列表查询接口

        操作连接列表查询接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConnections
        :type request: :class:`huaweicloudsdksecmaster.v1.ListConnectionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListConnectionsResponse`
        """
        http_info = self._list_connections_http_info(request)
        return self._call_api(**http_info)

    def list_connections_invoker(self, request):
        http_info = self._list_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/assetcredentials",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectionsResponse"
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
        if 'component_name' in local_var_params:
            query_params.append(('component_name', local_var_params['component_name']))
        if 'creator_name' in local_var_params:
            query_params.append(('creator_name', local_var_params['creator_name']))
        if 'modifier_name' in local_var_params:
            query_params.append(('modifier_name', local_var_params['modifier_name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'create_start_time' in local_var_params:
            query_params.append(('create_start_time', local_var_params['create_start_time']))
        if 'create_end_time' in local_var_params:
            query_params.append(('create_end_time', local_var_params['create_end_time']))
        if 'update_start_time' in local_var_params:
            query_params.append(('update_start_time', local_var_params['update_start_time']))
        if 'update_end_time' in local_var_params:
            query_params.append(('update_end_time', local_var_params['update_end_time']))
        if 'is_defense_type' in local_var_params:
            query_params.append(('is_defense_type', local_var_params['is_defense_type']))

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

    def list_dataclass(self, request):
        r"""查询数据类列表

        查询数据类列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataclass
        :type request: :class:`huaweicloudsdksecmaster.v1.ListDataclassRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListDataclassResponse`
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
        r"""查询字段列表

        查询字段列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataclassFields
        :type request: :class:`huaweicloudsdksecmaster.v1.ListDataclassFieldsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListDataclassFieldsResponse`
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
        r"""查询关联数据对象列表

        查询关联数据对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataobjectRelations
        :type request: :class:`huaweicloudsdksecmaster.v1.ListDataobjectRelationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListDataobjectRelationsResponse`
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

    def list_dataobjects(self, request):
        r"""列出所有数据对象

        列出所有与数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataobjects
        :type request: :class:`huaweicloudsdksecmaster.v1.ListDataobjectsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListDataobjectsResponse`
        """
        http_info = self._list_dataobjects_http_info(request)
        return self._call_api(**http_info)

    def list_dataobjects_invoker(self, request):
        http_info = self._list_dataobjects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dataobjects_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_name}/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataobjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_name' in local_var_params:
            path_params['dataclass_name'] = local_var_params['dataclass_name']

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

    def list_datapanel_objects(self, request):
        r"""查询数据对象列表

        数据面查询数据类纳管的数据对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatapanelObjects
        :type request: :class:`huaweicloudsdksecmaster.v1.ListDatapanelObjectsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListDatapanelObjectsResponse`
        """
        http_info = self._list_datapanel_objects_http_info(request)
        return self._call_api(**http_info)

    def list_datapanel_objects_invoker(self, request):
        http_info = self._list_datapanel_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_datapanel_objects_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/datapanel/{dataclass}/data-objects/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatapanelObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass' in local_var_params:
            path_params['dataclass'] = local_var_params['dataclass']

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

    def list_dataspaces(self, request):
        r"""获取数据空间列表

        获取数据空间列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataspaces
        :type request: :class:`huaweicloudsdksecmaster.v1.ListDataspacesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListDataspacesResponse`
        """
        http_info = self._list_dataspaces_http_info(request)
        return self._call_api(**http_info)

    def list_dataspaces_invoker(self, request):
        http_info = self._list_dataspaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dataspaces_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/dataspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataspacesResponse"
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
        if 'dataspace_name' in local_var_params:
            query_params.append(('dataspace_name', local_var_params['dataspace_name']))
        if 'dataspace_id' in local_var_params:
            query_params.append(('dataspace_id', local_var_params['dataspace_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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

    def list_history_component_configuration(self, request):
        r"""获取组件历史版本的配置数据

        获取组件历史版本的配置数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistoryComponentConfiguration
        :type request: :class:`huaweicloudsdksecmaster.v1.ListHistoryComponentConfigurationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListHistoryComponentConfigurationResponse`
        """
        http_info = self._list_history_component_configuration_http_info(request)
        return self._call_api(**http_info)

    def list_history_component_configuration_invoker(self, request):
        http_info = self._list_history_component_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_component_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/components/{component_id}/configurations/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryComponentConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

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

    def list_incidents(self, request):
        r"""搜索事件列表

        搜索事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIncidents
        :type request: :class:`huaweicloudsdksecmaster.v1.ListIncidentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListIncidentsResponse`
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
        r"""查询威胁情报列表

        查询威胁情报列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIndicators
        :type request: :class:`huaweicloudsdksecmaster.v1.ListIndicatorsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListIndicatorsResponse`
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

    def list_installation(self, request):
        r"""查询安装脚本列表

        查询安装脚本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstallation
        :type request: :class:`huaweicloudsdksecmaster.v1.ListInstallationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListInstallationResponse`
        """
        http_info = self._list_installation_http_info(request)
        return self._call_api(**http_info)

    def list_installation_invoker(self, request):
        http_info = self._list_installation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_installation_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/nodes/installation-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstallationResponse"
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

    def list_isap_components(self, request):
        r"""列出组件

        列出组件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIsapComponents
        :type request: :class:`huaweicloudsdksecmaster.v1.ListIsapComponentsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListIsapComponentsResponse`
        """
        http_info = self._list_isap_components_http_info(request)
        return self._call_api(**http_info)

    def list_isap_components_invoker(self, request):
        http_info = self._list_isap_components_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_isap_components_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/components",
            "request_type": request.__class__.__name__,
            "response_type": "ListIsapComponentsResponse"
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

    def list_layout(self, request):
        r"""查询布局列表

        查询布局列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLayout
        :type request: :class:`huaweicloudsdksecmaster.v1.ListLayoutRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListLayoutResponse`
        """
        http_info = self._list_layout_http_info(request)
        return self._call_api(**http_info)

    def list_layout_invoker(self, request):
        http_info = self._list_layout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_layout_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListLayoutResponse"
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

    def list_layout_wizards(self, request):
        r"""查询布局页面列表

        查询所有页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLayoutWizards
        :type request: :class:`huaweicloudsdksecmaster.v1.ListLayoutWizardsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListLayoutWizardsResponse`
        """
        http_info = self._list_layout_wizards_http_info(request)
        return self._call_api(**http_info)

    def list_layout_wizards_invoker(self, request):
        http_info = self._list_layout_wizards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_layout_wizards_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/{layout_id}/wizards",
            "request_type": request.__class__.__name__,
            "response_type": "ListLayoutWizardsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'layout_id' in local_var_params:
            path_params['layout_id'] = local_var_params['layout_id']

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

    def list_metrics(self, request):
        r"""获取指标列表

        获取指标列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetrics
        :type request: :class:`huaweicloudsdksecmaster.v1.ListMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListMetricsResponse`
        """
        http_info = self._list_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_metrics_invoker(self, request):
        http_info = self._list_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricsResponse"
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

    def list_modules(self, request):
        r"""查询模块列表

        查询所有模块
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListModules
        :type request: :class:`huaweicloudsdksecmaster.v1.ListModulesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListModulesResponse`
        """
        http_info = self._list_modules_http_info(request)
        return self._call_api(**http_info)

    def list_modules_invoker(self, request):
        http_info = self._list_modules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_modules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/modules",
            "request_type": request.__class__.__name__,
            "response_type": "ListModulesResponse"
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
        if 'module_type' in local_var_params:
            query_params.append(('module_type', local_var_params['module_type']))

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

    def list_nodes(self, request):
        r"""通过节点id查询组件信息

        查询节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNodes
        :type request: :class:`huaweicloudsdksecmaster.v1.ListNodesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListNodesResponse`
        """
        http_info = self._list_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_nodes_invoker(self, request):
        http_info = self._list_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_nodes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodesResponse"
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
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'node_name' in local_var_params:
            query_params.append(('node_name', local_var_params['node_name']))
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

    def list_notes(self, request):
        r"""搜索评论列表

        搜索评论列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotes
        :type request: :class:`huaweicloudsdksecmaster.v1.ListNotesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListNotesResponse`
        """
        http_info = self._list_notes_http_info(request)
        return self._call_api(**http_info)

    def list_notes_invoker(self, request):
        http_info = self._list_notes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/notes/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotesResponse"
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
            ['application/json;charset=utf-8'])

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

    def list_pipes(self, request):
        r"""获取数据管道列表

        获取数据管道列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipes
        :type request: :class:`huaweicloudsdksecmaster.v1.ListPipesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListPipesResponse`
        """
        http_info = self._list_pipes_http_info(request)
        return self._call_api(**http_info)

    def list_pipes_invoker(self, request):
        http_info = self._list_pipes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pipes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipesResponse"
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
        if 'dataspace_id' in local_var_params:
            query_params.append(('dataspace_id', local_var_params['dataspace_id']))
        if 'pipe_id' in local_var_params:
            query_params.append(('pipe_id', local_var_params['pipe_id']))
        if 'pipe_name' in local_var_params:
            query_params.append(('pipe_name', local_var_params['pipe_name']))
        if 'pipe_type' in local_var_params:
            query_params.append(('pipe_type', local_var_params['pipe_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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

    def list_playbook_actions(self, request):
        r"""查询剧本动作

        查询剧本动作列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookActions
        :type request: :class:`huaweicloudsdksecmaster.v1.ListPlaybookActionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListPlaybookActionsResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""查询剧本审核结果

        查询剧本审核结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookApproves
        :type request: :class:`huaweicloudsdksecmaster.v1.ListPlaybookApprovesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListPlaybookApprovesResponse`
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
        r"""查询剧本实例审计日志

        查询剧本实例审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookAuditLogs
        :type request: :class:`huaweicloudsdksecmaster.v1.ListPlaybookAuditLogsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListPlaybookAuditLogsResponse`
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
        r"""查询剧本实例列表

        查询剧本实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookInstances
        :type request: :class:`huaweicloudsdksecmaster.v1.ListPlaybookInstancesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListPlaybookInstancesResponse`
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
        if 'date_type' in local_var_params:
            query_params.append(('date_type', local_var_params['date_type']))
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
        r"""查询剧本版本列表

        查询剧本版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybookVersions
        :type request: :class:`huaweicloudsdksecmaster.v1.ListPlaybookVersionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListPlaybookVersionsResponse`
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
        r"""查询剧本列表

        查询剧本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlaybooks
        :type request: :class:`huaweicloudsdksecmaster.v1.ListPlaybooksRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListPlaybooksResponse`
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

    def list_project_tag(self, request):
        r"""查询项目标签

        查询租户在指定Project中实例类型的所有资源标签集合
        标签管理服务需要能够列出当前租户全部已使用的资源标签集合，为各服务Console打资源标签和过滤实例时提供标签联想功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTag
        :type request: :class:`huaweicloudsdksecmaster.v1.ListProjectTagRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListProjectTagResponse`
        """
        http_info = self._list_project_tag_http_info(request)
        return self._call_api(**http_info)

    def list_project_tag_invoker(self, request):
        http_info = self._list_project_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_tag_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def list_recipients_status(self, request):
        r"""查询收件人状态

        查询收件人状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecipientsStatus
        :type request: :class:`huaweicloudsdksecmaster.v1.ListRecipientsStatusRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListRecipientsStatusResponse`
        """
        http_info = self._list_recipients_status_http_info(request)
        return self._call_api(**http_info)

    def list_recipients_status_invoker(self, request):
        http_info = self._list_recipients_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_recipients_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/reports/emails/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecipientsStatusResponse"
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

    def list_regions(self, request):
        r"""查询区域列表

        查询区域列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRegions
        :type request: :class:`huaweicloudsdksecmaster.v1.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListRegionsResponse`
        """
        http_info = self._list_regions_http_info(request)
        return self._call_api(**http_info)

    def list_regions_invoker(self, request):
        http_info = self._list_regions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_regions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/collector/cloudlogs/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def list_reports(self, request):
        r"""获取报告列表

        获取报告列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReports
        :type request: :class:`huaweicloudsdksecmaster.v1.ListReportsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListReportsResponse`
        """
        http_info = self._list_reports_http_info(request)
        return self._call_api(**http_info)

    def list_reports_invoker(self, request):
        http_info = self._list_reports_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_reports_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/reports",
            "request_type": request.__class__.__name__,
            "response_type": "ListReportsResponse"
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
        if 'report_period' in local_var_params:
            query_params.append(('report_period', local_var_params['report_period']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_resource_instance(self, request):
        r"""查询资源实例列表

        使用标签过滤实例，查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstance
        :type request: :class:`huaweicloudsdksecmaster.v1.ListResourceInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListResourceInstanceResponse`
        """
        http_info = self._list_resource_instance_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instance_invoker(self, request):
        http_info = self._list_resource_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_resource_tag(self, request):
        r"""查询资源标签

        查询指定实例的标签信息
        标签管理服务需要使用该接口查询指定实例的全部标签数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTag
        :type request: :class:`huaweicloudsdksecmaster.v1.ListResourceTagRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListResourceTagResponse`
        """
        http_info = self._list_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def list_resource_tag_invoker(self, request):
        http_info = self._list_resource_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_tag_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def list_resources(self, request):
        r"""搜索资产列表

        搜索资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdksecmaster.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListResourcesResponse`
        """
        http_info = self._list_resources_http_info(request)
        return self._call_api(**http_info)

    def list_resources_invoker(self, request):
        http_info = self._list_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/resources/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_running_nodes(self, request):
        r"""列出运行中节点

        列出运行中节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRunningNodes
        :type request: :class:`huaweicloudsdksecmaster.v1.ListRunningNodesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListRunningNodesResponse`
        """
        http_info = self._list_running_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_running_nodes_invoker(self, request):
        http_info = self._list_running_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_running_nodes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/components/{component_id}/running-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListRunningNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'node_name' in local_var_params:
            query_params.append(('node_name', local_var_params['node_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_search_conditions(self, request):
        r"""获取检索条件列表

        获取检索条件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSearchConditions
        :type request: :class:`huaweicloudsdksecmaster.v1.ListSearchConditionsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListSearchConditionsResponse`
        """
        http_info = self._list_search_conditions_http_info(request)
        return self._call_api(**http_info)

    def list_search_conditions_invoker(self, request):
        http_info = self._list_search_conditions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_search_conditions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/search/conditions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSearchConditionsResponse"
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
        if 'pipe_id' in local_var_params:
            query_params.append(('pipe_id', local_var_params['pipe_id']))
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

    def list_search_histograms(self, request):
        r"""获取数据分布直方图

        获取数据分布直方图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSearchHistograms
        :type request: :class:`huaweicloudsdksecmaster.v1.ListSearchHistogramsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListSearchHistogramsResponse`
        """
        http_info = self._list_search_histograms_http_info(request)
        return self._call_api(**http_info)

    def list_search_histograms_invoker(self, request):
        http_info = self._list_search_histograms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_search_histograms_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/search/histograms",
            "request_type": request.__class__.__name__,
            "response_type": "ListSearchHistogramsResponse"
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

    def list_search_logs(self, request):
        r"""获取检索数据

        获取检索数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSearchLogs
        :type request: :class:`huaweicloudsdksecmaster.v1.ListSearchLogsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListSearchLogsResponse`
        """
        http_info = self._list_search_logs_http_info(request)
        return self._call_api(**http_info)

    def list_search_logs_invoker(self, request):
        http_info = self._list_search_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_search_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/search/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSearchLogsResponse"
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

    def list_service_agency(self, request):
        r"""查看委托信息

        check service linked agency
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceAgency
        :type request: :class:`huaweicloudsdksecmaster.v1.ListServiceAgencyRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListServiceAgencyResponse`
        """
        http_info = self._list_service_agency_http_info(request)
        return self._call_api(**http_info)

    def list_service_agency_invoker(self, request):
        http_info = self._list_service_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_service_agency_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/agency",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_shipper_authorizations(self, request):
        r"""获取投递授权信息列表

        获取投递授权信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListShipperAuthorizations
        :type request: :class:`huaweicloudsdksecmaster.v1.ListShipperAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListShipperAuthorizationsResponse`
        """
        http_info = self._list_shipper_authorizations_http_info(request)
        return self._call_api(**http_info)

    def list_shipper_authorizations_invoker(self, request):
        http_info = self._list_shipper_authorizations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_shipper_authorizations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "ListShipperAuthorizationsResponse"
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
        if 'source_region' in local_var_params:
            query_params.append(('source_region', local_var_params['source_region']))
        if 'destination_shipper_type' in local_var_params:
            query_params.append(('destination_shipper_type', local_var_params['destination_shipper_type']))
        if 'shipper_status' in local_var_params:
            query_params.append(('shipper_status', local_var_params['shipper_status']))
        if 'auth_status' in local_var_params:
            query_params.append(('auth_status', local_var_params['auth_status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_shippers(self, request):
        r"""查询投递信息

        查询投递信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListShippers
        :type request: :class:`huaweicloudsdksecmaster.v1.ListShippersRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListShippersResponse`
        """
        http_info = self._list_shippers_http_info(request)
        return self._call_api(**http_info)

    def list_shippers_invoker(self, request):
        http_info = self._list_shippers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_shippers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers",
            "request_type": request.__class__.__name__,
            "response_type": "ListShippersResponse"
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
        if 'dataspace_id' in local_var_params:
            query_params.append(('dataspace_id', local_var_params['dataspace_id']))
        if 'pipe_id' in local_var_params:
            query_params.append(('pipe_id', local_var_params['pipe_id']))
        if 'shipper_name' in local_var_params:
            query_params.append(('shipper_name', local_var_params['shipper_name']))
        if 'shipper_source_region' in local_var_params:
            query_params.append(('shipper_source_region', local_var_params['shipper_source_region']))
        if 'shipper_source_strategy' in local_var_params:
            query_params.append(('shipper_source_strategy', local_var_params['shipper_source_strategy']))
        if 'shipper_consumption_type' in local_var_params:
            query_params.append(('shipper_consumption_type', local_var_params['shipper_consumption_type']))
        if 'destination_shipper_type' in local_var_params:
            query_params.append(('destination_shipper_type', local_var_params['destination_shipper_type']))
        if 'shipper_status' in local_var_params:
            query_params.append(('shipper_status', local_var_params['shipper_status']))
        if 'create_time' in local_var_params:
            query_params.append(('create_time', local_var_params['create_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_subscription_product(self, request):
        r"""查询当前站点支持的商品清单

        查询当前站点SecMaster支持的商品清单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubscriptionProduct
        :type request: :class:`huaweicloudsdksecmaster.v1.ListSubscriptionProductRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListSubscriptionProductResponse`
        """
        http_info = self._list_subscription_product_http_info(request)
        return self._call_api(**http_info)

    def list_subscription_product_invoker(self, request):
        http_info = self._list_subscription_product_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_subscription_product_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subscriptions/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubscriptionProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_vpc_endpoint_service(self, request):
        r"""列出VPC终端节点服务

        列出VPC终端节点服务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpcEndpointService
        :type request: :class:`huaweicloudsdksecmaster.v1.ListVpcEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListVpcEndpointServiceResponse`
        """
        http_info = self._list_vpc_endpoint_service_http_info(request)
        return self._call_api(**http_info)

    def list_vpc_endpoint_service_invoker(self, request):
        http_info = self._list_vpc_endpoint_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vpc_endpoint_service_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/nodes/vpc-endpoint-services",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcEndpointServiceResponse"
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

    def list_vulnerabilities(self, request):
        r"""查询漏洞列表

        查询漏洞列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVulnerabilities
        :type request: :class:`huaweicloudsdksecmaster.v1.ListVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListVulnerabilitiesResponse`
        """
        http_info = self._list_vulnerabilities_http_info(request)
        return self._call_api(**http_info)

    def list_vulnerabilities_invoker(self, request):
        http_info = self._list_vulnerabilities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vulnerabilities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/vulnerability/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListVulnerabilitiesResponse"
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

    def list_workflows(self, request):
        r"""查询流程列表

        查询流程列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflows
        :type request: :class:`huaweicloudsdksecmaster.v1.ListWorkflowsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListWorkflowsResponse`
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

    def list_workspaces(self, request):
        r"""查询工作空间列表

        可通过工作空间名称、工作空间描述、创建时间等条件对租户的工作空间进行筛选。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkspaces
        :type request: :class:`huaweicloudsdksecmaster.v1.ListWorkspacesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ListWorkspacesResponse`
        """
        http_info = self._list_workspaces_http_info(request)
        return self._call_api(**http_info)

    def list_workspaces_invoker(self, request):
        http_info = self._list_workspaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workspaces_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkspacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'view_bind_id' in local_var_params:
            query_params.append(('view_bind_id', local_var_params['view_bind_id']))
        if 'view_bind_name' in local_var_params:
            query_params.append(('view_bind_name', local_var_params['view_bind_name']))
        if 'create_time_start' in local_var_params:
            query_params.append(('create_time_start', local_var_params['create_time_start']))
        if 'create_time_end' in local_var_params:
            query_params.append(('create_time_end', local_var_params['create_time_end']))
        if 'is_view' in local_var_params:
            query_params.append(('is_view', local_var_params['is_view']))
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))
        if 'normal_project_id' in local_var_params:
            query_params.append(('normal_project_id', local_var_params['normal_project_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def pause_shipper(self, request):
        r"""投递挂起

        投递挂起
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PauseShipper
        :type request: :class:`huaweicloudsdksecmaster.v1.PauseShipperRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.PauseShipperResponse`
        """
        http_info = self._pause_shipper_http_info(request)
        return self._call_api(**http_info)

    def pause_shipper_invoker(self, request):
        http_info = self._pause_shipper_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _pause_shipper_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/{shipper_id}/pause",
            "request_type": request.__class__.__name__,
            "response_type": "PauseShipperResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'shipper_id' in local_var_params:
            path_params['shipper_id'] = local_var_params['shipper_id']

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

    def resume_shipper(self, request):
        r"""启动投递

        启动投递
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResumeShipper
        :type request: :class:`huaweicloudsdksecmaster.v1.ResumeShipperRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ResumeShipperResponse`
        """
        http_info = self._resume_shipper_http_info(request)
        return self._call_api(**http_info)

    def resume_shipper_invoker(self, request):
        http_info = self._resume_shipper_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resume_shipper_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/{shipper_id}/resume",
            "request_type": request.__class__.__name__,
            "response_type": "ResumeShipperResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'shipper_id' in local_var_params:
            path_params['shipper_id'] = local_var_params['shipper_id']

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

    def retry_shipper(self, request):
        r"""重新投递

        重新投递
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryShipper
        :type request: :class:`huaweicloudsdksecmaster.v1.RetryShipperRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.RetryShipperResponse`
        """
        http_info = self._retry_shipper_http_info(request)
        return self._call_api(**http_info)

    def retry_shipper_invoker(self, request):
        http_info = self._retry_shipper_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_shipper_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/{shipper_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryShipperResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'shipper_id' in local_var_params:
            path_params['shipper_id'] = local_var_params['shipper_id']

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

    def retry_shipper_authorization(self, request):
        r"""重新授权

        重新授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryShipperAuthorization
        :type request: :class:`huaweicloudsdksecmaster.v1.RetryShipperAuthorizationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.RetryShipperAuthorizationResponse`
        """
        http_info = self._retry_shipper_authorization_http_info(request)
        return self._call_api(**http_info)

    def retry_shipper_authorization_invoker(self, request):
        http_info = self._retry_shipper_authorization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_shipper_authorization_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/{shipper_id}/authorization/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryShipperAuthorizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'shipper_id' in local_var_params:
            path_params['shipper_id'] = local_var_params['shipper_id']

        query_params = []
        if 'param' in local_var_params:
            query_params.append(('param', local_var_params['param']))

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

    def search_policy(self, request):
        r"""查询策略视图列表

        查询策略视图列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchPolicy
        :type request: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.SearchPolicyResponse`
        """
        http_info = self._search_policy_http_info(request)
        return self._call_api(**http_info)

    def search_policy_invoker(self, request):
        http_info = self._search_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/policys/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchPolicyResponse"
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
        if 'x_secmaster_version' in local_var_params:
            header_params['X-Secmaster-Version'] = local_var_params['x_secmaster_version']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["content-type", ]

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

    def search_policy_record(self, request):
        r"""查询任务视图列表

        查询任务视图列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchPolicyRecord
        :type request: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRecordRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRecordResponse`
        """
        http_info = self._search_policy_record_http_info(request)
        return self._call_api(**http_info)

    def search_policy_record_invoker(self, request):
        http_info = self._search_policy_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_policy_record_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/policy-records/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchPolicyRecordResponse"
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
        if 'x_secmaster_version' in local_var_params:
            header_params['X-Secmaster-Version'] = local_var_params['x_secmaster_version']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["content-type", ]

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

    def search_policy_record_by_policy_id(self, request):
        r"""根据策略ID查询历史记录列表

        根据策略ID查询历史记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchPolicyRecordByPolicyId
        :type request: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRecordByPolicyIdRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRecordByPolicyIdResponse`
        """
        http_info = self._search_policy_record_by_policy_id_http_info(request)
        return self._call_api(**http_info)

    def search_policy_record_by_policy_id_invoker(self, request):
        http_info = self._search_policy_record_by_policy_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_policy_record_by_policy_id_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/policy-records/{policy_id}/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchPolicyRecordByPolicyIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'x_secmaster_version' in local_var_params:
            header_params['X-Secmaster-Version'] = local_var_params['x_secmaster_version']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["content-type", ]

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
        r"""获取告警详情

        获取告警详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlert
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowAlertRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowAlertResponse`
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
        r"""查看告警规则

        查看告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowAlertRuleResponse`
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
        r"""查看告警规则模板

        查看告警规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlertRuleTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowAlertRuleTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowAlertRuleTemplateResponse`
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

    def show_aop_workflow(self, request):
        r"""查询流程详情

        查询流程详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAopWorkflow
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowAopWorkflowRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowAopWorkflowResponse`
        """
        http_info = self._show_aop_workflow_http_info(request)
        return self._call_api(**http_info)

    def show_aop_workflow_invoker(self, request):
        http_info = self._show_aop_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aop_workflow_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAopWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def show_aop_workflow_instance(self, request):
        r"""查询流程实例的详情

        查询流程实例的详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAopWorkflowInstance
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowAopWorkflowInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowAopWorkflowInstanceResponse`
        """
        http_info = self._show_aop_workflow_instance_http_info(request)
        return self._call_api(**http_info)

    def show_aop_workflow_instance_invoker(self, request):
        http_info = self._show_aop_workflow_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aop_workflow_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAopWorkflowInstanceResponse"
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
        if 'show_topology' in local_var_params:
            query_params.append(('show_topology', local_var_params['show_topology']))

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

    def show_aop_workflow_version(self, request):
        r"""查询流程版本的详细信息

        查询流程版本的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAopWorkflowVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowAopWorkflowVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowAopWorkflowVersionResponse`
        """
        http_info = self._show_aop_workflow_version_http_info(request)
        return self._call_api(**http_info)

    def show_aop_workflow_version_invoker(self, request):
        http_info = self._show_aop_workflow_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aop_workflow_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAopWorkflowVersionResponse"
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

    def show_attachment(self, request):
        r"""获取附件详情

        获取附件详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAttachment
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowAttachmentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowAttachmentResponse`
        """
        http_info = self._show_attachment_http_info(request)
        return self._call_api(**http_info)

    def show_attachment_invoker(self, request):
        http_info = self._show_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_attachment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/attachment/{attach_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'attach_id' in local_var_params:
            path_params['attach_id'] = local_var_params['attach_id']

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

    def show_classifier_info(self, request):
        r"""查询分类详情

        查询分类详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClassifierInfo
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowClassifierInfoRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowClassifierInfoResponse`
        """
        http_info = self._show_classifier_info_http_info(request)
        return self._call_api(**http_info)

    def show_classifier_info_invoker(self, request):
        http_info = self._show_classifier_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_classifier_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/classifiers/{classifier_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClassifierInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'classifier_id' in local_var_params:
            path_params['classifier_id'] = local_var_params['classifier_id']

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

    def show_cloud_log_tenant_whitelist(self, request):
        r"""获取是否开启行管

        获取是否开启行管
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudLogTenantWhitelist
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowCloudLogTenantWhitelistRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowCloudLogTenantWhitelistResponse`
        """
        http_info = self._show_cloud_log_tenant_whitelist_http_info(request)
        return self._call_api(**http_info)

    def show_cloud_log_tenant_whitelist_invoker(self, request):
        http_info = self._show_cloud_log_tenant_whitelist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cloud_log_tenant_whitelist_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/cloud-logs/tenant/whitelist",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCloudLogTenantWhitelistResponse"
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
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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

    def show_collector_channel(self, request):
        r"""展示采集通道

        展示采集通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCollectorChannel
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowCollectorChannelRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowCollectorChannelResponse`
        """
        http_info = self._show_collector_channel_http_info(request)
        return self._call_api(**http_info)

    def show_collector_channel_invoker(self, request):
        http_info = self._show_collector_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_collector_channel_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/{channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCollectorChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

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

    def show_collector_connection(self, request):
        r"""展示采集连接详情

        展示采集连接详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCollectorConnection
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowCollectorConnectionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowCollectorConnectionResponse`
        """
        http_info = self._show_collector_connection_http_info(request)
        return self._call_api(**http_info)

    def show_collector_connection_invoker(self, request):
        http_info = self._show_collector_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_collector_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCollectorConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_collector_parser(self, request):
        r"""获取采集解析器详情

        获取采集解析器详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCollectorParser
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowCollectorParserRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowCollectorParserResponse`
        """
        http_info = self._show_collector_parser_http_info(request)
        return self._call_api(**http_info)

    def show_collector_parser_invoker(self, request):
        http_info = self._show_collector_parser_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_collector_parser_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/logstash/parsers/{parser_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCollectorParserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'parser_id' in local_var_params:
            path_params['parser_id'] = local_var_params['parser_id']

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

    def show_component(self, request):
        r"""查询插件详细信息

        查询插件详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponent
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowComponentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowComponentResponse`
        """
        http_info = self._show_component_http_info(request)
        return self._call_api(**http_info)

    def show_component_invoker(self, request):
        http_info = self._show_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_component_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

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

    def show_component_action(self, request):
        r"""查询插件Action详情

        查询插件的action详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponentAction
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowComponentActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowComponentActionResponse`
        """
        http_info = self._show_component_action_http_info(request)
        return self._call_api(**http_info)

    def show_component_action_invoker(self, request):
        http_info = self._show_component_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_component_action_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components/{component_id}/action/{action_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))

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

    def show_component_template(self, request):
        r"""查询插件配置模板详情

        查询在配置流程时的插件配置模板详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponentTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowComponentTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowComponentTemplateResponse`
        """
        http_info = self._show_component_template_http_info(request)
        return self._call_api(**http_info)

    def show_component_template_invoker(self, request):
        http_info = self._show_component_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_component_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components/template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentTemplateResponse"
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

    def show_connection(self, request):
        r"""查询操作连接详情

        查询操作连接详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnection
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowConnectionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowConnectionResponse`
        """
        http_info = self._show_connection_http_info(request)
        return self._call_api(**http_info)

    def show_connection_invoker(self, request):
        http_info = self._show_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/assetcredentials/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def show_data_class_info(self, request):
        r"""展示数据类详情

        展示数据类详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataClassInfo
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowDataClassInfoRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowDataClassInfoResponse`
        """
        http_info = self._show_data_class_info_http_info(request)
        return self._call_api(**http_info)

    def show_data_class_info_invoker(self, request):
        http_info = self._show_data_class_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_data_class_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/dataclasses/{dataclass_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataClassInfoResponse"
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

    def show_dataobject(self, request):
        r"""查询数据对象

        查询数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataobject
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowDataobjectRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowDataobjectResponse`
        """
        http_info = self._show_dataobject_http_info(request)
        return self._call_api(**http_info)

    def show_dataobject_invoker(self, request):
        http_info = self._show_dataobject_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dataobject_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_name}/{data_object_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataobjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_name' in local_var_params:
            path_params['dataclass_name'] = local_var_params['dataclass_name']
        if 'data_object_id' in local_var_params:
            path_params['data_object_id'] = local_var_params['data_object_id']

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

    def show_datapanel_object(self, request):
        r"""查询数据面对象

        数据面查询数据类纳管的数据对象详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatapanelObject
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowDatapanelObjectRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowDatapanelObjectResponse`
        """
        http_info = self._show_datapanel_object_http_info(request)
        return self._call_api(**http_info)

    def show_datapanel_object_invoker(self, request):
        http_info = self._show_datapanel_object_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_datapanel_object_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/datapanel/{dataclass}/data-objects/{dataobject_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatapanelObjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass' in local_var_params:
            path_params['dataclass'] = local_var_params['dataclass']
        if 'dataobject_id' in local_var_params:
            path_params['dataobject_id'] = local_var_params['dataobject_id']

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

    def show_dataspace(self, request):
        r"""获取数据空间详情

        获取数据空间详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataspace
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowDataspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowDataspaceResponse`
        """
        http_info = self._show_dataspace_http_info(request)
        return self._call_api(**http_info)

    def show_dataspace_invoker(self, request):
        http_info = self._show_dataspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dataspace_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/dataspaces/{dataspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataspace_id' in local_var_params:
            path_params['dataspace_id'] = local_var_params['dataspace_id']

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

    def show_incident(self, request):
        r"""获取事件详情

        获取事件详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIncident
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowIncidentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowIncidentResponse`
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
        r"""查询威胁情报详情

        查询威胁情报详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIndicatorDetail
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowIndicatorDetailRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowIndicatorDetailResponse`
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

    def show_isap_component(self, request):
        r"""展示组件详情

        展示组件详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIsapComponent
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowIsapComponentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowIsapComponentResponse`
        """
        http_info = self._show_isap_component_http_info(request)
        return self._call_api(**http_info)

    def show_isap_component_invoker(self, request):
        http_info = self._show_isap_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_isap_component_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIsapComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def show_layout(self, request):
        r"""查询布局详情

        查询布局详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLayout
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowLayoutRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowLayoutResponse`
        """
        http_info = self._show_layout_http_info(request)
        return self._call_api(**http_info)

    def show_layout_invoker(self, request):
        http_info = self._show_layout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_layout_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/{layout_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLayoutResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'layout_id' in local_var_params:
            path_params['layout_id'] = local_var_params['layout_id']

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

    def show_layout_wizard(self, request):
        r"""查询布局页面

        查询布局页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLayoutWizard
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowLayoutWizardRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowLayoutWizardResponse`
        """
        http_info = self._show_layout_wizard_http_info(request)
        return self._call_api(**http_info)

    def show_layout_wizard_invoker(self, request):
        http_info = self._show_layout_wizard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_layout_wizard_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/wizards/{wizard_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLayoutWizardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'wizard_id' in local_var_params:
            path_params['wizard_id'] = local_var_params['wizard_id']

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

    def show_layout_wizard_by_field(self, request):
        r"""查询布局页面详情

        查询布局页面详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLayoutWizardByField
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowLayoutWizardByFieldRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowLayoutWizardByFieldResponse`
        """
        http_info = self._show_layout_wizard_by_field_http_info(request)
        return self._call_api(**http_info)

    def show_layout_wizard_by_field_invoker(self, request):
        http_info = self._show_layout_wizard_by_field_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_layout_wizard_by_field_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/wizards",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLayoutWizardByFieldResponse"
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
        if 'layout_id' in local_var_params:
            query_params.append(('layout_id', local_var_params['layout_id']))
        if 'field_id' in local_var_params:
            query_params.append(('field_id', local_var_params['field_id']))

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

    def show_mapper_detail(self, request):
        r"""查询映射详情

        查询映射详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMapperDetail
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowMapperDetailRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowMapperDetailResponse`
        """
        http_info = self._show_mapper_detail_http_info(request)
        return self._call_api(**http_info)

    def show_mapper_detail_invoker(self, request):
        http_info = self._show_mapper_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mapper_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/mappers/{mapper_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMapperDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'mapper_id' in local_var_params:
            path_params['mapper_id'] = local_var_params['mapper_id']

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

    def show_mapper_list(self, request):
        r"""查询映射列表

        查询映射列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMapperList
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowMapperListRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowMapperListResponse`
        """
        http_info = self._show_mapper_list_http_info(request)
        return self._call_api(**http_info)

    def show_mapper_list_invoker(self, request):
        http_info = self._show_mapper_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mapper_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/mappers/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMapperListResponse"
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

    def show_mapping_function(self, request):
        r"""查询分类映射函数

        查询分类映射函数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMappingFunction
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowMappingFunctionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowMappingFunctionResponse`
        """
        http_info = self._show_mapping_function_http_info(request)
        return self._call_api(**http_info)

    def show_mapping_function_invoker(self, request):
        http_info = self._show_mapping_function_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mapping_function_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/functions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMappingFunctionResponse"
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

    def show_mapping_info_list(self, request):
        r"""查询分类映射列表

        查询分类映射列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMappingInfoList
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowMappingInfoListRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowMappingInfoListResponse`
        """
        http_info = self._show_mapping_info_list_http_info(request)
        return self._call_api(**http_info)

    def show_mapping_info_list_invoker(self, request):
        http_info = self._show_mapping_info_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mapping_info_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMappingInfoListResponse"
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

    def show_metric_meta_data(self, request):
        r"""获取指标元数据

        获取指标元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricMetaData
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowMetricMetaDataRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowMetricMetaDataResponse`
        """
        http_info = self._show_metric_meta_data_http_info(request)
        return self._call_api(**http_info)

    def show_metric_meta_data_invoker(self, request):
        http_info = self._show_metric_meta_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_metric_meta_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/metrics/{metric_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetricMetaDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'metric_id' in local_var_params:
            path_params['metric_id'] = local_var_params['metric_id']

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

    def show_module(self, request):
        r"""查询模块详情

        查询模块详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowModule
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowModuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowModuleResponse`
        """
        http_info = self._show_module_http_info(request)
        return self._call_api(**http_info)

    def show_module_invoker(self, request):
        http_info = self._show_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_module_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/modules/{module_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def show_moniter_metric_stats(self, request):
        r"""获取指标统计数据

        获取指标统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMoniterMetricStats
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowMoniterMetricStatsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowMoniterMetricStatsResponse`
        """
        http_info = self._show_moniter_metric_stats_http_info(request)
        return self._call_api(**http_info)

    def show_moniter_metric_stats_invoker(self, request):
        http_info = self._show_moniter_metric_stats_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_moniter_metric_stats_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/moniter/metric/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMoniterMetricStatsResponse"
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

    def show_pipe(self, request):
        r"""获取数据管道详情

        获取数据管道详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipe
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPipeResponse`
        """
        http_info = self._show_pipe_http_info(request)
        return self._call_api(**http_info)

    def show_pipe_invoker(self, request):
        http_info = self._show_pipe_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipe_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def show_pipe_consumption(self, request):
        r"""获取实时消费配置

        获取实时消费配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipeConsumption
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPipeConsumptionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPipeConsumptionResponse`
        """
        http_info = self._show_pipe_consumption_http_info(request)
        return self._call_api(**http_info)

    def show_pipe_consumption_invoker(self, request):
        http_info = self._show_pipe_consumption_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipe_consumption_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}/consumption",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipeConsumptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def show_pipe_index(self, request):
        r"""获取索引信息

        获取索引信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipeIndex
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPipeIndexRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPipeIndexResponse`
        """
        http_info = self._show_pipe_index_http_info(request)
        return self._call_api(**http_info)

    def show_pipe_index_invoker(self, request):
        http_info = self._show_pipe_index_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipe_index_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}/index",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipeIndexResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def show_platform_managed(self, request):
        r"""获取行管信息

        获取行管信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlatformManaged
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPlatformManagedRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPlatformManagedResponse`
        """
        http_info = self._show_platform_managed_http_info(request)
        return self._call_api(**http_info)

    def show_platform_managed_invoker(self, request):
        http_info = self._show_platform_managed_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_platform_managed_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/siem/cloud-logs/managers",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlatformManagedResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def show_playbook(self, request):
        r"""查询剧本详情

        查询剧本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybook
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookResponse`
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
        r"""查询剧本实例详情

        查询剧本实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookInstance
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookInstanceResponse`
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
        r"""剧本运行监控

        剧本运行监控（待下线）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookMonitors
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookMonitorsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookMonitorsResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""查询剧本规则详情

        查询剧本规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookRuleResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""剧本数据统计

        剧本统计数据（待下线）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookStatistics
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookStatisticsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookStatisticsResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""查询剧本拓扑关系

        查询剧本拓扑关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookTopology
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookTopologyRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookTopologyResponse`
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
        r"""查询剧本版本详情

        查询剧本版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPlaybookVersionResponse`
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

    def show_policy(self, request):
        r"""查询策略视图对象

        查询策略视图对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicy
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPolicyRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPolicyResponse`
        """
        http_info = self._show_policy_http_info(request)
        return self._call_api(**http_info)

    def show_policy_invoker(self, request):
        http_info = self._show_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/policys/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'x_secmaster_version' in local_var_params:
            header_params['X-Secmaster-Version'] = local_var_params['x_secmaster_version']

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

    def show_pre_process_rules_list(self, request):
        r"""查询预处理规则列表

        查询预处理规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPreProcessRulesList
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowPreProcessRulesListRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowPreProcessRulesListResponse`
        """
        http_info = self._show_pre_process_rules_list_http_info(request)
        return self._call_api(**http_info)

    def show_pre_process_rules_list_invoker(self, request):
        http_info = self._show_pre_process_rules_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pre_process_rules_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/preprocess-rules/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPreProcessRulesListResponse"
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

    def show_report_info(self, request):
        r"""获取报告详情

        获取报告详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReportInfo
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowReportInfoRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowReportInfoResponse`
        """
        http_info = self._show_report_info_http_info(request)
        return self._call_api(**http_info)

    def show_report_info_invoker(self, request):
        http_info = self._show_report_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_report_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/reports/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

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

    def show_resource(self, request):
        r"""获取资产详情

        获取资产详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResource
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowResourceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowResourceResponse`
        """
        http_info = self._show_resource_http_info(request)
        return self._call_api(**http_info)

    def show_resource_invoker(self, request):
        http_info = self._show_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/resources/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_search_condition(self, request):
        r"""获取检索条件详情

        获取检索条件详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSearchCondition
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowSearchConditionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowSearchConditionResponse`
        """
        http_info = self._show_search_condition_http_info(request)
        return self._call_api(**http_info)

    def show_search_condition_invoker(self, request):
        http_info = self._show_search_condition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_search_condition_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/search/conditions/{condition_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSearchConditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'condition_id' in local_var_params:
            path_params['condition_id'] = local_var_params['condition_id']

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

    def show_shipper(self, request):
        r"""投递规则详情

        投递规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowShipper
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowShipperRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponse`
        """
        http_info = self._show_shipper_http_info(request)
        return self._call_api(**http_info)

    def show_shipper_invoker(self, request):
        http_info = self._show_shipper_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_shipper_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/{shipper_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowShipperResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'shipper_id' in local_var_params:
            path_params['shipper_id'] = local_var_params['shipper_id']

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

    def show_shipper_delegate_auth(self, request):
        r"""获取委托权限

        获取委托权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowShipperDelegateAuth
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowShipperDelegateAuthRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowShipperDelegateAuthResponse`
        """
        http_info = self._show_shipper_delegate_auth_http_info(request)
        return self._call_api(**http_info)

    def show_shipper_delegate_auth_invoker(self, request):
        http_info = self._show_shipper_delegate_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_shipper_delegate_auth_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/delegate/auth/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowShipperDelegateAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'agency_name' in local_var_params:
            query_params.append(('agency_name', local_var_params['agency_name']))

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

    def show_shipper_param(self, request):
        r"""参数查询

        参数查询接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowShipperParam
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowShipperParamRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowShipperParamResponse`
        """
        http_info = self._show_shipper_param_http_info(request)
        return self._call_api(**http_info)

    def show_shipper_param_invoker(self, request):
        http_info = self._show_shipper_param_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_shipper_param_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/shippers/params/{param_type}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowShipperParamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'param_type' in local_var_params:
            path_params['param_type'] = local_var_params['param_type']

        query_params = []
        if 'param' in local_var_params:
            query_params.append(('param', local_var_params['param']))

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

    def show_vulnerability(self, request):
        r"""获取漏洞详情

        获取漏洞详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVulnerability
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowVulnerabilityRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowVulnerabilityResponse`
        """
        http_info = self._show_vulnerability_http_info(request)
        return self._call_api(**http_info)

    def show_vulnerability_invoker(self, request):
        http_info = self._show_vulnerability_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vulnerability_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/vulnerability/{vul_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVulnerabilityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'vul_id' in local_var_params:
            path_params['vul_id'] = local_var_params['vul_id']

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

    def show_workspace(self, request):
        r"""查询工作空间详情

        查询工作空间名称、描述等详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkspace
        :type request: :class:`huaweicloudsdksecmaster.v1.ShowWorkspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowWorkspaceResponse`
        """
        http_info = self._show_workspace_http_info(request)
        return self._call_api(**http_info)

    def show_workspace_invoker(self, request):
        http_info = self._show_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_workspace_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkspaceResponse"
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

    def update_alert_rule(self, request):
        r"""更新告警规则

        更新告警规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlertRule
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateAlertRuleResponse`
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

    def update_aop_workflow(self, request):
        r"""更新流程

        更新流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAopWorkflow
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateAopWorkflowRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateAopWorkflowResponse`
        """
        http_info = self._update_aop_workflow_http_info(request)
        return self._call_api(**http_info)

    def update_aop_workflow_invoker(self, request):
        http_info = self._update_aop_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_aop_workflow_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAopWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def update_aop_workflow_version(self, request):
        r"""更新流程版本信息

        更新流程版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAopWorkflowVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateAopWorkflowVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateAopWorkflowVersionResponse`
        """
        http_info = self._update_aop_workflow_version_http_info(request)
        return self._call_api(**http_info)

    def update_aop_workflow_version_invoker(self, request):
        http_info = self._update_aop_workflow_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_aop_workflow_version_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAopWorkflowVersionResponse"
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

    def update_catalogue(self, request):
        r"""修改目录

        修改自定义目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCatalogue
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateCatalogueRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateCatalogueResponse`
        """
        http_info = self._update_catalogue_http_info(request)
        return self._call_api(**http_info)

    def update_catalogue_invoker(self, request):
        http_info = self._update_catalogue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_catalogue_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/catalogues/{catalogue_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCatalogueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'catalogue_id' in local_var_params:
            path_params['catalogue_id'] = local_var_params['catalogue_id']

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

    def update_classifier(self, request):
        r"""修改分类

        修改分类
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClassifier
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateClassifierRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateClassifierResponse`
        """
        http_info = self._update_classifier_http_info(request)
        return self._call_api(**http_info)

    def update_classifier_invoker(self, request):
        http_info = self._update_classifier_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_classifier_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/classifiers/{classifier_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClassifierResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'classifier_id' in local_var_params:
            path_params['classifier_id'] = local_var_params['classifier_id']

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

    def update_collector_channel(self, request):
        r"""更改采集通道

        更改采集通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCollectorChannel
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateCollectorChannelRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateCollectorChannelResponse`
        """
        http_info = self._update_collector_channel_http_info(request)
        return self._call_api(**http_info)

    def update_collector_channel_invoker(self, request):
        http_info = self._update_collector_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_collector_channel_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/{channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCollectorChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

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

    def update_collector_channel_group(self, request):
        r"""更新采集通道分组

        更新采集通道分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCollectorChannelGroup
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateCollectorChannelGroupRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateCollectorChannelGroupResponse`
        """
        http_info = self._update_collector_channel_group_http_info(request)
        return self._call_api(**http_info)

    def update_collector_channel_group_invoker(self, request):
        http_info = self._update_collector_channel_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_collector_channel_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/channels/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCollectorChannelGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
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

    def update_collector_connection(self, request):
        r"""更新采集连接

        更新采集连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCollectorConnection
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateCollectorConnectionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateCollectorConnectionResponse`
        """
        http_info = self._update_collector_connection_http_info(request)
        return self._call_api(**http_info)

    def update_collector_connection_invoker(self, request):
        http_info = self._update_collector_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_collector_connection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/collector/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCollectorConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def update_component_configuration(self, request):
        r"""点击保存按钮

        点击保存按钮
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateComponentConfiguration
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateComponentConfigurationRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateComponentConfigurationResponse`
        """
        http_info = self._update_component_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_component_configuration_invoker(self, request):
        http_info = self._update_component_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_component_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/components/{component_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateComponentConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
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

    def update_component_template(self, request):
        r"""更新插件配置模板

        更新某个在配置流程时的插件配置模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateComponentTemplate
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateComponentTemplateRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateComponentTemplateResponse`
        """
        http_info = self._update_component_template_http_info(request)
        return self._call_api(**http_info)

    def update_component_template_invoker(self, request):
        http_info = self._update_component_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_component_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/components/template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateComponentTemplateResponse"
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

    def update_configuration_dictionaries(self, request):
        r"""更新字典

        更新字典数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfigurationDictionaries
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateConfigurationDictionariesRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateConfigurationDictionariesResponse`
        """
        http_info = self._update_configuration_dictionaries_http_info(request)
        return self._call_api(**http_info)

    def update_configuration_dictionaries_invoker(self, request):
        http_info = self._update_configuration_dictionaries_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_configuration_dictionaries_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/configurations/dictionaries",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigurationDictionariesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def update_connection(self, request):
        r"""更新操作连接

        更新操作连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConnection
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateConnectionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateConnectionResponse`
        """
        http_info = self._update_connection_http_info(request)
        return self._call_api(**http_info)

    def update_connection_invoker(self, request):
        http_info = self._update_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_connection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/assetcredentials/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def update_dataobject(self, request):
        r"""编辑数据对象

        编辑数据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataobject
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateDataobjectRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateDataobjectResponse`
        """
        http_info = self._update_dataobject_http_info(request)
        return self._call_api(**http_info)

    def update_dataobject_invoker(self, request):
        http_info = self._update_dataobject_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_dataobject_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_name}/{data_object_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataobjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_name' in local_var_params:
            path_params['dataclass_name'] = local_var_params['dataclass_name']
        if 'data_object_id' in local_var_params:
            path_params['data_object_id'] = local_var_params['data_object_id']

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

    def update_dataspace(self, request):
        r"""修改数据空间

        修改数据空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataspace
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateDataspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateDataspaceResponse`
        """
        http_info = self._update_dataspace_http_info(request)
        return self._call_api(**http_info)

    def update_dataspace_invoker(self, request):
        http_info = self._update_dataspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_dataspace_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/dataspaces/{dataspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataspace_id' in local_var_params:
            path_params['dataspace_id'] = local_var_params['dataspace_id']

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

    def update_indicator(self, request):
        r"""更新威胁情报

        更新威胁情报
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIndicator
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateIndicatorResponse`
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

    def update_layout(self, request):
        r"""修改布局

        修改布局
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLayout
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateLayoutRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateLayoutResponse`
        """
        http_info = self._update_layout_http_info(request)
        return self._call_api(**http_info)

    def update_layout_invoker(self, request):
        http_info = self._update_layout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_layout_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/{layout_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLayoutResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'layout_id' in local_var_params:
            path_params['layout_id'] = local_var_params['layout_id']

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

    def update_layout_wizards(self, request):
        r"""批量更新布局页面

        更新页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLayoutWizards
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateLayoutWizardsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateLayoutWizardsResponse`
        """
        http_info = self._update_layout_wizards_http_info(request)
        return self._call_api(**http_info)

    def update_layout_wizards_invoker(self, request):
        http_info = self._update_layout_wizards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_layout_wizards_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/layouts/wizards",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLayoutWizardsResponse"
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

    def update_mapping_info_status(self, request):
        r"""修分类映射启用禁用状态

        修分类映射启用禁用状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMappingInfoStatus
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateMappingInfoStatusRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateMappingInfoStatusResponse`
        """
        http_info = self._update_mapping_info_status_http_info(request)
        return self._call_api(**http_info)

    def update_mapping_info_status_invoker(self, request):
        http_info = self._update_mapping_info_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_mapping_info_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/mappings/{mapping_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMappingInfoStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'mapping_id' in local_var_params:
            path_params['mapping_id'] = local_var_params['mapping_id']

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

    def update_metrics(self, request):
        r"""更新指标定义

        更新指标定义
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMetrics
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateMetricsRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateMetricsResponse`
        """
        http_info = self._update_metrics_http_info(request)
        return self._call_api(**http_info)

    def update_metrics_invoker(self, request):
        http_info = self._update_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_metrics_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/metrics/{metric_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'metric_id' in local_var_params:
            path_params['metric_id'] = local_var_params['metric_id']

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

    def update_module(self, request):
        r"""更新布局模块

        更新模块
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateModule
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateModuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateModuleResponse`
        """
        http_info = self._update_module_http_info(request)
        return self._call_api(**http_info)

    def update_module_invoker(self, request):
        http_info = self._update_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_module_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/modules/{module_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def update_node(self, request):
        r"""更新节点补充信息

        更新节点信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNode
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateNodeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateNodeResponse`
        """
        http_info = self._update_node_http_info(request)
        return self._call_api(**http_info)

    def update_node_invoker(self, request):
        http_info = self._update_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_node_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def update_pipe(self, request):
        r"""修改数据管道

        修改数据管道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePipe
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdatePipeRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdatePipeResponse`
        """
        http_info = self._update_pipe_http_info(request)
        return self._call_api(**http_info)

    def update_pipe_invoker(self, request):
        http_info = self._update_pipe_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_pipe_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePipeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def update_pipe_index(self, request):
        r"""修改索引

        修改索引
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePipeIndex
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdatePipeIndexRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdatePipeIndexResponse`
        """
        http_info = self._update_pipe_index_http_info(request)
        return self._call_api(**http_info)

    def update_pipe_index_invoker(self, request):
        http_info = self._update_pipe_index_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_pipe_index_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/pipes/{pipe_id}/index",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePipeIndexResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'pipe_id' in local_var_params:
            path_params['pipe_id'] = local_var_params['pipe_id']

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

    def update_playbook(self, request):
        r"""修改剧本

        修改剧本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybook
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdatePlaybookResponse`
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
        r"""更新剧本动作

        更新剧本动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookAction
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdatePlaybookActionResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""更新剧本规则

        更新剧本规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookRule
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdatePlaybookRuleResponse`
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

        response_headers = ["X-request-id", "X-API-Deprecation-Info", "X-API-Deprecation-Date", ]

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
        r"""更新剧本版本

        更新剧本版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePlaybookVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdatePlaybookVersionResponse`
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

    def update_recipients_email_status(self, request):
        r"""更新收件人邮箱状态

        更新收件人邮箱状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecipientsEmailStatus
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateRecipientsEmailStatusRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateRecipientsEmailStatusResponse`
        """
        http_info = self._update_recipients_email_status_http_info(request)
        return self._call_api(**http_info)

    def update_recipients_email_status_invoker(self, request):
        http_info = self._update_recipients_email_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_recipients_email_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/reports/emails",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecipientsEmailStatusResponse"
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

    def update_report(self, request):
        r"""更新报告

        更新报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateReport
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateReportRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateReportResponse`
        """
        http_info = self._update_report_http_info(request)
        return self._call_api(**http_info)

    def update_report_invoker(self, request):
        http_info = self._update_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_report_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/sa/reports/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

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

    def update_search_condition(self, request):
        r"""修改检索条件

        修改检索条件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSearchCondition
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateSearchConditionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateSearchConditionResponse`
        """
        http_info = self._update_search_condition_http_info(request)
        return self._call_api(**http_info)

    def update_search_condition_invoker(self, request):
        http_info = self._update_search_condition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_search_condition_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/search/conditions/{condition_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSearchConditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'condition_id' in local_var_params:
            path_params['condition_id'] = local_var_params['condition_id']

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

    def update_tag_value(self, request):
        r"""更新标签值

        更新标签值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTagValue
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateTagValueRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateTagValueResponse`
        """
        http_info = self._update_tag_value_http_info(request)
        return self._call_api(**http_info)

    def update_tag_value_invoker(self, request):
        http_info = self._update_tag_value_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_tag_value_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/{key}/tags/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTagValueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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

    def update_vpc_endpoint_service(self, request):
        r"""更新VPC终端节点服务

        更新VPC终端节点服务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVpcEndpointService
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateVpcEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateVpcEndpointServiceResponse`
        """
        http_info = self._update_vpc_endpoint_service_http_info(request)
        return self._call_api(**http_info)

    def update_vpc_endpoint_service_invoker(self, request):
        http_info = self._update_vpc_endpoint_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vpc_endpoint_service_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/nodes/vpc-endpoint-services",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpcEndpointServiceResponse"
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
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))

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

    def update_workspace(self, request):
        r"""更新工作空间

        更新工作空间名称、描述等信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkspace
        :type request: :class:`huaweicloudsdksecmaster.v1.UpdateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateWorkspaceResponse`
        """
        http_info = self._update_workspace_http_info(request)
        return self._call_api(**http_info)

    def update_workspace_invoker(self, request):
        http_info = self._update_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_workspace_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkspaceResponse"
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

    def upload_attachment(self, request):
        r"""上传附件

        上传附件至OBS
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadAttachment
        :type request: :class:`huaweicloudsdksecmaster.v1.UploadAttachmentRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.UploadAttachmentResponse`
        """
        http_info = self._upload_attachment_http_info(request)
        return self._call_api(**http_info)

    def upload_attachment_invoker(self, request):
        http_info = self._upload_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_attachment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/attachment/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadAttachmentResponse"
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
        if 'file_type' in local_var_params:
            form_params['fileType'] = local_var_params['file_type']
        if 'upload_file' in local_var_params:
            form_params['uploadFile'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def validate_aop_workflow_version(self, request):
        r"""校验流程版本

        校验流程版本.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateAopWorkflowVersion
        :type request: :class:`huaweicloudsdksecmaster.v1.ValidateAopWorkflowVersionRequest`
        :rtype: :class:`huaweicloudsdksecmaster.v1.ValidateAopWorkflowVersionResponse`
        """
        http_info = self._validate_aop_workflow_version_http_info(request)
        return self._call_api(**http_info)

    def validate_aop_workflow_version_invoker(self, request):
        http_info = self._validate_aop_workflow_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_aop_workflow_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/workflows/validation",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateAopWorkflowVersionResponse"
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

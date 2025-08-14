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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkclouddc'")


class CloudDCClient(Client):
    def __init__(self):
        super(CloudDCClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkclouddc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "BasicCredentials")
        else:
            if clazz.__name__ != "CloudDCClient":
                raise TypeError("client type error, support client type is CloudDCClient")
            client_builder = ClientBuilder(clazz, "BasicCredentials")

        

        return client_builder

    def batch_create_irack_tags(self, request):
        r"""批量创建机柜标签

        批量创建机柜标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateIrackTags
        :type request: :class:`huaweicloudsdkclouddc.v1.BatchCreateIrackTagsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.BatchCreateIrackTagsResponse`
        """
        http_info = self._batch_create_irack_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_irack_tags_invoker(self, request):
        http_info = self._batch_create_irack_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_irack_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/iracks/{id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateIrackTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def batch_create_tags(self, request):
        r"""批量创建资源标签

        批量创建资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateTags
        :type request: :class:`huaweicloudsdkclouddc.v1.BatchCreateTagsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.BatchCreateTagsResponse`
        """
        http_info = self._batch_create_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_tags_invoker(self, request):
        http_info = self._batch_create_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateTagsResponse"
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

    def batch_delete_irack_tags(self, request):
        r"""批量删除机柜标签

        批量删除机柜标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteIrackTags
        :type request: :class:`huaweicloudsdkclouddc.v1.BatchDeleteIrackTagsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.BatchDeleteIrackTagsResponse`
        """
        http_info = self._batch_delete_irack_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_irack_tags_invoker(self, request):
        http_info = self._batch_delete_irack_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_irack_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/iracks/{id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteIrackTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def batch_delete_tags(self, request):
        r"""批量删除资源标签

        批量删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTags
        :type request: :class:`huaweicloudsdkclouddc.v1.BatchDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.BatchDeleteTagsResponse`
        """
        http_info = self._batch_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_tags_invoker(self, request):
        http_info = self._batch_delete_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTagsResponse"
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

    def change_instance_password(self, request):
        r"""批量修改实例密码

        修改服务器管理账号（root用户或Administrator用户）密码
        前提条件：Instance state为running
        该接口为同步接口，全部成功或者全部失败
        约束：
        无符合安全要求的密码复杂度检查，非安全密码输入后，无错误提示。
        服务器开机或重启后，新密码生效（调用**ChangeServerPowerState**接口重启）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeInstancePassword
        :type request: :class:`huaweicloudsdkclouddc.v1.ChangeInstancePasswordRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ChangeInstancePasswordResponse`
        """
        http_info = self._change_instance_password_http_info(request)
        return self._call_api(**http_info)

    def change_instance_password_invoker(self, request):
        http_info = self._change_instance_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_instance_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/password",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeInstancePasswordResponse"
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

    def change_server_power_state(self, request):
        r"""批量修改物理服务器电源状态

        修改物理服务器电源状态，此接口为异步接口，电源状态修改成功与否需要根据查询物理服务器信息获得
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeServerPowerState
        :type request: :class:`huaweicloudsdkclouddc.v1.ChangeServerPowerStateRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ChangeServerPowerStateResponse`
        """
        http_info = self._change_server_power_state_http_info(request)
        return self._call_api(**http_info)

    def change_server_power_state_invoker(self, request):
        http_info = self._change_server_power_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_server_power_state_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/physicalservers/power-state",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeServerPowerStateResponse"
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

    def create_instance(self, request):
        r"""创建实例

        创建实例，支持指定IP等更多个性化参数创建实例。
        
        调度策略支持：
        1、指定服务器
        2、基于空闲随机调度策略
        
        支持VPC网络及AI参数面网络配置。
        
        此接口为异步接口，实例的创建和启动不是立即完成的，通过接口 **ShowInstanceStatus** 查询实例状态为 **running** 代表实例创建成功。
        接口约束：服务器**manage_state**为 **ready**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkclouddc.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
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

    def delete_instance(self, request):
        r"""删除实例

        指定物理服务器删除实例，此接口为异步接口，可通过 **ShowInstanceStatus** 查询实例状态，实例状态从 **shutting-down** 变为 **terminated**，表明删除实例成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkclouddc.v1.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_instances(self, request):
        r"""批量删除实例

        指定物理服务器批量删除实例，此接口为异步接口，可通过 **ShowInstanceStatus** 查询实例状态，实例状态从 **shutting-down** 变为 **terminated**，表明删除实例成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstances
        :type request: :class:`huaweicloudsdkclouddc.v1.DeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.DeleteInstancesResponse`
        """
        http_info = self._delete_instances_http_info(request)
        return self._call_api(**http_info)

    def delete_instances_invoker(self, request):
        http_info = self._delete_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstancesResponse"
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

    def download_server_logs(self, request):
        r"""下载日志文件

        下载服务器日志文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadServerLogs
        :type request: :class:`huaweicloudsdkclouddc.v1.DownloadServerLogsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.DownloadServerLogsResponse`
        """
        http_info = self._download_server_logs_http_info(request)
        return self._call_api(**http_info)

    def download_server_logs_invoker(self, request):
        http_info = self._download_server_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_server_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/{id}/logs/exports/{export_id}/content",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadServerLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'export_id' in local_var_params:
            path_params['export_id'] = local_var_params['export_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Content-Disposition", "Content-Transfer-Encoding", "Content-Type", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_server_logs(self, request):
        r"""导出服务器日志请求

        创建服务器日志导出异步任务。根据ShowLogsExportStatus查询status，当status状态为completed时，调用DownloadServerLogs下载日志文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportServerLogs
        :type request: :class:`huaweicloudsdkclouddc.v1.ExportServerLogsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ExportServerLogsResponse`
        """
        http_info = self._export_server_logs_http_info(request)
        return self._call_api(**http_info)

    def export_server_logs_invoker(self, request):
        http_info = self._export_server_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_server_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/physicalservers/{id}/logs/exports",
            "request_type": request.__class__.__name__,
            "response_type": "ExportServerLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Content-Disposition", "Content-Transfer-Encoding", "Content-Type", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_alarms(self, request):
        r"""服务器告警列表

        该 API 用于查询服务器告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarms
        :type request: :class:`huaweicloudsdkclouddc.v1.ListAlarmsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ListAlarmsResponse`
        """
        http_info = self._list_alarms_http_info(request)
        return self._call_api(**http_info)

    def list_alarms_invoker(self, request):
        http_info = self._list_alarms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarms_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alarm_record_id' in local_var_params:
            query_params.append(('alarm_record_id', local_var_params['alarm_record_id']))
        if 'alarm_status' in local_var_params:
            query_params.append(('alarm_status', local_var_params['alarm_status']))
        if 'alarm_type' in local_var_params:
            query_params.append(('alarm_type', local_var_params['alarm_type']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'alarm_level' in local_var_params:
            query_params.append(('alarm_level', local_var_params['alarm_level']))
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

    def list_events(self, request):
        r"""服务器事件列表

        该 API 用于查询服务器事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkclouddc.v1.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ListEventsResponse`
        """
        http_info = self._list_events_http_info(request)
        return self._call_api(**http_info)

    def list_events_invoker(self, request):
        http_info = self._list_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_events_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventsResponse"
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
        if 'event_level' in local_var_params:
            query_params.append(('event_level', local_var_params['event_level']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))

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

    def list_i_dcs(self, request):
        r"""查询 IDC 列表

        查询 IDC 列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIDcs
        :type request: :class:`huaweicloudsdkclouddc.v1.ListIDcsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ListIDcsResponse`
        """
        http_info = self._list_i_dcs_http_info(request)
        return self._call_api(**http_info)

    def list_i_dcs_invoker(self, request):
        http_info = self._list_i_dcs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_i_dcs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/idcs",
            "request_type": request.__class__.__name__,
            "response_type": "ListIDcsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_i_racks(self, request):
        r"""查询 iRack 实例列表

        用户下单后，用户上报iRack设备列表。该 API 可以查看 iRack 实例与关联imetal数量列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIRacks
        :type request: :class:`huaweicloudsdkclouddc.v1.ListIRacksRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ListIRacksResponse`
        """
        http_info = self._list_i_racks_http_info(request)
        return self._call_api(**http_info)

    def list_i_racks_invoker(self, request):
        http_info = self._list_i_racks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_i_racks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/iracks",
            "request_type": request.__class__.__name__,
            "response_type": "ListIRacksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_instances(self, request):
        r"""批量查询实例

        批量查询实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkclouddc.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'instance_state' in local_var_params:
            query_params.append(('instance_state', local_var_params['instance_state']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))

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

    def list_servers(self, request):
        r"""批量查询物理服务器

        List imetal servers
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServers
        :type request: :class:`huaweicloudsdkclouddc.v1.ListServersRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ListServersResponse`
        """
        http_info = self._list_servers_http_info(request)
        return self._call_api(**http_info)

    def list_servers_invoker(self, request):
        http_info = self._list_servers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_servers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers",
            "request_type": request.__class__.__name__,
            "response_type": "ListServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'manage_state' in local_var_params:
            query_params.append(('manage_state', local_var_params['manage_state']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def modify_instance_ip(self, request):
        r"""修改实例ip

        用户可选择指定的 iMetal 实例，修改ip。
        
        接口约束：iMetal 实例处于就绪状态（已调测成功）或修改ip失败同时为下电状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyInstanceIp
        :type request: :class:`huaweicloudsdkclouddc.v1.ModifyInstanceIpRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ModifyInstanceIpResponse`
        """
        http_info = self._modify_instance_ip_http_info(request)
        return self._call_api(**http_info)

    def modify_instance_ip_invoker(self, request):
        http_info = self._modify_instance_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_instance_ip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{id}/ip",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyInstanceIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def reinstall_os(self, request):
        r"""批量重新安装OS

        指定新OS镜像重新安装OS，此接口为异步接口，通过 **ShowInstanceStatus** 查询实例状态，当状态变为 **pending** 表明正在重装中，状态为 **running** 表明完成重装。
        前提条件：Instance state为running
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ReinstallOs
        :type request: :class:`huaweicloudsdkclouddc.v1.ReinstallOsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ReinstallOsResponse`
        """
        http_info = self._reinstall_os_http_info(request)
        return self._call_api(**http_info)

    def reinstall_os_invoker(self, request):
        http_info = self._reinstall_os_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reinstall_os_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/reinstall",
            "request_type": request.__class__.__name__,
            "response_type": "ReinstallOsResponse"
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

    def run_instances(self, request):
        r"""批量创建实例

        批量创建实例，其中调度策略支持：
        1、指定服务器
        2、基于空闲随机调度策略
        
        支持VPC网络及AI参数面网络配置。
        
        此接口为异步接口，实例的创建和启动不是立即完成的，通过接口 **ShowInstanceStatus** 查询实例状态为 **running** 代表实例创建成功。
        接口约束：服务器**manage_state**为 **ready**
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunInstances
        :type request: :class:`huaweicloudsdkclouddc.v1.RunInstancesRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.RunInstancesResponse`
        """
        http_info = self._run_instances_http_info(request)
        return self._call_api(**http_info)

    def run_instances_invoker(self, request):
        http_info = self._run_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "RunInstancesResponse"
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

    def show_alarm_summary(self, request):
        r"""服务器告警概览

        该 API 用于查询服务器告警概览
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlarmSummary
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowAlarmSummaryRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowAlarmSummaryResponse`
        """
        http_info = self._show_alarm_summary_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_summary_invoker(self, request):
        http_info = self._show_alarm_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alarm_summary_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/alarms/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmSummaryResponse"
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

    def show_alarm_trend(self, request):
        r"""服务器告警趋势

        该 API 用于查询服务器概览、服务器开机状态和服务器运行状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlarmTrend
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowAlarmTrendRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowAlarmTrendResponse`
        """
        http_info = self._show_alarm_trend_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_trend_invoker(self, request):
        http_info = self._show_alarm_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alarm_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/alarms/trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))

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

    def show_event(self, request):
        r"""查询事件定义

        查询事件定义
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEvent
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowEventRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowEventResponse`
        """
        http_info = self._show_event_http_info(request)
        return self._call_api(**http_info)

    def show_event_invoker(self, request):
        http_info = self._show_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_event_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/events/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

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

    def show_instance_status(self, request):
        r"""查询实例状态

        查询实例状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceStatus
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowInstanceStatusRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowInstanceStatusResponse`
        """
        http_info = self._show_instance_status_http_info(request)
        return self._call_api(**http_info)

    def show_instance_status_invoker(self, request):
        http_info = self._show_instance_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_logs_export_status(self, request):
        r"""查询日志导出状态

        查询日志采集状态及进度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogsExportStatus
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowLogsExportStatusRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowLogsExportStatusResponse`
        """
        http_info = self._show_logs_export_status_http_info(request)
        return self._call_api(**http_info)

    def show_logs_export_status_invoker(self, request):
        http_info = self._show_logs_export_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logs_export_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/{id}/logs/exports/{export_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogsExportStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'export_id' in local_var_params:
            path_params['export_id'] = local_var_params['export_id']

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

    def show_remote_console(self, request):
        r"""获取console地址信息

        获取console信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRemoteConsole
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowRemoteConsoleRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowRemoteConsoleResponse`
        """
        http_info = self._show_remote_console_http_info(request)
        return self._call_api(**http_info)

    def show_remote_console_invoker(self, request):
        http_info = self._show_remote_console_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_remote_console_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/{id}/remote-console-address",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRemoteConsoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_server(self, request):
        r"""查询物理服务器信息

        Get imetal server by id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowServer
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowServerRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowServerResponse`
        """
        http_info = self._show_server_http_info(request)
        return self._call_api(**http_info)

    def show_server_invoker(self, request):
        http_info = self._show_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_server_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_server_firmware_attributes(self, request):
        r"""查询服务器固件详细信息

        获取详细固件信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowServerFirmwareAttributes
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowServerFirmwareAttributesRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowServerFirmwareAttributesResponse`
        """
        http_info = self._show_server_firmware_attributes_http_info(request)
        return self._call_api(**http_info)

    def show_server_firmware_attributes_invoker(self, request):
        http_info = self._show_server_firmware_attributes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_server_firmware_attributes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/{id}/firmware-attributes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerFirmwareAttributesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_server_hardware_attributes(self, request):
        r"""查询服务器硬件详细信息

        获取详细硬件信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowServerHardwareAttributes
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowServerHardwareAttributesRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowServerHardwareAttributesResponse`
        """
        http_info = self._show_server_hardware_attributes_http_info(request)
        return self._call_api(**http_info)

    def show_server_hardware_attributes_invoker(self, request):
        http_info = self._show_server_hardware_attributes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_server_hardware_attributes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/{id}/hardware-attributes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerHardwareAttributesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_server_status(self, request):
        r"""服务器概览

        该 API 用于查询服务器概览、服务器开机状态和服务器运行状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowServerStatus
        :type request: :class:`huaweicloudsdkclouddc.v1.ShowServerStatusRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.ShowServerStatusResponse`
        """
        http_info = self._show_server_status_http_info(request)
        return self._call_api(**http_info)

    def show_server_status_invoker(self, request):
        http_info = self._show_server_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_server_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/physicalservers/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerStatusResponse"
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

    def update_i_dcs(self, request):
        r"""修改 IDC 描述

        修改 IDC 描述
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIDcs
        :type request: :class:`huaweicloudsdkclouddc.v1.UpdateIDcsRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.UpdateIDcsResponse`
        """
        http_info = self._update_i_dcs_http_info(request)
        return self._call_api(**http_info)

    def update_i_dcs_invoker(self, request):
        http_info = self._update_i_dcs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_i_dcs_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/idcs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIDcsResponse"
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

    def update_i_rack(self, request):
        r"""更新 iRack 实例

        更新iRack信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIRack
        :type request: :class:`huaweicloudsdkclouddc.v1.UpdateIRackRequest`
        :rtype: :class:`huaweicloudsdkclouddc.v1.UpdateIRackResponse`
        """
        http_info = self._update_i_rack_http_info(request)
        return self._call_api(**http_info)

    def update_i_rack_invoker(self, request):
        http_info = self._update_i_rack_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_i_rack_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/iracks/{irack_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIRackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'irack_id' in local_var_params:
            path_params['irack_id'] = local_var_params['irack_id']

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

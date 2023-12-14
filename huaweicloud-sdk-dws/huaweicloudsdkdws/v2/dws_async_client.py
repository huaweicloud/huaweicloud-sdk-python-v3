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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdws'")


class DwsAsyncClient(Client):
    def __init__(self):
        super(DwsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdws.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DwsAsyncClient":
                raise TypeError("client type error, support client type is DwsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_snapshot_cross_region_policy_async(self, request):
        """设置跨区域备份配置

        该接口用于设置跨区域备份配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddSnapshotCrossRegionPolicy
        :type request: :class:`huaweicloudsdkdws.v2.AddSnapshotCrossRegionPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.AddSnapshotCrossRegionPolicyResponse`
        """
        http_info = self._add_snapshot_cross_region_policy_http_info(request)
        return self._call_api(**http_info)

    def add_snapshot_cross_region_policy_async_invoker(self, request):
        http_info = self._add_snapshot_cross_region_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_snapshot_cross_region_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/snapshots/cross-region-policies",
            "request_type": request.__class__.__name__,
            "response_type": "AddSnapshotCrossRegionPolicyResponse"
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

    def add_workload_queue_async(self, request):
        """添加工作负载队列

        添加工作负载队列
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddWorkloadQueue
        :type request: :class:`huaweicloudsdkdws.v2.AddWorkloadQueueRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.AddWorkloadQueueResponse`
        """
        http_info = self._add_workload_queue_http_info(request)
        return self._call_api(**http_info)

    def add_workload_queue_async_invoker(self, request):
        http_info = self._add_workload_queue_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_workload_queue_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload/queues",
            "request_type": request.__class__.__name__,
            "response_type": "AddWorkloadQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def associate_eip_async(self, request):
        """集群绑定EIP

        集群绑定Eip
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateEip
        :type request: :class:`huaweicloudsdkdws.v2.AssociateEipRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.AssociateEipResponse`
        """
        http_info = self._associate_eip_http_info(request)
        return self._call_api(**http_info)

    def associate_eip_async_invoker(self, request):
        http_info = self._associate_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_eip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/eips/{eip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'eip_id' in local_var_params:
            path_params['eip_id'] = local_var_params['eip_id']

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

    def associate_elb_async(self, request):
        """集群绑定ELB

        集群绑定Elb接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateElb
        :type request: :class:`huaweicloudsdkdws.v2.AssociateElbRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.AssociateElbResponse`
        """
        http_info = self._associate_elb_http_info(request)
        return self._call_api(**http_info)

    def associate_elb_async_invoker(self, request):
        http_info = self._associate_elb_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_elb_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/elbs/{elb_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateElbResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'elb_id' in local_var_params:
            path_params['elb_id'] = local_var_params['elb_id']

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

    def batch_create_cluster_cn_async(self, request):
        """批量增加CN节点

        当用户集群创建后，实际需要的CN数量会随着业务需求而发生变化，因此管理CN节点功能的实现使用户可以根据实际需求动态调整集群CN数量。
        - 增删CN节点过程中不允许执行其他运维操作。
        - 增删CN节点过程中需要停止业务操作，建议在业务低峰期或业务中断情况下进行操作。
        - 增删CN节点时发生故障且回滚失败，需要用户登录后台进行处理，处理方案请参见《故障排除》中的“集群使用&gt;增删CN回滚失败”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateClusterCn
        :type request: :class:`huaweicloudsdkdws.v2.BatchCreateClusterCnRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.BatchCreateClusterCnResponse`
        """
        http_info = self._batch_create_cluster_cn_http_info(request)
        return self._call_api(**http_info)

    def batch_create_cluster_cn_async_invoker(self, request):
        http_info = self._batch_create_cluster_cn_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_cluster_cn_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/cns/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateClusterCnResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def batch_create_resource_tag_async(self, request):
        """批量添加标签

        为指定集群批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateResourceTag
        :type request: :class:`huaweicloudsdkdws.v2.BatchCreateResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.BatchCreateResourceTagResponse`
        """
        http_info = self._batch_create_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_create_resource_tag_async_invoker(self, request):
        http_info = self._batch_create_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_resource_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/tags/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def batch_delete_cluster_cn_async(self, request):
        """批量删除CN节点

        当用户集群创建后，实际需要的CN数量会随着业务需求而发生变化，因此管理CN节点功能的实现使用户可以根据实际需求动态调整集群CN数量。
        - 增删CN节点过程中不允许执行其他运维操作。
        - 增删CN节点过程中需要停止业务操作，建议在业务低峰期或业务中断情况下进行操作。
        - 增删CN节点时发生故障且回滚失败，需要用户登录后台进行处理，处理方案请参见《故障排除》中的“集群使用&gt;增删CN回滚失败”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteClusterCn
        :type request: :class:`huaweicloudsdkdws.v2.BatchDeleteClusterCnRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.BatchDeleteClusterCnResponse`
        """
        http_info = self._batch_delete_cluster_cn_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_cluster_cn_async_invoker(self, request):
        http_info = self._batch_delete_cluster_cn_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_cluster_cn_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/cns/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteClusterCnResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def batch_delete_resource_tag_async(self, request):
        """批量删除标签

        为指定集群批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteResourceTag
        :type request: :class:`huaweicloudsdkdws.v2.BatchDeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.BatchDeleteResourceTagResponse`
        """
        http_info = self._batch_delete_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resource_tag_async_invoker(self, request):
        http_info = self._batch_delete_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_resource_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/tags/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def cancel_readonly_cluster_async(self, request):
        """解除只读

        当集群进入只读状态时，无法进行数据库相关操作，用户可以在管理控制台解除集群的只读状态。触发只读状态可能是由于磁盘使用率过高，因此需要对集群数据进行清理或扩容。
        - 解除只读支持1.7.2及以上版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelReadonlyCluster
        :type request: :class:`huaweicloudsdkdws.v2.CancelReadonlyClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CancelReadonlyClusterResponse`
        """
        http_info = self._cancel_readonly_cluster_http_info(request)
        return self._call_api(**http_info)

    def cancel_readonly_cluster_async_invoker(self, request):
        http_info = self._cancel_readonly_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_readonly_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/cancel-readonly",
            "request_type": request.__class__.__name__,
            "response_type": "CancelReadonlyClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def check_cluster_async(self, request):
        """创建集群前检查

        创建集群前预检查
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckCluster
        :type request: :class:`huaweicloudsdkdws.v2.CheckClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CheckClusterResponse`
        """
        http_info = self._check_cluster_http_info(request)
        return self._call_api(**http_info)

    def check_cluster_async_invoker(self, request):
        http_info = self._check_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cluster-precheck",
            "request_type": request.__class__.__name__,
            "response_type": "CheckClusterResponse"
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

    def check_disaster_name_async(self, request):
        """检查容灾名称

        检查容灾名称
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckDisasterName
        :type request: :class:`huaweicloudsdkdws.v2.CheckDisasterNameRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CheckDisasterNameResponse`
        """
        http_info = self._check_disaster_name_http_info(request)
        return self._call_api(**http_info)

    def check_disaster_name_async_invoker(self, request):
        http_info = self._check_disaster_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_disaster_name_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/disaster-recovery/check-name",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDisasterNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dr_name' in local_var_params:
            query_params.append(('dr_name', local_var_params['dr_name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'standby_region' in local_var_params:
            query_params.append(('standby_region', local_var_params['standby_region']))
        if 'standby_project_id' in local_var_params:
            query_params.append(('standby_project_id', local_var_params['standby_project_id']))

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

    def check_table_restore_async(self, request):
        """用户恢复表名检测

        该接口用于用户恢复表名检测
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckTableRestore
        :type request: :class:`huaweicloudsdkdws.v2.CheckTableRestoreRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CheckTableRestoreResponse`
        """
        http_info = self._check_table_restore_http_info(request)
        return self._call_api(**http_info)

    def check_table_restore_async_invoker(self, request):
        http_info = self._check_table_restore_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_table_restore_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/snapshots/{snapshot_id}/table-restore-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckTableRestoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def convert_to_logical_cluster_async(self, request):
        """物理集群转换到逻辑集群

        逻辑集群-物理集群转换到逻辑集群
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConvertToLogicalCluster
        :type request: :class:`huaweicloudsdkdws.v2.ConvertToLogicalClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ConvertToLogicalClusterResponse`
        """
        http_info = self._convert_to_logical_cluster_http_info(request)
        return self._call_api(**http_info)

    def convert_to_logical_cluster_async_invoker(self, request):
        http_info = self._convert_to_logical_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _convert_to_logical_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/convert-to-logical-cluster/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "ConvertToLogicalClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

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

    def copy_snapshot_async(self, request):
        """复制快照

        该接口用于复制一个自动快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopySnapshot
        :type request: :class:`huaweicloudsdkdws.v2.CopySnapshotRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CopySnapshotResponse`
        """
        http_info = self._copy_snapshot_http_info(request)
        return self._call_api(**http_info)

    def copy_snapshot_async_invoker(self, request):
        http_info = self._copy_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_snapshot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/snapshots/{snapshot_id}/linked-copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopySnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def create_alarm_sub_async(self, request):
        """创建告警订阅

        创建告警订阅
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlarmSub
        :type request: :class:`huaweicloudsdkdws.v2.CreateAlarmSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateAlarmSubResponse`
        """
        http_info = self._create_alarm_sub_http_info(request)
        return self._call_api(**http_info)

    def create_alarm_sub_async_invoker(self, request):
        http_info = self._create_alarm_sub_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_alarm_sub_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/alarm-subs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlarmSubResponse"
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

    def create_cluster_async(self, request):
        """创建集群

        该接口用于创建集群。
        集群必须要运行在VPC之内，创建集群前，您需要先创建VPC，并获取VPC和子网的id。
        该接口为异步接口，创建集群需要10～15分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkdws.v2.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateClusterResponse`
        """
        http_info = self._create_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_async_invoker(self, request):
        http_info = self._create_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterResponse"
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

    def create_cluster_dns_async(self, request):
        """申请域名

        为指定集群申请域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateClusterDns
        :type request: :class:`huaweicloudsdkdws.v2.CreateClusterDnsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateClusterDnsResponse`
        """
        http_info = self._create_cluster_dns_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_dns_async_invoker(self, request):
        http_info = self._create_cluster_dns_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cluster_dns_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/dns",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterDnsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def create_cluster_v2_async(self, request):
        """V2创建集群

        该接口用于创建集群。
        集群必须要运行在VPC之内，创建集群前，您需要先创建VPC，并获取VPC和子网的id。
        该接口为异步接口，创建集群需要10～15分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateClusterV2
        :type request: :class:`huaweicloudsdkdws.v2.CreateClusterV2Request`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateClusterV2Response`
        """
        http_info = self._create_cluster_v2_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_v2_async_invoker(self, request):
        http_info = self._create_cluster_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cluster_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterV2Response"
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

    def create_cluster_workload_async(self, request):
        """设置资源管理

        设置资源管理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateClusterWorkload
        :type request: :class:`huaweicloudsdkdws.v2.CreateClusterWorkloadRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateClusterWorkloadResponse`
        """
        http_info = self._create_cluster_workload_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_workload_async_invoker(self, request):
        http_info = self._create_cluster_workload_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cluster_workload_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterWorkloadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def create_data_source_async(self, request):
        """创建数据源

        该接口用于创建一个数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDataSource
        :type request: :class:`huaweicloudsdkdws.v2.CreateDataSourceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateDataSourceResponse`
        """
        http_info = self._create_data_source_http_info(request)
        return self._call_api(**http_info)

    def create_data_source_async_invoker(self, request):
        http_info = self._create_data_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_data_source_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ext-data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def create_disaster_recovery_async(self, request):
        """创建容灾

        创建容灾
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.CreateDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateDisasterRecoveryResponse`
        """
        http_info = self._create_disaster_recovery_http_info(request)
        return self._call_api(**http_info)

    def create_disaster_recovery_async_invoker(self, request):
        http_info = self._create_disaster_recovery_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_disaster_recovery_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/disaster-recoveries",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDisasterRecoveryResponse"
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

    def create_event_sub_async(self, request):
        """创建订阅事件

        添加订阅的事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEventSub
        :type request: :class:`huaweicloudsdkdws.v2.CreateEventSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateEventSubResponse`
        """
        http_info = self._create_event_sub_http_info(request)
        return self._call_api(**http_info)

    def create_event_sub_async_invoker(self, request):
        http_info = self._create_event_sub_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_event_sub_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/event-subs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEventSubResponse"
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

    def create_logical_cluster_async(self, request):
        """创建逻辑集群

        逻辑集群-创建逻辑集群
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLogicalCluster
        :type request: :class:`huaweicloudsdkdws.v2.CreateLogicalClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateLogicalClusterResponse`
        """
        http_info = self._create_logical_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_logical_cluster_async_invoker(self, request):
        http_info = self._create_logical_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_logical_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogicalClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def create_snapshot_async(self, request):
        """创建快照

        该接口用于为指定集群创建快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSnapshot
        :type request: :class:`huaweicloudsdkdws.v2.CreateSnapshotRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateSnapshotResponse`
        """
        http_info = self._create_snapshot_http_info(request)
        return self._call_api(**http_info)

    def create_snapshot_async_invoker(self, request):
        http_info = self._create_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_snapshot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSnapshotResponse"
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

    def create_snapshot_policy_async(self, request):
        """添加快照策略

        该接口用于设置快照策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSnapshotPolicy
        :type request: :class:`huaweicloudsdkdws.v2.CreateSnapshotPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateSnapshotPolicyResponse`
        """
        http_info = self._create_snapshot_policy_http_info(request)
        return self._call_api(**http_info)

    def create_snapshot_policy_async_invoker(self, request):
        http_info = self._create_snapshot_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_snapshot_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/snapshot-policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSnapshotPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def create_workload_plan_async(self, request):
        """添加工作负载计划

        添加工作负载计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkloadPlan
        :type request: :class:`huaweicloudsdkdws.v2.CreateWorkloadPlanRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.CreateWorkloadPlanResponse`
        """
        http_info = self._create_workload_plan_http_info(request)
        return self._call_api(**http_info)

    def create_workload_plan_async_invoker(self, request):
        http_info = self._create_workload_plan_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workload_plan_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload/plans",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkloadPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def delete_alarm_sub_async(self, request):
        """删除告警订阅

        删除订阅的告警
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlarmSub
        :type request: :class:`huaweicloudsdkdws.v2.DeleteAlarmSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteAlarmSubResponse`
        """
        http_info = self._delete_alarm_sub_http_info(request)
        return self._call_api(**http_info)

    def delete_alarm_sub_async_invoker(self, request):
        http_info = self._delete_alarm_sub_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_alarm_sub_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/alarm-subs/{alarm_sub_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlarmSubResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_sub_id' in local_var_params:
            path_params['alarm_sub_id'] = local_var_params['alarm_sub_id']

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

    def delete_cluster_async(self, request):
        """删除集群

        此接口用于删除集群。集群删除后将释放此集群的所有资源，包括客户数据。为了安全起见，请在删除集群前为这个集群创建快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkdws.v2.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteClusterResponse`
        """
        http_info = self._delete_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_async_invoker(self, request):
        http_info = self._delete_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cluster_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def delete_cluster_dns_async(self, request):
        """删除集群域名

        删除指定集群域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteClusterDns
        :type request: :class:`huaweicloudsdkdws.v2.DeleteClusterDnsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteClusterDnsResponse`
        """
        http_info = self._delete_cluster_dns_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_dns_async_invoker(self, request):
        http_info = self._delete_cluster_dns_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cluster_dns_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/dns",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClusterDnsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
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

    def delete_cluster_nodes_async(self, request):
        """删除节点

        此接口用于删除节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteClusterNodes
        :type request: :class:`huaweicloudsdkdws.v2.DeleteClusterNodesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteClusterNodesResponse`
        """
        http_info = self._delete_cluster_nodes_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_nodes_async_invoker(self, request):
        http_info = self._delete_cluster_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cluster_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/nodes/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClusterNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def delete_data_source_async(self, request):
        """删除数据源

        该接口用于删除一个数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDataSource
        :type request: :class:`huaweicloudsdkdws.v2.DeleteDataSourceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteDataSourceResponse`
        """
        http_info = self._delete_data_source_http_info(request)
        return self._call_api(**http_info)

    def delete_data_source_async_invoker(self, request):
        http_info = self._delete_data_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_data_source_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ext-data-sources/{ext_data_source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'ext_data_source_id' in local_var_params:
            path_params['ext_data_source_id'] = local_var_params['ext_data_source_id']

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

    def delete_disaster_recovery_async(self, request):
        """删除容灾

        删除容灾。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.DeleteDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteDisasterRecoveryResponse`
        """
        http_info = self._delete_disaster_recovery_http_info(request)
        return self._call_api(**http_info)

    def delete_disaster_recovery_async_invoker(self, request):
        http_info = self._delete_disaster_recovery_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_disaster_recovery_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/disaster-recovery/{disaster_recovery_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDisasterRecoveryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def delete_event_sub_async(self, request):
        """删除订阅事件

        删除订阅的事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEventSub
        :type request: :class:`huaweicloudsdkdws.v2.DeleteEventSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteEventSubResponse`
        """
        http_info = self._delete_event_sub_http_info(request)
        return self._call_api(**http_info)

    def delete_event_sub_async_invoker(self, request):
        http_info = self._delete_event_sub_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_event_sub_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/event-subs/{event_sub_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEventSubResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_sub_id' in local_var_params:
            path_params['event_sub_id'] = local_var_params['event_sub_id']

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

    def delete_logical_cluster_async(self, request):
        """删除逻辑集群

        此接口用于删除逻辑集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLogicalCluster
        :type request: :class:`huaweicloudsdkdws.v2.DeleteLogicalClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteLogicalClusterResponse`
        """
        http_info = self._delete_logical_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_logical_cluster_async_invoker(self, request):
        http_info = self._delete_logical_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_logical_cluster_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters/{logical_cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogicalClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'logical_cluster_id' in local_var_params:
            path_params['logical_cluster_id'] = local_var_params['logical_cluster_id']

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

    def delete_snapshot_async(self, request):
        """删除快照

        该接口用于删除一个指定手动快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSnapshot
        :type request: :class:`huaweicloudsdkdws.v2.DeleteSnapshotRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteSnapshotResponse`
        """
        http_info = self._delete_snapshot_http_info(request)
        return self._call_api(**http_info)

    def delete_snapshot_async_invoker(self, request):
        http_info = self._delete_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_snapshot_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/snapshots/{snapshot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def delete_snapshot_cross_region_policy_async(self, request):
        """删除跨区域备份配置

        该接口用于删除跨区域备份配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSnapshotCrossRegionPolicy
        :type request: :class:`huaweicloudsdkdws.v2.DeleteSnapshotCrossRegionPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteSnapshotCrossRegionPolicyResponse`
        """
        http_info = self._delete_snapshot_cross_region_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_snapshot_cross_region_policy_async_invoker(self, request):
        http_info = self._delete_snapshot_cross_region_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_snapshot_cross_region_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/snapshots/cross-region-policies",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSnapshotCrossRegionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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

    def delete_snapshot_policy_async(self, request):
        """删除快照策略

        该接口用于删除一个快照策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSnapshotPolicy
        :type request: :class:`huaweicloudsdkdws.v2.DeleteSnapshotPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteSnapshotPolicyResponse`
        """
        http_info = self._delete_snapshot_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_snapshot_policy_async_invoker(self, request):
        http_info = self._delete_snapshot_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_snapshot_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/snapshot-policies/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSnapshotPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
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

    def delete_workload_plan_async(self, request):
        """删除工作负载计划

        删除工作负载计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkloadPlan
        :type request: :class:`huaweicloudsdkdws.v2.DeleteWorkloadPlanRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteWorkloadPlanResponse`
        """
        http_info = self._delete_workload_plan_http_info(request)
        return self._call_api(**http_info)

    def delete_workload_plan_async_invoker(self, request):
        http_info = self._delete_workload_plan_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workload_plan_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload/plans/{plan_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkloadPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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

    def delete_workload_queue_async(self, request):
        """删除工作负载队列

        该接口用于删除工作负载队列。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkloadQueue
        :type request: :class:`huaweicloudsdkdws.v2.DeleteWorkloadQueueRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DeleteWorkloadQueueResponse`
        """
        http_info = self._delete_workload_queue_http_info(request)
        return self._call_api(**http_info)

    def delete_workload_queue_async_invoker(self, request):
        http_info = self._delete_workload_queue_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workload_queue_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload/queues",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkloadQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'logical_cluster_name' in local_var_params:
            query_params.append(('logical_cluster_name', local_var_params['logical_cluster_name']))
        if 'workload_queue_name' in local_var_params:
            query_params.append(('workload_queue_name', local_var_params['workload_queue_name']))

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

    def disable_lts_logs_async(self, request):
        """关闭云服务日志

        该接口用于关闭集群LTS云日志服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableLtsLogs
        :type request: :class:`huaweicloudsdkdws.v2.DisableLtsLogsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DisableLtsLogsResponse`
        """
        http_info = self._disable_lts_logs_http_info(request)
        return self._call_api(**http_info)

    def disable_lts_logs_async_invoker(self, request):
        http_info = self._disable_lts_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_lts_logs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/lts-logs/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableLtsLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def disassociate_eip_async(self, request):
        """集群解绑EIP

        集群解绑Eip
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateEip
        :type request: :class:`huaweicloudsdkdws.v2.DisassociateEipRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DisassociateEipResponse`
        """
        http_info = self._disassociate_eip_http_info(request)
        return self._call_api(**http_info)

    def disassociate_eip_async_invoker(self, request):
        http_info = self._disassociate_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_eip_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/eips/{eip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'eip_id' in local_var_params:
            path_params['eip_id'] = local_var_params['eip_id']

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

    def disassociate_elb_async(self, request):
        """集群解绑ELB

        集群解绑Elb接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateElb
        :type request: :class:`huaweicloudsdkdws.v2.DisassociateElbRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.DisassociateElbResponse`
        """
        http_info = self._disassociate_elb_http_info(request)
        return self._call_api(**http_info)

    def disassociate_elb_async_invoker(self, request):
        http_info = self._disassociate_elb_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_elb_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/elbs/{elb_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateElbResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'elb_id' in local_var_params:
            path_params['elb_id'] = local_var_params['elb_id']

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

    def enable_logical_cluster_async(self, request):
        """切换逻辑集群开关

        此接口用于切换逻辑集群开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableLogicalCluster
        :type request: :class:`huaweicloudsdkdws.v2.EnableLogicalClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.EnableLogicalClusterResponse`
        """
        http_info = self._enable_logical_cluster_http_info(request)
        return self._call_api(**http_info)

    def enable_logical_cluster_async_invoker(self, request):
        http_info = self._enable_logical_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_logical_cluster_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableLogicalClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def enable_lts_logs_async(self, request):
        """开启云服务日志

        该接口用于开启集群LTS云日志服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableLtsLogs
        :type request: :class:`huaweicloudsdkdws.v2.EnableLtsLogsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.EnableLtsLogsResponse`
        """
        http_info = self._enable_lts_logs_http_info(request)
        return self._call_api(**http_info)

    def enable_lts_logs_async_invoker(self, request):
        http_info = self._enable_lts_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_lts_logs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/lts-logs/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableLtsLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def execute_cluster_upgrade_action_async(self, request):
        """下发集群升级相关操作

        下发集群升级相关操作
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteClusterUpgradeAction
        :type request: :class:`huaweicloudsdkdws.v2.ExecuteClusterUpgradeActionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ExecuteClusterUpgradeActionResponse`
        """
        http_info = self._execute_cluster_upgrade_action_http_info(request)
        return self._call_api(**http_info)

    def execute_cluster_upgrade_action_async_invoker(self, request):
        http_info = self._execute_cluster_upgrade_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_cluster_upgrade_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/upgrade-management/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteClusterUpgradeActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def execute_database_om_user_action_async(self, request):
        """执行运维用户操作

        进行数据库运维账户操作
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteDatabaseOmUserAction
        :type request: :class:`huaweicloudsdkdws.v2.ExecuteDatabaseOmUserActionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ExecuteDatabaseOmUserActionResponse`
        """
        http_info = self._execute_database_om_user_action_http_info(request)
        return self._call_api(**http_info)

    def execute_database_om_user_action_async_invoker(self, request):
        http_info = self._execute_database_om_user_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_database_om_user_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/db-manager/om-user/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteDatabaseOmUserActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def execute_redistribution_cluster_async(self, request):
        """下发重分布

        下发重分布
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteRedistributionCluster
        :type request: :class:`huaweicloudsdkdws.v2.ExecuteRedistributionClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ExecuteRedistributionClusterResponse`
        """
        http_info = self._execute_redistribution_cluster_http_info(request)
        return self._call_api(**http_info)

    def execute_redistribution_cluster_async_invoker(self, request):
        http_info = self._execute_redistribution_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_redistribution_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/redistribution",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteRedistributionClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def expand_instance_storage_async(self, request):
        """磁盘扩容

        随着客户业务的发展，磁盘空间往往最先出现资源瓶颈，在其他资源尚且充足的情况下，通过磁盘扩容可快速缓解存储资源瓶颈现象，操作过程中无需暂停业务，并且不会造成CPU、内存等资源浪费。
        - 磁盘扩容功能仅8.1.1.203及以上版本支持，并且创建集群规格需要为云数仓SSD云盘或实时数仓类型。
        - 按需+折扣套餐包消费模式下，存储扩容后超出折扣套餐包部分将按需收费。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandInstanceStorage
        :type request: :class:`huaweicloudsdkdws.v2.ExpandInstanceStorageRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ExpandInstanceStorageResponse`
        """
        http_info = self._expand_instance_storage_http_info(request)
        return self._call_api(**http_info)

    def expand_instance_storage_async_invoker(self, request):
        http_info = self._expand_instance_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _expand_instance_storage_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/expand-instance-storage",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandInstanceStorageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_alarm_configs_async(self, request):
        """查询告警配置

        查询告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmConfigs
        :type request: :class:`huaweicloudsdkdws.v2.ListAlarmConfigsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAlarmConfigsResponse`
        """
        http_info = self._list_alarm_configs_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_configs_async_invoker(self, request):
        http_info = self._list_alarm_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmConfigsResponse"
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

    def list_alarm_detail_async(self, request):
        """查询告警详情列表

        查询告警详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmDetail
        :type request: :class:`huaweicloudsdkdws.v2.ListAlarmDetailRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAlarmDetailResponse`
        """
        http_info = self._list_alarm_detail_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_detail_async_invoker(self, request):
        http_info = self._list_alarm_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'time_zone' in local_var_params:
            query_params.append(('time_zone', local_var_params['time_zone']))
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

    def list_alarm_statistic_async(self, request):
        """查询告警统计列表

        查询告警统计
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmStatistic
        :type request: :class:`huaweicloudsdkdws.v2.ListAlarmStatisticRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAlarmStatisticResponse`
        """
        http_info = self._list_alarm_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_statistic_async_invoker(self, request):
        http_info = self._list_alarm_statistic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_statistic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'time_zone' in local_var_params:
            query_params.append(('time_zone', local_var_params['time_zone']))

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

    def list_alarm_subs_async(self, request):
        """查询告警订阅列表

        查询订阅告警
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmSubs
        :type request: :class:`huaweicloudsdkdws.v2.ListAlarmSubsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAlarmSubsResponse`
        """
        http_info = self._list_alarm_subs_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_subs_async_invoker(self, request):
        http_info = self._list_alarm_subs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_subs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/alarm-subs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmSubsResponse"
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

    def list_audit_log_async(self, request):
        """查询日志记录

        查询审计日志记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditLog
        :type request: :class:`huaweicloudsdkdws.v2.ListAuditLogRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAuditLogResponse`
        """
        http_info = self._list_audit_log_http_info(request)
        return self._call_api(**http_info)

    def list_audit_log_async_invoker(self, request):
        http_info = self._list_audit_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/audit-log-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_availability_zones_async(self, request):
        """查询可用区列表

        在创建实例时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkdws.v2.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAvailabilityZonesResponse`
        """
        http_info = self._list_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zones_async_invoker(self, request):
        http_info = self._list_availability_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_availability_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/availability-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZonesResponse"
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

    def list_available_disaster_clusters_async(self, request):
        """查询可用容灾集群列表

        查询可用容灾集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableDisasterClusters
        :type request: :class:`huaweicloudsdkdws.v2.ListAvailableDisasterClustersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListAvailableDisasterClustersResponse`
        """
        http_info = self._list_available_disaster_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_available_disaster_clusters_async_invoker(self, request):
        http_info = self._list_available_disaster_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_available_disaster_clusters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/disaster-recovery-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableDisasterClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'primary_cluster_id' in local_var_params:
            query_params.append(('primary_cluster_id', local_var_params['primary_cluster_id']))
        if 'primary_spec_id' in local_var_params:
            query_params.append(('primary_spec_id', local_var_params['primary_spec_id']))
        if 'primary_cluster_dn_num' in local_var_params:
            query_params.append(('primary_cluster_dn_num', local_var_params['primary_cluster_dn_num']))
        if 'standby_region' in local_var_params:
            query_params.append(('standby_region', local_var_params['standby_region']))
        if 'standby_project_id' in local_var_params:
            query_params.append(('standby_project_id', local_var_params['standby_project_id']))
        if 'standby_az_code' in local_var_params:
            query_params.append(('standby_az_code', local_var_params['standby_az_code']))
        if 'dr_type' in local_var_params:
            query_params.append(('dr_type', local_var_params['dr_type']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'datastore_version' in local_var_params:
            query_params.append(('datastore_version', local_var_params['datastore_version']))

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

    def list_cluster_cn_async(self, request):
        """查询集群CN节点

        查询集群的CN节点列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterCn
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterCnRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterCnResponse`
        """
        http_info = self._list_cluster_cn_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_cn_async_invoker(self, request):
        http_info = self._list_cluster_cn_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_cn_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/cns",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterCnResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_cluster_configurations_async(self, request):
        """查询集群参数组

        查询集群所关联的参数组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterConfigurations
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterConfigurationsResponse`
        """
        http_info = self._list_cluster_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_configurations_async_invoker(self, request):
        http_info = self._list_cluster_configurations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_configurations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterConfigurationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_cluster_configurations_parameter_async(self, request):
        """查询集群参数配置

        查询集群所关联的参数组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterConfigurationsParameter
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterConfigurationsParameterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterConfigurationsParameterResponse`
        """
        http_info = self._list_cluster_configurations_parameter_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_configurations_parameter_async_invoker(self, request):
        http_info = self._list_cluster_configurations_parameter_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_configurations_parameter_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/configurations/{configuration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterConfigurationsParameterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def list_cluster_details_async(self, request):
        """查询集群详情

        该接口用于查询集群详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterDetails
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterDetailsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterDetailsResponse`
        """
        http_info = self._list_cluster_details_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_details_async_invoker(self, request):
        http_info = self._list_cluster_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_cluster_nodes_async(self, request):
        """查询节点列表

        查询节点列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterNodes
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterNodesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterNodesResponse`
        """
        http_info = self._list_cluster_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_nodes_async_invoker(self, request):
        http_info = self._list_cluster_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'deleted' in local_var_params:
            query_params.append(('deleted', local_var_params['deleted']))
        if 'node_ids' in local_var_params:
            query_params.append(('node_ids', local_var_params['node_ids']))
            collection_formats['node_ids'] = 'csv'
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'filter_by' in local_var_params:
            query_params.append(('filter_by', local_var_params['filter_by']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
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

    def list_cluster_scale_in_numbers_async(self, request):
        """查询合适的缩容数

        查询合适的缩容数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterScaleInNumbers
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterScaleInNumbersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterScaleInNumbersResponse`
        """
        http_info = self._list_cluster_scale_in_numbers_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_scale_in_numbers_async_invoker(self, request):
        http_info = self._list_cluster_scale_in_numbers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_scale_in_numbers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/shrink-numbers",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterScaleInNumbersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_cluster_snapshots_async(self, request):
        """查询集群快照列表

        该接口用于查询集群快照列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterSnapshots
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterSnapshotsResponse`
        """
        http_info = self._list_cluster_snapshots_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_snapshots_async_invoker(self, request):
        http_info = self._list_cluster_snapshots_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_snapshots_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterSnapshotsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_cluster_tags_async(self, request):
        """查询集群标签

        查询指定集群的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterTags
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterTagsResponse`
        """
        http_info = self._list_cluster_tags_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_tags_async_invoker(self, request):
        http_info = self._list_cluster_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_cluster_workload_async(self, request):
        """查询资源管理

        查询资管管理开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterWorkload
        :type request: :class:`huaweicloudsdkdws.v2.ListClusterWorkloadRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClusterWorkloadResponse`
        """
        http_info = self._list_cluster_workload_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_workload_async_invoker(self, request):
        http_info = self._list_cluster_workload_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_workload_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterWorkloadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_clusters_async(self, request):
        """查询集群列表

        该接口用于查询并显示集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusters
        :type request: :class:`huaweicloudsdkdws.v2.ListClustersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListClustersResponse`
        """
        http_info = self._list_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_clusters_async_invoker(self, request):
        http_info = self._list_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_clusters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListClustersResponse"
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

    def list_configurations_audit_records_async(self, request):
        """查询参数修改审计记录

        查询参数修改审计记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurationsAuditRecords
        :type request: :class:`huaweicloudsdkdws.v2.ListConfigurationsAuditRecordsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListConfigurationsAuditRecordsResponse`
        """
        http_info = self._list_configurations_audit_records_http_info(request)
        return self._call_api(**http_info)

    def list_configurations_audit_records_async_invoker(self, request):
        http_info = self._list_configurations_audit_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_configurations_audit_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/configurations/audit-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationsAuditRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'action_time' in local_var_params:
            query_params.append(('action_time', local_var_params['action_time']))
        if 'filter_by' in local_var_params:
            query_params.append(('filter_by', local_var_params['filter_by']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
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

    def list_data_source_async(self, request):
        """查询数据源

        该接口用于查询数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDataSource
        :type request: :class:`huaweicloudsdkdws.v2.ListDataSourceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListDataSourceResponse`
        """
        http_info = self._list_data_source_http_info(request)
        return self._call_api(**http_info)

    def list_data_source_async_invoker(self, request):
        http_info = self._list_data_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_data_source_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ext-data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_database_users_async(self, request):
        """查询所有数据库用户/角色

        查询所有数据库用户/角色
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabaseUsers
        :type request: :class:`huaweicloudsdkdws.v2.ListDatabaseUsersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListDatabaseUsersResponse`
        """
        http_info = self._list_database_users_http_info(request)
        return self._call_api(**http_info)

    def list_database_users_async_invoker(self, request):
        http_info = self._list_database_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_database_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/db-manager/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_disaster_recover_async(self, request):
        """查询容灾列表

        查询容灾列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDisasterRecover
        :type request: :class:`huaweicloudsdkdws.v2.ListDisasterRecoverRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListDisasterRecoverResponse`
        """
        http_info = self._list_disaster_recover_http_info(request)
        return self._call_api(**http_info)

    def list_disaster_recover_async_invoker(self, request):
        http_info = self._list_disaster_recover_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_disaster_recover_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/disaster-recoveries",
            "request_type": request.__class__.__name__,
            "response_type": "ListDisasterRecoverResponse"
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

    def list_dss_pools_async(self, request):
        """查询专属分布式存储池列表

        获取专属分布式存储池列表，只包括用户开通的SSD专属资源池信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDssPools
        :type request: :class:`huaweicloudsdkdws.v2.ListDssPoolsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListDssPoolsResponse`
        """
        http_info = self._list_dss_pools_http_info(request)
        return self._call_api(**http_info)

    def list_dss_pools_async_invoker(self, request):
        http_info = self._list_dss_pools_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dss_pools_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/dss-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListDssPoolsResponse"
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

    def list_elbs_async(self, request):
        """获取集群可绑定的ELB列表

        查询集群可以关联的Elb列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListElbs
        :type request: :class:`huaweicloudsdkdws.v2.ListElbsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListElbsResponse`
        """
        http_info = self._list_elbs_http_info(request)
        return self._call_api(**http_info)

    def list_elbs_async_invoker(self, request):
        http_info = self._list_elbs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_elbs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/elbs",
            "request_type": request.__class__.__name__,
            "response_type": "ListElbsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_event_specs_async(self, request):
        """查询事件配置

        查询事件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEventSpecs
        :type request: :class:`huaweicloudsdkdws.v2.ListEventSpecsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListEventSpecsResponse`
        """
        http_info = self._list_event_specs_http_info(request)
        return self._call_api(**http_info)

    def list_event_specs_async_invoker(self, request):
        http_info = self._list_event_specs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_specs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/event-specs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventSpecsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_name' in local_var_params:
            query_params.append(('spec_name', local_var_params['spec_name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'source_type' in local_var_params:
            query_params.append(('source_type', local_var_params['source_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
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

    def list_event_subs_async(self, request):
        """查询订阅事件

        查询订阅的事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEventSubs
        :type request: :class:`huaweicloudsdkdws.v2.ListEventSubsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListEventSubsResponse`
        """
        http_info = self._list_event_subs_http_info(request)
        return self._call_api(**http_info)

    def list_event_subs_async_invoker(self, request):
        http_info = self._list_event_subs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_subs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/event-subs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventSubsResponse"
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

    def list_events_async(self, request):
        """查询事件列表

        查询事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkdws.v2.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListEventsResponse`
        """
        http_info = self._list_events_http_info(request)
        return self._call_api(**http_info)

    def list_events_async_invoker(self, request):
        http_info = self._list_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/events",
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

    def list_host_disk_async(self, request):
        """openApi查询磁盘信息

        openApi查询磁盘信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostDisk
        :type request: :class:`huaweicloudsdkdws.v2.ListHostDiskRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListHostDiskResponse`
        """
        http_info = self._list_host_disk_http_info(request)
        return self._call_api(**http_info)

    def list_host_disk_async_invoker(self, request):
        http_info = self._list_host_disk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_disk_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/dms/disk",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostDiskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
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

    def list_host_net_async(self, request):
        """openapi获取网卡状态

        openapi获取网卡状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostNet
        :type request: :class:`huaweicloudsdkdws.v2.ListHostNetRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListHostNetResponse`
        """
        http_info = self._list_host_net_http_info(request)
        return self._call_api(**http_info)

    def list_host_net_async_invoker(self, request):
        http_info = self._list_host_net_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_net_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/dms/net",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostNetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
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

    def list_host_overview_async(self, request):
        """openApi查询主机概览

        openApi查询主机概览
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostOverview
        :type request: :class:`huaweicloudsdkdws.v2.ListHostOverviewRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListHostOverviewResponse`
        """
        http_info = self._list_host_overview_http_info(request)
        return self._call_api(**http_info)

    def list_host_overview_async_invoker(self, request):
        http_info = self._list_host_overview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_overview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/dms/host-overview",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostOverviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
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

    def list_job_details_async(self, request):
        """查询job进度

        查询job进度信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobDetails
        :type request: :class:`huaweicloudsdkdws.v2.ListJobDetailsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListJobDetailsResponse`
        """
        http_info = self._list_job_details_http_info(request)
        return self._call_api(**http_info)

    def list_job_details_async_invoker(self, request):
        http_info = self._list_job_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_job_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/job/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def list_logical_cluster_rings_async(self, request):
        """查询逻辑集群可用ring环节点信息

        查询逻辑集群可用ring环节点信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogicalClusterRings
        :type request: :class:`huaweicloudsdkdws.v2.ListLogicalClusterRingsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListLogicalClusterRingsResponse`
        """
        http_info = self._list_logical_cluster_rings_http_info(request)
        return self._call_api(**http_info)

    def list_logical_cluster_rings_async_invoker(self, request):
        http_info = self._list_logical_cluster_rings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_logical_cluster_rings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters/rings",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogicalClusterRingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_logical_cluster_tasks_async(self, request):
        """查询逻辑集群任务信息

        逻辑集群-查询逻辑集群任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogicalClusterTasks
        :type request: :class:`huaweicloudsdkdws.v2.ListLogicalClusterTasksRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListLogicalClusterTasksResponse`
        """
        http_info = self._list_logical_cluster_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_logical_cluster_tasks_async_invoker(self, request):
        http_info = self._list_logical_cluster_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_logical_cluster_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogicalClusterTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'logical_cluster_name' in local_var_params:
            query_params.append(('logical_cluster_name', local_var_params['logical_cluster_name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
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

    def list_logical_cluster_volumes_async(self, request):
        """查询逻辑集群磁盘信息

        逻辑集群-查询逻辑集群磁盘信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogicalClusterVolumes
        :type request: :class:`huaweicloudsdkdws.v2.ListLogicalClusterVolumesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListLogicalClusterVolumesResponse`
        """
        http_info = self._list_logical_cluster_volumes_http_info(request)
        return self._call_api(**http_info)

    def list_logical_cluster_volumes_async_invoker(self, request):
        http_info = self._list_logical_cluster_volumes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_logical_cluster_volumes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters/volumes",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogicalClusterVolumesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_logical_clusters_async(self, request):
        """查询逻辑集群列表

        逻辑集群-查询逻辑集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogicalClusters
        :type request: :class:`huaweicloudsdkdws.v2.ListLogicalClustersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListLogicalClustersResponse`
        """
        http_info = self._list_logical_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_logical_clusters_async_invoker(self, request):
        http_info = self._list_logical_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_logical_clusters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogicalClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_lts_logs_async(self, request):
        """获取LTS日志列表

        获取LTS日志列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLtsLogs
        :type request: :class:`huaweicloudsdkdws.v2.ListLtsLogsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListLtsLogsResponse`
        """
        http_info = self._list_lts_logs_http_info(request)
        return self._call_api(**http_info)

    def list_lts_logs_async_invoker(self, request):
        http_info = self._list_lts_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_lts_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/lts-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLtsLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_monitor_indicator_data_async(self, request):
        """openApi查询历史监控数据

        openApi查询历史监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMonitorIndicatorData
        :type request: :class:`huaweicloudsdkdws.v2.ListMonitorIndicatorDataRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListMonitorIndicatorDataResponse`
        """
        http_info = self._list_monitor_indicator_data_http_info(request)
        return self._call_api(**http_info)

    def list_monitor_indicator_data_async_invoker(self, request):
        http_info = self._list_monitor_indicator_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_monitor_indicator_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/dms/metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "ListMonitorIndicatorDataResponse"
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
        if 'function' in local_var_params:
            query_params.append(('function', local_var_params['function']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'indicator_name' in local_var_params:
            query_params.append(('indicator_name', local_var_params['indicator_name']))
        if 'dim0' in local_var_params:
            query_params.append(('dim0', local_var_params['dim0']))
        if 'dim1' in local_var_params:
            query_params.append(('dim1', local_var_params['dim1']))

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

    def list_monitor_indicators_async(self, request):
        """openApi查询性能监控指标

        openApi查询性能监控指标
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMonitorIndicators
        :type request: :class:`huaweicloudsdkdws.v2.ListMonitorIndicatorsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListMonitorIndicatorsResponse`
        """
        http_info = self._list_monitor_indicators_http_info(request)
        return self._call_api(**http_info)

    def list_monitor_indicators_async_invoker(self, request):
        http_info = self._list_monitor_indicators_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_monitor_indicators_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/dms/metric-data/indicators",
            "request_type": request.__class__.__name__,
            "response_type": "ListMonitorIndicatorsResponse"
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

    def list_node_types_async(self, request):
        """查询节点类型

        该接口用于查询所有GaussDB(DWS)服务支持的节点类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodeTypes
        :type request: :class:`huaweicloudsdkdws.v2.ListNodeTypesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListNodeTypesResponse`
        """
        http_info = self._list_node_types_http_info(request)
        return self._call_api(**http_info)

    def list_node_types_async_invoker(self, request):
        http_info = self._list_node_types_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_node_types_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/node-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodeTypesResponse"
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

    def list_queries_async(self, request):
        """查询SQL列表

        该接口用于查询实时SQL列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQueries
        :type request: :class:`huaweicloudsdkdws.v2.ListQueriesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListQueriesResponse`
        """
        http_info = self._list_queries_http_info(request)
        return self._call_api(**http_info)

    def list_queries_async_invoker(self, request):
        http_info = self._list_queries_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_queries_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/dms/queries",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_quotas_async(self, request):
        """查询配额

        查询单租户在GaussDB(DWS)服务下的配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkdws.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_async_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
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

    def list_snapshot_cross_region_async(self, request):
        """获取跨区域快照可用region

        该接口用于获取跨区域快照可用region
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSnapshotCrossRegion
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotCrossRegionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotCrossRegionResponse`
        """
        http_info = self._list_snapshot_cross_region_http_info(request)
        return self._call_api(**http_info)

    def list_snapshot_cross_region_async_invoker(self, request):
        http_info = self._list_snapshot_cross_region_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_snapshot_cross_region_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/snapshots/cross-regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotCrossRegionResponse"
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

    def list_snapshot_cross_region_policy_async(self, request):
        """查询所有跨区域快照配置

        该接口用于查询所有跨区域快照配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSnapshotCrossRegionPolicy
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotCrossRegionPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotCrossRegionPolicyResponse`
        """
        http_info = self._list_snapshot_cross_region_policy_http_info(request)
        return self._call_api(**http_info)

    def list_snapshot_cross_region_policy_async_invoker(self, request):
        http_info = self._list_snapshot_cross_region_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_snapshot_cross_region_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/snapshots/cross-region-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotCrossRegionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
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

    def list_snapshot_details_async(self, request):
        """查询快照详情

        该接口用于使用快照ID查询快照详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSnapshotDetails
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotDetailsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotDetailsResponse`
        """
        http_info = self._list_snapshot_details_http_info(request)
        return self._call_api(**http_info)

    def list_snapshot_details_async_invoker(self, request):
        http_info = self._list_snapshot_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_snapshot_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/snapshots/{snapshot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def list_snapshot_policy_async(self, request):
        """查询快照策略

        查询快照策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSnapshotPolicy
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotPolicyRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotPolicyResponse`
        """
        http_info = self._list_snapshot_policy_http_info(request)
        return self._call_api(**http_info)

    def list_snapshot_policy_async_invoker(self, request):
        http_info = self._list_snapshot_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_snapshot_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/snapshot-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_snapshot_statistics_async(self, request):
        """快照统计信息

        快照统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSnapshotStatistics
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotStatisticsResponse`
        """
        http_info = self._list_snapshot_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_snapshot_statistics_async_invoker(self, request):
        http_info = self._list_snapshot_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_snapshot_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/snapshots/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_snapshots_async(self, request):
        """查询快照列表

        该接口用于查询快照列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSnapshots
        :type request: :class:`huaweicloudsdkdws.v2.ListSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListSnapshotsResponse`
        """
        http_info = self._list_snapshots_http_info(request)
        return self._call_api(**http_info)

    def list_snapshots_async_invoker(self, request):
        http_info = self._list_snapshots_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_snapshots_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotsResponse"
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

    def list_statistics_async(self, request):
        """查询资源统计信息列表

        查询当前可用资源数量，其中包括“可用集群和总集群（个）”、“可用节点和总节点（个）”、“总容量（GB）”。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStatistics
        :type request: :class:`huaweicloudsdkdws.v2.ListStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListStatisticsResponse`
        """
        http_info = self._list_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_statistics_async_invoker(self, request):
        http_info = self._list_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListStatisticsResponse"
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

    def list_tables_statistic_async(self, request):
        """查询表倾斜或脏页率信息

        该接口用于查询表倾斜或脏页率信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTablesStatistic
        :type request: :class:`huaweicloudsdkdws.v2.ListTablesStatisticRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListTablesStatisticResponse`
        """
        http_info = self._list_tables_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_tables_statistic_async_invoker(self, request):
        http_info = self._list_tables_statistic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tables_statistic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/dms/tables/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListTablesStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'rate_type' in local_var_params:
            query_params.append(('rate_type', local_var_params['rate_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))

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

    def list_tags_async(self, request):
        """查询项目标签

        查询项目标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkdws.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
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

    def list_topo_rings_async(self, request):
        """查询集群拓扑ring环节点信息

        查询集群拓扑ring环节点信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopoRings
        :type request: :class:`huaweicloudsdkdws.v2.ListTopoRingsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListTopoRingsResponse`
        """
        http_info = self._list_topo_rings_http_info(request)
        return self._call_api(**http_info)

    def list_topo_rings_async_invoker(self, request):
        http_info = self._list_topo_rings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topo_rings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/topo/rings",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopoRingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_updatable_version_async(self, request):
        """获取集群可升级的目标版本

        获取集群可升级的目标版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUpdatableVersion
        :type request: :class:`huaweicloudsdkdws.v2.ListUpdatableVersionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListUpdatableVersionResponse`
        """
        http_info = self._list_updatable_version_http_info(request)
        return self._call_api(**http_info)

    def list_updatable_version_async_invoker(self, request):
        http_info = self._list_updatable_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_updatable_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/upgrade-management/avail-versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListUpdatableVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_update_record_async(self, request):
        """获取集群升级记录

        通过此api获取当前集群升级记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUpdateRecord
        :type request: :class:`huaweicloudsdkdws.v2.ListUpdateRecordRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListUpdateRecordResponse`
        """
        http_info = self._list_update_record_http_info(request)
        return self._call_api(**http_info)

    def list_update_record_async_invoker(self, request):
        http_info = self._list_update_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_update_record_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/upgrade-management/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListUpdateRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_workload_queue_async(self, request):
        """查询工作负载队列

        查询工作负载队列
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkloadQueue
        :type request: :class:`huaweicloudsdkdws.v2.ListWorkloadQueueRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ListWorkloadQueueResponse`
        """
        http_info = self._list_workload_queue_http_info(request)
        return self._call_api(**http_info)

    def list_workload_queue_async_invoker(self, request):
        http_info = self._list_workload_queue_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workload_queue_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload/queues",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkloadQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def pause_disaster_recovery_async(self, request):
        """停止容灾

        停止容灾
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PauseDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.PauseDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.PauseDisasterRecoveryResponse`
        """
        http_info = self._pause_disaster_recovery_http_info(request)
        return self._call_api(**http_info)

    def pause_disaster_recovery_async_invoker(self, request):
        http_info = self._pause_disaster_recovery_http_info(request)
        return AsyncInvoker(self, http_info)

    def _pause_disaster_recovery_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/pause",
            "request_type": request.__class__.__name__,
            "response_type": "PauseDisasterRecoveryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def reset_password_async(self, request):
        """重置密码

        此接口用于重置集群管理员密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkdws.v2.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ResetPasswordResponse`
        """
        http_info = self._reset_password_http_info(request)
        return self._call_api(**http_info)

    def reset_password_async_invoker(self, request):
        http_info = self._reset_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/reset-password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def resize_cluster_async(self, request):
        """扩容集群调整集群大小

        此接口用于扩容集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeCluster
        :type request: :class:`huaweicloudsdkdws.v2.ResizeClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ResizeClusterResponse`
        """
        http_info = self._resize_cluster_http_info(request)
        return self._call_api(**http_info)

    def resize_cluster_async_invoker(self, request):
        http_info = self._resize_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def resize_cluster_with_existed_nodes_async(self, request):
        """从空闲节点扩容

        此接口用于从空闲节点扩容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeClusterWithExistedNodes
        :type request: :class:`huaweicloudsdkdws.v2.ResizeClusterWithExistedNodesRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ResizeClusterWithExistedNodesResponse`
        """
        http_info = self._resize_cluster_with_existed_nodes_http_info(request)
        return self._call_api(**http_info)

    def resize_cluster_with_existed_nodes_async_invoker(self, request):
        http_info = self._resize_cluster_with_existed_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_cluster_with_existed_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/resize-with-existed-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeClusterWithExistedNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def restart_cluster_async(self, request):
        """重启集群

        此接口用于重启集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartCluster
        :type request: :class:`huaweicloudsdkdws.v2.RestartClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestartClusterResponse`
        """
        http_info = self._restart_cluster_http_info(request)
        return self._call_api(**http_info)

    def restart_cluster_async_invoker(self, request):
        http_info = self._restart_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def restart_logical_cluster_async(self, request):
        """重启逻辑集群

        此接口用于重启逻辑集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartLogicalCluster
        :type request: :class:`huaweicloudsdkdws.v2.RestartLogicalClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestartLogicalClusterResponse`
        """
        http_info = self._restart_logical_cluster_http_info(request)
        return self._call_api(**http_info)

    def restart_logical_cluster_async_invoker(self, request):
        http_info = self._restart_logical_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_logical_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters/{logical_cluster_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartLogicalClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'logical_cluster_id' in local_var_params:
            path_params['logical_cluster_id'] = local_var_params['logical_cluster_id']

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

    def restore_cluster_async(self, request):
        """恢复集群

        该接口用于使用快照恢复集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreCluster
        :type request: :class:`huaweicloudsdkdws.v2.RestoreClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestoreClusterResponse`
        """
        http_info = self._restore_cluster_http_info(request)
        return self._call_api(**http_info)

    def restore_cluster_async_invoker(self, request):
        http_info = self._restore_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/snapshots/{snapshot_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def restore_disaster_async(self, request):
        """恢复容灾

        恢复容灾
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreDisaster
        :type request: :class:`huaweicloudsdkdws.v2.RestoreDisasterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestoreDisasterResponse`
        """
        http_info = self._restore_disaster_http_info(request)
        return self._call_api(**http_info)

    def restore_disaster_async_invoker(self, request):
        http_info = self._restore_disaster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_disaster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/recovery",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreDisasterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def restore_redistribution_async(self, request):
        """恢复重分布

        此接口用于恢复重分布。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreRedistribution
        :type request: :class:`huaweicloudsdkdws.v2.RestoreRedistributionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestoreRedistributionResponse`
        """
        http_info = self._restore_redistribution_http_info(request)
        return self._call_api(**http_info)

    def restore_redistribution_async_invoker(self, request):
        http_info = self._restore_redistribution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_redistribution_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/redistribution/recovery",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreRedistributionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def restore_table_async(self, request):
        """恢复表

        该接口用于恢复表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreTable
        :type request: :class:`huaweicloudsdkdws.v2.RestoreTableRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.RestoreTableResponse`
        """
        http_info = self._restore_table_http_info(request)
        return self._call_api(**http_info)

    def restore_table_async_invoker(self, request):
        http_info = self._restore_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_table_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/snapshots/{snapshot_id}/table-restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def save_cluster_description_info_async(self, request):
        """保存集群描述信息

        保存集群描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SaveClusterDescriptionInfo
        :type request: :class:`huaweicloudsdkdws.v2.SaveClusterDescriptionInfoRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SaveClusterDescriptionInfoResponse`
        """
        http_info = self._save_cluster_description_info_http_info(request)
        return self._call_api(**http_info)

    def save_cluster_description_info_async_invoker(self, request):
        http_info = self._save_cluster_description_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _save_cluster_description_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/description",
            "request_type": request.__class__.__name__,
            "response_type": "SaveClusterDescriptionInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

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

    def show_cluster_redistribution_async(self, request):
        """查询重分布详情

        查询重分布详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterRedistribution
        :type request: :class:`huaweicloudsdkdws.v2.ShowClusterRedistributionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowClusterRedistributionResponse`
        """
        http_info = self._show_cluster_redistribution_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_redistribution_async_invoker(self, request):
        http_info = self._show_cluster_redistribution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_redistribution_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/redistribution",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterRedistributionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
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

    def show_database_authority_async(self, request):
        """查询数据库对象权限

        查询数据库对象权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDatabaseAuthority
        :type request: :class:`huaweicloudsdkdws.v2.ShowDatabaseAuthorityRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDatabaseAuthorityResponse`
        """
        http_info = self._show_database_authority_http_info(request)
        return self._call_api(**http_info)

    def show_database_authority_async_invoker(self, request):
        http_info = self._show_database_authority_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_database_authority_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/db-manager/authority",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatabaseAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))
        if 'schema' in local_var_params:
            query_params.append(('schema', local_var_params['schema']))
        if 'table' in local_var_params:
            query_params.append(('table', local_var_params['table']))

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

    def show_database_om_user_status_async(self, request):
        """获得集群运维账户状态

        获得数据库运维账户状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDatabaseOmUserStatus
        :type request: :class:`huaweicloudsdkdws.v2.ShowDatabaseOmUserStatusRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDatabaseOmUserStatusResponse`
        """
        http_info = self._show_database_om_user_status_http_info(request)
        return self._call_api(**http_info)

    def show_database_om_user_status_async_invoker(self, request):
        http_info = self._show_database_om_user_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_database_om_user_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/db-manager/om-user/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatabaseOmUserStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def show_database_user_async(self, request):
        """查询指定用户信息

        查询指定用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDatabaseUser
        :type request: :class:`huaweicloudsdkdws.v2.ShowDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDatabaseUserResponse`
        """
        http_info = self._show_database_user_http_info(request)
        return self._call_api(**http_info)

    def show_database_user_async_invoker(self, request):
        http_info = self._show_database_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_database_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/db-manager/users/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatabaseUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

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

    def show_disaster_detail_async(self, request):
        """查询容灾详情

        查询容灾详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDisasterDetail
        :type request: :class:`huaweicloudsdkdws.v2.ShowDisasterDetailRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDisasterDetailResponse`
        """
        http_info = self._show_disaster_detail_http_info(request)
        return self._call_api(**http_info)

    def show_disaster_detail_async_invoker(self, request):
        http_info = self._show_disaster_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_disaster_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/disaster-recovery/{disaster_recovery_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDisasterDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def show_disaster_progress_async(self, request):
        """容灾-查询容灾进度详情

        容灾-查询容灾进度详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDisasterProgress
        :type request: :class:`huaweicloudsdkdws.v2.ShowDisasterProgressRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowDisasterProgressResponse`
        """
        http_info = self._show_disaster_progress_http_info(request)
        return self._call_api(**http_info)

    def show_disaster_progress_async_invoker(self, request):
        http_info = self._show_disaster_progress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_disaster_progress_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/disaster-recovery/{disaster_recovery_id}/show-progress",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDisasterProgressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def show_instance_async(self, request):
        """查询单个实例

        查询单个实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkdws.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_async_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_query_detail_async(self, request):
        """查询SQL执行信息

        查询SQL执行信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQueryDetail
        :type request: :class:`huaweicloudsdkdws.v2.ShowQueryDetailRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowQueryDetailResponse`
        """
        http_info = self._show_query_detail_http_info(request)
        return self._call_api(**http_info)

    def show_query_detail_async_invoker(self, request):
        http_info = self._show_query_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_query_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/dms/queries/{query_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQueryDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

        query_params = []
        if 'ctime' in local_var_params:
            query_params.append(('ctime', local_var_params['ctime']))

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

    def show_workload_plan_async(self, request):
        """查询某个工作负载计划详细信息

        查询某个工作负载计划详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkloadPlan
        :type request: :class:`huaweicloudsdkdws.v2.ShowWorkloadPlanRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShowWorkloadPlanResponse`
        """
        http_info = self._show_workload_plan_http_info(request)
        return self._call_api(**http_info)

    def show_workload_plan_async_invoker(self, request):
        http_info = self._show_workload_plan_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workload_plan_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload/plans/{plan_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkloadPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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

    def shrink_cluster_async(self, request):
        """集群缩容

        该接口用于缩容集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShrinkCluster
        :type request: :class:`huaweicloudsdkdws.v2.ShrinkClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.ShrinkClusterResponse`
        """
        http_info = self._shrink_cluster_http_info(request)
        return self._call_api(**http_info)

    def shrink_cluster_async_invoker(self, request):
        http_info = self._shrink_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _shrink_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/cluster-shrink",
            "request_type": request.__class__.__name__,
            "response_type": "ShrinkClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def start_disaster_recovery_async(self, request):
        """启动容灾

        启动容灾
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.StartDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.StartDisasterRecoveryResponse`
        """
        http_info = self._start_disaster_recovery_http_info(request)
        return self._call_api(**http_info)

    def start_disaster_recovery_async_invoker(self, request):
        http_info = self._start_disaster_recovery_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_disaster_recovery_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartDisasterRecoveryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def start_workload_plan_async(self, request):
        """启动工作负载计划

        启动工作负载计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartWorkloadPlan
        :type request: :class:`huaweicloudsdkdws.v2.StartWorkloadPlanRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.StartWorkloadPlanResponse`
        """
        http_info = self._start_workload_plan_http_info(request)
        return self._call_api(**http_info)

    def start_workload_plan_async_invoker(self, request):
        http_info = self._start_workload_plan_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_workload_plan_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload/plans/{plan_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartWorkloadPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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

    def stop_redistribution_async(self, request):
        """暂停重分布

        此接口用于暂停重分布。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopRedistribution
        :type request: :class:`huaweicloudsdkdws.v2.StopRedistributionRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.StopRedistributionResponse`
        """
        http_info = self._stop_redistribution_http_info(request)
        return self._call_api(**http_info)

    def stop_redistribution_async_invoker(self, request):
        http_info = self._stop_redistribution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_redistribution_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/redistribution/suspend",
            "request_type": request.__class__.__name__,
            "response_type": "StopRedistributionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def stop_workload_plan_async(self, request):
        """停止工作负载计划

        停止工作负载计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopWorkloadPlan
        :type request: :class:`huaweicloudsdkdws.v2.StopWorkloadPlanRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.StopWorkloadPlanResponse`
        """
        http_info = self._stop_workload_plan_http_info(request)
        return self._call_api(**http_info)

    def stop_workload_plan_async_invoker(self, request):
        http_info = self._stop_workload_plan_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_workload_plan_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/workload/plans/{plan_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopWorkloadPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']

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

    def switch_failover_disaster_async(self, request):
        """容灾异常切换

        容灾-异常切换
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchFailoverDisaster
        :type request: :class:`huaweicloudsdkdws.v2.SwitchFailoverDisasterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SwitchFailoverDisasterResponse`
        """
        http_info = self._switch_failover_disaster_http_info(request)
        return self._call_api(**http_info)

    def switch_failover_disaster_async_invoker(self, request):
        http_info = self._switch_failover_disaster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_failover_disaster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/failover",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchFailoverDisasterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def switch_over_cluster_async(self, request):
        """主备恢复

        当集群状态为“非均衡”时会出现某些节点主实例增多，从而负载压力较大。这种情况下集群状态是正常的，但整体性能要低于均衡状态。可进行集群主备恢复操作将集群状态切换为“可用“状态。
        - 集群主备恢复仅8.1.1.202及以上版本支持。
        - 集群主备恢复将会短暂中断业务，中断时间根据用户自身业务量所决定，建议用户在业务低峰期执行此操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchOverCluster
        :type request: :class:`huaweicloudsdkdws.v2.SwitchOverClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SwitchOverClusterResponse`
        """
        http_info = self._switch_over_cluster_http_info(request)
        return self._call_api(**http_info)

    def switch_over_cluster_async_invoker(self, request):
        http_info = self._switch_over_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_over_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/switchover",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchOverClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def switchover_disaster_recovery_async(self, request):
        """灾备切换

        容灾-灾备切换
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchoverDisasterRecovery
        :type request: :class:`huaweicloudsdkdws.v2.SwitchoverDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SwitchoverDisasterRecoveryResponse`
        """
        http_info = self._switchover_disaster_recovery_http_info(request)
        return self._call_api(**http_info)

    def switchover_disaster_recovery_async_invoker(self, request):
        http_info = self._switchover_disaster_recovery_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switchover_disaster_recovery_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/disaster-recovery/{disaster_recovery_id}/switchover",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchoverDisasterRecoveryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def sync_iam_users_async(self, request):
        """同步IAM用户到数据库

        同步IAM用户到数据库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncIamUsers
        :type request: :class:`huaweicloudsdkdws.v2.SyncIamUsersRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.SyncIamUsersResponse`
        """
        http_info = self._sync_iam_users_http_info(request)
        return self._call_api(**http_info)

    def sync_iam_users_async_invoker(self, request):
        http_info = self._sync_iam_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_iam_users_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/db-manager/sync-iam-user",
            "request_type": request.__class__.__name__,
            "response_type": "SyncIamUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def update_alarm_sub_async(self, request):
        """更新告警订阅

        更新订阅的告警
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlarmSub
        :type request: :class:`huaweicloudsdkdws.v2.UpdateAlarmSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateAlarmSubResponse`
        """
        http_info = self._update_alarm_sub_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_sub_async_invoker(self, request):
        http_info = self._update_alarm_sub_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_alarm_sub_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/alarm-subs/{alarm_sub_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmSubResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_sub_id' in local_var_params:
            path_params['alarm_sub_id'] = local_var_params['alarm_sub_id']

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

    def update_cluster_dns_async(self, request):
        """修改集群域名

        为指定集群修改域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateClusterDns
        :type request: :class:`huaweicloudsdkdws.v2.UpdateClusterDnsRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateClusterDnsResponse`
        """
        http_info = self._update_cluster_dns_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_dns_async_invoker(self, request):
        http_info = self._update_cluster_dns_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cluster_dns_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/dns",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterDnsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def update_configuration_async(self, request):
        """修改集群参数配置

        修改集群使用的参数配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfiguration
        :type request: :class:`huaweicloudsdkdws.v2.UpdateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateConfigurationResponse`
        """
        http_info = self._update_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_configuration_async_invoker(self, request):
        http_info = self._update_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_configuration_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/configurations/{configuration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def update_data_source_async(self, request):
        """更新数据源

        该接口用于更新一个数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDataSource
        :type request: :class:`huaweicloudsdkdws.v2.UpdateDataSourceRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDataSourceResponse`
        """
        http_info = self._update_data_source_http_info(request)
        return self._call_api(**http_info)

    def update_data_source_async_invoker(self, request):
        http_info = self._update_data_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_data_source_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ext-data-sources/{ext_data_source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'ext_data_source_id' in local_var_params:
            path_params['ext_data_source_id'] = local_var_params['ext_data_source_id']

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

    def update_database_authority_async(self, request):
        """修改数据库对象权限

        修改数据库对象权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDatabaseAuthority
        :type request: :class:`huaweicloudsdkdws.v2.UpdateDatabaseAuthorityRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDatabaseAuthorityResponse`
        """
        http_info = self._update_database_authority_http_info(request)
        return self._call_api(**http_info)

    def update_database_authority_async_invoker(self, request):
        http_info = self._update_database_authority_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_database_authority_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/db-manager/authority",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabaseAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def update_database_user_info_async(self, request):
        """修改指定用户信息

        修改指定用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDatabaseUserInfo
        :type request: :class:`huaweicloudsdkdws.v2.UpdateDatabaseUserInfoRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDatabaseUserInfoResponse`
        """
        http_info = self._update_database_user_info_http_info(request)
        return self._call_api(**http_info)

    def update_database_user_info_async_invoker(self, request):
        http_info = self._update_database_user_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_database_user_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/clusters/{cluster_id}/db-manager/users/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabaseUserInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

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

    def update_disaster_info_async(self, request):
        """更新容灾配置

        更新容灾配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDisasterInfo
        :type request: :class:`huaweicloudsdkdws.v2.UpdateDisasterInfoRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDisasterInfoResponse`
        """
        http_info = self._update_disaster_info_http_info(request)
        return self._call_api(**http_info)

    def update_disaster_info_async_invoker(self, request):
        http_info = self._update_disaster_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_disaster_info_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/disaster-recovery/{disaster_recovery_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDisasterInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_id' in local_var_params:
            path_params['disaster_recovery_id'] = local_var_params['disaster_recovery_id']

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

    def update_event_sub_async(self, request):
        """更新订阅事件

        更新订阅事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEventSub
        :type request: :class:`huaweicloudsdkdws.v2.UpdateEventSubRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateEventSubResponse`
        """
        http_info = self._update_event_sub_http_info(request)
        return self._call_api(**http_info)

    def update_event_sub_async_invoker(self, request):
        http_info = self._update_event_sub_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_event_sub_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/event-subs/{event_sub_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEventSubResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_sub_id' in local_var_params:
            path_params['event_sub_id'] = local_var_params['event_sub_id']

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

    def update_logical_cluster_async(self, request):
        """编辑逻辑集群

        此接口用于编辑修改逻辑集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLogicalCluster
        :type request: :class:`huaweicloudsdkdws.v2.UpdateLogicalClusterRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateLogicalClusterResponse`
        """
        http_info = self._update_logical_cluster_http_info(request)
        return self._call_api(**http_info)

    def update_logical_cluster_async_invoker(self, request):
        http_info = self._update_logical_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_logical_cluster_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/logical-clusters/{logical_cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogicalClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'logical_cluster_id' in local_var_params:
            path_params['logical_cluster_id'] = local_var_params['logical_cluster_id']

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

    def update_maintenance_window_async(self, request):
        """修改运维时间窗

        您可以根据业务需求，设置可维护时间段。建议将可维护时间段设置在业务低峰期，避免业务在维护过程中异常中断。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMaintenanceWindow
        :type request: :class:`huaweicloudsdkdws.v2.UpdateMaintenanceWindowRequest`
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateMaintenanceWindowResponse`
        """
        http_info = self._update_maintenance_window_http_info(request)
        return self._call_api(**http_info)

    def update_maintenance_window_async_invoker(self, request):
        http_info = self._update_maintenance_window_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_maintenance_window_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/maintenance-window",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMaintenanceWindowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

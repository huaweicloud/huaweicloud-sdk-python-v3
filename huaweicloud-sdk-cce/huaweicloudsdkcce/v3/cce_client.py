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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcce'")


class CceClient(Client):
    def __init__(self):
        super(CceClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcce.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CceClient":
                raise TypeError("client type error, support client type is CceClient")
            client_builder = ClientBuilder(clazz)

        
        try:
            from .cce_exception_handler import CceExceptionHandler
            client_builder.with_exception_handler(CceExceptionHandler())
        except (ImportError, AttributeError):
            warnings.warn("failed to import 'CceExceptionHandler', please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcce'")

        return client_builder

    def add_node(self, request):
        r"""纳管节点

        该API用于在指定集群下纳管节点。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddNode
        :type request: :class:`huaweicloudsdkcce.v3.AddNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.AddNodeResponse`
        """
        http_info = self._add_node_http_info(request)
        return self._call_api(**http_info)

    def add_node_invoker(self, request):
        http_info = self._add_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/add",
            "request_type": request.__class__.__name__,
            "response_type": "AddNodeResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_nodes_to_node_pool(self, request):
        r"""自定义节点池纳管节点

        该API用于在指定集群自定义节点池下纳管节点。竞价实例不支持纳管。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddNodesToNodePool
        :type request: :class:`huaweicloudsdkcce.v3.AddNodesToNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.AddNodesToNodePoolResponse`
        """
        http_info = self._add_nodes_to_node_pool_http_info(request)
        return self._call_api(**http_info)

    def add_nodes_to_node_pool_invoker(self, request):
        http_info = self._add_nodes_to_node_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_nodes_to_node_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}/nodes/add",
            "request_type": request.__class__.__name__,
            "response_type": "AddNodesToNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def awake_cluster(self, request):
        r"""集群唤醒

        集群唤醒用于唤醒已休眠的集群，唤醒后，将继续收取控制节点资源费用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AwakeCluster
        :type request: :class:`huaweicloudsdkcce.v3.AwakeClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.AwakeClusterResponse`
        """
        http_info = self._awake_cluster_http_info(request)
        return self._call_api(**http_info)

    def awake_cluster_invoker(self, request):
        http_info = self._awake_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _awake_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/awake",
            "request_type": request.__class__.__name__,
            "response_type": "AwakeClusterResponse"
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

    def batch_create_cluster_tags(self, request):
        r"""批量添加指定集群的资源标签

        该API用于批量添加指定集群的资源标签。
        &gt; - 每个集群支持最多20个资源标签。
        &gt; - 此接口为幂等接口：创建时，如果创建的标签已经存在（key/value均相同视为重复），默认处理成功；key相同，value不同时会覆盖原有标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateClusterTags
        :type request: :class:`huaweicloudsdkcce.v3.BatchCreateClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.BatchCreateClusterTagsResponse`
        """
        http_info = self._batch_create_cluster_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_cluster_tags_invoker(self, request):
        http_info = self._batch_create_cluster_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_cluster_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateClusterTagsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_cluster_tags(self, request):
        r"""批量删除指定集群的资源标签

        该API用于批量删除指定集群的资源标签。
        &gt; - 此接口为幂等接口：删除时，如果删除的标签key不存在，默认处理成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteClusterTags
        :type request: :class:`huaweicloudsdkcce.v3.BatchDeleteClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.BatchDeleteClusterTagsResponse`
        """
        http_info = self._batch_delete_cluster_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_cluster_tags_invoker(self, request):
        http_info = self._batch_delete_cluster_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_cluster_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteClusterTagsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_sync_nodes(self, request):
        r"""批量同步节点

        该API用于批量同步节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSyncNodes
        :type request: :class:`huaweicloudsdkcce.v3.BatchSyncNodesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.BatchSyncNodesResponse`
        """
        http_info = self._batch_sync_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_sync_nodes_invoker(self, request):
        http_info = self._batch_sync_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_sync_nodes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/sync",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSyncNodesResponse"
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

    def continue_upgrade_cluster_task(self, request):
        r"""继续执行集群升级任务

        继续执行被暂停的集群升级任务。
        &gt; - 集群升级涉及多维度的组件升级操作，强烈建议统一通过CCE控制台执行交互式升级，降低集群升级过程的业务意外受损风险；
        &gt; - 当前集群升级相关接口受限开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ContinueUpgradeClusterTask
        :type request: :class:`huaweicloudsdkcce.v3.ContinueUpgradeClusterTaskRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ContinueUpgradeClusterTaskResponse`
        """
        http_info = self._continue_upgrade_cluster_task_http_info(request)
        return self._call_api(**http_info)

    def continue_upgrade_cluster_task_invoker(self, request):
        http_info = self._continue_upgrade_cluster_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _continue_upgrade_cluster_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade/continue",
            "request_type": request.__class__.__name__,
            "response_type": "ContinueUpgradeClusterTaskResponse"
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

    def create_addon_instance(self, request):
        r"""创建AddonInstance

        根据提供的插件模板，安装插件实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.CreateAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAddonInstanceResponse`
        """
        http_info = self._create_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def create_addon_instance_invoker(self, request):
        http_info = self._create_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_addon_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/addons",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAddonInstanceResponse"
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

    def create_cloud_persistent_volume_claims(self, request):
        r"""创建PVC（待废弃）

        该API用于在指定的Namespace下通过云存储服务中的云存储（EVS、SFS、OBS）去创建PVC（PersistentVolumeClaim）。该API待废弃，请使用Kubernetes PVC相关接口。
        
        
        &gt;存储管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。如果使用https://Endpoint/uri，则必须指定请求header中的X-Cluster-ID参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCloudPersistentVolumeClaims
        :type request: :class:`huaweicloudsdkcce.v3.CreateCloudPersistentVolumeClaimsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateCloudPersistentVolumeClaimsResponse`
        """
        http_info = self._create_cloud_persistent_volume_claims_http_info(request)
        return self._call_api(**http_info)

    def create_cloud_persistent_volume_claims_invoker(self, request):
        http_info = self._create_cloud_persistent_volume_claims_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cloud_persistent_volume_claims_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v1/namespaces/{namespace}/cloudpersistentvolumeclaims",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCloudPersistentVolumeClaimsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}
        if 'x_cluster_id' in local_var_params:
            header_params['X-Cluster-ID'] = local_var_params['x_cluster_id']

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

    def create_cluster(self, request):
        r"""创建集群

        该API用于创建一个空集群（即只有控制节点Master，没有工作节点Node）。请在调用本接口完成集群创建之后，通过[创建节点](cce_02_0242.xml)添加节点。
        
        
        &gt;   - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        &gt;   - 调用该接口创建集群时，默认不安装ICAgent，若需安装ICAgent，可在请求Body参数的annotations中加入\&quot;cluster.install.addons.external/install\&quot;:\&quot;[{\&quot;addonTemplateName\&quot;:\&quot;icagent\&quot;}]\&quot;的集群注解，将在创建集群时自动安装ICAgent。ICAgent是应用性能管理APM的采集代理，运行在应用所在的服务器上，用于实时采集探针所获取的数据，安装ICAgent是使用应用性能管理APM的前提。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkcce.v3.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateClusterResponse`
        """
        http_info = self._create_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_invoker(self, request):
        http_info = self._create_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters",
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_cluster_master_snapshot(self, request):
        r"""集群备份

        集群备份
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterMasterSnapshot
        :type request: :class:`huaweicloudsdkcce.v3.CreateClusterMasterSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateClusterMasterSnapshotResponse`
        """
        http_info = self._create_cluster_master_snapshot_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_master_snapshot_invoker(self, request):
        http_info = self._create_cluster_master_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_master_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3.1/projects/{project_id}/clusters/{cluster_id}/operation/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterMasterSnapshotResponse"
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

    def create_kubernetes_cluster_cert(self, request):
        r"""获取集群证书

        该API用于获取指定集群的证书信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateKubernetesClusterCert
        :type request: :class:`huaweicloudsdkcce.v3.CreateKubernetesClusterCertRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateKubernetesClusterCertResponse`
        """
        http_info = self._create_kubernetes_cluster_cert_http_info(request)
        return self._call_api(**http_info)

    def create_kubernetes_cluster_cert_invoker(self, request):
        http_info = self._create_kubernetes_cluster_cert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_kubernetes_cluster_cert_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/clustercert",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKubernetesClusterCertResponse"
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

        response_headers = ["Port-ID", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_node(self, request):
        r"""创建节点

        该API用于在指定集群下创建节点。
        &gt; - 若无集群，请先[创建集群](cce_02_0236.xml)。
        &gt; - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNode
        :type request: :class:`huaweicloudsdkcce.v3.CreateNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateNodeResponse`
        """
        http_info = self._create_node_http_info(request)
        return self._call_api(**http_info)

    def create_node_invoker(self, request):
        http_info = self._create_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'nodepool_scale_up' in local_var_params:
            query_params.append(('nodepoolScaleUp', local_var_params['nodepool_scale_up']))

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

    def create_node_pool(self, request):
        r"""创建节点池

        该API用于在指定集群下创建节点池。仅支持集群在处于可用、扩容、缩容状态时调用。
        
        1.21版本的集群创建节点池时支持绑定安全组，每个节点池最多绑定五个安全组。
        
        更新节点池的安全组后，只针对新创的pod生效，建议驱逐节点上原有的pod。
        
        &gt; 若无集群，请先[创建集群](cce_02_0236.xml)。
        &gt; 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNodePool
        :type request: :class:`huaweicloudsdkcce.v3.CreateNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateNodePoolResponse`
        """
        http_info = self._create_node_pool_http_info(request)
        return self._call_api(**http_info)

    def create_node_pool_invoker(self, request):
        http_info = self._create_node_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_node_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNodePoolResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_partition(self, request):
        r"""创建分区

        创建分区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePartition
        :type request: :class:`huaweicloudsdkcce.v3.CreatePartitionRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreatePartitionResponse`
        """
        http_info = self._create_partition_http_info(request)
        return self._call_api(**http_info)

    def create_partition_invoker(self, request):
        http_info = self._create_partition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_partition_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/partitions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePartitionResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_post_check(self, request):
        r"""集群升级后确认

        集群升级后确认，该接口建议配合Console使用，主要用于升级步骤完成后，客户确认集群状态和业务正常后做反馈。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePostCheck
        :type request: :class:`huaweicloudsdkcce.v3.CreatePostCheckRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreatePostCheckResponse`
        """
        http_info = self._create_post_check_http_info(request)
        return self._call_api(**http_info)

    def create_post_check_invoker(self, request):
        http_info = self._create_post_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_post_check_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/postcheck",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostCheckResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_pre_check(self, request):
        r"""集群升级前检查

        集群升级前检查
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePreCheck
        :type request: :class:`huaweicloudsdkcce.v3.CreatePreCheckRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreatePreCheckResponse`
        """
        http_info = self._create_pre_check_http_info(request)
        return self._call_api(**http_info)

    def create_pre_check_invoker(self, request):
        http_info = self._create_pre_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pre_check_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/precheck",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePreCheckResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_release(self, request):
        r"""创建模板实例

        创建模板实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRelease
        :type request: :class:`huaweicloudsdkcce.v3.CreateReleaseRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateReleaseResponse`
        """
        http_info = self._create_release_http_info(request)
        return self._call_api(**http_info)

    def create_release_invoker(self, request):
        http_info = self._create_release_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_release_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/cce/cam/v3/clusters/{cluster_id}/releases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReleaseResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_upgrade_work_flow(self, request):
        r"""开启集群升级流程引导任务

        该API用于创建一个集群升级流程引导任务。请在调用本接口完成引导任务创建之后，通过集群升级前检查开始检查任务。
        升级流程任务用于控制集群升级任务的执行流程，执行流程为 升级前检查 &#x3D;&gt; 集群升级 &#x3D;&gt; 升级后检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUpgradeWorkFlow
        :type request: :class:`huaweicloudsdkcce.v3.CreateUpgradeWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateUpgradeWorkFlowResponse`
        """
        http_info = self._create_upgrade_work_flow_http_info(request)
        return self._call_api(**http_info)

    def create_upgrade_work_flow_invoker(self, request):
        http_info = self._create_upgrade_work_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_upgrade_work_flow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgradeworkflows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUpgradeWorkFlowResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_addon_instance(self, request):
        r"""删除AddonInstance

        删除插件实例的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.DeleteAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteAddonInstanceResponse`
        """
        http_info = self._delete_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_addon_instance_invoker(self, request):
        http_info = self._delete_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_addon_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/api/v3/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAddonInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_chart(self, request):
        r"""删除模板

        删除模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteChart
        :type request: :class:`huaweicloudsdkcce.v3.DeleteChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteChartResponse`
        """
        http_info = self._delete_chart_http_info(request)
        return self._call_api(**http_info)

    def delete_chart_invoker(self, request):
        http_info = self._delete_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_chart_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/charts/{chart_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

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

    def delete_cloud_persistent_volume_claims(self, request):
        r"""删除PVC（待废弃）

        该API用于删除指定Namespace下的PVC（PersistentVolumeClaim）对象，并可以选择保留后端的云存储。该API待废弃，请使用Kubernetes PVC相关接口。
        &gt;存储管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。如果使用https://Endpoint/uri，则必须指定请求header中的X-Cluster-ID参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCloudPersistentVolumeClaims
        :type request: :class:`huaweicloudsdkcce.v3.DeleteCloudPersistentVolumeClaimsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteCloudPersistentVolumeClaimsResponse`
        """
        http_info = self._delete_cloud_persistent_volume_claims_http_info(request)
        return self._call_api(**http_info)

    def delete_cloud_persistent_volume_claims_invoker(self, request):
        http_info = self._delete_cloud_persistent_volume_claims_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cloud_persistent_volume_claims_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/api/v1/namespaces/{namespace}/cloudpersistentvolumeclaims/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCloudPersistentVolumeClaimsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []
        if 'delete_volume' in local_var_params:
            query_params.append(('deleteVolume', local_var_params['delete_volume']))
        if 'storage_type' in local_var_params:
            query_params.append(('storageType', local_var_params['storage_type']))

        header_params = {}
        if 'x_cluster_id' in local_var_params:
            header_params['X-Cluster-ID'] = local_var_params['x_cluster_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_cluster(self, request):
        r"""删除集群

        该API用于删除一个指定的集群。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkcce.v3.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteClusterResponse`
        """
        http_info = self._delete_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_invoker(self, request):
        http_info = self._delete_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cluster_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}",
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
        if 'delete_efs' in local_var_params:
            query_params.append(('delete_efs', local_var_params['delete_efs']))
        if 'delete_eni' in local_var_params:
            query_params.append(('delete_eni', local_var_params['delete_eni']))
        if 'delete_evs' in local_var_params:
            query_params.append(('delete_evs', local_var_params['delete_evs']))
        if 'delete_net' in local_var_params:
            query_params.append(('delete_net', local_var_params['delete_net']))
        if 'delete_obs' in local_var_params:
            query_params.append(('delete_obs', local_var_params['delete_obs']))
        if 'delete_sfs' in local_var_params:
            query_params.append(('delete_sfs', local_var_params['delete_sfs']))
        if 'delete_sfs30' in local_var_params:
            query_params.append(('delete_sfs30', local_var_params['delete_sfs30']))
        if 'lts_reclaim_policy' in local_var_params:
            query_params.append(('lts_reclaim_policy', local_var_params['lts_reclaim_policy']))
        if 'tobedeleted' in local_var_params:
            query_params.append(('tobedeleted', local_var_params['tobedeleted']))
        if 'ondemand_node_policy' in local_var_params:
            query_params.append(('ondemand_node_policy', local_var_params['ondemand_node_policy']))
        if 'periodic_node_policy' in local_var_params:
            query_params.append(('periodic_node_policy', local_var_params['periodic_node_policy']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""删除节点

        该API用于删除指定的节点。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNode
        :type request: :class:`huaweicloudsdkcce.v3.DeleteNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteNodeResponse`
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
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []
        if 'nodepool_scale_down' in local_var_params:
            query_params.append(('nodepoolScaleDown', local_var_params['nodepool_scale_down']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_node_pool(self, request):
        r"""删除节点池

        该API用于删除指定的节点池。
        &gt; 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNodePool
        :type request: :class:`huaweicloudsdkcce.v3.DeleteNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteNodePoolResponse`
        """
        http_info = self._delete_node_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_node_pool_invoker(self, request):
        http_info = self._delete_node_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_node_pool_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def delete_release(self, request):
        r"""删除指定模板实例

        删除指定模板实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRelease
        :type request: :class:`huaweicloudsdkcce.v3.DeleteReleaseRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteReleaseResponse`
        """
        http_info = self._delete_release_http_info(request)
        return self._call_api(**http_info)

    def delete_release_invoker(self, request):
        http_info = self._delete_release_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_release_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/cce/cam/v3/clusters/{cluster_id}/namespace/{namespace}/releases/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteReleaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
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

    def download_chart(self, request):
        r"""下载模板

        下载模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadChart
        :type request: :class:`huaweicloudsdkcce.v3.DownloadChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DownloadChartResponse`
        """
        http_info = self._download_chart_http_info(request)
        return self._call_api(**http_info)

    def download_chart_invoker(self, request):
        http_info = self._download_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_chart_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/charts/{chart_id}/archive",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

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

    def hibernate_cluster(self, request):
        r"""集群休眠

        集群休眠用于将运行中的集群置于休眠状态，休眠后，将不再收取控制节点资源费用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HibernateCluster
        :type request: :class:`huaweicloudsdkcce.v3.HibernateClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.HibernateClusterResponse`
        """
        http_info = self._hibernate_cluster_http_info(request)
        return self._call_api(**http_info)

    def hibernate_cluster_invoker(self, request):
        http_info = self._hibernate_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _hibernate_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/hibernate",
            "request_type": request.__class__.__name__,
            "response_type": "HibernateClusterResponse"
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

    def list_addon_instances(self, request):
        r"""获取AddonInstance列表

        获取集群所有已安装插件实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddonInstances
        :type request: :class:`huaweicloudsdkcce.v3.ListAddonInstancesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAddonInstancesResponse`
        """
        http_info = self._list_addon_instances_http_info(request)
        return self._call_api(**http_info)

    def list_addon_instances_invoker(self, request):
        http_info = self._list_addon_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_addon_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/addons",
            "request_type": request.__class__.__name__,
            "response_type": "ListAddonInstancesResponse"
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

    def list_addon_templates(self, request):
        r"""查询AddonTemplates列表

        插件模板查询接口，查询插件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddonTemplates
        :type request: :class:`huaweicloudsdkcce.v3.ListAddonTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAddonTemplatesResponse`
        """
        http_info = self._list_addon_templates_http_info(request)
        return self._call_api(**http_info)

    def list_addon_templates_invoker(self, request):
        http_info = self._list_addon_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_addon_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/addontemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAddonTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'addon_template_name' in local_var_params:
            query_params.append(('addon_template_name', local_var_params['addon_template_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""获取模板列表

        获取模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCharts
        :type request: :class:`huaweicloudsdkcce.v3.ListChartsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListChartsResponse`
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
            "resource_path": "/v2/charts",
            "request_type": request.__class__.__name__,
            "response_type": "ListChartsResponse"
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

    def list_cluster_master_snapshot_tasks(self, request):
        r"""获取集群备份任务详情列表

        获取集群备份任务详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterMasterSnapshotTasks
        :type request: :class:`huaweicloudsdkcce.v3.ListClusterMasterSnapshotTasksRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListClusterMasterSnapshotTasksResponse`
        """
        http_info = self._list_cluster_master_snapshot_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_master_snapshot_tasks_invoker(self, request):
        http_info = self._list_cluster_master_snapshot_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cluster_master_snapshot_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3.1/projects/{project_id}/clusters/{cluster_id}/operation/snapshot/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterMasterSnapshotTasksResponse"
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

    def list_cluster_upgrade_feature_gates(self, request):
        r"""获取集群升级特性开关配置

        获取集群升级特性开关配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterUpgradeFeatureGates
        :type request: :class:`huaweicloudsdkcce.v3.ListClusterUpgradeFeatureGatesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListClusterUpgradeFeatureGatesResponse`
        """
        http_info = self._list_cluster_upgrade_feature_gates_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_upgrade_feature_gates_invoker(self, request):
        http_info = self._list_cluster_upgrade_feature_gates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cluster_upgrade_feature_gates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/clusterupgradefeaturegates",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterUpgradeFeatureGatesResponse"
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

    def list_cluster_upgrade_paths(self, request):
        r"""获取集群升级路径

        获取集群升级路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterUpgradePaths
        :type request: :class:`huaweicloudsdkcce.v3.ListClusterUpgradePathsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListClusterUpgradePathsResponse`
        """
        http_info = self._list_cluster_upgrade_paths_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_upgrade_paths_invoker(self, request):
        http_info = self._list_cluster_upgrade_paths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cluster_upgrade_paths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/clusterupgradepaths",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterUpgradePathsResponse"
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

    def list_clusters(self, request):
        r"""获取指定项目下的集群

        该API用于获取指定项目下所有集群的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusters
        :type request: :class:`huaweicloudsdkcce.v3.ListClustersRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListClustersResponse`
        """
        http_info = self._list_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_clusters_invoker(self, request):
        http_info = self._list_clusters_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_clusters_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_node_pools(self, request):
        r"""获取集群下所有节点池

        该API用于获取集群下所有节点池。
        &gt; - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        &gt; - nodepool是集群中具有相同配置的节点实例的子集。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNodePools
        :type request: :class:`huaweicloudsdkcce.v3.ListNodePoolsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListNodePoolsResponse`
        """
        http_info = self._list_node_pools_http_info(request)
        return self._call_api(**http_info)

    def list_node_pools_invoker(self, request):
        http_info = self._list_node_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_node_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodePoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'show_default_node_pool' in local_var_params:
            query_params.append(('showDefaultNodePool', local_var_params['show_default_node_pool']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""获取集群下所有节点

        该API用于通过集群ID获取指定集群下所有节点的详细信息。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNodes
        :type request: :class:`huaweicloudsdkcce.v3.ListNodesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListNodesResponse`
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
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodesResponse"
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

    def list_partitions(self, request):
        r"""获取分区列表

        获取分区列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPartitions
        :type request: :class:`huaweicloudsdkcce.v3.ListPartitionsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListPartitionsResponse`
        """
        http_info = self._list_partitions_http_info(request)
        return self._call_api(**http_info)

    def list_partitions_invoker(self, request):
        http_info = self._list_partitions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_partitions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/partitions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartitionsResponse"
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

    def list_pre_check_tasks(self, request):
        r"""获取集群升级前检查任务详情列表

        获取集群升级前检查任务详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPreCheckTasks
        :type request: :class:`huaweicloudsdkcce.v3.ListPreCheckTasksRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListPreCheckTasksResponse`
        """
        http_info = self._list_pre_check_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_pre_check_tasks_invoker(self, request):
        http_info = self._list_pre_check_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pre_check_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/precheck/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListPreCheckTasksResponse"
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

    def list_releases(self, request):
        r"""获取模板实例列表

        获取模板实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReleases
        :type request: :class:`huaweicloudsdkcce.v3.ListReleasesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListReleasesResponse`
        """
        http_info = self._list_releases_http_info(request)
        return self._call_api(**http_info)

    def list_releases_invoker(self, request):
        http_info = self._list_releases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_releases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cce/cam/v3/clusters/{cluster_id}/releases",
            "request_type": request.__class__.__name__,
            "response_type": "ListReleasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'chart_id' in local_var_params:
            query_params.append(('chart_id', local_var_params['chart_id']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_upgrade_cluster_tasks(self, request):
        r"""获取集群升级任务详情列表

        获取集群升级任务详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUpgradeClusterTasks
        :type request: :class:`huaweicloudsdkcce.v3.ListUpgradeClusterTasksRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListUpgradeClusterTasksResponse`
        """
        http_info = self._list_upgrade_cluster_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_upgrade_cluster_tasks_invoker(self, request):
        http_info = self._list_upgrade_cluster_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_upgrade_cluster_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListUpgradeClusterTasksResponse"
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

    def list_upgrade_work_flows(self, request):
        r"""获取UpgradeWorkFlows列表

        获取历史集群升级引导任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUpgradeWorkFlows
        :type request: :class:`huaweicloudsdkcce.v3.ListUpgradeWorkFlowsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListUpgradeWorkFlowsResponse`
        """
        http_info = self._list_upgrade_work_flows_http_info(request)
        return self._call_api(**http_info)

    def list_upgrade_work_flows_invoker(self, request):
        http_info = self._list_upgrade_work_flows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_upgrade_work_flows_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgradeworkflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListUpgradeWorkFlowsResponse"
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

    def lock_nodepool_node_scale_down(self, request):
        r"""节点开启缩容保护。

        该API用于节点开启缩容保护，开启缩容保护的节点无法通过修改节点池个数的方式被缩容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LockNodepoolNodeScaleDown
        :type request: :class:`huaweicloudsdkcce.v3.LockNodepoolNodeScaleDownRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.LockNodepoolNodeScaleDownResponse`
        """
        http_info = self._lock_nodepool_node_scale_down_http_info(request)
        return self._call_api(**http_info)

    def lock_nodepool_node_scale_down_invoker(self, request):
        http_info = self._lock_nodepool_node_scale_down_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _lock_nodepool_node_scale_down_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/locknodescaledown",
            "request_type": request.__class__.__name__,
            "response_type": "LockNodepoolNodeScaleDownResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def migrate_node(self, request):
        r"""节点迁移

        该API用于在指定集群下迁移节点到另一集群。
        
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateNode
        :type request: :class:`huaweicloudsdkcce.v3.MigrateNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.MigrateNodeResponse`
        """
        http_info = self._migrate_node_http_info(request)
        return self._call_api(**http_info)

    def migrate_node_invoker(self, request):
        http_info = self._migrate_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_node_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/operation/migrateto/{target_cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'target_cluster_id' in local_var_params:
            path_params['target_cluster_id'] = local_var_params['target_cluster_id']

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

    def pause_upgrade_cluster_task(self, request):
        r"""暂停集群升级任务

        暂停集群升级任务。
        &gt; - 集群升级涉及多维度的组件升级操作，强烈建议统一通过CCE控制台执行交互式升级，降低集群升级过程的业务意外受损风险；
        &gt; - 当前集群升级相关接口受限开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PauseUpgradeClusterTask
        :type request: :class:`huaweicloudsdkcce.v3.PauseUpgradeClusterTaskRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.PauseUpgradeClusterTaskResponse`
        """
        http_info = self._pause_upgrade_cluster_task_http_info(request)
        return self._call_api(**http_info)

    def pause_upgrade_cluster_task_invoker(self, request):
        http_info = self._pause_upgrade_cluster_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _pause_upgrade_cluster_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade/pause",
            "request_type": request.__class__.__name__,
            "response_type": "PauseUpgradeClusterTaskResponse"
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

    def remove_node(self, request):
        r"""节点移除

        该API用于在指定集群下移除节点。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveNode
        :type request: :class:`huaweicloudsdkcce.v3.RemoveNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.RemoveNodeResponse`
        """
        http_info = self._remove_node_http_info(request)
        return self._call_api(**http_info)

    def remove_node_invoker(self, request):
        http_info = self._remove_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_node_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/operation/remove",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveNodeResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_node(self, request):
        r"""重置节点

        该API用于在指定集群下重置节点。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetNode
        :type request: :class:`huaweicloudsdkcce.v3.ResetNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ResetNodeResponse`
        """
        http_info = self._reset_node_http_info(request)
        return self._call_api(**http_info)

    def reset_node_invoker(self, request):
        http_info = self._reset_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetNodeResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def resize_cluster(self, request):
        r"""变更集群规格

        该API用于变更一个指定集群的规格。
        
        &gt;   - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        &gt;   [- 使用限制请参考[变更集群规格](https://support.huaweicloud.com/usermanual-cce/cce_10_0403.html)。](tag:hws)
        &gt;   [- 使用限制请参考[变更集群规格](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0403.html)](tag:hws_hk)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeCluster
        :type request: :class:`huaweicloudsdkcce.v3.ResizeClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ResizeClusterResponse`
        """
        http_info = self._resize_cluster_http_info(request)
        return self._call_api(**http_info)

    def resize_cluster_invoker(self, request):
        http_info = self._resize_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/resize",
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def retry_upgrade_cluster_task(self, request):
        r"""重试集群升级任务

        重新执行失败的集群升级任务。
        &gt; - 集群升级涉及多维度的组件升级操作，强烈建议统一通过CCE控制台执行交互式升级，降低集群升级过程的业务意外受损风险；
        &gt; - 当前集群升级相关接口受限开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryUpgradeClusterTask
        :type request: :class:`huaweicloudsdkcce.v3.RetryUpgradeClusterTaskRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.RetryUpgradeClusterTaskResponse`
        """
        http_info = self._retry_upgrade_cluster_task_http_info(request)
        return self._call_api(**http_info)

    def retry_upgrade_cluster_task_invoker(self, request):
        http_info = self._retry_upgrade_cluster_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_upgrade_cluster_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryUpgradeClusterTaskResponse"
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

    def revoke_kubernetes_cluster_cert(self, request):
        r"""吊销用户的集群证书

        该API用于吊销指定集群的用户证书
        
        &gt; 吊销操作完成后，此证书申请人之前下载的证书和 kubectl 配置文件无法再用于连接集群。此证书申请人可以重新下载证书或 kubectl 配置文件，并使用新下载的文件连接集群
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokeKubernetesClusterCert
        :type request: :class:`huaweicloudsdkcce.v3.RevokeKubernetesClusterCertRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.RevokeKubernetesClusterCertResponse`
        """
        http_info = self._revoke_kubernetes_cluster_cert_http_info(request)
        return self._call_api(**http_info)

    def revoke_kubernetes_cluster_cert_invoker(self, request):
        http_info = self._revoke_kubernetes_cluster_cert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _revoke_kubernetes_cluster_cert_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/clustercertrevoke",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeKubernetesClusterCertResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def rollback_addon_instance(self, request):
        r"""回滚AddonInstance

        将插件实例回滚到升级前的版本。只有在当前插件实例版本支持回滚到升级前的版本（status.isRollbackable为true），且插件实例状态为running（运行中）、available（可用）、abnormal（不可用）、upgradeFailed（升级失败）、rollbackFailed（回滚失败）时支持回滚。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollbackAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.RollbackAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.RollbackAddonInstanceResponse`
        """
        http_info = self._rollback_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def rollback_addon_instance_invoker(self, request):
        http_info = self._rollback_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rollback_addon_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/addons/{id}/operation/rollback",
            "request_type": request.__class__.__name__,
            "response_type": "RollbackAddonInstanceResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def scale_node_pool(self, request):
        r"""伸缩节点池

        该API用于伸缩指定的节点池
        &gt; 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ScaleNodePool
        :type request: :class:`huaweicloudsdkcce.v3.ScaleNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ScaleNodePoolResponse`
        """
        http_info = self._scale_node_pool_http_info(request)
        return self._call_api(**http_info)

    def scale_node_pool_invoker(self, request):
        http_info = self._scale_node_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _scale_node_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}/operation/scale",
            "request_type": request.__class__.__name__,
            "response_type": "ScaleNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def show_addon_instance(self, request):
        r"""获取AddonInstance详情

        获取插件实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.ShowAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAddonInstanceResponse`
        """
        http_info = self._show_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def show_addon_instance_invoker(self, request):
        http_info = self._show_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_addon_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAddonInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_chart(self, request):
        r"""获取模板

        获取模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowChart
        :type request: :class:`huaweicloudsdkcce.v3.ShowChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowChartResponse`
        """
        http_info = self._show_chart_http_info(request)
        return self._call_api(**http_info)

    def show_chart_invoker(self, request):
        http_info = self._show_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_chart_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/charts/{chart_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

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

    def show_chart_values(self, request):
        r"""获取模板Values

        获取模板Values
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowChartValues
        :type request: :class:`huaweicloudsdkcce.v3.ShowChartValuesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowChartValuesResponse`
        """
        http_info = self._show_chart_values_http_info(request)
        return self._call_api(**http_info)

    def show_chart_values_invoker(self, request):
        http_info = self._show_chart_values_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_chart_values_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/charts/{chart_id}/values",
            "request_type": request.__class__.__name__,
            "response_type": "ShowChartValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

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

    def show_cluster(self, request):
        r"""获取指定的集群

        该API用于获取指定集群的详细信息。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCluster
        :type request: :class:`huaweicloudsdkcce.v3.ShowClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowClusterResponse`
        """
        http_info = self._show_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_invoker(self, request):
        http_info = self._show_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cluster_config(self, request):
        r"""查询集群日志配置信息

        获取集群组件上报的LTS的配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterConfig
        :type request: :class:`huaweicloudsdkcce.v3.ShowClusterConfigRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowClusterConfigResponse`
        """
        http_info = self._show_cluster_config_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_config_invoker(self, request):
        http_info = self._show_cluster_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/cluster/{cluster_id}/log-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterConfigResponse"
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

    def show_cluster_configuration_details(self, request):
        r"""查询指定集群支持配置的参数列表

        该API用于查询CCE服务下指定集群支持配置的参数列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterConfigurationDetails
        :type request: :class:`huaweicloudsdkcce.v3.ShowClusterConfigurationDetailsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowClusterConfigurationDetailsResponse`
        """
        http_info = self._show_cluster_configuration_details_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_configuration_details_invoker(self, request):
        http_info = self._show_cluster_configuration_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_configuration_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/configuration/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterConfigurationDetailsResponse"
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

    def show_cluster_endpoints(self, request):
        r"""获取集群访问的地址

        该API用于通过集群ID获取集群访问的地址，包括PrivateIP(HA集群返回VIP)与PublicIP
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterEndpoints
        :type request: :class:`huaweicloudsdkcce.v3.ShowClusterEndpointsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowClusterEndpointsResponse`
        """
        http_info = self._show_cluster_endpoints_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_endpoints_invoker(self, request):
        http_info = self._show_cluster_endpoints_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_endpoints_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/openapi",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterEndpointsResponse"
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

    def show_cluster_support_configuration(self, request):
        r"""根据集群版本类型等查询集群支持的详细配置项，用于集群创建时指定

        该API用于根据集群版本类型等查询集群支持的详细配置项，用于集群创建时指定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterSupportConfiguration
        :type request: :class:`huaweicloudsdkcce.v3.ShowClusterSupportConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowClusterSupportConfigurationResponse`
        """
        http_info = self._show_cluster_support_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_support_configuration_invoker(self, request):
        http_info = self._show_cluster_support_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_support_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/clusters/configuration/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterSupportConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'cluster_type' in local_var_params:
            query_params.append(('cluster_type', local_var_params['cluster_type']))
        if 'cluster_version' in local_var_params:
            query_params.append(('cluster_version', local_var_params['cluster_version']))
        if 'network_mode' in local_var_params:
            query_params.append(('network_mode', local_var_params['network_mode']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cluster_upgrade_info(self, request):
        r"""获取集群升级相关信息

        获取集群升级相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterUpgradeInfo
        :type request: :class:`huaweicloudsdkcce.v3.ShowClusterUpgradeInfoRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowClusterUpgradeInfoResponse`
        """
        http_info = self._show_cluster_upgrade_info_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_upgrade_info_invoker(self, request):
        http_info = self._show_cluster_upgrade_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_upgrade_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/upgradeinfo",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterUpgradeInfoResponse"
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

    def show_job(self, request):
        r"""获取任务信息

        该API用于获取任务信息。通过某一任务请求下发后返回的jobID来查询指定任务的进度。
        &gt; - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        &gt; - 该接口通常使用场景为：
        &gt;   - 创建、删除集群时，查询相应任务的进度。
        &gt;   - 创建、删除节点时，查询相应任务的进度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkcce.v3.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
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

    def show_node(self, request):
        r"""获取指定的节点

        该API用于通过节点ID获取指定节点的详细信息。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNode
        :type request: :class:`huaweicloudsdkcce.v3.ShowNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowNodeResponse`
        """
        http_info = self._show_node_http_info(request)
        return self._call_api(**http_info)

    def show_node_invoker(self, request):
        http_info = self._show_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_node_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def show_node_pool(self, request):
        r"""获取指定的节点池

        该API用于获取指定节点池的详细信息。
        &gt; 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNodePool
        :type request: :class:`huaweicloudsdkcce.v3.ShowNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowNodePoolResponse`
        """
        http_info = self._show_node_pool_http_info(request)
        return self._call_api(**http_info)

    def show_node_pool_invoker(self, request):
        http_info = self._show_node_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_node_pool_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def show_node_pool_configuration_details(self, request):
        r"""查询指定节点池支持配置的参数列表

        该API用于查询CCE服务下指定节点池支持配置的参数列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNodePoolConfigurationDetails
        :type request: :class:`huaweicloudsdkcce.v3.ShowNodePoolConfigurationDetailsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowNodePoolConfigurationDetailsResponse`
        """
        http_info = self._show_node_pool_configuration_details_http_info(request)
        return self._call_api(**http_info)

    def show_node_pool_configuration_details_invoker(self, request):
        http_info = self._show_node_pool_configuration_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_node_pool_configuration_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}/configuration/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodePoolConfigurationDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def show_node_pool_configurations(self, request):
        r"""查询指定节点池支持配置的参数内容

        该API用于查询指定节点池支持配置的参数内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNodePoolConfigurations
        :type request: :class:`huaweicloudsdkcce.v3.ShowNodePoolConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowNodePoolConfigurationsResponse`
        """
        http_info = self._show_node_pool_configurations_http_info(request)
        return self._call_api(**http_info)

    def show_node_pool_configurations_invoker(self, request):
        http_info = self._show_node_pool_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_node_pool_configurations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodePoolConfigurationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def show_partition(self, request):
        r"""获取分区详情

        获取分区详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPartition
        :type request: :class:`huaweicloudsdkcce.v3.ShowPartitionRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowPartitionResponse`
        """
        http_info = self._show_partition_http_info(request)
        return self._call_api(**http_info)

    def show_partition_invoker(self, request):
        http_info = self._show_partition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_partition_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/partitions/{partition_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartitionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'partition_name' in local_var_params:
            path_params['partition_name'] = local_var_params['partition_name']

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

    def show_pre_check(self, request):
        r"""获取集群升级前检查任务详情

        获取集群升级前检查任务详情，任务ID由调用集群检查API后从响应体中uid字段获取。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPreCheck
        :type request: :class:`huaweicloudsdkcce.v3.ShowPreCheckRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowPreCheckResponse`
        """
        http_info = self._show_pre_check_http_info(request)
        return self._call_api(**http_info)

    def show_pre_check_invoker(self, request):
        http_info = self._show_pre_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pre_check_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/precheck/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPreCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_quotas(self, request):
        r"""查询CCE服务下的资源配额

        该API用于查询CCE服务下的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkcce.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasResponse"
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

    def show_release(self, request):
        r"""获取指定模板实例

        获取指定模板实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRelease
        :type request: :class:`huaweicloudsdkcce.v3.ShowReleaseRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowReleaseResponse`
        """
        http_info = self._show_release_http_info(request)
        return self._call_api(**http_info)

    def show_release_invoker(self, request):
        http_info = self._show_release_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_release_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cce/cam/v3/clusters/{cluster_id}/namespace/{namespace}/releases/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReleaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
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

    def show_release_history(self, request):
        r"""查询指定模板实例历史记录

        查询指定模板实例历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReleaseHistory
        :type request: :class:`huaweicloudsdkcce.v3.ShowReleaseHistoryRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowReleaseHistoryResponse`
        """
        http_info = self._show_release_history_http_info(request)
        return self._call_api(**http_info)

    def show_release_history_invoker(self, request):
        http_info = self._show_release_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_release_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cce/cam/v3/clusters/{cluster_id}/namespace/{namespace}/releases/{name}/history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReleaseHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
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

    def show_upgrade_cluster_task(self, request):
        r"""获取集群升级任务详情

        获取集群升级任务详情，任务ID由调用集群升级API后从响应体中uid字段获取。
        &gt; - 集群升级涉及多维度的组件升级操作，强烈建议统一通过CCE控制台执行交互式升级，降低集群升级过程的业务意外受损风险；
        &gt; - 当前集群升级相关接口受限开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpgradeClusterTask
        :type request: :class:`huaweicloudsdkcce.v3.ShowUpgradeClusterTaskRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowUpgradeClusterTaskResponse`
        """
        http_info = self._show_upgrade_cluster_task_http_info(request)
        return self._call_api(**http_info)

    def show_upgrade_cluster_task_invoker(self, request):
        http_info = self._show_upgrade_cluster_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_upgrade_cluster_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpgradeClusterTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_upgrade_work_flow(self, request):
        r"""获取指定集群升级引导任务详情

        该API用于通过升级引导任务ID获取任务的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpgradeWorkFlow
        :type request: :class:`huaweicloudsdkcce.v3.ShowUpgradeWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowUpgradeWorkFlowResponse`
        """
        http_info = self._show_upgrade_work_flow_http_info(request)
        return self._call_api(**http_info)

    def show_upgrade_work_flow_invoker(self, request):
        http_info = self._show_upgrade_work_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_upgrade_work_flow_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgradeworkflows/{upgrade_workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpgradeWorkFlowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'upgrade_workflow_id' in local_var_params:
            path_params['upgrade_workflow_id'] = local_var_params['upgrade_workflow_id']

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

    def show_user_charts_quotas(self, request):
        r"""获取用户模板配额

        获取用户模板配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserChartsQuotas
        :type request: :class:`huaweicloudsdkcce.v3.ShowUserChartsQuotasRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowUserChartsQuotasResponse`
        """
        http_info = self._show_user_charts_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_user_charts_quotas_invoker(self, request):
        http_info = self._show_user_charts_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_charts_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/charts/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserChartsQuotasResponse"
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

    def sync_node(self, request):
        r"""同步节点

        该API用于同步节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SyncNode
        :type request: :class:`huaweicloudsdkcce.v3.SyncNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.SyncNodeResponse`
        """
        http_info = self._sync_node_http_info(request)
        return self._call_api(**http_info)

    def sync_node_invoker(self, request):
        http_info = self._sync_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _sync_node_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/api/v2/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def unlock_nodepool_node_scale_down(self, request):
        r"""节点关闭缩容保护。

        该API用于节点关闭缩容保护，关闭缩容保护的节点可以通过修改节点池个数的方式被缩容，只允许按需节点关闭缩容保护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnlockNodepoolNodeScaleDown
        :type request: :class:`huaweicloudsdkcce.v3.UnlockNodepoolNodeScaleDownRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UnlockNodepoolNodeScaleDownResponse`
        """
        http_info = self._unlock_nodepool_node_scale_down_http_info(request)
        return self._call_api(**http_info)

    def unlock_nodepool_node_scale_down_invoker(self, request):
        http_info = self._unlock_nodepool_node_scale_down_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unlock_nodepool_node_scale_down_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/unlocknodescaledown",
            "request_type": request.__class__.__name__,
            "response_type": "UnlockNodepoolNodeScaleDownResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_addon_instance(self, request):
        r"""更新AddonInstance

        更新插件实例的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAddonInstanceResponse`
        """
        http_info = self._update_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def update_addon_instance_invoker(self, request):
        http_info = self._update_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_addon_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAddonInstanceResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_chart(self, request):
        r"""更新模板

        更新模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateChart
        :type request: :class:`huaweicloudsdkcce.v3.UpdateChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateChartResponse`
        """
        http_info = self._update_chart_http_info(request)
        return self._call_api(**http_info)

    def update_chart_invoker(self, request):
        http_info = self._update_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_chart_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/charts/{chart_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'parameters' in local_var_params:
            form_params['parameters'] = local_var_params['parameters']
        if 'content' in local_var_params:
            form_params['content'] = local_var_params['content']

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

    def update_cluster(self, request):
        r"""更新指定的集群

        该API用于更新指定的集群。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCluster
        :type request: :class:`huaweicloudsdkcce.v3.UpdateClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateClusterResponse`
        """
        http_info = self._update_cluster_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_invoker(self, request):
        http_info = self._update_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_cluster_eip(self, request):
        r"""绑定、解绑集群公网apiserver地址

        该API用于通过集群ID绑定、解绑集群公网apiserver地址
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterEip
        :type request: :class:`huaweicloudsdkcce.v3.UpdateClusterEipRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateClusterEipResponse`
        """
        http_info = self._update_cluster_eip_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_eip_invoker(self, request):
        http_info = self._update_cluster_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_eip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/mastereip",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterEipResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_cluster_log_config(self, request):
        r"""配置集群日志

        用户可以选择集群管理节点上哪些组件的日志上报LTS
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterLogConfig
        :type request: :class:`huaweicloudsdkcce.v3.UpdateClusterLogConfigRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateClusterLogConfigResponse`
        """
        http_info = self._update_cluster_log_config_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_log_config_invoker(self, request):
        http_info = self._update_cluster_log_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_log_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/projects/{project_id}/cluster/{cluster_id}/log-configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterLogConfigResponse"
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
            ['application/json'])

        auth_settings = []

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
        r"""更新指定的节点

        该API用于更新指定的节点。
        &gt; - 当前仅支持更新metadata下的name字段，即节点的名字。
        &gt; - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNode
        :type request: :class:`huaweicloudsdkcce.v3.UpdateNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateNodeResponse`
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
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
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

    def update_node_pool(self, request):
        r"""更新指定节点池

        该API用于更新指定的节点池。仅支持集群在处于可用、扩容、缩容状态时调用。
        
        
        &gt; - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        &gt; - 当前仅支持更新节点池名称，spec下的initialNodeCount，k8sTags，taints，login，userTags与节点池的扩缩容配置相关字段。若此次更新未设置相关值，默认更新为初始值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNodePool
        :type request: :class:`huaweicloudsdkcce.v3.UpdateNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateNodePoolResponse`
        """
        http_info = self._update_node_pool_http_info(request)
        return self._call_api(**http_info)

    def update_node_pool_invoker(self, request):
        http_info = self._update_node_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_node_pool_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def update_node_pool_configuration(self, request):
        r"""修改指定节点池配置参数的值

        该API用于修改CCE服务下指定节点池配置参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNodePoolConfiguration
        :type request: :class:`huaweicloudsdkcce.v3.UpdateNodePoolConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateNodePoolConfigurationResponse`
        """
        http_info = self._update_node_pool_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_node_pool_configuration_invoker(self, request):
        http_info = self._update_node_pool_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_node_pool_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNodePoolConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def update_partition(self, request):
        r"""更新分区

        更新分区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePartition
        :type request: :class:`huaweicloudsdkcce.v3.UpdatePartitionRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdatePartitionResponse`
        """
        http_info = self._update_partition_http_info(request)
        return self._call_api(**http_info)

    def update_partition_invoker(self, request):
        http_info = self._update_partition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_partition_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/partitions/{partition_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePartitionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'partition_name' in local_var_params:
            path_params['partition_name'] = local_var_params['partition_name']

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

    def update_release(self, request):
        r"""更新指定模板实例

        更新指定模板实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRelease
        :type request: :class:`huaweicloudsdkcce.v3.UpdateReleaseRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateReleaseResponse`
        """
        http_info = self._update_release_http_info(request)
        return self._call_api(**http_info)

    def update_release_invoker(self, request):
        http_info = self._update_release_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_release_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/cce/cam/v3/clusters/{cluster_id}/namespace/{namespace}/releases/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReleaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upgrade_cluster(self, request):
        r"""集群升级

        集群升级。
        &gt; - 集群升级涉及多维度的组件升级操作，强烈建议统一通过CCE控制台执行交互式升级，降低集群升级过程的业务意外受损风险；
        &gt; - 当前集群升级相关接口受限开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeCluster
        :type request: :class:`huaweicloudsdkcce.v3.UpgradeClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeClusterResponse`
        """
        http_info = self._upgrade_cluster_http_info(request)
        return self._call_api(**http_info)

    def upgrade_cluster_invoker(self, request):
        http_info = self._upgrade_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeClusterResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upgrade_node_pool(self, request):
        r"""同步节点池

        该API用于同步节点池中已有节点的配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeNodePool
        :type request: :class:`huaweicloudsdkcce.v3.UpgradeNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeNodePoolResponse`
        """
        http_info = self._upgrade_node_pool_http_info(request)
        return self._call_api(**http_info)

    def upgrade_node_pool_invoker(self, request):
        http_info = self._upgrade_node_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_node_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}/operation/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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

    def upgrade_work_flow_update(self, request):
        r"""更新指定集群升级引导任务状态

        该API用于更新指定集群升级引导任务状态，当前仅适用于取消升级流程
        调用该API时升级流程引导任务状态不能为进行中(running) 已完成(success) 已取消(cancel),升级子任务状态不能为running(进行中) init(已初始化) pause(任务被暂停) queue(队列中)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeWorkFlowUpdate
        :type request: :class:`huaweicloudsdkcce.v3.UpgradeWorkFlowUpdateRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeWorkFlowUpdateResponse`
        """
        http_info = self._upgrade_work_flow_update_http_info(request)
        return self._call_api(**http_info)

    def upgrade_work_flow_update_invoker(self, request):
        http_info = self._upgrade_work_flow_update_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_work_flow_update_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgradeworkflows/{upgrade_workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeWorkFlowUpdateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'upgrade_workflow_id' in local_var_params:
            path_params['upgrade_workflow_id'] = local_var_params['upgrade_workflow_id']

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

    def upload_chart(self, request):
        r"""上传模板

        上传模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadChart
        :type request: :class:`huaweicloudsdkcce.v3.UploadChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UploadChartResponse`
        """
        http_info = self._upload_chart_http_info(request)
        return self._call_api(**http_info)

    def upload_chart_invoker(self, request):
        http_info = self._upload_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_chart_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/charts",
            "request_type": request.__class__.__name__,
            "response_type": "UploadChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'parameters' in local_var_params:
            form_params['parameters'] = local_var_params['parameters']
        if 'content' in local_var_params:
            form_params['content'] = local_var_params['content']

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

    def show_version(self, request):
        r"""查询API版本信息列表

        该API用于查询CCE服务当前支持的API版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVersion
        :type request: :class:`huaweicloudsdkcce.v3.ShowVersionRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowVersionResponse`
        """
        http_info = self._show_version_http_info(request)
        return self._call_api(**http_info)

    def show_version_invoker(self, request):
        http_info = self._show_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionResponse"
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

    def batch_create_autopilot_cluster_tags(self, request):
        r"""批量添加指定集群的资源标签

        该API用于批量添加指定集群的资源标签。
        &gt; - 每个集群支持最多20个资源标签。
        &gt; - 此接口为幂等接口：创建时，如果创建的标签已经存在（key/value均相同视为重复），默认处理成功；key相同，value不同时会覆盖原有标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateAutopilotClusterTags
        :type request: :class:`huaweicloudsdkcce.v3.BatchCreateAutopilotClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.BatchCreateAutopilotClusterTagsResponse`
        """
        http_info = self._batch_create_autopilot_cluster_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_autopilot_cluster_tags_invoker(self, request):
        http_info = self._batch_create_autopilot_cluster_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_autopilot_cluster_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateAutopilotClusterTagsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_autopilot_cluster_tags(self, request):
        r"""批量删除指定集群的资源标签

        该API用于批量删除指定集群的资源标签。
        &gt; - 此接口为幂等接口：删除时，如果删除的标签key不存在，默认处理成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAutopilotClusterTags
        :type request: :class:`huaweicloudsdkcce.v3.BatchDeleteAutopilotClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.BatchDeleteAutopilotClusterTagsResponse`
        """
        http_info = self._batch_delete_autopilot_cluster_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_autopilot_cluster_tags_invoker(self, request):
        http_info = self._batch_delete_autopilot_cluster_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_autopilot_cluster_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAutopilotClusterTagsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_autopilot_addon_instance(self, request):
        r"""创建AddonInstance

        根据提供的插件模板，安装插件实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotAddonInstanceResponse`
        """
        http_info = self._create_autopilot_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_addon_instance_invoker(self, request):
        http_info = self._create_autopilot_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_addon_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/addons",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotAddonInstanceResponse"
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

    def create_autopilot_cluster(self, request):
        r"""创建集群

        该API用于创建一个空集群（即只有控制节点Master，没有工作节点Node）。
        
        
        &gt;   - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        &gt;   - 调用该接口创建集群时，默认不安装ICAgent，若需安装ICAgent，可在请求Body参数的annotations中加入\&quot;cluster.install.addons.external/install\&quot;:\&quot;[{\&quot;addonTemplateName\&quot;:\&quot;icagent\&quot;}]\&quot;的集群注解，将在创建集群时自动安装ICAgent。ICAgent是应用性能管理APM的采集代理，运行在应用所在的服务器上，用于实时采集探针所获取的数据，安装ICAgent是使用应用性能管理APM的前提。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotCluster
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotClusterResponse`
        """
        http_info = self._create_autopilot_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_cluster_invoker(self, request):
        http_info = self._create_autopilot_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotClusterResponse"
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

    def create_autopilot_cluster_master_snapshot(self, request):
        r"""集群备份

        集群备份
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotClusterMasterSnapshot
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotClusterMasterSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotClusterMasterSnapshotResponse`
        """
        http_info = self._create_autopilot_cluster_master_snapshot_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_cluster_master_snapshot_invoker(self, request):
        http_info = self._create_autopilot_cluster_master_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_cluster_master_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3.1/projects/{project_id}/clusters/{cluster_id}/operation/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotClusterMasterSnapshotResponse"
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

    def create_autopilot_kubernetes_cluster_cert(self, request):
        r"""获取集群证书

        该API用于获取指定集群的证书信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotKubernetesClusterCert
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotKubernetesClusterCertRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotKubernetesClusterCertResponse`
        """
        http_info = self._create_autopilot_kubernetes_cluster_cert_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_kubernetes_cluster_cert_invoker(self, request):
        http_info = self._create_autopilot_kubernetes_cluster_cert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_kubernetes_cluster_cert_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/clustercert",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotKubernetesClusterCertResponse"
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

        response_headers = ["Port-ID", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_autopilot_maintenance_window(self, request):
        r"""创建集群维护窗口

        该API用于创建集群维护窗口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotMaintenanceWindow
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotMaintenanceWindowRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotMaintenanceWindowResponse`
        """
        http_info = self._create_autopilot_maintenance_window_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_maintenance_window_invoker(self, request):
        http_info = self._create_autopilot_maintenance_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_maintenance_window_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/maintenancewindows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotMaintenanceWindowResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_autopilot_post_check(self, request):
        r"""集群升级后确认

        集群升级后确认，该接口建议配合Console使用，主要用于升级步骤完成后，客户确认集群状态和业务正常后做反馈。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotPostCheck
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotPostCheckRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotPostCheckResponse`
        """
        http_info = self._create_autopilot_post_check_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_post_check_invoker(self, request):
        http_info = self._create_autopilot_post_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_post_check_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/postcheck",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotPostCheckResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_autopilot_pre_check(self, request):
        r"""集群升级前检查

        集群升级前检查
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotPreCheck
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotPreCheckRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotPreCheckResponse`
        """
        http_info = self._create_autopilot_pre_check_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_pre_check_invoker(self, request):
        http_info = self._create_autopilot_pre_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_pre_check_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/precheck",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotPreCheckResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_autopilot_release(self, request):
        r"""创建模板实例

        创建模板实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotRelease
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotReleaseRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotReleaseResponse`
        """
        http_info = self._create_autopilot_release_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_release_invoker(self, request):
        http_info = self._create_autopilot_release_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_release_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/cam/v3/clusters/{cluster_id}/releases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotReleaseResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_autopilot_upgrade_work_flow(self, request):
        r"""开启集群升级流程引导任务

        该API用于创建一个集群升级流程引导任务。请在调用本接口完成引导任务创建之后，通过集群升级前检查开始检查任务。
        升级流程任务用于控制集群升级任务的执行流程，执行流程为 升级前检查 &#x3D;&gt; 集群升级 &#x3D;&gt; 升级后检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutopilotUpgradeWorkFlow
        :type request: :class:`huaweicloudsdkcce.v3.CreateAutopilotUpgradeWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAutopilotUpgradeWorkFlowResponse`
        """
        http_info = self._create_autopilot_upgrade_work_flow_http_info(request)
        return self._call_api(**http_info)

    def create_autopilot_upgrade_work_flow_invoker(self, request):
        http_info = self._create_autopilot_upgrade_work_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_autopilot_upgrade_work_flow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgradeworkflows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutopilotUpgradeWorkFlowResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_autopilot_addon_instance(self, request):
        r"""删除AddonInstance

        删除插件实例的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAutopilotAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.DeleteAutopilotAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteAutopilotAddonInstanceResponse`
        """
        http_info = self._delete_autopilot_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_autopilot_addon_instance_invoker(self, request):
        http_info = self._delete_autopilot_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_autopilot_addon_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autopilot/v3/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAutopilotAddonInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_autopilot_chart(self, request):
        r"""删除模板

        删除模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAutopilotChart
        :type request: :class:`huaweicloudsdkcce.v3.DeleteAutopilotChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteAutopilotChartResponse`
        """
        http_info = self._delete_autopilot_chart_http_info(request)
        return self._call_api(**http_info)

    def delete_autopilot_chart_invoker(self, request):
        http_info = self._delete_autopilot_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_autopilot_chart_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autopilot/v2/charts/{chart_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAutopilotChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

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

    def delete_autopilot_cluster(self, request):
        r"""删除集群

        该API用于删除一个指定的集群。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAutopilotCluster
        :type request: :class:`huaweicloudsdkcce.v3.DeleteAutopilotClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteAutopilotClusterResponse`
        """
        http_info = self._delete_autopilot_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_autopilot_cluster_invoker(self, request):
        http_info = self._delete_autopilot_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_autopilot_cluster_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAutopilotClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'delete_efs' in local_var_params:
            query_params.append(('delete_efs', local_var_params['delete_efs']))
        if 'delete_eni' in local_var_params:
            query_params.append(('delete_eni', local_var_params['delete_eni']))
        if 'delete_net' in local_var_params:
            query_params.append(('delete_net', local_var_params['delete_net']))
        if 'delete_obs' in local_var_params:
            query_params.append(('delete_obs', local_var_params['delete_obs']))
        if 'delete_sfs30' in local_var_params:
            query_params.append(('delete_sfs30', local_var_params['delete_sfs30']))
        if 'lts_reclaim_policy' in local_var_params:
            query_params.append(('lts_reclaim_policy', local_var_params['lts_reclaim_policy']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_autopilot_maintenance_window(self, request):
        r"""删除集群维护窗口

        该API用于删除集群维护窗口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAutopilotMaintenanceWindow
        :type request: :class:`huaweicloudsdkcce.v3.DeleteAutopilotMaintenanceWindowRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteAutopilotMaintenanceWindowResponse`
        """
        http_info = self._delete_autopilot_maintenance_window_http_info(request)
        return self._call_api(**http_info)

    def delete_autopilot_maintenance_window_invoker(self, request):
        http_info = self._delete_autopilot_maintenance_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_autopilot_maintenance_window_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/maintenancewindows",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAutopilotMaintenanceWindowResponse"
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

    def delete_autopilot_release(self, request):
        r"""删除指定模板实例

        删除指定模板实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAutopilotRelease
        :type request: :class:`huaweicloudsdkcce.v3.DeleteAutopilotReleaseRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteAutopilotReleaseResponse`
        """
        http_info = self._delete_autopilot_release_http_info(request)
        return self._call_api(**http_info)

    def delete_autopilot_release_invoker(self, request):
        http_info = self._delete_autopilot_release_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_autopilot_release_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autopilot/cam/v3/clusters/{cluster_id}/namespace/{namespace}/releases/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAutopilotReleaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
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

    def download_autopilot_chart(self, request):
        r"""下载模板

        下载模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAutopilotChart
        :type request: :class:`huaweicloudsdkcce.v3.DownloadAutopilotChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DownloadAutopilotChartResponse`
        """
        http_info = self._download_autopilot_chart_http_info(request)
        return self._call_api(**http_info)

    def download_autopilot_chart_invoker(self, request):
        http_info = self._download_autopilot_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_autopilot_chart_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v2/charts/{chart_id}/archive",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAutopilotChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

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

    def list_autopilot_addon_instances(self, request):
        r"""获取AddonInstance列表

        获取集群所有已安装插件实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotAddonInstances
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotAddonInstancesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotAddonInstancesResponse`
        """
        http_info = self._list_autopilot_addon_instances_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_addon_instances_invoker(self, request):
        http_info = self._list_autopilot_addon_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_addon_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/addons",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotAddonInstancesResponse"
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

    def list_autopilot_addon_templates(self, request):
        r"""查询AddonTemplates列表

        插件模板查询接口，查询插件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotAddonTemplates
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotAddonTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotAddonTemplatesResponse`
        """
        http_info = self._list_autopilot_addon_templates_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_addon_templates_invoker(self, request):
        http_info = self._list_autopilot_addon_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_addon_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/addontemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotAddonTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'addon_template_name' in local_var_params:
            query_params.append(('addon_template_name', local_var_params['addon_template_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_autopilot_charts(self, request):
        r"""获取模板列表

        获取模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotCharts
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotChartsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotChartsResponse`
        """
        http_info = self._list_autopilot_charts_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_charts_invoker(self, request):
        http_info = self._list_autopilot_charts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_charts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v2/charts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotChartsResponse"
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

    def list_autopilot_cluster_master_snapshot_tasks(self, request):
        r"""获取集群备份任务详情列表

        获取集群备份任务详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotClusterMasterSnapshotTasks
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotClusterMasterSnapshotTasksRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotClusterMasterSnapshotTasksResponse`
        """
        http_info = self._list_autopilot_cluster_master_snapshot_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_cluster_master_snapshot_tasks_invoker(self, request):
        http_info = self._list_autopilot_cluster_master_snapshot_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_cluster_master_snapshot_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3.1/projects/{project_id}/clusters/{cluster_id}/operation/snapshot/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotClusterMasterSnapshotTasksResponse"
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

    def list_autopilot_cluster_upgrade_feature_gates(self, request):
        r"""获取集群升级特性开关配置

        获取集群升级特性开关配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotClusterUpgradeFeatureGates
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotClusterUpgradeFeatureGatesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotClusterUpgradeFeatureGatesResponse`
        """
        http_info = self._list_autopilot_cluster_upgrade_feature_gates_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_cluster_upgrade_feature_gates_invoker(self, request):
        http_info = self._list_autopilot_cluster_upgrade_feature_gates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_cluster_upgrade_feature_gates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/clusterupgradefeaturegates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotClusterUpgradeFeatureGatesResponse"
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

    def list_autopilot_cluster_upgrade_paths(self, request):
        r"""获取集群升级路径

        获取集群升级路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotClusterUpgradePaths
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotClusterUpgradePathsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotClusterUpgradePathsResponse`
        """
        http_info = self._list_autopilot_cluster_upgrade_paths_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_cluster_upgrade_paths_invoker(self, request):
        http_info = self._list_autopilot_cluster_upgrade_paths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_cluster_upgrade_paths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/clusterupgradepaths",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotClusterUpgradePathsResponse"
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

    def list_autopilot_clusters(self, request):
        r"""获取指定项目下的集群

        该API用于获取指定项目下所有集群的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotClusters
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotClustersRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotClustersResponse`
        """
        http_info = self._list_autopilot_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_clusters_invoker(self, request):
        http_info = self._list_autopilot_clusters_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_clusters_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_autopilot_pre_check_tasks(self, request):
        r"""获取集群升级前检查任务详情列表

        获取集群升级前检查任务详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotPreCheckTasks
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotPreCheckTasksRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotPreCheckTasksResponse`
        """
        http_info = self._list_autopilot_pre_check_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_pre_check_tasks_invoker(self, request):
        http_info = self._list_autopilot_pre_check_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_pre_check_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/precheck/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotPreCheckTasksResponse"
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

    def list_autopilot_releases(self, request):
        r"""获取模板实例列表

        获取模板实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotReleases
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotReleasesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotReleasesResponse`
        """
        http_info = self._list_autopilot_releases_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_releases_invoker(self, request):
        http_info = self._list_autopilot_releases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_releases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/cam/v3/clusters/{cluster_id}/releases",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotReleasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'chart_id' in local_var_params:
            query_params.append(('chart_id', local_var_params['chart_id']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_autopilot_upgrade_cluster_tasks(self, request):
        r"""获取集群升级任务详情列表

        获取集群升级任务详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotUpgradeClusterTasks
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotUpgradeClusterTasksRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotUpgradeClusterTasksResponse`
        """
        http_info = self._list_autopilot_upgrade_cluster_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_upgrade_cluster_tasks_invoker(self, request):
        http_info = self._list_autopilot_upgrade_cluster_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_upgrade_cluster_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotUpgradeClusterTasksResponse"
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

    def list_autopilot_upgrade_plans(self, request):
        r"""获取自动升级计划

        该API用于获取集群自动升级计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotUpgradePlans
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotUpgradePlansRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotUpgradePlansResponse`
        """
        http_info = self._list_autopilot_upgrade_plans_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_upgrade_plans_invoker(self, request):
        http_info = self._list_autopilot_upgrade_plans_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_upgrade_plans_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/upgradeplans",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotUpgradePlansResponse"
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

    def list_autopilot_upgrade_work_flows(self, request):
        r"""获取UpgradeWorkFlows列表

        获取历史集群升级引导任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutopilotUpgradeWorkFlows
        :type request: :class:`huaweicloudsdkcce.v3.ListAutopilotUpgradeWorkFlowsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAutopilotUpgradeWorkFlowsResponse`
        """
        http_info = self._list_autopilot_upgrade_work_flows_http_info(request)
        return self._call_api(**http_info)

    def list_autopilot_upgrade_work_flows_invoker(self, request):
        http_info = self._list_autopilot_upgrade_work_flows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_autopilot_upgrade_work_flows_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgradeworkflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutopilotUpgradeWorkFlowsResponse"
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

    def retry_autopilot_upgrade_cluster_task(self, request):
        r"""重试集群升级任务

        重新执行失败的集群升级任务。
        &gt; - 集群升级涉及多维度的组件升级操作，强烈建议统一通过CCE控制台执行交互式升级，降低集群升级过程的业务意外受损风险；
        &gt; - 当前集群升级相关接口受限开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryAutopilotUpgradeClusterTask
        :type request: :class:`huaweicloudsdkcce.v3.RetryAutopilotUpgradeClusterTaskRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.RetryAutopilotUpgradeClusterTaskResponse`
        """
        http_info = self._retry_autopilot_upgrade_cluster_task_http_info(request)
        return self._call_api(**http_info)

    def retry_autopilot_upgrade_cluster_task_invoker(self, request):
        http_info = self._retry_autopilot_upgrade_cluster_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_autopilot_upgrade_cluster_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryAutopilotUpgradeClusterTaskResponse"
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

    def rollback_autopilot_addon_instance(self, request):
        r"""回滚AddonInstance

        将插件实例回滚到升级前的版本。只有在当前插件实例版本支持回滚到升级前的版本（status.isRollbackable为true），且插件实例状态为running（运行中）、available（可用）、abnormal（不可用）、upgradeFailed（升级失败）、rollbackFailed（回滚失败）时支持回滚。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollbackAutopilotAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.RollbackAutopilotAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.RollbackAutopilotAddonInstanceResponse`
        """
        http_info = self._rollback_autopilot_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def rollback_autopilot_addon_instance_invoker(self, request):
        http_info = self._rollback_autopilot_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rollback_autopilot_addon_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/addons/{id}/operation/rollback",
            "request_type": request.__class__.__name__,
            "response_type": "RollbackAutopilotAddonInstanceResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_autopilot_addon_instance(self, request):
        r"""获取AddonInstance详情

        获取插件实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotAddonInstanceResponse`
        """
        http_info = self._show_autopilot_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_addon_instance_invoker(self, request):
        http_info = self._show_autopilot_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_addon_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotAddonInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_autopilot_chart(self, request):
        r"""获取模板

        获取模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotChart
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotChartResponse`
        """
        http_info = self._show_autopilot_chart_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_chart_invoker(self, request):
        http_info = self._show_autopilot_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_chart_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v2/charts/{chart_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

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

    def show_autopilot_chart_values(self, request):
        r"""获取模板Values

        获取模板Values
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotChartValues
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotChartValuesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotChartValuesResponse`
        """
        http_info = self._show_autopilot_chart_values_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_chart_values_invoker(self, request):
        http_info = self._show_autopilot_chart_values_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_chart_values_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v2/charts/{chart_id}/values",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotChartValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

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

    def show_autopilot_cluster(self, request):
        r"""获取指定的集群

        该API用于获取指定集群的详细信息。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotCluster
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotClusterResponse`
        """
        http_info = self._show_autopilot_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_cluster_invoker(self, request):
        http_info = self._show_autopilot_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_cluster_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_autopilot_cluster_endpoints(self, request):
        r"""获取集群访问的地址

        该API用于通过集群ID获取集群访问的地址，包括PrivateIP(HA集群返回VIP)与PublicIP
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotClusterEndpoints
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotClusterEndpointsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotClusterEndpointsResponse`
        """
        http_info = self._show_autopilot_cluster_endpoints_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_cluster_endpoints_invoker(self, request):
        http_info = self._show_autopilot_cluster_endpoints_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_cluster_endpoints_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/openapi",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotClusterEndpointsResponse"
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

    def show_autopilot_cluster_upgrade_info(self, request):
        r"""获取集群升级相关信息

        获取集群升级相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotClusterUpgradeInfo
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotClusterUpgradeInfoRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotClusterUpgradeInfoResponse`
        """
        http_info = self._show_autopilot_cluster_upgrade_info_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_cluster_upgrade_info_invoker(self, request):
        http_info = self._show_autopilot_cluster_upgrade_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_cluster_upgrade_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/upgradeinfo",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotClusterUpgradeInfoResponse"
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

    def show_autopilot_job(self, request):
        r"""获取任务信息

        该API用于获取任务信息。通过某一任务请求下发后返回的jobID来查询指定任务的进度。
        &gt; - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        &gt; - 该接口通常使用场景为：
        &gt;   - 创建、删除集群时，查询相应任务的进度。
        &gt;   - 创建、删除节点时，查询相应任务的进度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotJob
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotJobRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotJobResponse`
        """
        http_info = self._show_autopilot_job_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_job_invoker(self, request):
        http_info = self._show_autopilot_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotJobResponse"
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

    def show_autopilot_maintenance_window(self, request):
        r"""获取集群维护窗口

        该API用于获取集群维护窗口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotMaintenanceWindow
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotMaintenanceWindowRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotMaintenanceWindowResponse`
        """
        http_info = self._show_autopilot_maintenance_window_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_maintenance_window_invoker(self, request):
        http_info = self._show_autopilot_maintenance_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_maintenance_window_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/maintenancewindows",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotMaintenanceWindowResponse"
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

    def show_autopilot_pre_check(self, request):
        r"""获取集群升级前检查任务详情

        获取集群升级前检查任务详情，任务ID由调用集群检查API后从响应体中uid字段获取。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotPreCheck
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotPreCheckRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotPreCheckResponse`
        """
        http_info = self._show_autopilot_pre_check_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_pre_check_invoker(self, request):
        http_info = self._show_autopilot_pre_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_pre_check_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/precheck/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotPreCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_autopilot_quotas(self, request):
        r"""查询CCE服务下的资源配额

        该API用于查询CCE服务下的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotQuotas
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotQuotasRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotQuotasResponse`
        """
        http_info = self._show_autopilot_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_quotas_invoker(self, request):
        http_info = self._show_autopilot_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotQuotasResponse"
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

    def show_autopilot_release(self, request):
        r"""获取指定模板实例

        获取指定模板实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotRelease
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotReleaseRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotReleaseResponse`
        """
        http_info = self._show_autopilot_release_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_release_invoker(self, request):
        http_info = self._show_autopilot_release_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_release_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/cam/v3/clusters/{cluster_id}/namespace/{namespace}/releases/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotReleaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
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

    def show_autopilot_release_history(self, request):
        r"""查询指定模板实例历史记录

        查询指定模板实例历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotReleaseHistory
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotReleaseHistoryRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotReleaseHistoryResponse`
        """
        http_info = self._show_autopilot_release_history_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_release_history_invoker(self, request):
        http_info = self._show_autopilot_release_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_release_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/cam/v3/clusters/{cluster_id}/namespace/{namespace}/releases/{name}/history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotReleaseHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
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

    def show_autopilot_upgrade_cluster_task(self, request):
        r"""获取集群升级任务详情

        获取集群升级任务详情，任务ID由调用集群升级API后从响应体中uid字段获取。
        &gt; - 集群升级涉及多维度的组件升级操作，强烈建议统一通过CCE控制台执行交互式升级，降低集群升级过程的业务意外受损风险；
        &gt; - 当前集群升级相关接口受限开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotUpgradeClusterTask
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotUpgradeClusterTaskRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotUpgradeClusterTaskResponse`
        """
        http_info = self._show_autopilot_upgrade_cluster_task_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_upgrade_cluster_task_invoker(self, request):
        http_info = self._show_autopilot_upgrade_cluster_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_upgrade_cluster_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotUpgradeClusterTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_autopilot_upgrade_work_flow(self, request):
        r"""获取指定集群升级引导任务详情

        该API用于通过升级引导任务ID获取任务的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotUpgradeWorkFlow
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotUpgradeWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotUpgradeWorkFlowResponse`
        """
        http_info = self._show_autopilot_upgrade_work_flow_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_upgrade_work_flow_invoker(self, request):
        http_info = self._show_autopilot_upgrade_work_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_upgrade_work_flow_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgradeworkflows/{upgrade_workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotUpgradeWorkFlowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'upgrade_workflow_id' in local_var_params:
            path_params['upgrade_workflow_id'] = local_var_params['upgrade_workflow_id']

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

    def show_autopilot_user_charts_quotas(self, request):
        r"""获取用户模板配额

        获取用户模板配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutopilotUserChartsQuotas
        :type request: :class:`huaweicloudsdkcce.v3.ShowAutopilotUserChartsQuotasRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAutopilotUserChartsQuotasResponse`
        """
        http_info = self._show_autopilot_user_charts_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_autopilot_user_charts_quotas_invoker(self, request):
        http_info = self._show_autopilot_user_charts_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_autopilot_user_charts_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autopilot/v2/charts/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutopilotUserChartsQuotasResponse"
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

    def update_autopilot_addon_instance(self, request):
        r"""更新AddonInstance

        更新插件实例的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutopilotAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAutopilotAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAutopilotAddonInstanceResponse`
        """
        http_info = self._update_autopilot_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def update_autopilot_addon_instance_invoker(self, request):
        http_info = self._update_autopilot_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_autopilot_addon_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autopilot/v3/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutopilotAddonInstanceResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_autopilot_chart(self, request):
        r"""更新模板

        更新模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutopilotChart
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAutopilotChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAutopilotChartResponse`
        """
        http_info = self._update_autopilot_chart_http_info(request)
        return self._call_api(**http_info)

    def update_autopilot_chart_invoker(self, request):
        http_info = self._update_autopilot_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_autopilot_chart_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autopilot/v2/charts/{chart_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutopilotChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chart_id' in local_var_params:
            path_params['chart_id'] = local_var_params['chart_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'parameters' in local_var_params:
            form_params['parameters'] = local_var_params['parameters']
        if 'content' in local_var_params:
            form_params['content'] = local_var_params['content']

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

    def update_autopilot_cluster(self, request):
        r"""更新指定的集群

        该API用于更新指定的集群。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutopilotCluster
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAutopilotClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAutopilotClusterResponse`
        """
        http_info = self._update_autopilot_cluster_http_info(request)
        return self._call_api(**http_info)

    def update_autopilot_cluster_invoker(self, request):
        http_info = self._update_autopilot_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_autopilot_cluster_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutopilotClusterResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_autopilot_cluster_eip(self, request):
        r"""绑定、解绑集群公网apiserver地址

        该API用于通过集群ID绑定、解绑集群公网apiserver地址
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutopilotClusterEip
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAutopilotClusterEipRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAutopilotClusterEipResponse`
        """
        http_info = self._update_autopilot_cluster_eip_http_info(request)
        return self._call_api(**http_info)

    def update_autopilot_cluster_eip_invoker(self, request):
        http_info = self._update_autopilot_cluster_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_autopilot_cluster_eip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/mastereip",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutopilotClusterEipResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_autopilot_maintenance_window(self, request):
        r"""更新集群维护窗口

        该API用于更新集群维护窗口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutopilotMaintenanceWindow
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAutopilotMaintenanceWindowRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAutopilotMaintenanceWindowResponse`
        """
        http_info = self._update_autopilot_maintenance_window_http_info(request)
        return self._call_api(**http_info)

    def update_autopilot_maintenance_window_invoker(self, request):
        http_info = self._update_autopilot_maintenance_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_autopilot_maintenance_window_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/maintenancewindows",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutopilotMaintenanceWindowResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_autopilot_release(self, request):
        r"""更新指定模板实例

        更新指定模板实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutopilotRelease
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAutopilotReleaseRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAutopilotReleaseResponse`
        """
        http_info = self._update_autopilot_release_http_info(request)
        return self._call_api(**http_info)

    def update_autopilot_release_invoker(self, request):
        http_info = self._update_autopilot_release_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_autopilot_release_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autopilot/cam/v3/clusters/{cluster_id}/namespace/{namespace}/releases/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutopilotReleaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_autopilot_upgrade_plan(self, request):
        r"""延期自动升级计划

        该API用于延期集群自动升级计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutopilotUpgradePlan
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAutopilotUpgradePlanRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAutopilotUpgradePlanResponse`
        """
        http_info = self._update_autopilot_upgrade_plan_http_info(request)
        return self._call_api(**http_info)

    def update_autopilot_upgrade_plan_invoker(self, request):
        http_info = self._update_autopilot_upgrade_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_autopilot_upgrade_plan_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/upgradeplans/{upgrade_plan_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutopilotUpgradePlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'upgrade_plan_id' in local_var_params:
            path_params['upgrade_plan_id'] = local_var_params['upgrade_plan_id']

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

    def upgrade_autopilot_cluster(self, request):
        r"""集群升级

        集群升级。
        &gt; - 集群升级涉及多维度的组件升级操作，强烈建议统一通过CCE控制台执行交互式升级，降低集群升级过程的业务意外受损风险；
        &gt; - 当前集群升级相关接口受限开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeAutopilotCluster
        :type request: :class:`huaweicloudsdkcce.v3.UpgradeAutopilotClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeAutopilotClusterResponse`
        """
        http_info = self._upgrade_autopilot_cluster_http_info(request)
        return self._call_api(**http_info)

    def upgrade_autopilot_cluster_invoker(self, request):
        http_info = self._upgrade_autopilot_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_autopilot_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeAutopilotClusterResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upgrade_autopilot_work_flow_update(self, request):
        r"""更新指定集群升级引导任务状态

        该API用于更新指定集群升级引导任务状态，当前仅适用于取消升级流程
        调用该API时升级流程引导任务状态不能为进行中(running) 已完成(success) 已取消(cancel),升级子任务状态不能为running(进行中) init(已初始化) pause(任务被暂停) queue(队列中)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeAutopilotWorkFlowUpdate
        :type request: :class:`huaweicloudsdkcce.v3.UpgradeAutopilotWorkFlowUpdateRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeAutopilotWorkFlowUpdateResponse`
        """
        http_info = self._upgrade_autopilot_work_flow_update_http_info(request)
        return self._call_api(**http_info)

    def upgrade_autopilot_work_flow_update_invoker(self, request):
        http_info = self._upgrade_autopilot_work_flow_update_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_autopilot_work_flow_update_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/autopilot/v3/projects/{project_id}/clusters/{cluster_id}/operation/upgradeworkflows/{upgrade_workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeAutopilotWorkFlowUpdateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'upgrade_workflow_id' in local_var_params:
            path_params['upgrade_workflow_id'] = local_var_params['upgrade_workflow_id']

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

    def upload_autopilot_chart(self, request):
        r"""上传模板

        上传模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadAutopilotChart
        :type request: :class:`huaweicloudsdkcce.v3.UploadAutopilotChartRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UploadAutopilotChartResponse`
        """
        http_info = self._upload_autopilot_chart_http_info(request)
        return self._call_api(**http_info)

    def upload_autopilot_chart_invoker(self, request):
        http_info = self._upload_autopilot_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_autopilot_chart_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autopilot/v2/charts",
            "request_type": request.__class__.__name__,
            "response_type": "UploadAutopilotChartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'parameters' in local_var_params:
            form_params['parameters'] = local_var_params['parameters']
        if 'content' in local_var_params:
            form_params['content'] = local_var_params['content']

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

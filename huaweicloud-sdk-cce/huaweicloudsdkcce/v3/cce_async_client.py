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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcce'")


class CceAsyncClient(Client):
    def __init__(self):
        super(CceAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcce.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CceAsyncClient":
                raise TypeError("client type error, support client type is CceAsyncClient")
            client_builder = ClientBuilder(clazz)

        
        try:
            from .cce_exception_handler import CceExceptionHandler
            client_builder.with_exception_handler(CceExceptionHandler())
        except (ImportError, AttributeError):
            warnings.warn("failed to import 'CceExceptionHandler', please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcce'")

        return client_builder

    def add_node_async(self, request):
        """纳管节点

        该API用于在指定集群下纳管节点。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddNode
        :type request: :class:`huaweicloudsdkcce.v3.AddNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.AddNodeResponse`
        """
        http_info = self._add_node_http_info(request)
        return self._call_api(**http_info)

    def add_node_async_invoker(self, request):
        http_info = self._add_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_node_http_info(self, request):
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

    def awake_cluster_async(self, request):
        """集群唤醒

        集群唤醒用于唤醒已休眠的集群，唤醒后，将继续收取控制节点资源费用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AwakeCluster
        :type request: :class:`huaweicloudsdkcce.v3.AwakeClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.AwakeClusterResponse`
        """
        http_info = self._awake_cluster_http_info(request)
        return self._call_api(**http_info)

    def awake_cluster_async_invoker(self, request):
        http_info = self._awake_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _awake_cluster_http_info(self, request):
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

    def batch_create_cluster_tags_async(self, request):
        """批量添加指定集群的资源标签

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

    def batch_create_cluster_tags_async_invoker(self, request):
        http_info = self._batch_create_cluster_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_cluster_tags_http_info(self, request):
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

    def batch_delete_cluster_tags_async(self, request):
        """批量删除指定集群的资源标签

        该API用于批量删除指定集群的资源标签。
        &gt; - 此接口为幂等接口：删除时，如果删除的标签key不存在，默认处理成功。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteClusterTags
        :type request: :class:`huaweicloudsdkcce.v3.BatchDeleteClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.BatchDeleteClusterTagsResponse`
        """
        http_info = self._batch_delete_cluster_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_cluster_tags_async_invoker(self, request):
        http_info = self._batch_delete_cluster_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_cluster_tags_http_info(self, request):
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

    def continue_upgrade_cluster_task_async(self, request):
        """继续执行集群升级任务

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

    def continue_upgrade_cluster_task_async_invoker(self, request):
        http_info = self._continue_upgrade_cluster_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _continue_upgrade_cluster_task_http_info(self, request):
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

    def create_addon_instance_async(self, request):
        """创建AddonInstance

        根据提供的插件模板，安装插件实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.CreateAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateAddonInstanceResponse`
        """
        http_info = self._create_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def create_addon_instance_async_invoker(self, request):
        http_info = self._create_addon_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_addon_instance_http_info(self, request):
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

    def create_cloud_persistent_volume_claims_async(self, request):
        """创建PVC（待废弃）

        该API用于在指定的Namespace下通过云存储服务中的云存储（EVS、SFS、OBS）去创建PVC（PersistentVolumeClaim）。该API待废弃，请使用Kubernetes PVC相关接口。
        
        
        &gt;存储管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。如果使用https://Endpoint/uri，则必须指定请求header中的X-Cluster-ID参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCloudPersistentVolumeClaims
        :type request: :class:`huaweicloudsdkcce.v3.CreateCloudPersistentVolumeClaimsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateCloudPersistentVolumeClaimsResponse`
        """
        http_info = self._create_cloud_persistent_volume_claims_http_info(request)
        return self._call_api(**http_info)

    def create_cloud_persistent_volume_claims_async_invoker(self, request):
        http_info = self._create_cloud_persistent_volume_claims_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cloud_persistent_volume_claims_http_info(self, request):
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

    def create_cluster_async(self, request):
        """创建集群

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

    def create_cluster_async_invoker(self, request):
        http_info = self._create_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cluster_http_info(self, request):
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

    def create_kubernetes_cluster_cert_async(self, request):
        """获取集群证书

        该API用于获取指定集群的证书信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKubernetesClusterCert
        :type request: :class:`huaweicloudsdkcce.v3.CreateKubernetesClusterCertRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.CreateKubernetesClusterCertResponse`
        """
        http_info = self._create_kubernetes_cluster_cert_http_info(request)
        return self._call_api(**http_info)

    def create_kubernetes_cluster_cert_async_invoker(self, request):
        http_info = self._create_kubernetes_cluster_cert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_kubernetes_cluster_cert_http_info(self, request):
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

    def create_node_async(self, request):
        """创建节点

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

    def create_node_async_invoker(self, request):
        http_info = self._create_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_node_http_info(self, request):
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

    def create_node_pool_async(self, request):
        """创建节点池

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

    def create_node_pool_async_invoker(self, request):
        http_info = self._create_node_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_node_pool_http_info(self, request):
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

    def delete_addon_instance_async(self, request):
        """删除AddonInstance

        删除插件实例的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.DeleteAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteAddonInstanceResponse`
        """
        http_info = self._delete_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_addon_instance_async_invoker(self, request):
        http_info = self._delete_addon_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_addon_instance_http_info(self, request):
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

    def delete_cloud_persistent_volume_claims_async(self, request):
        """删除PVC（待废弃）

        该API用于删除指定Namespace下的PVC（PersistentVolumeClaim）对象，并可以选择保留后端的云存储。该API待废弃，请使用Kubernetes PVC相关接口。
        &gt;存储管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。如果使用https://Endpoint/uri，则必须指定请求header中的X-Cluster-ID参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCloudPersistentVolumeClaims
        :type request: :class:`huaweicloudsdkcce.v3.DeleteCloudPersistentVolumeClaimsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteCloudPersistentVolumeClaimsResponse`
        """
        http_info = self._delete_cloud_persistent_volume_claims_http_info(request)
        return self._call_api(**http_info)

    def delete_cloud_persistent_volume_claims_async_invoker(self, request):
        http_info = self._delete_cloud_persistent_volume_claims_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cloud_persistent_volume_claims_http_info(self, request):
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

    def delete_cluster_async(self, request):
        """删除集群

        该API用于删除一个指定的集群。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkcce.v3.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteClusterResponse`
        """
        http_info = self._delete_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_async_invoker(self, request):
        http_info = self._delete_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cluster_http_info(self, request):
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
        if 'tobedeleted' in local_var_params:
            query_params.append(('tobedeleted', local_var_params['tobedeleted']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_node_async(self, request):
        """删除节点

        该API用于删除指定的节点。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNode
        :type request: :class:`huaweicloudsdkcce.v3.DeleteNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteNodeResponse`
        """
        http_info = self._delete_node_http_info(request)
        return self._call_api(**http_info)

    def delete_node_async_invoker(self, request):
        http_info = self._delete_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_node_http_info(self, request):
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

    def delete_node_pool_async(self, request):
        """删除节点池

        该API用于删除指定的节点池。
        &gt; 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNodePool
        :type request: :class:`huaweicloudsdkcce.v3.DeleteNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteNodePoolResponse`
        """
        http_info = self._delete_node_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_node_pool_async_invoker(self, request):
        http_info = self._delete_node_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_node_pool_http_info(self, request):
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

    def hibernate_cluster_async(self, request):
        """集群休眠

        集群休眠用于将运行中的集群置于休眠状态，休眠后，将不再收取控制节点资源费用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for HibernateCluster
        :type request: :class:`huaweicloudsdkcce.v3.HibernateClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.HibernateClusterResponse`
        """
        http_info = self._hibernate_cluster_http_info(request)
        return self._call_api(**http_info)

    def hibernate_cluster_async_invoker(self, request):
        http_info = self._hibernate_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _hibernate_cluster_http_info(self, request):
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

    def list_addon_instances_async(self, request):
        """获取AddonInstance列表

        获取集群所有已安装插件实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAddonInstances
        :type request: :class:`huaweicloudsdkcce.v3.ListAddonInstancesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAddonInstancesResponse`
        """
        http_info = self._list_addon_instances_http_info(request)
        return self._call_api(**http_info)

    def list_addon_instances_async_invoker(self, request):
        http_info = self._list_addon_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_addon_instances_http_info(self, request):
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

    def list_addon_templates_async(self, request):
        """查询AddonTemplates列表

        插件模板查询接口，查询插件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAddonTemplates
        :type request: :class:`huaweicloudsdkcce.v3.ListAddonTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListAddonTemplatesResponse`
        """
        http_info = self._list_addon_templates_http_info(request)
        return self._call_api(**http_info)

    def list_addon_templates_async_invoker(self, request):
        http_info = self._list_addon_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_addon_templates_http_info(self, request):
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

    def list_clusters_async(self, request):
        """获取指定项目下的集群

        该API用于获取指定项目下所有集群的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusters
        :type request: :class:`huaweicloudsdkcce.v3.ListClustersRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListClustersResponse`
        """
        http_info = self._list_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_clusters_async_invoker(self, request):
        http_info = self._list_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_clusters_http_info(self, request):
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

    def list_node_pools_async(self, request):
        """获取集群下所有节点池

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

    def list_node_pools_async_invoker(self, request):
        http_info = self._list_node_pools_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_node_pools_http_info(self, request):
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

    def list_nodes_async(self, request):
        """获取集群下所有节点

        该API用于通过集群ID获取指定集群下所有节点的详细信息。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodes
        :type request: :class:`huaweicloudsdkcce.v3.ListNodesRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ListNodesResponse`
        """
        http_info = self._list_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_nodes_async_invoker(self, request):
        http_info = self._list_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nodes_http_info(self, request):
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

    def migrate_node_async(self, request):
        """节点迁移

        该API用于在指定集群下迁移节点到另一集群（仅支持在同一VPC、同一项目下的不同集群之间进行迁移，且迁移前后的集群类型需相同）。
        [CCE Turbo集群下弹性云服务-物理机类型节点不支持迁移。](tag:hws,hws_hk,dt)
        
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for MigrateNode
        :type request: :class:`huaweicloudsdkcce.v3.MigrateNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.MigrateNodeResponse`
        """
        http_info = self._migrate_node_http_info(request)
        return self._call_api(**http_info)

    def migrate_node_async_invoker(self, request):
        http_info = self._migrate_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _migrate_node_http_info(self, request):
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

    def pause_upgrade_cluster_task_async(self, request):
        """暂停集群升级任务

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

    def pause_upgrade_cluster_task_async_invoker(self, request):
        http_info = self._pause_upgrade_cluster_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _pause_upgrade_cluster_task_http_info(self, request):
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

    def remove_node_async(self, request):
        """节点移除

        该API用于在指定集群下移除节点。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveNode
        :type request: :class:`huaweicloudsdkcce.v3.RemoveNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.RemoveNodeResponse`
        """
        http_info = self._remove_node_http_info(request)
        return self._call_api(**http_info)

    def remove_node_async_invoker(self, request):
        http_info = self._remove_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_node_http_info(self, request):
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

    def reset_node_async(self, request):
        """重置节点

        该API用于在指定集群下重置节点。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetNode
        :type request: :class:`huaweicloudsdkcce.v3.ResetNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ResetNodeResponse`
        """
        http_info = self._reset_node_http_info(request)
        return self._call_api(**http_info)

    def reset_node_async_invoker(self, request):
        http_info = self._reset_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_node_http_info(self, request):
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

    def resize_cluster_async(self, request):
        """变更集群规格

        该API用于变更一个指定集群的规格。
        
        &gt;   - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        &gt;   - 使用限制请参考：[[变更集群规格](https://support.huaweicloud.com/usermanual-cce/cce_10_0403.html)。](tag:hws)[[变更集群规格](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0403.html)](tag:hws_hk)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeCluster
        :type request: :class:`huaweicloudsdkcce.v3.ResizeClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ResizeClusterResponse`
        """
        http_info = self._resize_cluster_http_info(request)
        return self._call_api(**http_info)

    def resize_cluster_async_invoker(self, request):
        http_info = self._resize_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_cluster_http_info(self, request):
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

    def retry_upgrade_cluster_task_async(self, request):
        """重试集群升级任务

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

    def retry_upgrade_cluster_task_async_invoker(self, request):
        http_info = self._retry_upgrade_cluster_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _retry_upgrade_cluster_task_http_info(self, request):
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

    def rollback_addon_instance_async(self, request):
        """回滚AddonInstance

        将插件实例回滚到升级前的版本。只有在当前插件实例版本支持回滚到升级前的版本（status.isRollbackable为true），且插件实例状态为running（运行中）、available（可用）、abnormal（不可用）、upgradeFailed（升级失败）、rollbackFailed（回滚失败）时支持回滚。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RollbackAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.RollbackAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.RollbackAddonInstanceResponse`
        """
        http_info = self._rollback_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def rollback_addon_instance_async_invoker(self, request):
        http_info = self._rollback_addon_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _rollback_addon_instance_http_info(self, request):
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

    def show_addon_instance_async(self, request):
        """获取AddonInstance详情

        获取插件实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.ShowAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowAddonInstanceResponse`
        """
        http_info = self._show_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def show_addon_instance_async_invoker(self, request):
        http_info = self._show_addon_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_addon_instance_http_info(self, request):
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

    def show_cluster_async(self, request):
        """获取指定的集群

        该API用于获取指定集群的详细信息。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCluster
        :type request: :class:`huaweicloudsdkcce.v3.ShowClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowClusterResponse`
        """
        http_info = self._show_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_async_invoker(self, request):
        http_info = self._show_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_http_info(self, request):
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

    def show_cluster_endpoints_async(self, request):
        """获取集群访问的地址

        该API用于通过集群ID获取集群访问的地址，包括PrivateIP(HA集群返回VIP)与PublicIP
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterEndpoints
        :type request: :class:`huaweicloudsdkcce.v3.ShowClusterEndpointsRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowClusterEndpointsResponse`
        """
        http_info = self._show_cluster_endpoints_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_endpoints_async_invoker(self, request):
        http_info = self._show_cluster_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_endpoints_http_info(self, request):
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

    def show_job_async(self, request):
        """获取任务信息

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

    def show_job_async_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_http_info(self, request):
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

    def show_node_async(self, request):
        """获取指定的节点

        该API用于通过节点ID获取指定节点的详细信息。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNode
        :type request: :class:`huaweicloudsdkcce.v3.ShowNodeRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowNodeResponse`
        """
        http_info = self._show_node_http_info(request)
        return self._call_api(**http_info)

    def show_node_async_invoker(self, request):
        http_info = self._show_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_node_http_info(self, request):
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

    def show_node_pool_async(self, request):
        """获取指定的节点池

        该API用于获取指定节点池的详细信息。
        &gt; 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNodePool
        :type request: :class:`huaweicloudsdkcce.v3.ShowNodePoolRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowNodePoolResponse`
        """
        http_info = self._show_node_pool_http_info(request)
        return self._call_api(**http_info)

    def show_node_pool_async_invoker(self, request):
        http_info = self._show_node_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_node_pool_http_info(self, request):
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

    def show_quotas_async(self, request):
        """查询CCE服务下的资源配额

        该API用于查询CCE服务下的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkcce.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_async_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quotas_http_info(self, request):
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

    def show_upgrade_cluster_task_async(self, request):
        """获取集群升级任务详情

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

    def show_upgrade_cluster_task_async_invoker(self, request):
        http_info = self._show_upgrade_cluster_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_upgrade_cluster_task_http_info(self, request):
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

    def update_addon_instance_async(self, request):
        """更新AddonInstance

        更新插件实例的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAddonInstance
        :type request: :class:`huaweicloudsdkcce.v3.UpdateAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateAddonInstanceResponse`
        """
        http_info = self._update_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def update_addon_instance_async_invoker(self, request):
        http_info = self._update_addon_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_addon_instance_http_info(self, request):
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

    def update_cluster_async(self, request):
        """更新指定的集群

        该API用于更新指定的集群。
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCluster
        :type request: :class:`huaweicloudsdkcce.v3.UpdateClusterRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateClusterResponse`
        """
        http_info = self._update_cluster_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_async_invoker(self, request):
        http_info = self._update_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cluster_http_info(self, request):
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

    def update_cluster_eip_async(self, request):
        """绑定、解绑集群公网apiserver地址

        该API用于通过集群ID绑定、解绑集群公网apiserver地址
        &gt;集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateClusterEip
        :type request: :class:`huaweicloudsdkcce.v3.UpdateClusterEipRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.UpdateClusterEipResponse`
        """
        http_info = self._update_cluster_eip_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_eip_async_invoker(self, request):
        http_info = self._update_cluster_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cluster_eip_http_info(self, request):
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

    def update_node_async(self, request):
        """更新指定的节点

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

    def update_node_async_invoker(self, request):
        http_info = self._update_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_node_http_info(self, request):
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

    def update_node_pool_async(self, request):
        """更新指定节点池

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

    def update_node_pool_async_invoker(self, request):
        http_info = self._update_node_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_node_pool_http_info(self, request):
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

    def upgrade_cluster_async(self, request):
        """集群升级

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

    def upgrade_cluster_async_invoker(self, request):
        http_info = self._upgrade_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_cluster_http_info(self, request):
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

    def show_version_async(self, request):
        """查询API版本信息列表。

        该API用于查询CCE服务当前支持的API版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVersion
        :type request: :class:`huaweicloudsdkcce.v3.ShowVersionRequest`
        :rtype: :class:`huaweicloudsdkcce.v3.ShowVersionResponse`
        """
        http_info = self._show_version_http_info(request)
        return self._call_api(**http_info)

    def show_version_async_invoker(self, request):
        http_info = self._show_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_version_http_info(self, request):
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

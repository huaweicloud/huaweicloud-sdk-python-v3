# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CceClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(CceClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcce.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CceClient":
            raise TypeError("client type error, support client type is CceClient")

        return ClientBuilder(clazz)

    def awake_cluster(self, request):
        """集群唤醒

        集群唤醒用于唤醒已休眠的集群，唤醒后，将继续收取控制节点资源费用。

        :param AwakeClusterRequest request
        :return: AwakeClusterResponse
        """
        return self.awake_cluster_with_http_info(request)

    def awake_cluster_with_http_info(self, request):
        """集群唤醒

        集群唤醒用于唤醒已休眠的集群，唤醒后，将继续收取控制节点资源费用。

        :param AwakeClusterRequest request
        :return: AwakeClusterResponse
        """

        all_params = ['cluster_id', 'content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/awake',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AwakeClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_addon_instance(self, request):
        """创建AddonInstance

        根据提供的插件模板，安装插件实例。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param CreateAddonInstanceRequest request
        :return: CreateAddonInstanceResponse
        """
        return self.create_addon_instance_with_http_info(request)

    def create_addon_instance_with_http_info(self, request):
        """创建AddonInstance

        根据提供的插件模板，安装插件实例。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param CreateAddonInstanceRequest request
        :return: CreateAddonInstanceResponse
        """

        all_params = ['content_type', 'create_addon_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/addons',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAddonInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_cloud_persistent_volume_claims(self, request):
        """创建PVC

        该API用于在指定的Namespace下通过云存储服务中的云存储（EVS、SFS、OBS）去创建PVC（PersistentVolumeClaim）。  >存储管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。如果使用https://Endpoint/uri，则必须指定请求header中的X-Cluster-ID参数。 

        :param CreateCloudPersistentVolumeClaimsRequest request
        :return: CreateCloudPersistentVolumeClaimsResponse
        """
        return self.create_cloud_persistent_volume_claims_with_http_info(request)

    def create_cloud_persistent_volume_claims_with_http_info(self, request):
        """创建PVC

        该API用于在指定的Namespace下通过云存储服务中的云存储（EVS、SFS、OBS）去创建PVC（PersistentVolumeClaim）。  >存储管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。如果使用https://Endpoint/uri，则必须指定请求header中的X-Cluster-ID参数。 

        :param CreateCloudPersistentVolumeClaimsRequest request
        :return: CreateCloudPersistentVolumeClaimsResponse
        """

        all_params = ['namespace', 'content_type', 'create_cloud_persistent_volume_claims_request_body', 'x_cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_cluster_id' in local_var_params:
            header_params['X-Cluster-ID'] = local_var_params['x_cluster_id']

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
            resource_path='/api/v1/namespaces/{namespace}/cloudpersistentvolumeclaims',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCloudPersistentVolumeClaimsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_cluster(self, request):
        """创建集群

        该API用于创建一个空集群（即只有控制节点Master，没有工作节点Node）。请在调用本接口完成集群创建之后，通过[创建节点](https://support.huaweicloud.com/api-cce/cce_02_0242.html)添加节点。   >   - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。 >   - 调用该接口创建集群时，默认不安装ICAgent。ICAgent是应用性能管理APM的采集代理，运行在应用所在的服务器上，用于实时采集探针所获取的数据，安装ICAgent是使用应用性能管理APM的前提。若需安装ICAgent，请参照[安装ICAgent](https://support.huaweicloud.com/usermanual-apm/apm_02_0013.html)。 >   - 默认情况下，一个账户只能创建 5 个集群（每个Region下），如果您需要创建更多的集群，请[提交工单](https://console.huaweicloud.com/console/#/quota)申请增加配额。

        :param CreateClusterRequest request
        :return: CreateClusterResponse
        """
        return self.create_cluster_with_http_info(request)

    def create_cluster_with_http_info(self, request):
        """创建集群

        该API用于创建一个空集群（即只有控制节点Master，没有工作节点Node）。请在调用本接口完成集群创建之后，通过[创建节点](https://support.huaweicloud.com/api-cce/cce_02_0242.html)添加节点。   >   - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。 >   - 调用该接口创建集群时，默认不安装ICAgent。ICAgent是应用性能管理APM的采集代理，运行在应用所在的服务器上，用于实时采集探针所获取的数据，安装ICAgent是使用应用性能管理APM的前提。若需安装ICAgent，请参照[安装ICAgent](https://support.huaweicloud.com/usermanual-apm/apm_02_0013.html)。 >   - 默认情况下，一个账户只能创建 5 个集群（每个Region下），如果您需要创建更多的集群，请[提交工单](https://console.huaweicloud.com/console/#/quota)申请增加配额。

        :param CreateClusterRequest request
        :return: CreateClusterResponse
        """

        all_params = ['content_type', 'create_cluster_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/projects/{project_id}/clusters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_kubernetes_cluster_cert(self, request):
        """获取集群证书

        该API用于获取指定集群的证书信息。

        :param CreateKubernetesClusterCertRequest request
        :return: CreateKubernetesClusterCertResponse
        """
        return self.create_kubernetes_cluster_cert_with_http_info(request)

    def create_kubernetes_cluster_cert_with_http_info(self, request):
        """获取集群证书

        该API用于获取指定集群的证书信息。

        :param CreateKubernetesClusterCertRequest request
        :return: CreateKubernetesClusterCertResponse
        """

        all_params = ['cluster_id', 'content_type', 'create_kubernetes_cluster_cert_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/clustercert',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateKubernetesClusterCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_node(self, request):
        """创建节点

        该API用于在指定集群下创建节点。 > 若无集群，请先[创建集群](https://support.huaweicloud.com/api-cce/cce_02_0236.html)。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param CreateNodeRequest request
        :return: CreateNodeResponse
        """
        return self.create_node_with_http_info(request)

    def create_node_with_http_info(self, request):
        """创建节点

        该API用于在指定集群下创建节点。 > 若无集群，请先[创建集群](https://support.huaweicloud.com/api-cce/cce_02_0236.html)。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param CreateNodeRequest request
        :return: CreateNodeResponse
        """

        all_params = ['cluster_id', 'content_type', 'create_node_request_body', 'nodepool_scale_up']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'nodepool_scale_up' in local_var_params:
            query_params.append(('nodepoolScaleUp', local_var_params['nodepool_scale_up']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_node_pool(self, request):
        """创建节点池

        该API用于在指定集群下创建节点池。仅支持集群在处于可用、扩容、缩容状态时调用。 > 若无集群，请先[创建集群](https://support.huaweicloud.com/api-cce/cce_02_0236.html)。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 

        :param CreateNodePoolRequest request
        :return: CreateNodePoolResponse
        """
        return self.create_node_pool_with_http_info(request)

    def create_node_pool_with_http_info(self, request):
        """创建节点池

        该API用于在指定集群下创建节点池。仅支持集群在处于可用、扩容、缩容状态时调用。 > 若无集群，请先[创建集群](https://support.huaweicloud.com/api-cce/cce_02_0236.html)。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 

        :param CreateNodePoolRequest request
        :return: CreateNodePoolResponse
        """

        all_params = ['content_type', 'cluster_id', 'create_node_pool_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNodePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_addon_instance(self, request):
        """删除AddonInstance

        删除插件实例的功能。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param DeleteAddonInstanceRequest request
        :return: DeleteAddonInstanceResponse
        """
        return self.delete_addon_instance_with_http_info(request)

    def delete_addon_instance_with_http_info(self, request):
        """删除AddonInstance

        删除插件实例的功能。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param DeleteAddonInstanceRequest request
        :return: DeleteAddonInstanceResponse
        """

        all_params = ['content_type', 'id', 'cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/addons/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAddonInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_cloud_persistent_volume_claims(self, request):
        """删除PVC

        该API用于删除指定Namespace下的PVC（PersistentVolumeClaim）对象，并可以选择保留后端的云存储。 >存储管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。如果使用https://Endpoint/uri，则必须指定请求header中的X-Cluster-ID参数。 

        :param DeleteCloudPersistentVolumeClaimsRequest request
        :return: DeleteCloudPersistentVolumeClaimsResponse
        """
        return self.delete_cloud_persistent_volume_claims_with_http_info(request)

    def delete_cloud_persistent_volume_claims_with_http_info(self, request):
        """删除PVC

        该API用于删除指定Namespace下的PVC（PersistentVolumeClaim）对象，并可以选择保留后端的云存储。 >存储管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。如果使用https://Endpoint/uri，则必须指定请求header中的X-Cluster-ID参数。 

        :param DeleteCloudPersistentVolumeClaimsRequest request
        :return: DeleteCloudPersistentVolumeClaimsResponse
        """

        all_params = ['name', 'namespace', 'content_type', 'x_cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_cluster_id' in local_var_params:
            header_params['X-Cluster-ID'] = local_var_params['x_cluster_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v1/namespaces/{namespace}/cloudpersistentvolumeclaims/{name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCloudPersistentVolumeClaimsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_cluster(self, request):
        """删除集群

        该API用于删除一个指定的集群。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param DeleteClusterRequest request
        :return: DeleteClusterResponse
        """
        return self.delete_cluster_with_http_info(request)

    def delete_cluster_with_http_info(self, request):
        """删除集群

        该API用于删除一个指定的集群。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param DeleteClusterRequest request
        :return: DeleteClusterResponse
        """

        all_params = ['cluster_id', 'content_type', 'error_status', 'delete_efs', 'delete_eni', 'delete_evs', 'delete_net', 'delete_obs', 'delete_sfs']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))
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

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_node(self, request):
        """删除节点

        该API用于删除指定的节点。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 

        :param DeleteNodeRequest request
        :return: DeleteNodeResponse
        """
        return self.delete_node_with_http_info(request)

    def delete_node_with_http_info(self, request):
        """删除节点

        该API用于删除指定的节点。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 

        :param DeleteNodeRequest request
        :return: DeleteNodeResponse
        """

        all_params = ['cluster_id', 'node_id', 'content_type', 'error_status', 'nodepool_scale_down']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))
        if 'nodepool_scale_down' in local_var_params:
            query_params.append(('nodepoolScaleDown', local_var_params['nodepool_scale_down']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_node_pool(self, request):
        """删除节点池

        该API用于删除指定的节点池。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 

        :param DeleteNodePoolRequest request
        :return: DeleteNodePoolResponse
        """
        return self.delete_node_pool_with_http_info(request)

    def delete_node_pool_with_http_info(self, request):
        """删除节点池

        该API用于删除指定的节点池。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 

        :param DeleteNodePoolRequest request
        :return: DeleteNodePoolResponse
        """

        all_params = ['cluster_id', 'nodepool_id', 'content_type', 'error_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNodePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def hibernate_cluster(self, request):
        """集群休眠

        1、集群休眠后，将无法在此集群上创建和管理工作负载等资源。  2、按需付费集群休眠后，将暂停收取控制节点资源费用，集群所属的节点、绑定的弹性IP、带宽等资源按各自的计费方式（“包年/包月”或“按需付费”）进行收费。

        :param HibernateClusterRequest request
        :return: HibernateClusterResponse
        """
        return self.hibernate_cluster_with_http_info(request)

    def hibernate_cluster_with_http_info(self, request):
        """集群休眠

        1、集群休眠后，将无法在此集群上创建和管理工作负载等资源。  2、按需付费集群休眠后，将暂停收取控制节点资源费用，集群所属的节点、绑定的弹性IP、带宽等资源按各自的计费方式（“包年/包月”或“按需付费”）进行收费。

        :param HibernateClusterRequest request
        :return: HibernateClusterResponse
        """

        all_params = ['cluster_id', 'content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/hibernate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='HibernateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_addon_instances(self, request):
        """获取AddonInstance列表

        获取集群所有已安装插件实例 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param ListAddonInstancesRequest request
        :return: ListAddonInstancesResponse
        """
        return self.list_addon_instances_with_http_info(request)

    def list_addon_instances_with_http_info(self, request):
        """获取AddonInstance列表

        获取集群所有已安装插件实例 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param ListAddonInstancesRequest request
        :return: ListAddonInstancesResponse
        """

        all_params = ['content_type', 'cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/addons',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAddonInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_addon_templates(self, request):
        """查询AddonTemplates列表

        插件模板查询接口，查询插件信息。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param ListAddonTemplatesRequest request
        :return: ListAddonTemplatesResponse
        """
        return self.list_addon_templates_with_http_info(request)

    def list_addon_templates_with_http_info(self, request):
        """查询AddonTemplates列表

        插件模板查询接口，查询插件信息。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param ListAddonTemplatesRequest request
        :return: ListAddonTemplatesResponse
        """

        all_params = ['content_type', 'addon_template_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'addon_template_name' in local_var_params:
            query_params.append(('addon_template_name', local_var_params['addon_template_name']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/addontemplates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAddonTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_clusters(self, request):
        """获取指定项目下的集群

        该API用于获取指定项目下所有集群的详细信息。

        :param ListClustersRequest request
        :return: ListClustersResponse
        """
        return self.list_clusters_with_http_info(request)

    def list_clusters_with_http_info(self, request):
        """获取指定项目下的集群

        该API用于获取指定项目下所有集群的详细信息。

        :param ListClustersRequest request
        :return: ListClustersResponse
        """

        all_params = ['content_type', 'error_status', 'detail', 'status', 'type', 'version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClustersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_node_pools(self, request):
        """获取集群下所有节点池

        该API用于获取集群下所有节点池。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 > - nodepool是集群中具有相同配置的节点实例的子集。 

        :param ListNodePoolsRequest request
        :return: ListNodePoolsResponse
        """
        return self.list_node_pools_with_http_info(request)

    def list_node_pools_with_http_info(self, request):
        """获取集群下所有节点池

        该API用于获取集群下所有节点池。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 > - nodepool是集群中具有相同配置的节点实例的子集。 

        :param ListNodePoolsRequest request
        :return: ListNodePoolsResponse
        """

        all_params = ['cluster_id', 'content_type', 'error_status', 'show_default_node_pool']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))
        if 'show_default_node_pool' in local_var_params:
            query_params.append(('showDefaultNodePool', local_var_params['show_default_node_pool']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNodePoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_nodes(self, request):
        """获取集群下所有节点

        该API用于通过集群ID获取指定集群下所有节点的详细信息。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param ListNodesRequest request
        :return: ListNodesResponse
        """
        return self.list_nodes_with_http_info(request)

    def list_nodes_with_http_info(self, request):
        """获取集群下所有节点

        该API用于通过集群ID获取指定集群下所有节点的详细信息。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param ListNodesRequest request
        :return: ListNodesResponse
        """

        all_params = ['cluster_id', 'content_type', 'error_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_addon_instance(self, request):
        """获取AddonInstance详情

        获取插件实例详情。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param ShowAddonInstanceRequest request
        :return: ShowAddonInstanceResponse
        """
        return self.show_addon_instance_with_http_info(request)

    def show_addon_instance_with_http_info(self, request):
        """获取AddonInstance详情

        获取插件实例详情。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param ShowAddonInstanceRequest request
        :return: ShowAddonInstanceResponse
        """

        all_params = ['content_type', 'id', 'cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/addons/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAddonInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cluster(self, request):
        """获取指定的集群

        该API用于获取指定集群的详细信息。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param ShowClusterRequest request
        :return: ShowClusterResponse
        """
        return self.show_cluster_with_http_info(request)

    def show_cluster_with_http_info(self, request):
        """获取指定的集群

        该API用于获取指定集群的详细信息。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param ShowClusterRequest request
        :return: ShowClusterResponse
        """

        all_params = ['cluster_id', 'content_type', 'error_status', 'detail']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_job(self, request):
        """获取任务信息

        该API用于获取任务信息。通过某一任务请求下发后返回的jobID来查询指定任务的进度。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 > - 该接口通常使用场景为： >   - 创建、删除集群时，查询相应任务的进度。 >   - 创建、删除节点时，查询相应任务的进度。 

        :param ShowJobRequest request
        :return: ShowJobResponse
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        """获取任务信息

        该API用于获取任务信息。通过某一任务请求下发后返回的jobID来查询指定任务的进度。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 > - 该接口通常使用场景为： >   - 创建、删除集群时，查询相应任务的进度。 >   - 创建、删除节点时，查询相应任务的进度。 

        :param ShowJobRequest request
        :return: ShowJobResponse
        """

        all_params = ['job_id', 'content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_node(self, request):
        """获取指定的节点

        该API用于通过节点ID获取指定节点的详细信息。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param ShowNodeRequest request
        :return: ShowNodeResponse
        """
        return self.show_node_with_http_info(request)

    def show_node_with_http_info(self, request):
        """获取指定的节点

        该API用于通过节点ID获取指定节点的详细信息。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param ShowNodeRequest request
        :return: ShowNodeResponse
        """

        all_params = ['cluster_id', 'node_id', 'content_type', 'error_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_node_pool(self, request):
        """获取指定的节点池

        该API用于获取指定节点池的详细信息。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 

        :param ShowNodePoolRequest request
        :return: ShowNodePoolResponse
        """
        return self.show_node_pool_with_http_info(request)

    def show_node_pool_with_http_info(self, request):
        """获取指定的节点池

        该API用于获取指定节点池的详细信息。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 

        :param ShowNodePoolRequest request
        :return: ShowNodePoolResponse
        """

        all_params = ['cluster_id', 'nodepool_id', 'content_type', 'error_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNodePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_addon_instance(self, request):
        """更新AddonInstance

        更新插件实例的功能。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param UpdateAddonInstanceRequest request
        :return: UpdateAddonInstanceResponse
        """
        return self.update_addon_instance_with_http_info(request)

    def update_addon_instance_with_http_info(self, request):
        """更新AddonInstance

        更新插件实例的功能。 >插件管理的URL格式为：https://{clusterid}.Endpoint/uri。其中{clusterid}为集群ID，uri为资源路径，也即API访问的路径。 

        :param UpdateAddonInstanceRequest request
        :return: UpdateAddonInstanceResponse
        """

        all_params = ['id', 'content_type', 'update_addon_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/addons/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAddonInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_cluster(self, request):
        """更新指定的集群

        该API用于更新指定的集群。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param UpdateClusterRequest request
        :return: UpdateClusterResponse
        """
        return self.update_cluster_with_http_info(request)

    def update_cluster_with_http_info(self, request):
        """更新指定的集群

        该API用于更新指定的集群。 > 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。

        :param UpdateClusterRequest request
        :return: UpdateClusterResponse
        """

        all_params = ['cluster_id', 'content_type', 'update_cluster_request_body', 'error_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_node(self, request):
        """更新指定的节点

        该API用于更新指定的节点。 > - 当前仅支持更新metadata下的name字段，即节点的名字。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。 

        :param UpdateNodeRequest request
        :return: UpdateNodeResponse
        """
        return self.update_node_with_http_info(request)

    def update_node_with_http_info(self, request):
        """更新指定的节点

        该API用于更新指定的节点。 > - 当前仅支持更新metadata下的name字段，即节点的名字。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径。 

        :param UpdateNodeRequest request
        :return: UpdateNodeResponse
        """

        all_params = ['cluster_id', 'node_id', 'content_type', 'update_node_request_body', 'error_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_node_pool(self, request):
        """更新指定节点池

        该API用于更新指定的节点池。仅支持集群在处于可用、扩容、缩容状态时调用。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 > - 当前仅支持更新节点池名称，spec下的initialNodeCount，k8sTags， taints，login，userTags与节点池的扩缩容配置相关字段。

        :param UpdateNodePoolRequest request
        :return: UpdateNodePoolResponse
        """
        return self.update_node_pool_with_http_info(request)

    def update_node_pool_with_http_info(self, request):
        """更新指定节点池

        该API用于更新指定的节点池。仅支持集群在处于可用、扩容、缩容状态时调用。 > - 集群管理的URL格式为：https://Endpoint/uri。其中uri为资源路径，也即API访问的路径 > - 当前仅支持更新节点池名称，spec下的initialNodeCount，k8sTags， taints，login，userTags与节点池的扩缩容配置相关字段。

        :param UpdateNodePoolRequest request
        :return: UpdateNodePoolResponse
        """

        all_params = ['cluster_id', 'nodepool_id', 'content_type', 'update_node_pool_request_body', 'error_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

        query_params = []
        if 'error_status' in local_var_params:
            query_params.append(('errorStatus', local_var_params['error_status']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNodePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)

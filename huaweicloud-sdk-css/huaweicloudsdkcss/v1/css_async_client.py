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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcss'")


class CssAsyncClient(Client):
    def __init__(self):
        super(CssAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcss.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CssAsyncClient":
                raise TypeError("client type error, support client type is CssAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_independent_node_async(self, request):
        """添加独立master、client

        由于集群数据面业务的增长或者不确定性，很难在一开始就能够把集群的规模形态想明白，该接口能够在非独立master和client的集群上面独立master、client角色。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddIndependentNode
        :type request: :class:`huaweicloudsdkcss.v1.AddIndependentNodeRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.AddIndependentNodeResponse`
        """
        http_info = self._add_independent_node_http_info(request)
        return self._call_api(**http_info)

    def add_independent_node_async_invoker(self, request):
        http_info = self._add_independent_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_independent_node_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/type/{type}/independent",
            "request_type": request.__class__.__name__,
            "response_type": "AddIndependentNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

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

    def change_mode_async(self, request):
        """安全模式修改

        该接口用于切换集群的安全模式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeMode
        :type request: :class:`huaweicloudsdkcss.v1.ChangeModeRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ChangeModeResponse`
        """
        http_info = self._change_mode_http_info(request)
        return self._call_api(**http_info)

    def change_mode_async_invoker(self, request):
        http_info = self._change_mode_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_mode_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/mode/change",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeModeResponse"
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

    def change_security_group_async(self, request):
        """切换安全组

        该接口可以在集群创建成功后，修改安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeSecurityGroup
        :type request: :class:`huaweicloudsdkcss.v1.ChangeSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ChangeSecurityGroupResponse`
        """
        http_info = self._change_security_group_http_info(request)
        return self._call_api(**http_info)

    def change_security_group_async_invoker(self, request):
        http_info = self._change_security_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_security_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/sg/change",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeSecurityGroupResponse"
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

    def create_ai_ops_async(self, request):
        """创建一次集群检测任务

        该接口用于创建一个集群检测任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAiOps
        :type request: :class:`huaweicloudsdkcss.v1.CreateAiOpsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateAiOpsResponse`
        """
        http_info = self._create_ai_ops_http_info(request)
        return self._call_api(**http_info)

    def create_ai_ops_async_invoker(self, request):
        http_info = self._create_ai_ops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ai_ops_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ai-ops",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAiOpsResponse"
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

    def create_auto_create_policy_async(self, request):
        """设置自动创建快照策略

        该接口用于设置自动创建快照，默认一天创建一个快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAutoCreatePolicy
        :type request: :class:`huaweicloudsdkcss.v1.CreateAutoCreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateAutoCreatePolicyResponse`
        """
        http_info = self._create_auto_create_policy_http_info(request)
        return self._call_api(**http_info)

    def create_auto_create_policy_async_invoker(self, request):
        http_info = self._create_auto_create_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_auto_create_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutoCreatePolicyResponse"
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

    def create_bind_public_async(self, request):
        """开启公网访问

        该接口用于开启公网访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBindPublic
        :type request: :class:`huaweicloudsdkcss.v1.CreateBindPublicRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateBindPublicResponse`
        """
        http_info = self._create_bind_public_http_info(request)
        return self._call_api(**http_info)

    def create_bind_public_async_invoker(self, request):
        http_info = self._create_bind_public_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_bind_public_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/public/open",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBindPublicResponse"
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

    def create_cluster_async(self, request):
        """创建集群

        该接口用于创建集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkcss.v1.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClusterResponse`
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_clusters_tags_async(self, request):
        """添加指定集群标签

        该接口用于给指定集群添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateClustersTags
        :type request: :class:`huaweicloudsdkcss.v1.CreateClustersTagsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClustersTagsResponse`
        """
        http_info = self._create_clusters_tags_http_info(request)
        return self._call_api(**http_info)

    def create_clusters_tags_async_invoker(self, request):
        http_info = self._create_clusters_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_clusters_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/{resource_type}/{cluster_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClustersTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def create_elb_listener_async(self, request):
        """es监听器配置。

        该接口用于es监听器配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateElbListener
        :type request: :class:`huaweicloudsdkcss.v1.CreateElbListenerRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateElbListenerResponse`
        """
        http_info = self._create_elb_listener_http_info(request)
        return self._call_api(**http_info)

    def create_elb_listener_async_invoker(self, request):
        http_info = self._create_elb_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_elb_listener_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/es-listeners",
            "request_type": request.__class__.__name__,
            "response_type": "CreateElbListenerResponse"
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

    def create_load_ik_thesaurus_async(self, request):
        """加载自定义词库

        该接口用于加载存放于OBS的自定义词库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLoadIkThesaurus
        :type request: :class:`huaweicloudsdkcss.v1.CreateLoadIkThesaurusRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateLoadIkThesaurusResponse`
        """
        http_info = self._create_load_ik_thesaurus_http_info(request)
        return self._call_api(**http_info)

    def create_load_ik_thesaurus_async_invoker(self, request):
        http_info = self._create_load_ik_thesaurus_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_load_ik_thesaurus_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/thesaurus",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLoadIkThesaurusResponse"
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

    def create_log_backup_async(self, request):
        """备份日志

        该接口用于备份日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLogBackup
        :type request: :class:`huaweicloudsdkcss.v1.CreateLogBackupRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateLogBackupResponse`
        """
        http_info = self._create_log_backup_http_info(request)
        return self._call_api(**http_info)

    def create_log_backup_async_invoker(self, request):
        http_info = self._create_log_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_log_backup_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/collect",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogBackupResponse"
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

    def create_snapshot_async(self, request):
        """手动创建快照

        该接口用于手动创建一个快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSnapshot
        :type request: :class:`huaweicloudsdkcss.v1.CreateSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateSnapshotResponse`
        """
        http_info = self._create_snapshot_http_info(request)
        return self._call_api(**http_info)

    def create_snapshot_async_invoker(self, request):
        http_info = self._create_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_snapshot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSnapshotResponse"
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

    def delete_ai_ops_async(self, request):
        """删除一个检测任务记录

        该接口用于删除一个检测任务记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAiOps
        :type request: :class:`huaweicloudsdkcss.v1.DeleteAiOpsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteAiOpsResponse`
        """
        http_info = self._delete_ai_ops_http_info(request)
        return self._call_api(**http_info)

    def delete_ai_ops_async_invoker(self, request):
        http_info = self._delete_ai_ops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ai_ops_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ai-ops/{aiops_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAiOpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'aiops_id' in local_var_params:
            path_params['aiops_id'] = local_var_params['aiops_id']

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

        此接口用于删除集群。集群删除将释放此集群的所有资源，包括客户数据。如果需要保留客户集群数据，建议在删除集群前先创建快照。
        
        &gt;此接口亦可用于包年/包月集群退订。公安冻结的集群不能删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkcss.v1.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteClusterResponse`
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
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_clusters_tags_async(self, request):
        """删除集群标签

        此接口用于删除集群标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteClustersTags
        :type request: :class:`huaweicloudsdkcss.v1.DeleteClustersTagsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteClustersTagsResponse`
        """
        http_info = self._delete_clusters_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_clusters_tags_async_invoker(self, request):
        http_info = self._delete_clusters_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_clusters_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/{resource_type}/{cluster_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClustersTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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

    def delete_ik_thesaurus_async(self, request):
        """删除自定义词库

        该接口用于删除自定义词库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIkThesaurus
        :type request: :class:`huaweicloudsdkcss.v1.DeleteIkThesaurusRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteIkThesaurusResponse`
        """
        http_info = self._delete_ik_thesaurus_http_info(request)
        return self._call_api(**http_info)

    def delete_ik_thesaurus_async_invoker(self, request):
        http_info = self._delete_ik_thesaurus_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ik_thesaurus_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/thesaurus",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIkThesaurusResponse"
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

    def delete_snapshot_async(self, request):
        """删除快照

        该接口用于删除快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSnapshot
        :type request: :class:`huaweicloudsdkcss.v1.DeleteSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteSnapshotResponse`
        """
        http_info = self._delete_snapshot_http_info(request)
        return self._call_api(**http_info)

    def delete_snapshot_async_invoker(self, request):
        http_info = self._delete_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_snapshot_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
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

    def download_cert_async(self, request):
        """下载安全证书

        该接口用于下载安全证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadCert
        :type request: :class:`huaweicloudsdkcss.v1.DownloadCertRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DownloadCertResponse`
        """
        http_info = self._download_cert_http_info(request)
        return self._call_api(**http_info)

    def download_cert_async_invoker(self, request):
        http_info = self._download_cert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_cert_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/cer/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadCertResponse"
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

    def enable_or_disable_elb_async(self, request):
        """打开或关闭es负载均衡器

        该接口打开或关闭es负载均衡器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableOrDisableElb
        :type request: :class:`huaweicloudsdkcss.v1.EnableOrDisableElbRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.EnableOrDisableElbResponse`
        """
        http_info = self._enable_or_disable_elb_http_info(request)
        return self._call_api(**http_info)

    def enable_or_disable_elb_async_invoker(self, request):
        http_info = self._enable_or_disable_elb_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_or_disable_elb_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/loadbalancers/es-switch",
            "request_type": request.__class__.__name__,
            "response_type": "EnableOrDisableElbResponse"
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

    def list_ai_ops_async(self, request):
        """获取智能运维任务列表及详情

        该接口用于获取智能运维任务列表及详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAiOps
        :type request: :class:`huaweicloudsdkcss.v1.ListAiOpsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListAiOpsResponse`
        """
        http_info = self._list_ai_ops_http_info(request)
        return self._call_api(**http_info)

    def list_ai_ops_async_invoker(self, request):
        http_info = self._list_ai_ops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ai_ops_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ai-ops",
            "request_type": request.__class__.__name__,
            "response_type": "ListAiOpsResponse"
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
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_clusters_details_async(self, request):
        """查询集群列表

        该接口用于查询并显示集群列表以及集群的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClustersDetails
        :type request: :class:`huaweicloudsdkcss.v1.ListClustersDetailsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListClustersDetailsResponse`
        """
        http_info = self._list_clusters_details_http_info(request)
        return self._call_api(**http_info)

    def list_clusters_details_async_invoker(self, request):
        http_info = self._list_clusters_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_clusters_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListClustersDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastoreType', local_var_params['datastore_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_clusters_tags_async(self, request):
        """查询所有标签

        该接口用于查询指定region下的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClustersTags
        :type request: :class:`huaweicloudsdkcss.v1.ListClustersTagsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListClustersTagsResponse`
        """
        http_info = self._list_clusters_tags_http_info(request)
        return self._call_api(**http_info)

    def list_clusters_tags_async_invoker(self, request):
        http_info = self._list_clusters_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_clusters_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListClustersTagsResponse"
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

    def list_elb_certs_async(self, request):
        """查询证书列表

        该接口用于查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListElbCerts
        :type request: :class:`huaweicloudsdkcss.v1.ListElbCertsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListElbCertsResponse`
        """
        http_info = self._list_elb_certs_http_info(request)
        return self._call_api(**http_info)

    def list_elb_certs_async_invoker(self, request):
        http_info = self._list_elb_certs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_elb_certs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/elb/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListElbCertsResponse"
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

    def list_elbs_async(self, request):
        """查询集群支持的elbv3负载均衡器

        展示查询集群支持的elbv3负载均衡器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListElbs
        :type request: :class:`huaweicloudsdkcss.v1.ListElbsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListElbsResponse`
        """
        http_info = self._list_elbs_http_info(request)
        return self._call_api(**http_info)

    def list_elbs_async_invoker(self, request):
        http_info = self._list_elbs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_elbs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/loadbalancers",
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

    def list_flavors_async(self, request):
        """获取实例规格列表

        该接口用于查询并显示支持的实例规格对应的ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkcss.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_async_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/es-flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
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

    def list_images_async(self, request):
        """获取目标镜像ID

        该接口用于获取当前集群的可升级目标镜像ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImages
        :type request: :class:`huaweicloudsdkcss.v1.ListImagesRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListImagesResponse`
        """
        http_info = self._list_images_http_info(request)
        return self._call_api(**http_info)

    def list_images_async_invoker(self, request):
        http_info = self._list_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/target/{upgrade_type}/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'upgrade_type' in local_var_params:
            path_params['upgrade_type'] = local_var_params['upgrade_type']

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

    def list_logs_job_async(self, request):
        """查询作业列表

        该接口用于查询具体某个集群的日志任务记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogsJob
        :type request: :class:`huaweicloudsdkcss.v1.ListLogsJobRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListLogsJobResponse`
        """
        http_info = self._list_logs_job_http_info(request)
        return self._call_api(**http_info)

    def list_logs_job_async_invoker(self, request):
        http_info = self._list_logs_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_logs_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogsJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
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

    def list_smn_topics_async(self, request):
        """获取智能运维告警可用的SMN主题

        该接口用于获取智能运维告警可用的SMN主题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmnTopics
        :type request: :class:`huaweicloudsdkcss.v1.ListSmnTopicsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListSmnTopicsResponse`
        """
        http_info = self._list_smn_topics_http_info(request)
        return self._call_api(**http_info)

    def list_smn_topics_async_invoker(self, request):
        http_info = self._list_smn_topics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smn_topics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/domains/{domain_id}/ai-ops/smn-topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmnTopicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

        该接口用于查询集群的所有快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSnapshots
        :type request: :class:`huaweicloudsdkcss.v1.ListSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListSnapshotsResponse`
        """
        http_info = self._list_snapshots_http_info(request)
        return self._call_api(**http_info)

    def list_snapshots_async_invoker(self, request):
        http_info = self._list_snapshots_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_snapshots_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotsResponse"
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

    def list_ymls_async(self, request):
        """获取参数配置列表

        该接口用于获取当前集群现有的参数配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListYmls
        :type request: :class:`huaweicloudsdkcss.v1.ListYmlsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListYmlsResponse`
        """
        http_info = self._list_ymls_http_info(request)
        return self._call_api(**http_info)

    def list_ymls_async_invoker(self, request):
        http_info = self._list_ymls_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ymls_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ymls/template",
            "request_type": request.__class__.__name__,
            "response_type": "ListYmlsResponse"
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

    def list_ymls_job_async(self, request):
        """获取参数配置任务列表

        该接口可获取参数配置的任务操作列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListYmlsJob
        :type request: :class:`huaweicloudsdkcss.v1.ListYmlsJobRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListYmlsJobResponse`
        """
        http_info = self._list_ymls_job_http_info(request)
        return self._call_api(**http_info)

    def list_ymls_job_async_invoker(self, request):
        http_info = self._list_ymls_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ymls_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ymls/joblists",
            "request_type": request.__class__.__name__,
            "response_type": "ListYmlsJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
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

    def reset_password_async(self, request):
        """修改密码

        该接口用于修改集群密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkcss.v1.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ResetPasswordResponse`
        """
        http_info = self._reset_password_http_info(request)
        return self._call_api(**http_info)

    def reset_password_async_invoker(self, request):
        http_info = self._reset_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/password/reset",
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
            ['application/json'])

        auth_settings = []

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

        此接口用于重启集群，重启集群将导致业务中断。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartCluster
        :type request: :class:`huaweicloudsdkcss.v1.RestartClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.RestartClusterResponse`
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
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def restore_snapshot_async(self, request):
        """恢复快照

        该接口用于手动恢复一个快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreSnapshot
        :type request: :class:`huaweicloudsdkcss.v1.RestoreSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.RestoreSnapshotResponse`
        """
        http_info = self._restore_snapshot_http_info(request)
        return self._call_api(**http_info)

    def restore_snapshot_async_invoker(self, request):
        http_info = self._restore_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_snapshot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def retry_upgrade_task_async(self, request):
        """重试升级失败任务

        由于升级过程时间较长，可能由于网络等原因导致升级失败，可以通过该接口重试该任务或终止该任务的影响。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryUpgradeTask
        :type request: :class:`huaweicloudsdkcss.v1.RetryUpgradeTaskRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.RetryUpgradeTaskResponse`
        """
        http_info = self._retry_upgrade_task_http_info(request)
        return self._call_api(**http_info)

    def retry_upgrade_task_async_invoker(self, request):
        http_info = self._retry_upgrade_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _retry_upgrade_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/upgrade/{action_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryUpgradeTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []
        if 'retry_mode' in local_var_params:
            query_params.append(('retry_mode', local_var_params['retry_mode']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_create_policy_async(self, request):
        """查询自动创建快照的策略

        该接口用于查询自动创建快照策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoCreatePolicy
        :type request: :class:`huaweicloudsdkcss.v1.ShowAutoCreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowAutoCreatePolicyResponse`
        """
        http_info = self._show_auto_create_policy_http_info(request)
        return self._call_api(**http_info)

    def show_auto_create_policy_async_invoker(self, request):
        http_info = self._show_auto_create_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_create_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoCreatePolicyResponse"
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

    def show_cluster_detail_async(self, request):
        """查询集群详情

        该接口用于查询并显示单个集群详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterDetail
        :type request: :class:`huaweicloudsdkcss.v1.ShowClusterDetailRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowClusterDetailResponse`
        """
        http_info = self._show_cluster_detail_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_detail_async_invoker(self, request):
        http_info = self._show_cluster_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterDetailResponse"
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

    def show_cluster_tag_async(self, request):
        """查询指定集群的标签

        该接口用于查询指定集群的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClusterTag
        :type request: :class:`huaweicloudsdkcss.v1.ShowClusterTagRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowClusterTagResponse`
        """
        http_info = self._show_cluster_tag_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_tag_async_invoker(self, request):
        http_info = self._show_cluster_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/{resource_type}/{cluster_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
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

    def show_elb_detail_async(self, request):
        """获取该esELB的信息，以及页面需要展示健康检查状态

        该接口用于获取该esELB的信息，以及页面需要展示健康检查状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowElbDetail
        :type request: :class:`huaweicloudsdkcss.v1.ShowElbDetailRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowElbDetailResponse`
        """
        http_info = self._show_elb_detail_http_info(request)
        return self._call_api(**http_info)

    def show_elb_detail_async_invoker(self, request):
        http_info = self._show_elb_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_elb_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/es-listeners",
            "request_type": request.__class__.__name__,
            "response_type": "ShowElbDetailResponse"
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

    def show_get_log_setting_async(self, request):
        """查询日志基础配置

        该接口用于日志基础配置查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGetLogSetting
        :type request: :class:`huaweicloudsdkcss.v1.ShowGetLogSettingRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowGetLogSettingResponse`
        """
        http_info = self._show_get_log_setting_http_info(request)
        return self._call_api(**http_info)

    def show_get_log_setting_async_invoker(self, request):
        http_info = self._show_get_log_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_get_log_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/settings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetLogSettingResponse"
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

    def show_ik_thesaurus_async(self, request):
        """查询自定义词库状态

        该接口用于查询自定义词库的加载状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIkThesaurus
        :type request: :class:`huaweicloudsdkcss.v1.ShowIkThesaurusRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowIkThesaurusResponse`
        """
        http_info = self._show_ik_thesaurus_http_info(request)
        return self._call_api(**http_info)

    def show_ik_thesaurus_async_invoker(self, request):
        http_info = self._show_ik_thesaurus_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ik_thesaurus_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/thesaurus",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIkThesaurusResponse"
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

    def show_log_backup_async(self, request):
        """查询日志

        该接口用于查询日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLogBackup
        :type request: :class:`huaweicloudsdkcss.v1.ShowLogBackupRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowLogBackupResponse`
        """
        http_info = self._show_log_backup_http_info(request)
        return self._call_api(**http_info)

    def show_log_backup_async_invoker(self, request):
        http_info = self._show_log_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_log_backup_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogBackupResponse"
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

    def show_vpcep_connection_async(self, request):
        """获取终端节点连接

        该接口用于获取终端节点连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpcepConnection
        :type request: :class:`huaweicloudsdkcss.v1.ShowVpcepConnectionRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowVpcepConnectionResponse`
        """
        http_info = self._show_vpcep_connection_http_info(request)
        return self._call_api(**http_info)

    def show_vpcep_connection_async_invoker(self, request):
        http_info = self._show_vpcep_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpcep_connection_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpcepConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
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

    def start_auto_setting_async(self, request):
        """自动设置集群快照的基础配置（不推荐使用）

        该接口用于自动设置集群快照的基础配置，包括配置OBS桶和IAM委托。
        
        
        - “OBS桶”：快照存储的OBS桶位置。
        
        - “备份路径”：快照在OBS桶中的存放路径。
        
        - “IAM委托”：由于需要将快照保存在OBS中，所以需要在IAM中设置对应的委托获取对OBS服务的授权。
        
        &gt;自动设置集群快照接口将会自动创建快照OBS桶和委托。如果有多个集群，每个集群使用这个接口都会创建一个不一样的OBS桶，可能会导致OBS的配额不够，较多的OBS桶也难以维护。建议可以直接使用[修改集群快照的基础配置](UpdateSnapshotSetting.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartAutoSetting
        :type request: :class:`huaweicloudsdkcss.v1.StartAutoSettingRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartAutoSettingResponse`
        """
        http_info = self._start_auto_setting_http_info(request)
        return self._call_api(**http_info)

    def start_auto_setting_async_invoker(self, request):
        http_info = self._start_auto_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_auto_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/auto_setting",
            "request_type": request.__class__.__name__,
            "response_type": "StartAutoSettingResponse"
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

    def start_log_auto_backup_policy_async(self, request):
        """开启日志自动备份策略

        该接口用于日志自动备份策略开启。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartLogAutoBackupPolicy
        :type request: :class:`huaweicloudsdkcss.v1.StartLogAutoBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartLogAutoBackupPolicyResponse`
        """
        http_info = self._start_log_auto_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def start_log_auto_backup_policy_async_invoker(self, request):
        http_info = self._start_log_auto_backup_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_log_auto_backup_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/policy/update",
            "request_type": request.__class__.__name__,
            "response_type": "StartLogAutoBackupPolicyResponse"
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

    def start_logs_async(self, request):
        """开启日志功能

        该接口用于开启日志功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartLogs
        :type request: :class:`huaweicloudsdkcss.v1.StartLogsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartLogsResponse`
        """
        http_info = self._start_logs_http_info(request)
        return self._call_api(**http_info)

    def start_logs_async_invoker(self, request):
        http_info = self._start_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_logs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/open",
            "request_type": request.__class__.__name__,
            "response_type": "StartLogsResponse"
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

    def start_public_whitelist_async(self, request):
        """开启公网访问控制白名单

        该接口用于开启公网访问控制白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartPublicWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.StartPublicWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartPublicWhitelistResponse`
        """
        http_info = self._start_public_whitelist_http_info(request)
        return self._call_api(**http_info)

    def start_public_whitelist_async_invoker(self, request):
        http_info = self._start_public_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_public_whitelist_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/public/whitelist/update",
            "request_type": request.__class__.__name__,
            "response_type": "StartPublicWhitelistResponse"
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

    def start_vpecp_async(self, request):
        """开启终端节点服务

        该接口用于开启终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartVpecp
        :type request: :class:`huaweicloudsdkcss.v1.StartVpecpRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartVpecpResponse`
        """
        http_info = self._start_vpecp_http_info(request)
        return self._call_api(**http_info)

    def start_vpecp_async_invoker(self, request):
        http_info = self._start_vpecp_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_vpecp_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/open",
            "request_type": request.__class__.__name__,
            "response_type": "StartVpecpResponse"
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

    def stop_log_auto_backup_policy_async(self, request):
        """关闭日志自动备份策略

        该接口用于日志自动备份策略关闭。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopLogAutoBackupPolicy
        :type request: :class:`huaweicloudsdkcss.v1.StopLogAutoBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopLogAutoBackupPolicyResponse`
        """
        http_info = self._stop_log_auto_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def stop_log_auto_backup_policy_async_invoker(self, request):
        http_info = self._stop_log_auto_backup_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_log_auto_backup_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/policy/close",
            "request_type": request.__class__.__name__,
            "response_type": "StopLogAutoBackupPolicyResponse"
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

    def stop_logs_async(self, request):
        """关闭日志功能

        该接口用于关闭日志功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopLogs
        :type request: :class:`huaweicloudsdkcss.v1.StopLogsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopLogsResponse`
        """
        http_info = self._stop_logs_http_info(request)
        return self._call_api(**http_info)

    def stop_logs_async_invoker(self, request):
        http_info = self._stop_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_logs_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/close",
            "request_type": request.__class__.__name__,
            "response_type": "StopLogsResponse"
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

    def stop_public_whitelist_async(self, request):
        """关闭公网访问控制白名单

        该接口用于关闭公网访问控制白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopPublicWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.StopPublicWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopPublicWhitelistResponse`
        """
        http_info = self._stop_public_whitelist_http_info(request)
        return self._call_api(**http_info)

    def stop_public_whitelist_async_invoker(self, request):
        http_info = self._stop_public_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_public_whitelist_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/public/whitelist/close",
            "request_type": request.__class__.__name__,
            "response_type": "StopPublicWhitelistResponse"
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

    def stop_snapshot_async(self, request):
        """停用快照功能

        该接口用于停用快照功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopSnapshot
        :type request: :class:`huaweicloudsdkcss.v1.StopSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopSnapshotResponse`
        """
        http_info = self._stop_snapshot_http_info(request)
        return self._call_api(**http_info)

    def stop_snapshot_async_invoker(self, request):
        http_info = self._stop_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_snapshot_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "StopSnapshotResponse"
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

    def stop_vpecp_async(self, request):
        """关闭终端节点服务

        该接口用于关闭终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopVpecp
        :type request: :class:`huaweicloudsdkcss.v1.StopVpecpRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopVpecpResponse`
        """
        http_info = self._stop_vpecp_http_info(request)
        return self._call_api(**http_info)

    def stop_vpecp_async_invoker(self, request):
        http_info = self._stop_vpecp_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_vpecp_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/close",
            "request_type": request.__class__.__name__,
            "response_type": "StopVpecpResponse"
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

    def update_az_by_instance_type_async(self, request):
        """切换集群实例AZ

        该接口通过指定节点类型切换AZ。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAzByInstanceType
        :type request: :class:`huaweicloudsdkcss.v1.UpdateAzByInstanceTypeRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateAzByInstanceTypeResponse`
        """
        http_info = self._update_az_by_instance_type_http_info(request)
        return self._call_api(**http_info)

    def update_az_by_instance_type_async_invoker(self, request):
        http_info = self._update_az_by_instance_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_az_by_instance_type_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/inst-type/{inst_type}/azmigrate",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAzByInstanceTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'inst_type' in local_var_params:
            path_params['inst_type'] = local_var_params['inst_type']

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

    def update_batch_clusters_tags_async(self, request):
        """批量添加或删除集群标签

        该接口用于对集群批量添加或删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBatchClustersTags
        :type request: :class:`huaweicloudsdkcss.v1.UpdateBatchClustersTagsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateBatchClustersTagsResponse`
        """
        http_info = self._update_batch_clusters_tags_http_info(request)
        return self._call_api(**http_info)

    def update_batch_clusters_tags_async_invoker(self, request):
        http_info = self._update_batch_clusters_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_batch_clusters_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/{resource_type}/{cluster_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBatchClustersTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def update_cluster_name_async(self, request):
        """修改集群名称

        该接口用于修改集群名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateClusterName
        :type request: :class:`huaweicloudsdkcss.v1.UpdateClusterNameRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateClusterNameResponse`
        """
        http_info = self._update_cluster_name_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_name_async_invoker(self, request):
        http_info = self._update_cluster_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cluster_name_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/changename",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterNameResponse"
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

    def update_es_listener_async(self, request):
        """更新es监听器

        该接口用于更新es监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEsListener
        :type request: :class:`huaweicloudsdkcss.v1.UpdateEsListenerRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateEsListenerResponse`
        """
        http_info = self._update_es_listener_http_info(request)
        return self._call_api(**http_info)

    def update_es_listener_async_invoker(self, request):
        http_info = self._update_es_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_es_listener_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/es-listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEsListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def update_extend_cluster_async(self, request):
        """扩容集群

        该接口用于集群扩容实例（仅支持扩容elasticsearch实例）。只扩容普通节点，且只针对要扩容的集群实例不存在特殊节点（Master、Client、冷数据节点）的情况。
        
        集群扩容实例的数量和存储容量，请参考[扩容实例的数量和存储容量](UpdateExtendInstanceStorage.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateExtendCluster
        :type request: :class:`huaweicloudsdkcss.v1.UpdateExtendClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateExtendClusterResponse`
        """
        http_info = self._update_extend_cluster_http_info(request)
        return self._call_api(**http_info)

    def update_extend_cluster_async_invoker(self, request):
        http_info = self._update_extend_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_extend_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateExtendClusterResponse"
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

    def update_extend_instance_storage_async(self, request):
        """扩容实例的数量和存储容量

        该接口用于集群扩容不同类型实例的个数以及存储容量。已经存在独立Master、Client、冷数据节点的集群使用该接口扩容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateExtendInstanceStorage
        :type request: :class:`huaweicloudsdkcss.v1.UpdateExtendInstanceStorageRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateExtendInstanceStorageResponse`
        """
        http_info = self._update_extend_instance_storage_http_info(request)
        return self._call_api(**http_info)

    def update_extend_instance_storage_async_invoker(self, request):
        http_info = self._update_extend_instance_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_extend_instance_storage_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/role_extend",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateExtendInstanceStorageResponse"
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

    def update_flavor_async(self, request):
        """变更规格

        该接口用于变更集群规格。只支持变更ess节点类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFlavor
        :type request: :class:`huaweicloudsdkcss.v1.UpdateFlavorRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateFlavorResponse`
        """
        http_info = self._update_flavor_http_info(request)
        return self._call_api(**http_info)

    def update_flavor_async_invoker(self, request):
        http_info = self._update_flavor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_flavor_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/flavor",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFlavorResponse"
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

    def update_flavor_by_type_async(self, request):
        """指定节点类型规格变更

        修改集群规格。支持修改:
        - ess： 数据节点。
        - ess-cold: 冷数据节点。
        - ess-client: Client节点。
        - ess-master: Master节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFlavorByType
        :type request: :class:`huaweicloudsdkcss.v1.UpdateFlavorByTypeRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateFlavorByTypeResponse`
        """
        http_info = self._update_flavor_by_type_http_info(request)
        return self._call_api(**http_info)

    def update_flavor_by_type_async_invoker(self, request):
        http_info = self._update_flavor_by_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_flavor_by_type_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/{types}/flavor",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFlavorByTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'types' in local_var_params:
            path_params['types'] = local_var_params['types']

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

    def update_instance_async(self, request):
        """节点替换

        该接口用于替换失败节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkcss.v1.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateInstanceResponse`
        """
        http_info = self._update_instance_http_info(request)
        return self._call_api(**http_info)

    def update_instance_async_invoker(self, request):
        http_info = self._update_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/instance/{instance_id}/replace",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
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

    def update_log_setting_async(self, request):
        """修改日志基础配置

        该接口用于修改日志基础配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLogSetting
        :type request: :class:`huaweicloudsdkcss.v1.UpdateLogSettingRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateLogSettingResponse`
        """
        http_info = self._update_log_setting_http_info(request)
        return self._call_api(**http_info)

    def update_log_setting_async_invoker(self, request):
        http_info = self._update_log_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_log_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/logs/settings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogSettingResponse"
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

    def update_ondemand_cluster_to_period_async(self, request):
        """按需集群转包周期

        该接口用于按需集群转包周期集群。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOndemandClusterToPeriod
        :type request: :class:`huaweicloudsdkcss.v1.UpdateOndemandClusterToPeriodRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateOndemandClusterToPeriodResponse`
        """
        http_info = self._update_ondemand_cluster_to_period_http_info(request)
        return self._call_api(**http_info)

    def update_ondemand_cluster_to_period_async_invoker(self, request):
        http_info = self._update_ondemand_cluster_to_period_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ondemand_cluster_to_period_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/cluster/{cluster_id}/period",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOndemandClusterToPeriodResponse"
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

    def update_public_band_width_async(self, request):
        """修改公网访问带宽

        该接口用于修改公网访问带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicBandWidth
        :type request: :class:`huaweicloudsdkcss.v1.UpdatePublicBandWidthRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdatePublicBandWidthResponse`
        """
        http_info = self._update_public_band_width_http_info(request)
        return self._call_api(**http_info)

    def update_public_band_width_async_invoker(self, request):
        http_info = self._update_public_band_width_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_public_band_width_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/public/bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicBandWidthResponse"
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

    def update_shrink_cluster_async(self, request):
        """指定节点类型缩容

        该接口用于集群对不同类型实例的个数以及存储容量进行缩容。包周期类型的集群不支持通过api进行指定节点类型缩容操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateShrinkCluster
        :type request: :class:`huaweicloudsdkcss.v1.UpdateShrinkClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateShrinkClusterResponse`
        """
        http_info = self._update_shrink_cluster_http_info(request)
        return self._call_api(**http_info)

    def update_shrink_cluster_async_invoker(self, request):
        http_info = self._update_shrink_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_shrink_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/extend/{project_id}/clusters/{cluster_id}/role/shrink",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateShrinkClusterResponse"
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

    def update_shrink_nodes_async(self, request):
        """指定节点缩容

        该接口可以对集群现有节点中指定节点进行缩容。包周期类型的集群不支持通过api进行指定节点缩容操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateShrinkNodes
        :type request: :class:`huaweicloudsdkcss.v1.UpdateShrinkNodesRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateShrinkNodesResponse`
        """
        http_info = self._update_shrink_nodes_http_info(request)
        return self._call_api(**http_info)

    def update_shrink_nodes_async_invoker(self, request):
        http_info = self._update_shrink_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_shrink_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/node/offline",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateShrinkNodesResponse"
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

    def update_snapshot_setting_async(self, request):
        """修改集群快照的基础配置

        该接口用于修改集群快照的基础配置，可修改OBS桶和IAM委托。
        
        可以使用该接口开启快照功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSnapshotSetting
        :type request: :class:`huaweicloudsdkcss.v1.UpdateSnapshotSettingRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateSnapshotSettingResponse`
        """
        http_info = self._update_snapshot_setting_http_info(request)
        return self._call_api(**http_info)

    def update_snapshot_setting_async_invoker(self, request):
        http_info = self._update_snapshot_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_snapshot_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/setting",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSnapshotSettingResponse"
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

    def update_unbind_public_async(self, request):
        """关闭公网访问

        该接口用于关闭公网访问。包周期类型的集群不支持通过api进行关闭公网访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUnbindPublic
        :type request: :class:`huaweicloudsdkcss.v1.UpdateUnbindPublicRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateUnbindPublicResponse`
        """
        http_info = self._update_unbind_public_http_info(request)
        return self._call_api(**http_info)

    def update_unbind_public_async_invoker(self, request):
        http_info = self._update_unbind_public_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_unbind_public_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/public/close",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUnbindPublicResponse"
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

    def update_vpcep_connection_async(self, request):
        """更新终端节点连接

        该接口用于更新终端节点连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpcepConnection
        :type request: :class:`huaweicloudsdkcss.v1.UpdateVpcepConnectionRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateVpcepConnectionResponse`
        """
        http_info = self._update_vpcep_connection_http_info(request)
        return self._call_api(**http_info)

    def update_vpcep_connection_async_invoker(self, request):
        http_info = self._update_vpcep_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpcep_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/connections",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpcepConnectionResponse"
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

    def update_vpcep_whitelist_async(self, request):
        """修改终端节点服务白名单

        该接口用于修改终端节点服务白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpcepWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.UpdateVpcepWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateVpcepWhitelistResponse`
        """
        http_info = self._update_vpcep_whitelist_http_info(request)
        return self._call_api(**http_info)

    def update_vpcep_whitelist_async_invoker(self, request):
        http_info = self._update_vpcep_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpcep_whitelist_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/permissions",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpcepWhitelistResponse"
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

    def update_ymls_async(self, request):
        """修改参数配置

        该接口用于修改参数配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateYmls
        :type request: :class:`huaweicloudsdkcss.v1.UpdateYmlsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateYmlsResponse`
        """
        http_info = self._update_ymls_http_info(request)
        return self._call_api(**http_info)

    def update_ymls_async_invoker(self, request):
        http_info = self._update_ymls_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ymls_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/ymls/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateYmlsResponse"
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

    def upgrade_core_async(self, request):
        """集群内核升级

        该接口用于将低版本的ES升级到高版本或同版本ES。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeCore
        :type request: :class:`huaweicloudsdkcss.v1.UpgradeCoreRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpgradeCoreResponse`
        """
        http_info = self._upgrade_core_http_info(request)
        return self._call_api(**http_info)

    def upgrade_core_async_invoker(self, request):
        http_info = self._upgrade_core_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_core_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/inst-type/{inst_type}/image/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeCoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'inst_type' in local_var_params:
            path_params['inst_type'] = local_var_params['inst_type']

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

    def upgrade_detail_async(self, request):
        """获取升级详情信息

        由于升级过程时间较长，该接口可以展示当前升级（切换AZ）节点的各个阶段信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeDetail
        :type request: :class:`huaweicloudsdkcss.v1.UpgradeDetailRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpgradeDetailResponse`
        """
        http_info = self._upgrade_detail_http_info(request)
        return self._call_api(**http_info)

    def upgrade_detail_async_invoker(self, request):
        http_info = self._upgrade_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/upgrade/detail",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'action_mode' in local_var_params:
            query_params.append(('action_mode', local_var_params['action_mode']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_kibana_public_async(self, request):
        """开启Kibana公网访问

        该接口用于开启Kibana公网访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartKibanaPublic
        :type request: :class:`huaweicloudsdkcss.v1.StartKibanaPublicRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartKibanaPublicResponse`
        """
        http_info = self._start_kibana_public_http_info(request)
        return self._call_api(**http_info)

    def start_kibana_public_async_invoker(self, request):
        http_info = self._start_kibana_public_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_kibana_public_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/publickibana/open",
            "request_type": request.__class__.__name__,
            "response_type": "StartKibanaPublicResponse"
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

    def stop_public_kibana_whitelist_async(self, request):
        """关闭Kibana公网访问控制

        该接口用于关闭Kibana公网访问控制。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopPublicKibanaWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.StopPublicKibanaWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopPublicKibanaWhitelistResponse`
        """
        http_info = self._stop_public_kibana_whitelist_http_info(request)
        return self._call_api(**http_info)

    def stop_public_kibana_whitelist_async_invoker(self, request):
        http_info = self._stop_public_kibana_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_public_kibana_whitelist_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/publickibana/whitelist/close",
            "request_type": request.__class__.__name__,
            "response_type": "StopPublicKibanaWhitelistResponse"
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

    def update_alter_kibana_async(self, request):
        """修改Kibana公网带宽

        该接口用于修改Kibana公网带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlterKibana
        :type request: :class:`huaweicloudsdkcss.v1.UpdateAlterKibanaRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateAlterKibanaResponse`
        """
        http_info = self._update_alter_kibana_http_info(request)
        return self._call_api(**http_info)

    def update_alter_kibana_async_invoker(self, request):
        http_info = self._update_alter_kibana_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_alter_kibana_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/publickibana/bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlterKibanaResponse"
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

    def update_close_kibana_async(self, request):
        """关闭Kibana公网访问

        该接口用于关闭Kibana公网访问。包周期类型集群不支持通过api进行关闭Kibana公网访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCloseKibana
        :type request: :class:`huaweicloudsdkcss.v1.UpdateCloseKibanaRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateCloseKibanaResponse`
        """
        http_info = self._update_close_kibana_http_info(request)
        return self._call_api(**http_info)

    def update_close_kibana_async_invoker(self, request):
        http_info = self._update_close_kibana_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_close_kibana_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/publickibana/close",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCloseKibanaResponse"
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

    def update_public_kibana_whitelist_async(self, request):
        """修改Kibana公网访问控制

        该接口通过修改kibana白名单，修改kibana的访问权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicKibanaWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.UpdatePublicKibanaWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdatePublicKibanaWhitelistResponse`
        """
        http_info = self._update_public_kibana_whitelist_http_info(request)
        return self._call_api(**http_info)

    def update_public_kibana_whitelist_async_invoker(self, request):
        http_info = self._update_public_kibana_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_public_kibana_whitelist_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/publickibana/whitelist/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicKibanaWhitelistResponse"
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

    def add_favorite_async(self, request):
        """添加到自定义模板

        该接口用于添加到自定义模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddFavorite
        :type request: :class:`huaweicloudsdkcss.v1.AddFavoriteRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.AddFavoriteResponse`
        """
        http_info = self._add_favorite_http_info(request)
        return self._call_api(**http_info)

    def add_favorite_async_invoker(self, request):
        http_info = self._add_favorite_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_favorite_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/favorite",
            "request_type": request.__class__.__name__,
            "response_type": "AddFavoriteResponse"
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

    def create_cnf_async(self, request):
        """创建配置文件

        该接口用于创建配置文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCnf
        :type request: :class:`huaweicloudsdkcss.v1.CreateCnfRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateCnfResponse`
        """
        http_info = self._create_cnf_http_info(request)
        return self._call_api(**http_info)

    def create_cnf_async_invoker(self, request):
        http_info = self._create_cnf_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cnf_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/submit",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCnfResponse"
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

    def delete_conf_async(self, request):
        """删除配置文件

        删除配置文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConf
        :type request: :class:`huaweicloudsdkcss.v1.DeleteConfRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteConfResponse`
        """
        http_info = self._delete_conf_http_info(request)
        return self._call_api(**http_info)

    def delete_conf_async_invoker(self, request):
        http_info = self._delete_conf_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_conf_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfResponse"
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

    def delete_config_async(self, request):
        """删除配置文件V2

        删除配置文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfig
        :type request: :class:`huaweicloudsdkcss.v1.DeleteConfigRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteConfigResponse`
        """
        http_info = self._delete_config_http_info(request)
        return self._call_api(**http_info)

    def delete_config_async_invoker(self, request):
        http_info = self._delete_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/clusters/{cluster_id}/lgsconf/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfigResponse"
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

    def delete_template_async(self, request):
        """删除自定义模板

        该接口用于删除自定义模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkcss.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_async_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/lgsconf/deletetemplate",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
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

    def list_actions_async(self, request):
        """查询操作记录

        该接口用于查询操作记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListActions
        :type request: :class:`huaweicloudsdkcss.v1.ListActionsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListActionsResponse`
        """
        http_info = self._list_actions_http_info(request)
        return self._call_api(**http_info)

    def list_actions_async_invoker(self, request):
        http_info = self._list_actions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_actions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/listactions",
            "request_type": request.__class__.__name__,
            "response_type": "ListActionsResponse"
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

    def list_certs_async(self, request):
        """查询证书列表

        该接口用于查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCerts
        :type request: :class:`huaweicloudsdkcss.v1.ListCertsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListCertsResponse`
        """
        http_info = self._list_certs_http_info(request)
        return self._call_api(**http_info)

    def list_certs_async_invoker(self, request):
        http_info = self._list_certs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_certs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/certs",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'certs_type' in local_var_params:
            query_params.append(('certsType', local_var_params['certs_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_confs_async(self, request):
        """查询配置文件列表

        该接口用于查询配置文件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfs
        :type request: :class:`huaweicloudsdkcss.v1.ListConfsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListConfsResponse`
        """
        http_info = self._list_confs_http_info(request)
        return self._call_api(**http_info)

    def list_confs_async_invoker(self, request):
        http_info = self._list_confs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_confs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/listconfs",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfsResponse"
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

    def list_pipelines_async(self, request):
        """查询pipeline列表

        该接口用于查询pipeline列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPipelines
        :type request: :class:`huaweicloudsdkcss.v1.ListPipelinesRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListPipelinesResponse`
        """
        http_info = self._list_pipelines_http_info(request)
        return self._call_api(**http_info)

    def list_pipelines_async_invoker(self, request):
        http_info = self._list_pipelines_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pipelines_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/listpipelines",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipelinesResponse"
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

    def list_templates_async(self, request):
        """查询模板列表

        该接口用于查询模板列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkcss.v1.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_async_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/lgsconf/template",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def show_get_conf_detail_async(self, request):
        """查询配置文件内容

        该接口用于查询配置文件内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGetConfDetail
        :type request: :class:`huaweicloudsdkcss.v1.ShowGetConfDetailRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowGetConfDetailResponse`
        """
        http_info = self._show_get_conf_detail_http_info(request)
        return self._call_api(**http_info)

    def show_get_conf_detail_async_invoker(self, request):
        http_info = self._show_get_conf_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_get_conf_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/confdetail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetConfDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def start_connectivity_test_async(self, request):
        """连通性测试

        该接口用于连通性测试。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartConnectivityTest
        :type request: :class:`huaweicloudsdkcss.v1.StartConnectivityTestRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartConnectivityTestResponse`
        """
        http_info = self._start_connectivity_test_http_info(request)
        return self._call_api(**http_info)

    def start_connectivity_test_async_invoker(self, request):
        http_info = self._start_connectivity_test_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_connectivity_test_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/checkconnection",
            "request_type": request.__class__.__name__,
            "response_type": "StartConnectivityTestResponse"
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

    def start_pipeline_async(self, request):
        """启动pipeline迁移数据

        该接口用于启动pipeline迁移数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartPipeline
        :type request: :class:`huaweicloudsdkcss.v1.StartPipelineRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartPipelineResponse`
        """
        http_info = self._start_pipeline_http_info(request)
        return self._call_api(**http_info)

    def start_pipeline_async_invoker(self, request):
        http_info = self._start_pipeline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_pipeline_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartPipelineResponse"
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

    def stop_hot_pipeline_async(self, request):
        """热停止pipeline迁移数据。

        该接口用于热停止pipeline迁移数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopHotPipeline
        :type request: :class:`huaweicloudsdkcss.v1.StopHotPipelineRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopHotPipelineResponse`
        """
        http_info = self._stop_hot_pipeline_http_info(request)
        return self._call_api(**http_info)

    def stop_hot_pipeline_async_invoker(self, request):
        http_info = self._stop_hot_pipeline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_hot_pipeline_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/hot-stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopHotPipelineResponse"
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

    def stop_pipeline_async(self, request):
        """停止pipeline迁移数据

        该接口用于停止pipeline迁移数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopPipeline
        :type request: :class:`huaweicloudsdkcss.v1.StopPipelineRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopPipelineResponse`
        """
        http_info = self._stop_pipeline_http_info(request)
        return self._call_api(**http_info)

    def stop_pipeline_async_invoker(self, request):
        http_info = self._stop_pipeline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_pipeline_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopPipelineResponse"
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

    def update_cnf_async(self, request):
        """更新配置文件

        该接口用于更新配置文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCnf
        :type request: :class:`huaweicloudsdkcss.v1.UpdateCnfRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateCnfResponse`
        """
        http_info = self._update_cnf_http_info(request)
        return self._call_api(**http_info)

    def update_cnf_async_invoker(self, request):
        http_info = self._update_cnf_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cnf_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCnfResponse"
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

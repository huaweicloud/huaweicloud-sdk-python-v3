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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmrs'")


class MrsClient(Client):
    def __init__(self):
        super(MrsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmrs.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "MrsClient":
                raise TypeError("client type error, support client type is MrsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_cluster_tags(self, request):
        """批量添加集群标签

        为指定集群批量添加标签。
        
        一个集群上最多有10个标签。
        
        此接口为幂等接口：
        
        - 创建时，同一个集群不允许重复key，如果数据库存在就覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateClusterTags
        :type request: :class:`huaweicloudsdkmrs.v1.BatchCreateClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.BatchCreateClusterTagsResponse`
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
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/tags/action",
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
        """批量删除集群标签

        为指定集群批量删除标签。
        
        一个集群上最多有10个标签。
        
        此接口为幂等接口：
        
        -
        删除时，如果删除的标签不存在，默认处理成功，删除时不对标签字符集范围做校验。Key长度36个unicode字符，value为43个unicode字符。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteClusterTags
        :type request: :class:`huaweicloudsdkmrs.v1.BatchDeleteClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.BatchDeleteClusterTagsResponse`
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
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/tags/action",
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

    def create_and_execute_job(self, request):
        """新增作业并执行（废弃）

        如需使用作业管理接口请参考apiv2接口使用，本接口后续不再进行维护。
        在MRS集群中新增一个作业，并执行作业。该接口不兼容Sahara。
        集群ID可参考[查询集群列表](https://support.huaweicloud.com/api-mrs/ListClusters.html)接口获取。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAndExecuteJob
        :type request: :class:`huaweicloudsdkmrs.v1.CreateAndExecuteJobRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.CreateAndExecuteJobResponse`
        """
        http_info = self._create_and_execute_job_http_info(request)
        return self._call_api(**http_info)

    def create_and_execute_job_invoker(self, request):
        http_info = self._create_and_execute_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_and_execute_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/jobs/submit-job",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAndExecuteJobResponse"
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

    def create_cluster(self, request):
        """创建集群并执行作业

        创建一个MRS集群，并在集群中提交一个作业。该接口不兼容Sahara。
        支持同一时间并发创建10个集群。
        使用接口前，您需要先获取下的资源信息。
        - 通过VPC创建或查询VPC、子网
        - 通过ECS创建或查询密钥对
        - 通过[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)获取区域信息
        - 参考[MRS服务支持的组件](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)获取MRS版本及对应版本支持的组件信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkmrs.v1.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.CreateClusterResponse`
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
            "resource_path": "/v1.1/{project_id}/run-job-flow",
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

    def create_cluster_tag(self, request):
        """给指定集群添加标签

        为特定的集群添加一个tag。
        一个集群上最多有10个标签，此接口为幂等接口。添加标签时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterTag
        :type request: :class:`huaweicloudsdkmrs.v1.CreateClusterTagRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.CreateClusterTagResponse`
        """
        http_info = self._create_cluster_tag_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_tag_invoker(self, request):
        http_info = self._create_cluster_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterTagResponse"
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

    def create_scaling_policy(self, request):
        """配置弹性伸缩规则

        对弹性伸缩规则进行编辑。
        
        在创建集群并执行作业接口中也可以创建弹性伸缩规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScalingPolicy
        :type request: :class:`huaweicloudsdkmrs.v1.CreateScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.CreateScalingPolicyResponse`
        """
        http_info = self._create_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def create_scaling_policy_invoker(self, request):
        http_info = self._create_scaling_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_scaling_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/autoscaling-policy/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScalingPolicyResponse"
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

    def delete_cluster(self, request):
        """删除集群

        数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。
        
        处于如下状态的集群不允许删除：
        - scaling-out：扩容中
        - scaling-in：缩容中
        - starting：启动中
        - terminating：删除中
        - terminated：已删除
        - failed：失败
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkmrs.v1.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.DeleteClusterResponse`
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
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}",
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

    def delete_cluster_tag(self, request):
        """删除指定集群的标签

        删除特定集群的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClusterTag
        :type request: :class:`huaweicloudsdkmrs.v1.DeleteClusterTagRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.DeleteClusterTagResponse`
        """
        http_info = self._delete_cluster_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_tag_invoker(self, request):
        http_info = self._delete_cluster_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cluster_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClusterTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
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

    def delete_job_execution(self, request):
        """删除作业执行对象（废弃）

        如需使用作业管理接口请参考apiv2接口使用，本接口后续不再进行维护。
        删除指定的作业执行对象。该接口兼容Sahara。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteJobExecution
        :type request: :class:`huaweicloudsdkmrs.v1.DeleteJobExecutionRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.DeleteJobExecutionResponse`
        """
        http_info = self._delete_job_execution_http_info(request)
        return self._call_api(**http_info)

    def delete_job_execution_invoker(self, request):
        http_info = self._delete_job_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_job_execution_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.1/{project_id}/job-executions/{job_execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteJobExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_execution_id' in local_var_params:
            path_params['job_execution_id'] = local_var_params['job_execution_id']

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

    def list_all_tags(self, request):
        """查询所有标签

        查询租户在指定Region下的所有标签集合 。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllTags
        :type request: :class:`huaweicloudsdkmrs.v1.ListAllTagsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ListAllTagsResponse`
        """
        http_info = self._list_all_tags_http_info(request)
        return self._call_api(**http_info)

    def list_all_tags_invoker(self, request):
        http_info = self._list_all_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/clusters/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllTagsResponse"
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

    def list_cluster_tags(self, request):
        """查询指定集群的标签

        查询指定集群的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterTags
        :type request: :class:`huaweicloudsdkmrs.v1.ListClusterTagsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ListClusterTagsResponse`
        """
        http_info = self._list_cluster_tags_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_tags_invoker(self, request):
        http_info = self._list_cluster_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cluster_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/tags",
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

    def list_clusters(self, request):
        """查询集群列表

        查看用户创建的集群列表信息。该接口不兼容Sahara。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusters
        :type request: :class:`huaweicloudsdkmrs.v1.ListClustersRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ListClustersResponse`
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
            "resource_path": "/v1.1/{project_id}/cluster_infos",
            "request_type": request.__class__.__name__,
            "response_type": "ListClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'current_page' in local_var_params:
            query_params.append(('currentPage', local_var_params['current_page']))
        if 'cluster_name' in local_var_params:
            query_params.append(('clusterName', local_var_params['cluster_name']))
        if 'cluster_state' in local_var_params:
            query_params.append(('clusterState', local_var_params['cluster_state']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterpriseProjectId', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_clusters_by_tags(self, request):
        """查询特定标签的集群列表

        使用标签过滤集群。
        
        集群默认按照创建时间倒序，集群tag也按照创建时间倒序。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClustersByTags
        :type request: :class:`huaweicloudsdkmrs.v1.ListClustersByTagsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ListClustersByTagsResponse`
        """
        http_info = self._list_clusters_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_clusters_by_tags_invoker(self, request):
        http_info = self._list_clusters_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_clusters_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/clusters/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListClustersByTagsResponse"
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

    def list_execute_job(self, request):
        """查询作业exe对象列表（废弃）

        如需使用作业管理接口请参考apiv2接口使用，本接口后续不再进行维护。
        查询所有作业的exe对象列表。该接口不兼容Sahara。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExecuteJob
        :type request: :class:`huaweicloudsdkmrs.v1.ListExecuteJobRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ListExecuteJobResponse`
        """
        http_info = self._list_execute_job_http_info(request)
        return self._call_api(**http_info)

    def list_execute_job_invoker(self, request):
        http_info = self._list_execute_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_execute_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/job-exes",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecuteJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'current_page' in local_var_params:
            query_params.append(('current_page', local_var_params['current_page']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_hosts(self, request):
        """查询主机列表

        该接口用于查询输入集群的主机列表详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHosts
        :type request: :class:`huaweicloudsdkmrs.v1.ListHostsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ListHostsResponse`
        """
        http_info = self._list_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_hosts_invoker(self, request):
        http_info = self._list_hosts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_hosts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'current_page' in local_var_params:
            query_params.append(('currentPage', local_var_params['current_page']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cluster_details(self, request):
        """查询集群详情

        查看指定集群的详细信息。该接口不兼容Sahara。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterDetails
        :type request: :class:`huaweicloudsdkmrs.v1.ShowClusterDetailsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ShowClusterDetailsResponse`
        """
        http_info = self._show_cluster_details_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_details_invoker(self, request):
        http_info = self._show_cluster_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/cluster_infos/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterDetailsResponse"
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

    def show_job_exes(self, request):
        """查询作业exe对象详情（废弃）

        如需使用作业管理接口请参考apiv2接口使用，本接口后续不再进行维护。
        查询指定作业的exe对象详细信息。该接口不兼容Sahara。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobExes
        :type request: :class:`huaweicloudsdkmrs.v1.ShowJobExesRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ShowJobExesResponse`
        """
        http_info = self._show_job_exes_http_info(request)
        return self._call_api(**http_info)

    def show_job_exes_invoker(self, request):
        http_info = self._show_job_exes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_exes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/job-exes/{job_exe_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobExesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_exe_id' in local_var_params:
            path_params['job_exe_id'] = local_var_params['job_exe_id']

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

    def update_cluster_scaling(self, request):
        """调整集群节点

        创建集群后，扩容/缩容集群Core节点或者Task节点。MRS集群创建成功后不支持调整Master节点数量，即不支持扩缩容Master节点。该接口不兼容Sahara。
        处于running状态的集群才允许扩容/缩容，其他状态则不允许扩容/缩容。 集群状态和集群ID可参考[查询集群列表](https://support.huaweicloud.com/api-mrs/ListClusters.html)接口获取。 本章节的接口只支持流式集群、分析集群和混合集群，不支持自定义集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterScaling
        :type request: :class:`huaweicloudsdkmrs.v1.UpdateClusterScalingRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.UpdateClusterScalingResponse`
        """
        http_info = self._update_cluster_scaling_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_scaling_invoker(self, request):
        http_info = self._update_cluster_scaling_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_scaling_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.1/{project_id}/cluster_infos/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterScalingResponse"
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

    def list_available_zones(self, request):
        """查询可用区信息

        在创建集群时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableZones
        :type request: :class:`huaweicloudsdkmrs.v1.ListAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkmrs.v1.ListAvailableZonesResponse`
        """
        http_info = self._list_available_zones_http_info(request)
        return self._call_api(**http_info)

    def list_available_zones_invoker(self, request):
        http_info = self._list_available_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{region_id}/available-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region_id' in local_var_params:
            path_params['region_id'] = local_var_params['region_id']

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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

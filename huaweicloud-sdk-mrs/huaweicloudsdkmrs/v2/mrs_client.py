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
        self.model_package = importlib.import_module("huaweicloudsdkmrs.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "MrsClient":
                raise TypeError("client type error, support client type is MrsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_delete_jobs(self, request):
        """批量删除作业

        在MRS集群中批量删除作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteJobs
        :type request: :class:`huaweicloudsdkmrs.v2.BatchDeleteJobsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.BatchDeleteJobsResponse`
        """
        http_info = self._batch_delete_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_jobs_invoker(self, request):
        http_info = self._batch_delete_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/job-executions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteJobsResponse"
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

    def create_cluster(self, request):
        """创建集群

        创建一个MRS集群。使用接口前，您需要先获取下的资源信息。
        - 通过VPC创建或查询VPC、子网
        - 通过ECS创建或查询密钥对
        - 通过[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)获取区域信息
        - 参考[MRS服务支持的组件](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)获取MRS版本及对应版本支持的组件信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkmrs.v2.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.CreateClusterResponse`
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
            "resource_path": "/v2/{project_id}/clusters",
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

    def create_execute_job(self, request):
        """新增并执行作业

        在MRS集群中新增并提交一个作业。
        
        需要先在集群详情页的“概览”页签，单击“IAM用户同步”右侧的“同步”进行IAM用户同步，然后再通过该接口提交作业。
        
        如需使用OBS加密功能，请先参考“MRS用户指南 &gt; 管理现有集群 &gt; 作业管理 &gt; 使用OBS加密数据运行作业”页面进行相关配置后，再调用API接口运行作业。
        
        所有示例中涉及的OBS路径、样例文件及终端节点和AKSK，请提前准备并在提交请求时根据实际情况替换。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateExecuteJob
        :type request: :class:`huaweicloudsdkmrs.v2.CreateExecuteJobRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.CreateExecuteJobResponse`
        """
        http_info = self._create_execute_job_http_info(request)
        return self._call_api(**http_info)

    def create_execute_job_invoker(self, request):
        http_info = self._create_execute_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_execute_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/job-executions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExecuteJobResponse"
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

    def run_job_flow(self, request):
        """创建集群并提交作业

        创建一个MRS集群并提交作业，并支持作业完成后删除集群，支持MRS 1.8.9及以上集群版本使用。使用接口前，您需要先获取下的资源信息。
        - 通过VPC创建或查询VPC、子网
        - 通过ECS创建或查询密钥对
        - 通过[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)获取区域信息
        - 参考[MRS服务支持的组件](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)获取MRS版本及对应版本支持的组件信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunJobFlow
        :type request: :class:`huaweicloudsdkmrs.v2.RunJobFlowRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.RunJobFlowResponse`
        """
        http_info = self._run_job_flow_http_info(request)
        return self._call_api(**http_info)

    def run_job_flow_invoker(self, request):
        http_info = self._run_job_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_job_flow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/run-job-flow",
            "request_type": request.__class__.__name__,
            "response_type": "RunJobFlowResponse"
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

    def show_agency_mapping(self, request):
        """查询用户（组）与IAM委托的映射关系

        获取用户（组）与IAM委托之间的映射关系的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAgencyMapping
        :type request: :class:`huaweicloudsdkmrs.v2.ShowAgencyMappingRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowAgencyMappingResponse`
        """
        http_info = self._show_agency_mapping_http_info(request)
        return self._call_api(**http_info)

    def show_agency_mapping_invoker(self, request):
        http_info = self._show_agency_mapping_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_agency_mapping_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/agency-mapping",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgencyMappingResponse"
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

    def show_auto_scaling_policy(self, request):
        """查看弹性伸缩策略

        查看指定集群的所有的弹性伸缩策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoScalingPolicy
        :type request: :class:`huaweicloudsdkmrs.v2.ShowAutoScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowAutoScalingPolicyResponse`
        """
        http_info = self._show_auto_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def show_auto_scaling_policy_invoker(self, request):
        http_info = self._show_auto_scaling_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auto_scaling_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/autoscaling-policy/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoScalingPolicyResponse"
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

    def show_job_exe_list_new(self, request):
        """查询作业列表信息

        在MRS指定集群中查询作业列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobExeListNew
        :type request: :class:`huaweicloudsdkmrs.v2.ShowJobExeListNewRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowJobExeListNewResponse`
        """
        http_info = self._show_job_exe_list_new_http_info(request)
        return self._call_api(**http_info)

    def show_job_exe_list_new_invoker(self, request):
        http_info = self._show_job_exe_list_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_exe_list_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/job-executions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobExeListNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'job_state' in local_var_params:
            query_params.append(('job_state', local_var_params['job_state']))
        if 'job_result' in local_var_params:
            query_params.append(('job_result', local_var_params['job_result']))
        if 'queue' in local_var_params:
            query_params.append(('queue', local_var_params['queue']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'submitted_time_begin' in local_var_params:
            query_params.append(('submitted_time_begin', local_var_params['submitted_time_begin']))
        if 'submitted_time_end' in local_var_params:
            query_params.append(('submitted_time_end', local_var_params['submitted_time_end']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_single_job_exe(self, request):
        """查询单个作业信息

        在MRS集群中查询指定作业的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSingleJobExe
        :type request: :class:`huaweicloudsdkmrs.v2.ShowSingleJobExeRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowSingleJobExeResponse`
        """
        http_info = self._show_single_job_exe_http_info(request)
        return self._call_api(**http_info)

    def show_single_job_exe_invoker(self, request):
        http_info = self._show_single_job_exe_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_single_job_exe_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/job-executions/{job_execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSingleJobExeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_execution_id' in local_var_params:
            path_params['job_execution_id'] = local_var_params['job_execution_id']
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

    def show_sql_result_with_job(self, request):
        """获取SQL结果

        在MRS集群中查询SparkSql和SparkScript两种类型作业的SQL语句运行完成后返回的查询结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlResultWithJob
        :type request: :class:`huaweicloudsdkmrs.v2.ShowSqlResultWithJobRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowSqlResultWithJobResponse`
        """
        http_info = self._show_sql_result_with_job_http_info(request)
        return self._call_api(**http_info)

    def show_sql_result_with_job_invoker(self, request):
        http_info = self._show_sql_result_with_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_result_with_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/job-executions/{job_execution_id}/sql-result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlResultWithJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_execution_id' in local_var_params:
            path_params['job_execution_id'] = local_var_params['job_execution_id']
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

    def stop_job(self, request):
        """终止作业

        在MRS集群中终止指定作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopJob
        :type request: :class:`huaweicloudsdkmrs.v2.StopJobRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.StopJobResponse`
        """
        http_info = self._stop_job_http_info(request)
        return self._call_api(**http_info)

    def stop_job_invoker(self, request):
        http_info = self._stop_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/job-executions/{job_execution_id}/kill",
            "request_type": request.__class__.__name__,
            "response_type": "StopJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_execution_id' in local_var_params:
            path_params['job_execution_id'] = local_var_params['job_execution_id']
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

    def update_agency_mapping(self, request):
        """更新用户（组）与IAM委托的映射关系

        更新用户（组）与IAM委托之间的映射关系。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAgencyMapping
        :type request: :class:`huaweicloudsdkmrs.v2.UpdateAgencyMappingRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.UpdateAgencyMappingResponse`
        """
        http_info = self._update_agency_mapping_http_info(request)
        return self._call_api(**http_info)

    def update_agency_mapping_invoker(self, request):
        http_info = self._update_agency_mapping_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_agency_mapping_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/agency-mapping",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAgencyMappingResponse"
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

    def update_cluster_name(self, request):
        """修改集群名称

        修改集群名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterName
        :type request: :class:`huaweicloudsdkmrs.v2.UpdateClusterNameRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.UpdateClusterNameResponse`
        """
        http_info = self._update_cluster_name_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_name_invoker(self, request):
        http_info = self._update_cluster_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/cluster-name",
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

    def add_component(self, request):
        """集群添加组件

        集群添加组件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddComponent
        :type request: :class:`huaweicloudsdkmrs.v2.AddComponentRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.AddComponentResponse`
        """
        http_info = self._add_component_http_info(request)
        return self._call_api(**http_info)

    def add_component_invoker(self, request):
        http_info = self._add_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_component_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/components",
            "request_type": request.__class__.__name__,
            "response_type": "AddComponentResponse"
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

    def expand_cluster(self, request):
        """扩容集群

        对MRS集群进行扩容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandCluster
        :type request: :class:`huaweicloudsdkmrs.v2.ExpandClusterRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ExpandClusterResponse`
        """
        http_info = self._expand_cluster_http_info(request)
        return self._call_api(**http_info)

    def expand_cluster_invoker(self, request):
        http_info = self._expand_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/expand",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandClusterResponse"
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

    def shrink_cluster(self, request):
        """缩容集群

        对MRS集群进行缩容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShrinkCluster
        :type request: :class:`huaweicloudsdkmrs.v2.ShrinkClusterRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShrinkClusterResponse`
        """
        http_info = self._shrink_cluster_http_info(request)
        return self._call_api(**http_info)

    def shrink_cluster_invoker(self, request):
        http_info = self._shrink_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _shrink_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/shrink",
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

    def create_data_connector(self, request):
        """创建数据连接

        创建数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataConnector
        :type request: :class:`huaweicloudsdkmrs.v2.CreateDataConnectorRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.CreateDataConnectorResponse`
        """
        http_info = self._create_data_connector_http_info(request)
        return self._call_api(**http_info)

    def create_data_connector_invoker(self, request):
        http_info = self._create_data_connector_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_data_connector_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/data-connectors",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataConnectorResponse"
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

    def delete_data_connector(self, request):
        """删除数据连接

        删除数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataConnector
        :type request: :class:`huaweicloudsdkmrs.v2.DeleteDataConnectorRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.DeleteDataConnectorResponse`
        """
        http_info = self._delete_data_connector_http_info(request)
        return self._call_api(**http_info)

    def delete_data_connector_invoker(self, request):
        http_info = self._delete_data_connector_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_data_connector_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/data-connectors/{connector_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataConnectorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

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

    def list_data_connector(self, request):
        """查询数据连接列表

        查询数据连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataConnector
        :type request: :class:`huaweicloudsdkmrs.v2.ListDataConnectorRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ListDataConnectorResponse`
        """
        http_info = self._list_data_connector_http_info(request)
        return self._call_api(**http_info)

    def list_data_connector_invoker(self, request):
        http_info = self._list_data_connector_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_data_connector_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/data-connectors",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataConnectorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'connector_id' in local_var_params:
            query_params.append(('connector_id', local_var_params['connector_id']))
        if 'source_type' in local_var_params:
            query_params.append(('source_type', local_var_params['source_type']))
        if 'connector_name' in local_var_params:
            query_params.append(('connector_name', local_var_params['connector_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'available' in local_var_params:
            query_params.append(('available', local_var_params['available']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_data_connector(self, request):
        """更新数据连接

        更新数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataConnector
        :type request: :class:`huaweicloudsdkmrs.v2.UpdateDataConnectorRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.UpdateDataConnectorResponse`
        """
        http_info = self._update_data_connector_http_info(request)
        return self._call_api(**http_info)

    def update_data_connector_invoker(self, request):
        http_info = self._update_data_connector_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_data_connector_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/data-connectors/{connector_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataConnectorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

        query_params = []

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

    def show_hdfs_file_list(self, request):
        """获取指定目录文件列表

        在MRS集群中获取指定目录文件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHdfsFileList
        :type request: :class:`huaweicloudsdkmrs.v2.ShowHdfsFileListRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowHdfsFileListResponse`
        """
        http_info = self._show_hdfs_file_list_http_info(request)
        return self._call_api(**http_info)

    def show_hdfs_file_list_invoker(self, request):
        http_info = self._show_hdfs_file_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_hdfs_file_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHdfsFileListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

    def cancel_sql(self, request):
        """取消SQL执行任务

        在MRS集群中取消一条SQL的执行任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelSql
        :type request: :class:`huaweicloudsdkmrs.v2.CancelSqlRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.CancelSqlResponse`
        """
        http_info = self._cancel_sql_http_info(request)
        return self._call_api(**http_info)

    def cancel_sql_invoker(self, request):
        http_info = self._cancel_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/sql-execution/{sql_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'sql_id' in local_var_params:
            path_params['sql_id'] = local_var_params['sql_id']

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

    def execute_sql(self, request):
        """提交SQL语句

        在MRS集群中提交并执行一条SQL语句。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteSql
        :type request: :class:`huaweicloudsdkmrs.v2.ExecuteSqlRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ExecuteSqlResponse`
        """
        http_info = self._execute_sql_http_info(request)
        return self._call_api(**http_info)

    def execute_sql_invoker(self, request):
        http_info = self._execute_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/sql-execution",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteSqlResponse"
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

    def show_sql_result(self, request):
        """查询SQL结果

        在MRS集群中查询一条SQL的执行结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlResult
        :type request: :class:`huaweicloudsdkmrs.v2.ShowSqlResultRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowSqlResultResponse`
        """
        http_info = self._show_sql_result_http_info(request)
        return self._call_api(**http_info)

    def show_sql_result_invoker(self, request):
        http_info = self._show_sql_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/clusters/{cluster_id}/sql-execution/{sql_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'sql_id' in local_var_params:
            path_params['sql_id'] = local_var_params['sql_id']

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

    def show_mrs_version_list(self, request):
        """展示MRS版本列表

        展示MRS版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMrsVersionList
        :type request: :class:`huaweicloudsdkmrs.v2.ShowMrsVersionListRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowMrsVersionListResponse`
        """
        http_info = self._show_mrs_version_list_http_info(request)
        return self._call_api(**http_info)

    def show_mrs_version_list_invoker(self, request):
        http_info = self._show_mrs_version_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mrs_version_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/metadata/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMrsVersionListResponse"
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

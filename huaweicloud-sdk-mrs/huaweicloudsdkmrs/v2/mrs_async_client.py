# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class MrsAsyncClient(Client):
    def __init__(self):
        super(MrsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmrs.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "MrsClient":
            raise TypeError("client type error, support client type is MrsClient")

        return ClientBuilder(clazz)

    def batch_delete_jobs_async(self, request):
        """批量删除作业

        在MRS集群中批量删除作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteJobs
        :type request: :class:`huaweicloudsdkmrs.v2.BatchDeleteJobsRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.BatchDeleteJobsResponse`
        """
        return self._batch_delete_jobs_with_http_info(request)

    def _batch_delete_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

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
            resource_path='/v2/{project_id}/clusters/{cluster_id}/job-executions/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cluster_async(self, request):
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
        return self._create_cluster_with_http_info(request)

    def _create_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v2/{project_id}/clusters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_execute_job_async(self, request):
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
        return self._create_execute_job_with_http_info(request)

    def _create_execute_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

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
            resource_path='/v2/{project_id}/clusters/{cluster_id}/job-executions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateExecuteJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_job_flow_async(self, request):
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
        return self._run_job_flow_with_http_info(request)

    def _run_job_flow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v2/{project_id}/run-job-flow',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunJobFlowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_agency_mapping_async(self, request):
        """查询用户（组）与IAM委托的映射关系

        获取用户（组）与IAM委托之间的映射关系的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgencyMapping
        :type request: :class:`huaweicloudsdkmrs.v2.ShowAgencyMappingRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowAgencyMappingResponse`
        """
        return self._show_agency_mapping_with_http_info(request)

    def _show_agency_mapping_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/agency-mapping',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAgencyMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_auto_scaling_policy_async(self, request):
        """查看弹性伸缩策略

        查看指定集群的所有的弹性伸缩策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoScalingPolicy
        :type request: :class:`huaweicloudsdkmrs.v2.ShowAutoScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowAutoScalingPolicyResponse`
        """
        return self._show_auto_scaling_policy_with_http_info(request)

    def _show_auto_scaling_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/autoscaling-policy/{cluster_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAutoScalingPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_exe_list_new_async(self, request):
        """查询作业列表信息

        在MRS指定集群中查询作业列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobExeListNew
        :type request: :class:`huaweicloudsdkmrs.v2.ShowJobExeListNewRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowJobExeListNewResponse`
        """
        return self._show_job_exe_list_new_with_http_info(request)

    def _show_job_exe_list_new_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/job-executions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobExeListNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_single_job_exe_async(self, request):
        """查询单个作业信息

        在MRS集群中查询指定作业的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSingleJobExe
        :type request: :class:`huaweicloudsdkmrs.v2.ShowSingleJobExeRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowSingleJobExeResponse`
        """
        return self._show_single_job_exe_with_http_info(request)

    def _show_single_job_exe_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/job-executions/{job_execution_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSingleJobExeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_result_with_job_async(self, request):
        """获取SQL结果

        在MRS集群中查询SparkSql和SparkScript两种类型作业的SQL语句运行完成后返回的查询结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSqlResultWithJob
        :type request: :class:`huaweicloudsdkmrs.v2.ShowSqlResultWithJobRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowSqlResultWithJobResponse`
        """
        return self._show_sql_result_with_job_with_http_info(request)

    def _show_sql_result_with_job_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/job-executions/{job_execution_id}/sql-result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSqlResultWithJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_job_async(self, request):
        """终止作业

        在MRS集群中终止指定作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopJob
        :type request: :class:`huaweicloudsdkmrs.v2.StopJobRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.StopJobResponse`
        """
        return self._stop_job_with_http_info(request)

    def _stop_job_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/job-executions/{job_execution_id}/kill',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_agency_mapping_async(self, request):
        """更新用户（组）与IAM委托的映射关系

        更新用户（组）与IAM委托之间的映射关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAgencyMapping
        :type request: :class:`huaweicloudsdkmrs.v2.UpdateAgencyMappingRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.UpdateAgencyMappingResponse`
        """
        return self._update_agency_mapping_with_http_info(request)

    def _update_agency_mapping_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/agency-mapping',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAgencyMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cluster_name_async(self, request):
        """修改集群名称

        修改集群名称
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateClusterName
        :type request: :class:`huaweicloudsdkmrs.v2.UpdateClusterNameRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.UpdateClusterNameResponse`
        """
        return self._update_cluster_name_with_http_info(request)

    def _update_cluster_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/cluster-name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateClusterNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def expand_cluster_async(self, request):
        """扩容集群

        对MRS集群进行扩容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandCluster
        :type request: :class:`huaweicloudsdkmrs.v2.ExpandClusterRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ExpandClusterResponse`
        """
        return self._expand_cluster_with_http_info(request)

    def _expand_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/expand',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def shrink_cluster_async(self, request):
        """缩容集群

        对MRS集群进行缩容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShrinkCluster
        :type request: :class:`huaweicloudsdkmrs.v2.ShrinkClusterRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShrinkClusterResponse`
        """
        return self._shrink_cluster_with_http_info(request)

    def _shrink_cluster_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/shrink',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShrinkClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_data_connector_async(self, request):
        """创建数据连接

        创建数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDataConnector
        :type request: :class:`huaweicloudsdkmrs.v2.CreateDataConnectorRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.CreateDataConnectorResponse`
        """
        return self._create_data_connector_with_http_info(request)

    def _create_data_connector_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v2/{project_id}/data-connectors',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDataConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_data_connector_async(self, request):
        """删除数据连接

        删除数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDataConnector
        :type request: :class:`huaweicloudsdkmrs.v2.DeleteDataConnectorRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.DeleteDataConnectorResponse`
        """
        return self._delete_data_connector_with_http_info(request)

    def _delete_data_connector_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/data-connectors/{connector_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDataConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_data_connector_async(self, request):
        """查询数据连接列表

        查询数据连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDataConnector
        :type request: :class:`huaweicloudsdkmrs.v2.ListDataConnectorRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ListDataConnectorResponse`
        """
        return self._list_data_connector_with_http_info(request)

    def _list_data_connector_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/data-connectors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_data_connector_async(self, request):
        """更新数据连接

        更新数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDataConnector
        :type request: :class:`huaweicloudsdkmrs.v2.UpdateDataConnectorRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.UpdateDataConnectorResponse`
        """
        return self._update_data_connector_with_http_info(request)

    def _update_data_connector_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

        query_params = []

        header_params = {}

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
            resource_path='/v2/{project_id}/data-connectors/{connector_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDataConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_hdfs_file_list_async(self, request):
        """获取指定目录文件列表

        在MRS集群中获取指定目录文件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHdfsFileList
        :type request: :class:`huaweicloudsdkmrs.v2.ShowHdfsFileListRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowHdfsFileListResponse`
        """
        return self._show_hdfs_file_list_with_http_info(request)

    def _show_hdfs_file_list_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHdfsFileListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_sql_async(self, request):
        """取消SQL执行任务

        在MRS集群中取消一条SQL的执行任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelSql
        :type request: :class:`huaweicloudsdkmrs.v2.CancelSqlRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.CancelSqlResponse`
        """
        return self._cancel_sql_with_http_info(request)

    def _cancel_sql_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/sql-execution/{sql_id}/cancel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelSqlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_sql_async(self, request):
        """提交SQL语句

        在MRS集群中提交并执行一条SQL语句。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteSql
        :type request: :class:`huaweicloudsdkmrs.v2.ExecuteSqlRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ExecuteSqlResponse`
        """
        return self._execute_sql_with_http_info(request)

    def _execute_sql_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

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
            resource_path='/v2/{project_id}/clusters/{cluster_id}/sql-execution',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteSqlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_result_async(self, request):
        """查询SQL结果

        在MRS集群中查询一条SQL的执行结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSqlResult
        :type request: :class:`huaweicloudsdkmrs.v2.ShowSqlResultRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowSqlResultResponse`
        """
        return self._show_sql_result_with_http_info(request)

    def _show_sql_result_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/clusters/{cluster_id}/sql-execution/{sql_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSqlResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_mrs_version_list_async(self, request):
        """展示MRS版本列表

        展示MRS版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMrsVersionList
        :type request: :class:`huaweicloudsdkmrs.v2.ShowMrsVersionListRequest`
        :rtype: :class:`huaweicloudsdkmrs.v2.ShowMrsVersionListResponse`
        """
        return self._show_mrs_version_list_with_http_info(request)

    def _show_mrs_version_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/metadata/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMrsVersionListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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

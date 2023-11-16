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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcdm'")


class CdmClient(Client):
    def __init__(self):
        super(CdmClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcdm.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CdmClient":
                raise TypeError("client type error, support client type is CdmClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_and_start_random_cluster_job(self, request):
        """随机集群创建作业并执行

        随机集群创建作业并执行接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAndStartRandomClusterJob
        :type request: :class:`huaweicloudsdkcdm.v1.CreateAndStartRandomClusterJobRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.CreateAndStartRandomClusterJobResponse`
        """
        http_info = self._create_and_start_random_cluster_job_http_info(request)
        return self._call_api(**http_info)

    def create_and_start_random_cluster_job_invoker(self, request):
        http_info = self._create_and_start_random_cluster_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_and_start_random_cluster_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/clusters/job",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAndStartRandomClusterJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def create_cluster(self, request):
        """创建集群

        创建集群接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkcdm.v1.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.CreateClusterResponse`
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
            "resource_path": "/v1.1/{project_id}/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def create_job(self, request):
        """指定集群创建作业

        指定集群创建作业接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateJob
        :type request: :class:`huaweicloudsdkcdm.v1.CreateJobRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.CreateJobResponse`
        """
        http_info = self._create_job_http_info(request)
        return self._call_api(**http_info)

    def create_job_invoker(self, request):
        http_info = self._create_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/job",
            "request_type": request.__class__.__name__,
            "response_type": "CreateJobResponse"
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

    def create_link(self, request):
        """创建连接

        创建连接接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLink
        :type request: :class:`huaweicloudsdkcdm.v1.CreateLinkRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.CreateLinkResponse`
        """
        http_info = self._create_link_http_info(request)
        return self._call_api(**http_info)

    def create_link_invoker(self, request):
        http_info = self._create_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_link_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/link",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'validate' in local_var_params:
            query_params.append(('validate', local_var_params['validate']))

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

    def delete_cluster(self, request):
        """删除集群

        删除集群接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkcdm.v1.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.DeleteClusterResponse`
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

    def delete_job(self, request):
        """删除作业

        删除作业接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkcdm.v1.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.DeleteJobResponse`
        """
        http_info = self._delete_job_http_info(request)
        return self._call_api(**http_info)

    def delete_job_invoker(self, request):
        http_info = self._delete_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/job/{job_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_link(self, request):
        """删除连接

        删除连接接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLink
        :type request: :class:`huaweicloudsdkcdm.v1.DeleteLinkRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.DeleteLinkResponse`
        """
        http_info = self._delete_link_http_info(request)
        return self._call_api(**http_info)

    def delete_link_invoker(self, request):
        http_info = self._delete_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_link_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/link/{link_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'link_name' in local_var_params:
            path_params['link_name'] = local_var_params['link_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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

        查询集群列表接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusters
        :type request: :class:`huaweicloudsdkcdm.v1.ListClustersRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.ListClustersResponse`
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
            "resource_path": "/v1.1/{project_id}/clusters",
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

    def restart_cluster(self, request):
        """重启集群

        重启集群接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartCluster
        :type request: :class:`huaweicloudsdkcdm.v1.RestartClusterRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.RestartClusterResponse`
        """
        http_info = self._restart_cluster_http_info(request)
        return self._call_api(**http_info)

    def restart_cluster_invoker(self, request):
        http_info = self._restart_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/action",
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

    def show_cluster_detail(self, request):
        """查询集群详情

        查询集群详情接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterDetail
        :type request: :class:`huaweicloudsdkcdm.v1.ShowClusterDetailRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.ShowClusterDetailResponse`
        """
        http_info = self._show_cluster_detail_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_detail_invoker(self, request):
        http_info = self._show_cluster_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}",
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

    def show_job_status(self, request):
        """查询作业状态

        查询作业状态接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobStatus
        :type request: :class:`huaweicloudsdkcdm.v1.ShowJobStatusRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.ShowJobStatusResponse`
        """
        http_info = self._show_job_status_http_info(request)
        return self._call_api(**http_info)

    def show_job_status_invoker(self, request):
        http_info = self._show_job_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/job/{job_name}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_jobs(self, request):
        """查询作业

        查询作业接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobs
        :type request: :class:`huaweicloudsdkcdm.v1.ShowJobsRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.ShowJobsResponse`
        """
        http_info = self._show_jobs_http_info(request)
        return self._call_api(**http_info)

    def show_jobs_invoker(self, request):
        http_info = self._show_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/job/{job_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'job_type' in local_var_params:
            query_params.append(('jobType', local_var_params['job_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_link(self, request):
        """查询连接

        查询连接接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLink
        :type request: :class:`huaweicloudsdkcdm.v1.ShowLinkRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.ShowLinkResponse`
        """
        http_info = self._show_link_http_info(request)
        return self._call_api(**http_info)

    def show_link_invoker(self, request):
        http_info = self._show_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_link_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/link/{link_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'link_name' in local_var_params:
            path_params['link_name'] = local_var_params['link_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_submissions(self, request):
        """查询作业执行历史

        查询作业执行历史接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSubmissions
        :type request: :class:`huaweicloudsdkcdm.v1.ShowSubmissionsRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.ShowSubmissionsResponse`
        """
        http_info = self._show_submissions_http_info(request)
        return self._call_api(**http_info)

    def show_submissions_invoker(self, request):
        http_info = self._show_submissions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_submissions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/submissions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubmissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'jname' in local_var_params:
            query_params.append(('jname', local_var_params['jname']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_cluster(self, request):
        """启动集群

        启动集群接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartCluster
        :type request: :class:`huaweicloudsdkcdm.v1.StartClusterRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.StartClusterResponse`
        """
        http_info = self._start_cluster_http_info(request)
        return self._call_api(**http_info)

    def start_cluster_invoker(self, request):
        http_info = self._start_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StartClusterResponse"
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

    def start_job(self, request):
        """启动作业

        启动作业接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartJob
        :type request: :class:`huaweicloudsdkcdm.v1.StartJobRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.StartJobResponse`
        """
        http_info = self._start_job_http_info(request)
        return self._call_api(**http_info)

    def start_job_invoker(self, request):
        http_info = self._start_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/job/{job_name}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_cluster(self, request):
        """停止集群

        停止集群接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopCluster
        :type request: :class:`huaweicloudsdkcdm.v1.StopClusterRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.StopClusterResponse`
        """
        http_info = self._stop_cluster_http_info(request)
        return self._call_api(**http_info)

    def stop_cluster_invoker(self, request):
        http_info = self._stop_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StopClusterResponse"
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

    def stop_job(self, request):
        """停止作业

        停止作业接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopJob
        :type request: :class:`huaweicloudsdkcdm.v1.StopJobRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.StopJobResponse`
        """
        http_info = self._stop_job_http_info(request)
        return self._call_api(**http_info)

    def stop_job_invoker(self, request):
        http_info = self._stop_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/job/{job_name}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_job(self, request):
        """修改作业

        修改作业接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkcdm.v1.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.UpdateJobResponse`
        """
        http_info = self._update_job_http_info(request)
        return self._call_api(**http_info)

    def update_job_invoker(self, request):
        http_info = self._update_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/job/{job_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

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

    def update_link(self, request):
        """修改连接

        修改连接接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLink
        :type request: :class:`huaweicloudsdkcdm.v1.UpdateLinkRequest`
        :rtype: :class:`huaweicloudsdkcdm.v1.UpdateLinkResponse`
        """
        http_info = self._update_link_http_info(request)
        return self._call_api(**http_info)

    def update_link_invoker(self, request):
        http_info = self._update_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_link_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.1/{project_id}/clusters/{cluster_id}/cdm/link/{link_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'link_name' in local_var_params:
            path_params['link_name'] = local_var_params['link_name']

        query_params = []

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

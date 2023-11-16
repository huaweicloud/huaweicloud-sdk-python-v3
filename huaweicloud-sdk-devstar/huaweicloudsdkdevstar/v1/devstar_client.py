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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdevstar'")


class DevStarClient(Client):
    def __init__(self):
        super(DevStarClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdevstar.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "DevStarClient":
                raise TypeError("client type error, support client type is DevStarClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def show_application_release_repositories(self, request):
        """通过应用Id获取软件发布仓库列表 

        通过应用Id获取软件发布仓库列表 
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplicationReleaseRepositories
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowApplicationReleaseRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowApplicationReleaseRepositoriesResponse`
        """
        http_info = self._show_application_release_repositories_http_info(request)
        return self._call_api(**http_info)

    def show_application_release_repositories_invoker(self, request):
        http_info = self._show_application_release_repositories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_application_release_repositories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/applications/{application_id}/release-repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationReleaseRepositoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_application_res_delete_status(self, request):
        """查询应用关联资源删除状态

        根据应用Id查询应用关联的代码仓、流水线删除状态 使用场景：用户删除应用关联的资源（如代码仓、流水线...）后，通过该接口实时查询代码仓、流水线删除状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplicationResDeleteStatus
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowApplicationResDeleteStatusRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowApplicationResDeleteStatusResponse`
        """
        http_info = self._show_application_res_delete_status_http_info(request)
        return self._call_api(**http_info)

    def show_application_res_delete_status_invoker(self, request):
        http_info = self._show_application_res_delete_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_application_res_delete_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/application-resources/{application_id}/delete-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationResDeleteStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_application_dependent_resources(self, request):
        """获取应用依赖元数据资源

        根据应用Id获取依赖元数据资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplicationDependentResources
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowApplicationDependentResourcesRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowApplicationDependentResourcesResponse`
        """
        http_info = self._show_application_dependent_resources_http_info(request)
        return self._call_api(**http_info)

    def show_application_dependent_resources_invoker(self, request):
        http_info = self._show_application_dependent_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_application_dependent_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/applications/{application_id}/dependent-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationDependentResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_application_v3(self, request):
        """获取应用详情

        根据应用Id获取应用详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplicationV3
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowApplicationV3Request`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowApplicationV3Response`
        """
        http_info = self._show_application_v3_http_info(request)
        return self._call_api(**http_info)

    def show_application_v3_invoker(self, request):
        http_info = self._show_application_v3_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_application_v3_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationV3Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_application(self, request):
        """更新应用信息

        根据应用Id更新对应有权限的应用信息
        - 允许更新信息的信息包含
        name,description,icon
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplication
        :type request: :class:`huaweicloudsdkdevstar.v1.UpdateApplicationRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.UpdateApplicationResponse`
        """
        http_info = self._update_application_http_info(request)
        return self._call_api(**http_info)

    def update_application_invoker(self, request):
        http_info = self._update_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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

    def delete_application_v4(self, request):
        """删除应用信息

        根据应用Id删除应用，并可以选择删除其关联的代码仓、流水线资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplicationV4
        :type request: :class:`huaweicloudsdkdevstar.v1.DeleteApplicationV4Request`
        :rtype: :class:`huaweicloudsdkdevstar.v1.DeleteApplicationV4Response`
        """
        http_info = self._delete_application_v4_http_info(request)
        return self._call_api(**http_info)

    def delete_application_v4_invoker(self, request):
        http_info = self._delete_application_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_v4_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'is_delete_repository' in local_var_params:
            query_params.append(('is_delete_repository', local_var_params['is_delete_repository']))
        if 'pipeline_ids' in local_var_params:
            query_params.append(('pipeline_ids', local_var_params['pipeline_ids']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_applications_v6(self, request):
        """获取应用列表

        获取我创建的应用列表
        当前只支持查询我创建的应用，其中请求参数is_created_by_self需为true
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplicationsV6
        :type request: :class:`huaweicloudsdkdevstar.v1.ListApplicationsV6Request`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ListApplicationsV6Response`
        """
        http_info = self._list_applications_v6_http_info(request)
        return self._call_api(**http_info)

    def list_applications_v6_invoker(self, request):
        http_info = self._list_applications_v6_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_applications_v6_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v6/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationsV6Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'attention' in local_var_params:
            query_params.append(('attention', local_var_params['attention']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'topic_id' in local_var_params:
            query_params.append(('topic_id', local_var_params['topic_id']))
        if 'is_created_by_self' in local_var_params:
            query_params.append(('is_created_by_self', local_var_params['is_created_by_self']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_application_code(self, request):
        """下载模板产物

        下载模板产物。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadApplicationCode
        :type request: :class:`huaweicloudsdkdevstar.v1.DownloadApplicationCodeRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.DownloadApplicationCodeResponse`
        """
        http_info = self._download_application_code_http_info(request)
        return self._call_api(**http_info)

    def download_application_code_invoker(self, request):
        http_info = self._download_application_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_application_code_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/application-codes",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadApplicationCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def confirm_deployment_job(self, request):
        """部署任务执行变更人工审核

        部署任务执行变更人工审核，终止或者继续部署任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmDeploymentJob
        :type request: :class:`huaweicloudsdkdevstar.v1.ConfirmDeploymentJobRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ConfirmDeploymentJobResponse`
        """
        http_info = self._confirm_deployment_job_http_info(request)
        return self._call_api(**http_info)

    def confirm_deployment_job_invoker(self, request):
        http_info = self._confirm_deployment_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _confirm_deployment_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/applications/{application_id}/environments/{environment_tag}/confirm",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmDeploymentJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'environment_tag' in local_var_params:
            path_params['environment_tag'] = local_var_params['environment_tag']

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

    def create_deployment_jobs(self, request):
        """创建部署任务

        创建部署任务，并触发任务执行，当前只支持函数部署。
        其中，报文中file_id为查询软件版本包接口返回版本包id;
        handler为在函数部署方式下，入口函数名称，从应用代码中获取，格式为“包名.类名.函数名称”，例如：com.example.demo.APIGTrigger.handler。
        也可以从应用详情接口返回结构template_deployment中直接获取。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeploymentJobs
        :type request: :class:`huaweicloudsdkdevstar.v1.CreateDeploymentJobsRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.CreateDeploymentJobsResponse`
        """
        http_info = self._create_deployment_jobs_http_info(request)
        return self._call_api(**http_info)

    def create_deployment_jobs_invoker(self, request):
        http_info = self._create_deployment_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_deployment_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/applications/{application_id}/environments/{environment_tag}/deployment-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeploymentJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'environment_tag' in local_var_params:
            path_params['environment_tag'] = local_var_params['environment_tag']

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

    def show_deployment_jobs(self, request):
        """查询应用环境部署任务详情

        查询应用环境部署任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeploymentJobs
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowDeploymentJobsRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowDeploymentJobsResponse`
        """
        http_info = self._show_deployment_jobs_http_info(request)
        return self._call_api(**http_info)

    def show_deployment_jobs_invoker(self, request):
        http_info = self._show_deployment_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_deployment_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/applications/{application_id}/environments/{environment_tag}/deployment-jobs/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeploymentJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'environment_tag' in local_var_params:
            path_params['environment_tag'] = local_var_params['environment_tag']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def run_codehub_template_job(self, request):
        """CodeHub 模板生成代码

        使用CodeHub模板创建应用代码。
        
        通过 Codehub 模板创建生成应用代码的任务，并将应用代码存储于指定的 CodeHub 仓库中或者生成代码压缩包，可以通过返回的任务 ID 查询相关任务状态。
        
        - 接口鉴权方式
        通过华为云服务获取的用户token。
        
        - 代码生成位置
        应用代码生成后的地址，目前支持codehub地址和压缩包下载地址。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCodehubTemplateJob
        :type request: :class:`huaweicloudsdkdevstar.v1.RunCodehubTemplateJobRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.RunCodehubTemplateJobResponse`
        """
        http_info = self._run_codehub_template_job_http_info(request)
        return self._call_api(**http_info)

    def run_codehub_template_job_invoker(self, request):
        http_info = self._run_codehub_template_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_codehub_template_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/jobs/codehub",
            "request_type": request.__class__.__name__,
            "response_type": "RunCodehubTemplateJobResponse"
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

    def run_devstar_template_job(self, request):
        """Devstar 模板生成代码

        使用DevStar的模板创建应用代码。
        
        通过 DevStar 模板创建生成应用代码的任务，并将应用代码存储于指定的 CodeHub 仓库中，可以通过返回的任务 ID 查询相关任务状态。
        
        - 接口鉴权方式
        通过华为云服务获取的用户token。
        
        - 代码生成位置
        应用代码生成后的地址，目前支持codehub地址和压缩包下载地址。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunDevstarTemplateJob
        :type request: :class:`huaweicloudsdkdevstar.v1.RunDevstarTemplateJobRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.RunDevstarTemplateJobResponse`
        """
        http_info = self._run_devstar_template_job_http_info(request)
        return self._call_api(**http_info)

    def run_devstar_template_job_invoker(self, request):
        http_info = self._run_devstar_template_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_devstar_template_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/jobs/template",
            "request_type": request.__class__.__name__,
            "response_type": "RunDevstarTemplateJobResponse"
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

    def show_job_detail(self, request):
        """查询任务详情

        查询任务的详情。
        
        通过任务ID可以查看任务的状态
        当任务结束时返回应用代码存放的位置。
        
        - 接口鉴权方式
        通过华为云服务获取的用户token。
        
        - 代码生成位置
        应用代码生成后的地址，目前支持codehub地址和压缩包下载地址。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowJobDetailResponse`
        """
        http_info = self._show_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_job_detail_invoker(self, request):
        http_info = self._show_job_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pipeline_templates(self, request):
        """流水线模板列表查询

        流水线模板列表查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelineTemplates
        :type request: :class:`huaweicloudsdkdevstar.v1.ListPipelineTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ListPipelineTemplatesResponse`
        """
        http_info = self._list_pipeline_templates_http_info(request)
        return self._call_api(**http_info)

    def list_pipeline_templates_invoker(self, request):
        http_info = self._list_pipeline_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pipeline_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/pipeline-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipelineTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pipeline_last_status_v2(self, request):
        """查询流水线最近一次运行状态查询接口

        查询应用流水线最近一次运行状态查询接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipelineLastStatusV2
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowPipelineLastStatusV2Request`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowPipelineLastStatusV2Response`
        """
        http_info = self._show_pipeline_last_status_v2_http_info(request)
        return self._call_api(**http_info)

    def show_pipeline_last_status_v2_invoker(self, request):
        http_info = self._show_pipeline_last_status_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipeline_last_status_v2_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/pipelines/{pipeline_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipelineLastStatusV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_pipeline(self, request):
        """根据流水线Id操作流水线启动

        根据流水线Id操作流水线启动
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartPipeline
        :type request: :class:`huaweicloudsdkdevstar.v1.StartPipelineRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.StartPipelineResponse`
        """
        http_info = self._start_pipeline_http_info(request)
        return self._call_api(**http_info)

    def start_pipeline_invoker(self, request):
        http_info = self._start_pipeline_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_pipeline_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/pipelines/{pipeline_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartPipelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_projects_v4(self, request):
        """获取用户有权限的DevStar存量DevCloud项目列表

        获取用户有权限的DevStar存量DevCloud项目列表。
        来源包括：1.DevStar创建的DevCloud项目；2.DevStar应用有关联DevCloud项目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectsV4
        :type request: :class:`huaweicloudsdkdevstar.v1.ListProjectsV4Request`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ListProjectsV4Response`
        """
        http_info = self._list_projects_v4_http_info(request)
        return self._call_api(**http_info)

    def list_projects_v4_invoker(self, request):
        http_info = self._list_projects_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_projects_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectsV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_repository_duplicate_name(self, request):
        """检查仓库名称是否重名

        检查仓库名称是否重名
        - 校验规则
            同一个项目下的仓库名称不能存在重复,当结果为true时,校验通过,仓库名称可用,否则,校验不通过,当前项目下的仓库名称已存在,不可用
        - 必传参数
            project_id,name,region_id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckRepositoryDuplicateName
        :type request: :class:`huaweicloudsdkdevstar.v1.CheckRepositoryDuplicateNameRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.CheckRepositoryDuplicateNameResponse`
        """
        http_info = self._check_repository_duplicate_name_http_info(request)
        return self._call_api(**http_info)

    def check_repository_duplicate_name_invoker(self, request):
        http_info = self._check_repository_duplicate_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_repository_duplicate_name_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/check-repository-duplicate-name",
            "request_type": request.__class__.__name__,
            "response_type": "CheckRepositoryDuplicateNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_repository_by_cloud_ide(self, request):
        """使用 CloudIDE 实例打开应用代码

        使用 CloudIDE 实例打开应用代码。CloudIDE会保存用户项目数据，相同用户使用同一个CloudIDE，使用要求：
        - 用户需为登录状态。
        - 拥有仓库权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryByCloudIde
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowRepositoryByCloudIdeRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowRepositoryByCloudIdeResponse`
        """
        http_info = self._show_repository_by_cloud_ide_http_info(request)
        return self._call_api(**http_info)

    def show_repository_by_cloud_ide_invoker(self, request):
        http_info = self._show_repository_by_cloud_ide_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repository_by_cloud_ide_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_id}/show/cloudide",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryByCloudIdeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'repository_ssh_url' in local_var_params:
            query_params.append(('repository_ssh_url', local_var_params['repository_ssh_url']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'space_prefix' in local_var_params:
            query_params.append(('space_prefix', local_var_params['space_prefix']))
        if 'is_open_last' in local_var_params:
            query_params.append(('is_open_last', local_var_params['is_open_last']))
        if 'is_free' in local_var_params:
            query_params.append(('is_free', local_var_params['is_free']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_repository_statistical_data_v2(self, request):
        """应用代码仓库统计信息

        查询代码仓库的统计信息,包括代码仓的名称,代码行数等信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryStatisticalDataV2
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowRepositoryStatisticalDataV2Request`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowRepositoryStatisticalDataV2Response`
        """
        http_info = self._show_repository_statistical_data_v2_http_info(request)
        return self._call_api(**http_info)

    def show_repository_statistical_data_v2_invoker(self, request):
        http_info = self._show_repository_statistical_data_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repository_statistical_data_v2_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/statistical-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryStatisticalDataV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_template_file(self, request):
        """读取模板文件

        该接口可以用于模板作者或模板维护人读取模板文件内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateFile
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowTemplateFileRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowTemplateFileResponse`
        """
        http_info = self._show_template_file_http_info(request)
        return self._call_api(**http_info)

    def show_template_file_invoker(self, request):
        http_info = self._show_template_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_template_file_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/templates/{template_id}/files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_template_view_histories(self, request):
        """同步模板浏览记录

        未登录状态下，将用户浏览过的模板缓存在浏览器中，登录时，调用该接口同步模板浏览记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplateViewHistories
        :type request: :class:`huaweicloudsdkdevstar.v1.CreateTemplateViewHistoriesRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.CreateTemplateViewHistoriesResponse`
        """
        http_info = self._create_template_view_histories_http_info(request)
        return self._call_api(**http_info)

    def create_template_view_histories_invoker(self, request):
        http_info = self._create_template_view_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_template_view_histories_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/templates/view-histories",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateViewHistoriesResponse"
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

    def list_published_templates(self, request):
        """查询模板列表（V1）

        查询模板列表，推荐使用/v1/templates/query接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublishedTemplates
        :type request: :class:`huaweicloudsdkdevstar.v1.ListPublishedTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ListPublishedTemplatesResponse`
        """
        http_info = self._list_published_templates_http_info(request)
        return self._call_api(**http_info)

    def list_published_templates_invoker(self, request):
        http_info = self._list_published_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_published_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublishedTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_template_view_histories(self, request):
        """我浏览的模板记录

        查询DevStar或者CodeLabs登录用户浏览过的模板（只返回最近浏览的5个模板）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateViewHistories
        :type request: :class:`huaweicloudsdkdevstar.v1.ListTemplateViewHistoriesRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ListTemplateViewHistoriesResponse`
        """
        http_info = self._list_template_view_histories_http_info(request)
        return self._call_api(**http_info)

    def list_template_view_histories_invoker(self, request):
        http_info = self._list_template_view_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_template_view_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/templates/view-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateViewHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'platform_source' in local_var_params:
            query_params.append(('platform_source', local_var_params['platform_source']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_templates(self, request):
        """查询模板列表

        查询模板列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkdevstar.v1.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_templates_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/templates/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
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

    def list_templates_v2(self, request):
        """查询模板列表（V2）

        查询模板列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplatesV2
        :type request: :class:`huaweicloudsdkdevstar.v1.ListTemplatesV2Request`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ListTemplatesV2Response`
        """
        http_info = self._list_templates_v2_http_info(request)
        return self._call_api(**http_info)

    def list_templates_v2_invoker(self, request):
        http_info = self._list_templates_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_templates_v2_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/templates/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def show_template_v3(self, request):
        """查询模板详情（V3）

        获取指定模板详情，包括模板id、名称、描述、作者、标签、上架时间等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateV3
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowTemplateV3Request`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowTemplateV3Response`
        """
        http_info = self._show_template_v3_http_info(request)
        return self._call_api(**http_info)

    def show_template_v3_invoker(self, request):
        http_info = self._show_template_v3_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_template_v3_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateV3Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_template_detail(self, request):
        """查询模板详情（V1）

        查询模板详情，推荐使用V3版本接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateDetail
        :type request: :class:`huaweicloudsdkdevstar.v1.ShowTemplateDetailRequest`
        :rtype: :class:`huaweicloudsdkdevstar.v1.ShowTemplateDetailResponse`
        """
        http_info = self._show_template_detail_http_info(request)
        return self._call_api(**http_info)

    def show_template_detail_invoker(self, request):
        http_info = self._show_template_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_template_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkres'")


class ResAsyncClient(Client):
    def __init__(self):
        super(ResAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkres.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ResAsyncClient":
                raise TypeError("client type error, support client type is ResAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_res_datasource_async(self, request):
        """创建数据源

        在指定的工作空间下面创建一个新的数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResDatasource
        :type request: :class:`huaweicloudsdkres.v1.CreateResDatasourceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.CreateResDatasourceResponse`
        """
        http_info = self._create_res_datasource_http_info(request)
        return self._call_api(**http_info)

    def create_res_datasource_async_invoker(self, request):
        http_info = self._create_res_datasource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_res_datasource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResDatasourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def create_res_intelligent_scene_async(self, request):
        """创建智能场景

        在指定工作空间下面创建智能场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResIntelligentScene
        :type request: :class:`huaweicloudsdkres.v1.CreateResIntelligentSceneRequest`
        :rtype: :class:`huaweicloudsdkres.v1.CreateResIntelligentSceneResponse`
        """
        http_info = self._create_res_intelligent_scene_http_info(request)
        return self._call_api(**http_info)

    def create_res_intelligent_scene_async_invoker(self, request):
        http_info = self._create_res_intelligent_scene_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_res_intelligent_scene_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/intelligent-scenes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResIntelligentSceneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def create_res_job_async(self, request):
        """新建训练作业

        新建训练作业元数据，新建成功之后可手动执行此任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResJob
        :type request: :class:`huaweicloudsdkres.v1.CreateResJobRequest`
        :rtype: :class:`huaweicloudsdkres.v1.CreateResJobResponse`
        """
        http_info = self._create_res_job_http_info(request)
        return self._call_api(**http_info)

    def create_res_job_async_invoker(self, request):
        http_info = self._create_res_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_res_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def create_res_jobs_async(self, request):
        """新建多个训练作业

        批量新建作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResJobs
        :type request: :class:`huaweicloudsdkres.v1.CreateResJobsRequest`
        :rtype: :class:`huaweicloudsdkres.v1.CreateResJobsResponse`
        """
        http_info = self._create_res_jobs_http_info(request)
        return self._call_api(**http_info)

    def create_res_jobs_async_invoker(self, request):
        http_info = self._create_res_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_res_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def create_res_online_instance_async(self, request):
        """新建在线服务

        新建在线服务元数据，新建成功之后可手动发布此服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResOnlineInstance
        :type request: :class:`huaweicloudsdkres.v1.CreateResOnlineInstanceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.CreateResOnlineInstanceResponse`
        """
        http_info = self._create_res_online_instance_http_info(request)
        return self._call_api(**http_info)

    def create_res_online_instance_async_invoker(self, request):
        http_info = self._create_res_online_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_res_online_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/service-instance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResOnlineInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def create_res_scene_async(self, request):
        """创建自定义场景

        在指定工作空间下面创建自定义场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResScene
        :type request: :class:`huaweicloudsdkres.v1.CreateResSceneRequest`
        :rtype: :class:`huaweicloudsdkres.v1.CreateResSceneResponse`
        """
        http_info = self._create_res_scene_http_info(request)
        return self._call_api(**http_info)

    def create_res_scene_async_invoker(self, request):
        http_info = self._create_res_scene_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_res_scene_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/scenes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResSceneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def create_res_workspace_async(self, request):
        """创建工作空间

        用于在推荐系统下面创建独立的工作空间，用于资源的隔离，用户可以在工作空间下面继续创建数据源、场景以及推荐任务等。是否有工作空间的操作权限取决于用户是否属于当前工作空间绑定的企业项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResWorkspace
        :type request: :class:`huaweicloudsdkres.v1.CreateResWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.CreateResWorkspaceResponse`
        """
        http_info = self._create_res_workspace_http_info(request)
        return self._call_api(**http_info)

    def create_res_workspace_async_invoker(self, request):
        http_info = self._create_res_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_res_workspace_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResWorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def delete_res_datasource_async(self, request):
        """删除数据源

        删除数据源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResDatasource
        :type request: :class:`huaweicloudsdkres.v1.DeleteResDatasourceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.DeleteResDatasourceResponse`
        """
        http_info = self._delete_res_datasource_http_info(request)
        return self._call_api(**http_info)

    def delete_res_datasource_async_invoker(self, request):
        http_info = self._delete_res_datasource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_res_datasource_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResDatasourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_res_job_async(self, request):
        """删除训练作业

        删除指定作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResJob
        :type request: :class:`huaweicloudsdkres.v1.DeleteResJobRequest`
        :rtype: :class:`huaweicloudsdkres.v1.DeleteResJobResponse`
        """
        http_info = self._delete_res_job_http_info(request)
        return self._call_api(**http_info)

    def delete_res_job_async_invoker(self, request):
        http_info = self._delete_res_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_res_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instance/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_res_online_instance_async(self, request):
        """删除在线服务

        删除在线服务实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResOnlineInstance
        :type request: :class:`huaweicloudsdkres.v1.DeleteResOnlineInstanceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.DeleteResOnlineInstanceResponse`
        """
        http_info = self._delete_res_online_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_res_online_instance_async_invoker(self, request):
        http_info = self._delete_res_online_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_res_online_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/service-instance/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResOnlineInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_res_scene_async(self, request):
        """删除场景

        该接口用于删除场景，删除之后不能恢复，请您谨慎操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResScene
        :type request: :class:`huaweicloudsdkres.v1.DeleteResSceneRequest`
        :rtype: :class:`huaweicloudsdkres.v1.DeleteResSceneResponse`
        """
        http_info = self._delete_res_scene_http_info(request)
        return self._call_api(**http_info)

    def delete_res_scene_async_invoker(self, request):
        http_info = self._delete_res_scene_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_res_scene_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/scenes/{scene_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResSceneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'scene_id' in local_var_params:
            path_params['scene_id'] = local_var_params['scene_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_res_workspace_async(self, request):
        """删除工作空间

        删除指定工作空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResWorkspace
        :type request: :class:`huaweicloudsdkres.v1.DeleteResWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.DeleteResWorkspaceResponse`
        """
        http_info = self._delete_res_workspace_http_info(request)
        return self._call_api(**http_info)

    def delete_res_workspace_async_invoker(self, request):
        http_info = self._delete_res_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_res_workspace_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResWorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_res_datasources_async(self, request):
        """查询数据源列表

        查询当前工作空间下的数据源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResDatasources
        :type request: :class:`huaweicloudsdkres.v1.ListResDatasourcesRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ListResDatasourcesResponse`
        """
        http_info = self._list_res_datasources_http_info(request)
        return self._call_api(**http_info)

    def list_res_datasources_async_invoker(self, request):
        http_info = self._list_res_datasources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_res_datasources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResDatasourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_res_enterprises_async(self, request):
        """查询企业项目列表

        查询用户在当前项目id下的企业项目列表。在创建工作空间时需要提供企业项目id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResEnterprises
        :type request: :class:`huaweicloudsdkres.v1.ListResEnterprisesRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ListResEnterprisesResponse`
        """
        http_info = self._list_res_enterprises_http_info(request)
        return self._call_api(**http_info)

    def list_res_enterprises_async_invoker(self, request):
        http_info = self._list_res_enterprises_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_res_enterprises_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/enterprise-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListResEnterprisesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_res_online_service_details_async(self, request):
        """查询在线服务详情

        根据给定的workspace_id和resource_id及category查询在线服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResOnlineServiceDetails
        :type request: :class:`huaweicloudsdkres.v1.ListResOnlineServiceDetailsRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ListResOnlineServiceDetailsResponse`
        """
        http_info = self._list_res_online_service_details_http_info(request)
        return self._call_api(**http_info)

    def list_res_online_service_details_async_invoker(self, request):
        http_info = self._list_res_online_service_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_res_online_service_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/service-instance",
            "request_type": request.__class__.__name__,
            "response_type": "ListResOnlineServiceDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_res_resource_spec_async(self, request):
        """查询训练规格

        查询当前推荐系统所提供的离线计算规格，实时计算规格和排序模型训练规格。在创建数据源和场景时，需要提供此信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResResourceSpec
        :type request: :class:`huaweicloudsdkres.v1.ListResResourceSpecRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ListResResourceSpecResponse`
        """
        http_info = self._list_res_resource_spec_http_info(request)
        return self._call_api(**http_info)

    def list_res_resource_spec_async_invoker(self, request):
        http_info = self._list_res_resource_spec_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_res_resource_spec_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/resource-specs",
            "request_type": request.__class__.__name__,
            "response_type": "ListResResourceSpecResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_res_scenes_async(self, request):
        """查询场景列表

        查询当前工作空间下的场景列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResScenes
        :type request: :class:`huaweicloudsdkres.v1.ListResScenesRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ListResScenesResponse`
        """
        http_info = self._list_res_scenes_http_info(request)
        return self._call_api(**http_info)

    def list_res_scenes_async_invoker(self, request):
        http_info = self._list_res_scenes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_res_scenes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/scenes",
            "request_type": request.__class__.__name__,
            "response_type": "ListResScenesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_res_workspaces_async(self, request):
        """查询工作空间列表

        用于查询当前用户具有操作权限的工作空间列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResWorkspaces
        :type request: :class:`huaweicloudsdkres.v1.ListResWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ListResWorkspacesResponse`
        """
        http_info = self._list_res_workspaces_http_info(request)
        return self._call_api(**http_info)

    def list_res_workspaces_async_invoker(self, request):
        http_info = self._list_res_workspaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_res_workspaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListResWorkspacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_res_datasource_async(self, request):
        """查询数据源详情

        查询指定数据源的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResDatasource
        :type request: :class:`huaweicloudsdkres.v1.ShowResDatasourceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ShowResDatasourceResponse`
        """
        http_info = self._show_res_datasource_http_info(request)
        return self._call_api(**http_info)

    def show_res_datasource_async_invoker(self, request):
        http_info = self._show_res_datasource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_res_datasource_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResDatasourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_res_datasource_work_detail_async(self, request):
        """查询数据源任务结果

        查询指定数据源下离线任务的结果。其中包括数据格式，数据检测、数据探索及效果评估的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResDatasourceWorkDetail
        :type request: :class:`huaweicloudsdkres.v1.ShowResDatasourceWorkDetailRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ShowResDatasourceWorkDetailResponse`
        """
        http_info = self._show_res_datasource_work_detail_http_info(request)
        return self._call_api(**http_info)

    def show_res_datasource_work_detail_async_invoker(self, request):
        http_info = self._show_res_datasource_work_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_res_datasource_work_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{resource_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResDatasourceWorkDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_res_job_async(self, request):
        """查询训练作业

        查询resource_id（数据源id或场景id）下的指定类型的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResJob
        :type request: :class:`huaweicloudsdkres.v1.ShowResJobRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ShowResJobResponse`
        """
        http_info = self._show_res_job_http_info(request)
        return self._call_api(**http_info)

    def show_res_job_async_invoker(self, request):
        http_info = self._show_res_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_res_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instance",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_res_recall_set_async(self, request):
        """查询训练作业候选集

        查询给定workspaces_id和指定resource_id下的候选集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResRecallSet
        :type request: :class:`huaweicloudsdkres.v1.ShowResRecallSetRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ShowResRecallSetResponse`
        """
        http_info = self._show_res_recall_set_http_info(request)
        return self._call_api(**http_info)

    def show_res_recall_set_async_invoker(self, request):
        http_info = self._show_res_recall_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_res_recall_set_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/result-set",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResRecallSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'use_type' in local_var_params:
            query_params.append(('use_type', local_var_params['use_type']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_res_scene_async(self, request):
        """查询场景详情

        查询指定场景的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResScene
        :type request: :class:`huaweicloudsdkres.v1.ShowResSceneRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ShowResSceneResponse`
        """
        http_info = self._show_res_scene_http_info(request)
        return self._call_api(**http_info)

    def show_res_scene_async_invoker(self, request):
        http_info = self._show_res_scene_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_res_scene_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/scenes/{scene_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResSceneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'scene_id' in local_var_params:
            path_params['scene_id'] = local_var_params['scene_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_res_wrokspace_async(self, request):
        """查询工作空间详情

        查询指定工作空间的具体信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResWrokspace
        :type request: :class:`huaweicloudsdkres.v1.ShowResWrokspaceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.ShowResWrokspaceResponse`
        """
        http_info = self._show_res_wrokspace_http_info(request)
        return self._call_api(**http_info)

    def show_res_wrokspace_async_invoker(self, request):
        http_info = self._show_res_wrokspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_res_wrokspace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResWrokspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_res_job_async(self, request):
        """执行作业

        执行独立的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartResJob
        :type request: :class:`huaweicloudsdkres.v1.StartResJobRequest`
        :rtype: :class:`huaweicloudsdkres.v1.StartResJobResponse`
        """
        http_info = self._start_res_job_http_info(request)
        return self._call_api(**http_info)

    def start_res_job_async_invoker(self, request):
        http_info = self._start_res_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_res_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/jobs/{job_id}/schedule-job",
            "request_type": request.__class__.__name__,
            "response_type": "StartResJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_res_scene_jobs_async(self, request):
        """执行场景

        执行场景下面的所有作业和服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartResSceneJobs
        :type request: :class:`huaweicloudsdkres.v1.StartResSceneJobsRequest`
        :rtype: :class:`huaweicloudsdkres.v1.StartResSceneJobsResponse`
        """
        http_info = self._start_res_scene_jobs_http_info(request)
        return self._call_api(**http_info)

    def start_res_scene_jobs_async_invoker(self, request):
        http_info = self._start_res_scene_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_res_scene_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/schedule-scene",
            "request_type": request.__class__.__name__,
            "response_type": "StartResSceneJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_res_datasource_async(self, request):
        """修改数据源内容

        修改指定数据源的配置内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResDatasource
        :type request: :class:`huaweicloudsdkres.v1.UpdateResDatasourceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.UpdateResDatasourceResponse`
        """
        http_info = self._update_res_datasource_http_info(request)
        return self._call_api(**http_info)

    def update_res_datasource_async_invoker(self, request):
        http_info = self._update_res_datasource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_res_datasource_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResDatasourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def update_res_datastruct_async(self, request):
        """修改数据源特征

        修改数据源中的特征。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResDatastruct
        :type request: :class:`huaweicloudsdkres.v1.UpdateResDatastructRequest`
        :rtype: :class:`huaweicloudsdkres.v1.UpdateResDatastructResponse`
        """
        http_info = self._update_res_datastruct_http_info(request)
        return self._call_api(**http_info)

    def update_res_datastruct_async_invoker(self, request):
        http_info = self._update_res_datastruct_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_res_datastruct_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{datasource_id}/data-struct",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResDatastructResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def update_res_intelligent_scene_async(self, request):
        """更新智能场景内容

        更新智能场景的内容信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResIntelligentScene
        :type request: :class:`huaweicloudsdkres.v1.UpdateResIntelligentSceneRequest`
        :rtype: :class:`huaweicloudsdkres.v1.UpdateResIntelligentSceneResponse`
        """
        http_info = self._update_res_intelligent_scene_http_info(request)
        return self._call_api(**http_info)

    def update_res_intelligent_scene_async_invoker(self, request):
        http_info = self._update_res_intelligent_scene_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_res_intelligent_scene_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/intelligent-scenes/{scene_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResIntelligentSceneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scene_id' in local_var_params:
            path_params['scene_id'] = local_var_params['scene_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def update_res_job_async(self, request):
        """修改训练作业参数

        修改指定作业的元数据信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResJob
        :type request: :class:`huaweicloudsdkres.v1.UpdateResJobRequest`
        :rtype: :class:`huaweicloudsdkres.v1.UpdateResJobResponse`
        """
        http_info = self._update_res_job_http_info(request)
        return self._call_api(**http_info)

    def update_res_job_async_invoker(self, request):
        http_info = self._update_res_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_res_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instance/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def update_res_online_instance_async(self, request):
        """修改在线服务参数

        修改指定在线服务的元数据内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResOnlineInstance
        :type request: :class:`huaweicloudsdkres.v1.UpdateResOnlineInstanceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.UpdateResOnlineInstanceResponse`
        """
        http_info = self._update_res_online_instance_http_info(request)
        return self._call_api(**http_info)

    def update_res_online_instance_async_invoker(self, request):
        http_info = self._update_res_online_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_res_online_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/service-instance/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResOnlineInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'content_type' in local_var_params:
            query_params.append(('Content-Type', local_var_params['content_type']))

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

    def update_res_scene_async(self, request):
        """更新自定义场景内容

        更新自定义场景的内容信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResScene
        :type request: :class:`huaweicloudsdkres.v1.UpdateResSceneRequest`
        :rtype: :class:`huaweicloudsdkres.v1.UpdateResSceneResponse`
        """
        http_info = self._update_res_scene_http_info(request)
        return self._call_api(**http_info)

    def update_res_scene_async_invoker(self, request):
        http_info = self._update_res_scene_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_res_scene_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}/scenes/{scene_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResSceneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scene_id' in local_var_params:
            path_params['scene_id'] = local_var_params['scene_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def update_res_workspace_async(self, request):
        """更新工作空间

        更新工作空间信息, 只允许更新描述信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResWorkspace
        :type request: :class:`huaweicloudsdkres.v1.UpdateResWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkres.v1.UpdateResWorkspaceResponse`
        """
        http_info = self._update_res_workspace_http_info(request)
        return self._call_api(**http_info)

    def update_res_workspace_async_invoker(self, request):
        http_info = self._update_res_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_res_workspace_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResWorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

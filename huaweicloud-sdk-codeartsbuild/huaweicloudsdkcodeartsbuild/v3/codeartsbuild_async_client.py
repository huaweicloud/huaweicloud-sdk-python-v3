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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodeartsbuild'")


class CodeArtsBuildAsyncClient(Client):
    def __init__(self):
        super(CodeArtsBuildAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartsbuild.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeArtsBuildAsyncClient":
                raise TypeError("client type error, support client type is CodeArtsBuildAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_build_job_async(self, request):
        r"""创建构建任务

        创建构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobResponse`
        """
        http_info = self._create_build_job_http_info(request)
        return self._call_api(**http_info)

    def create_build_job_async_invoker(self, request):
        http_info = self._create_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBuildJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_templates_async(self, request):
        r"""创建构建模板

        创建构建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTemplates
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplatesResponse`
        """
        http_info = self._create_templates_http_info(request)
        return self._call_api(**http_info)

    def create_templates_async_invoker(self, request):
        http_info = self._create_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_templates_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/templates/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplatesResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_build_job_async(self, request):
        r"""删除构建任务

        删除构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteBuildJobResponse`
        """
        http_info = self._delete_build_job_http_info(request)
        return self._call_api(**http_info)

    def delete_build_job_async_invoker(self, request):
        http_info = self._delete_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/{job_id}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBuildJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_templates_async(self, request):
        r"""删除构建模板

        删除构建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTemplates
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteTemplatesResponse`
        """
        http_info = self._delete_templates_http_info(request)
        return self._call_api(**http_info)

    def delete_templates_async_invoker(self, request):
        http_info = self._delete_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_templates_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/templates/{uuid}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_build_job_async(self, request):
        r"""禁用构建任务

        禁用构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DisableBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DisableBuildJobResponse`
        """
        http_info = self._disable_build_job_http_info(request)
        return self._call_api(**http_info)

    def disable_build_job_async_invoker(self, request):
        http_info = self._disable_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/{job_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableBuildJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_notice_async(self, request):
        r"""取消通知

        取消通知
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableNotice
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DisableNoticeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DisableNoticeResponse`
        """
        http_info = self._disable_notice_http_info(request)
        return self._call_api(**http_info)

    def disable_notice_async_invoker(self, request):
        http_info = self._disable_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_notice_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/notice/{job_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableNoticeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'notice_type' in local_var_params:
            query_params.append(('notice_type', local_var_params['notice_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_build_log_async(self, request):
        r"""下载全量构建日志

        下载全量构建日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadBuildLog
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadBuildLogRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadBuildLogResponse`
        """
        http_info = self._download_build_log_http_info(request)
        return self._call_api(**http_info)

    def download_build_log_async_invoker(self, request):
        http_info = self._download_build_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_build_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{record_id}/download-log",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadBuildLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []
        if 'log_level' in local_var_params:
            query_params.append(('log_level', local_var_params['log_level']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_keystore_async(self, request):
        r"""KeyStore文件下载

        下载指定租户下的KeyStore文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadKeystore
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadKeystoreRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadKeystoreResponse`
        """
        http_info = self._download_keystore_http_info(request)
        return self._call_api(**http_info)

    def download_keystore_async_invoker(self, request):
        http_info = self._download_keystore_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_keystore_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/keystore",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadKeystoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_real_time_log_async(self, request):
        r"""下载构建实时日志

        下载构建实时日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadRealTimeLog
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadRealTimeLogRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadRealTimeLogResponse`
        """
        http_info = self._download_real_time_log_http_info(request)
        return self._call_api(**http_info)

    def download_real_time_log_async_invoker(self, request):
        http_info = self._download_real_time_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_real_time_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/{build_no}/real-time-log",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadRealTimeLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'length' in local_var_params:
            query_params.append(('length', local_var_params['length']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_task_log_async(self, request):
        r"""下载构建步骤日志

        下载构建步骤日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadTaskLog
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadTaskLogRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadTaskLogResponse`
        """
        http_info = self._download_task_log_http_info(request)
        return self._call_api(**http_info)

    def download_task_log_async_invoker(self, request):
        http_info = self._download_task_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_task_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{record_id}/task-log",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadTaskLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'log_level' in local_var_params:
            query_params.append(('log_level', local_var_params['log_level']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_build_job_async(self, request):
        r"""恢复构建任务

        恢复构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.EnableBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.EnableBuildJobResponse`
        """
        http_info = self._enable_build_job_http_info(request)
        return self._call_api(**http_info)

    def enable_build_job_async_invoker(self, request):
        http_info = self._enable_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/{job_id}/recover",
            "request_type": request.__class__.__name__,
            "response_type": "EnableBuildJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_build_info_record_async(self, request):
        r"""获取任务构建记录列表

        获取任务构建记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuildInfoRecord
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildInfoRecordRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildInfoRecordResponse`
        """
        http_info = self._list_build_info_record_http_info(request)
        return self._call_api(**http_info)

    def list_build_info_record_async_invoker(self, request):
        http_info = self._list_build_info_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_build_info_record_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/build-info-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListBuildInfoRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_job_config_async(self, request):
        r"""获取构建任务详情

        获取构建任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobConfig
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListJobConfigRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListJobConfigResponse`
        """
        http_info = self._list_job_config_http_info(request)
        return self._call_api(**http_info)

    def list_job_config_async_invoker(self, request):
        http_info = self._list_job_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_job_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'get_all_params' in local_var_params:
            query_params.append(('get_all_params', local_var_params['get_all_params']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_notice_async(self, request):
        r"""查询通知

        查询通知
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotice
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListNoticeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListNoticeResponse`
        """
        http_info = self._list_notice_http_info(request)
        return self._call_api(**http_info)

    def list_notice_async_invoker(self, request):
        http_info = self._list_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notice_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/notice/{job_id}/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListNoticeResponse"
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

        auth_settings = ['apig-auth-iam']

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
        r"""查询构建模板

        查询构建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_async_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/templates/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def run_job_async(self, request):
        r"""执行构建任务

        执行构建任务,可传自定义参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.RunJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.RunJobResponse`
        """
        http_info = self._run_job_http_info(request)
        return self._call_api(**http_info)

    def run_job_async_invoker(self, request):
        http_info = self._run_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/build",
            "request_type": request.__class__.__name__,
            "response_type": "RunJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_history_details_async(self, request):
        r"""获取构建历史详情信息接口

        获取构建历史详情信息接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHistoryDetails
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowHistoryDetailsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowHistoryDetailsResponse`
        """
        http_info = self._show_history_details_http_info(request)
        return self._call_api(**http_info)

    def show_history_details_async_invoker(self, request):
        http_info = self._show_history_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_history_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/{build_number}/history-details",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_number' in local_var_params:
            path_params['build_number'] = local_var_params['build_number']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_list_by_project_id_async(self, request):
        r"""查看项目下用户的构建任务列表

        查看项目下用户的构建任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobListByProjectId
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobListByProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobListByProjectIdResponse`
        """
        http_info = self._show_job_list_by_project_id_http_info(request)
        return self._call_api(**http_info)

    def show_job_list_by_project_id_async_invoker(self, request):
        http_info = self._show_job_list_by_project_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_list_by_project_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobListByProjectIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_status_async(self, request):
        r"""查看任务运行状态

        查看任务运行状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobStatus
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobStatusResponse`
        """
        http_info = self._show_job_status_http_info(request)
        return self._call_api(**http_info)

    def show_job_status_async_invoker(self, request):
        http_info = self._show_job_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobStatusResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_success_ratio_async(self, request):
        r"""根据开始时间和结束时间查看构建任务的构建成功率

        根据开始时间和结束时间查看构建任务的构建成功率
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobSuccessRatio
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobSuccessRatioRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobSuccessRatioResponse`
        """
        http_info = self._show_job_success_ratio_http_info(request)
        return self._call_api(**http_info)

    def show_job_success_ratio_async_invoker(self, request):
        http_info = self._show_job_success_ratio_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_success_ratio_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/success-ratio",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobSuccessRatioResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_last_history_async(self, request):
        r"""查询指定代码仓库最近一次成功的构建历史

        查询指定代码仓库最近一次成功的构建历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLastHistory
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowLastHistoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowLastHistoryResponse`
        """
        http_info = self._show_last_history_http_info(request)
        return self._call_api(**http_info)

    def show_last_history_async_invoker(self, request):
        http_info = self._show_last_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_last_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{project_id}/last-history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLastHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'repository_name' in local_var_params:
            query_params.append(('repository_name', local_var_params['repository_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_list_history_async(self, request):
        r"""查看构建任务的构建历史列表

        查看构建任务的构建历史列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListHistory
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowListHistoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowListHistoryResponse`
        """
        http_info = self._show_list_history_http_info(request)
        return self._call_api(**http_info)

    def show_list_history_async_invoker(self, request):
        http_info = self._show_list_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_list_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_list_period_history_async(self, request):
        r"""根据开始时间和结束时间查看构建任务的构建历史列表

        根据开始时间和结束时间查看构建任务的构建历史列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListPeriodHistory
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowListPeriodHistoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowListPeriodHistoryResponse`
        """
        http_info = self._show_list_period_history_http_info(request)
        return self._call_api(**http_info)

    def show_list_period_history_async_invoker(self, request):
        http_info = self._show_list_period_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_list_period_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/period-history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListPeriodHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_output_info_async(self, request):
        r"""获取构建产物详情信息

        获取构建产物详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOutputInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowOutputInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowOutputInfoResponse`
        """
        http_info = self._show_output_info_http_info(request)
        return self._call_api(**http_info)

    def show_output_info_async_invoker(self, request):
        http_info = self._show_output_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_output_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/{build_no}/output-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOutputInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_record_detail_async(self, request):
        r"""获取构建记录信息

        获取构建记录信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordDetail
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRecordDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRecordDetailResponse`
        """
        http_info = self._show_record_detail_http_info(request)
        return self._call_api(**http_info)

    def show_record_detail_async_invoker(self, request):
        http_info = self._show_record_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/jobs/{job_id}/{build_no}/record-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_build_job_async(self, request):
        r"""停止构建任务

        停止构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.StopBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.StopBuildJobResponse`
        """
        http_info = self._stop_build_job_http_info(request)
        return self._call_api(**http_info)

    def stop_build_job_async_invoker(self, request):
        http_info = self._stop_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/{job_id}/{build_no}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopBuildJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_build_job_async(self, request):
        r"""更新构建任务

        更新构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateBuildJobResponse`
        """
        http_info = self._update_build_job_http_info(request)
        return self._call_api(**http_info)

    def update_build_job_async_invoker(self, request):
        http_info = self._update_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBuildJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_notice_async(self, request):
        r"""更新通知

        更新通知
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNotice
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateNoticeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateNoticeResponse`
        """
        http_info = self._update_notice_http_info(request)
        return self._call_api(**http_info)

    def update_notice_async_invoker(self, request):
        http_info = self._update_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notice_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/notice/{job_id}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNoticeResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_related_project_info_async(self, request):
        r"""获取项目列表

        获取项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelatedProjectInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListRelatedProjectInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListRelatedProjectInfoResponse`
        """
        http_info = self._list_related_project_info_http_info(request)
        return self._call_api(**http_info)

    def list_related_project_info_async_invoker(self, request):
        http_info = self._list_related_project_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_related_project_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/domain/project/related-page",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelatedProjectInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_project_permission_async(self, request):
        r"""获取用户权限

        获取用户权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectPermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowProjectPermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowProjectPermissionResponse`
        """
        http_info = self._show_project_permission_http_info(request)
        return self._call_api(**http_info)

    def show_project_permission_async_invoker(self, request):
        http_info = self._show_project_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/domain/user-permission",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_related_project_async(self, request):
        r"""获取当前用户的项目信息列表

        获取当前用户的项目信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRelatedProject
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRelatedProjectRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRelatedProjectResponse`
        """
        http_info = self._show_related_project_http_info(request)
        return self._call_api(**http_info)

    def show_related_project_async_invoker(self, request):
        http_info = self._show_related_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_related_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/domain/project/related",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRelatedProjectResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_summary_build_job_info_async(self, request):
        r"""获取租户任务总数和成功率接口

        获取租户任务总数和成功率接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSummaryBuildJobInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowSummaryBuildJobInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowSummaryBuildJobInfoResponse`
        """
        http_info = self._show_summary_build_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_summary_build_job_info_async_invoker(self, request):
        http_info = self._show_summary_build_job_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_summary_build_job_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/domain/job-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSummaryBuildJobInfoResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_user_over_package_quota_async(self, request):
        r"""当前用户所在项目所属租户的包周期每月时长是否超额

        当前用户所在项目所属租户的包周期每月时长是否超额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserOverPackageQuota
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowUserOverPackageQuotaRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowUserOverPackageQuotaResponse`
        """
        http_info = self._show_user_over_package_quota_http_info(request)
        return self._call_api(**http_info)

    def show_user_over_package_quota_async_invoker(self, request):
        http_info = self._show_user_over_package_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_over_package_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/domain/package/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserOverPackageQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_dockerfile_template_async(self, request):
        r"""获取dockerfileTemplate

        获取dockerfileTemplate
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDockerfileTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowDockerfileTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowDockerfileTemplateResponse`
        """
        http_info = self._show_dockerfile_template_http_info(request)
        return self._call_api(**http_info)

    def show_dockerfile_template_async_invoker(self, request):
        http_info = self._show_dockerfile_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dockerfile_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/image/dockerfile-template",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDockerfileTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_image_template_list_async(self, request):
        r"""获取镜像模板列表

        获取镜像模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageTemplateList
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowImageTemplateListRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowImageTemplateListResponse`
        """
        http_info = self._show_image_template_list_http_info(request)
        return self._call_api(**http_info)

    def show_image_template_list_async_invoker(self, request):
        http_info = self._show_image_template_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_template_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/image/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageTemplateListResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_job_count_is_top_limit_async(self, request):
        r"""检查任务数量是否上限

        检查任务数量是否上限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckJobCountIsTopLimit
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CheckJobCountIsTopLimitRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CheckJobCountIsTopLimitResponse`
        """
        http_info = self._check_job_count_is_top_limit_http_info(request)
        return self._call_api(**http_info)

    def check_job_count_is_top_limit_async_invoker(self, request):
        http_info = self._check_job_count_is_top_limit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_job_count_is_top_limit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/check/count",
            "request_type": request.__class__.__name__,
            "response_type": "CheckJobCountIsTopLimitResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_job_name_is_exists_async(self, request):
        r"""查看项目下任务名是否存在

        查看项目下任务名是否存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckJobNameIsExists
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CheckJobNameIsExistsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CheckJobNameIsExistsResponse`
        """
        http_info = self._check_job_name_is_exists_http_info(request)
        return self._call_api(**http_info)

    def check_job_name_is_exists_async_invoker(self, request):
        http_info = self._check_job_name_is_exists_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_job_name_is_exists_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/check/exist",
            "request_type": request.__class__.__name__,
            "response_type": "CheckJobNameIsExistsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_webhook_url_async(self, request):
        r"""检查webhook地址参数

        检查webhook地址参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckWebhookUrl
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CheckWebhookUrlRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CheckWebhookUrlResponse`
        """
        http_info = self._check_webhook_url_http_info(request)
        return self._call_api(**http_info)

    def check_webhook_url_async_invoker(self, request):
        http_info = self._check_webhook_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_webhook_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/check/webhook-url",
            "request_type": request.__class__.__name__,
            "response_type": "CheckWebhookUrlResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def clear_recycling_jobs_async(self, request):
        r"""清空回收站中的任务

        清空回收站中的任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ClearRecyclingJobs
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ClearRecyclingJobsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ClearRecyclingJobsResponse`
        """
        http_info = self._clear_recycling_jobs_http_info(request)
        return self._call_api(**http_info)

    def clear_recycling_jobs_async_invoker(self, request):
        http_info = self._clear_recycling_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _clear_recycling_jobs_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/job/recycling-empty",
            "request_type": request.__class__.__name__,
            "response_type": "ClearRecyclingJobsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def copy_job_async(self, request):
        r"""复制构建任务

        复制构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CopyJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CopyJobResponse`
        """
        http_info = self._copy_job_http_info(request)
        return self._call_api(**http_info)

    def copy_job_async_invoker(self, request):
        http_info = self._copy_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_new_job_async(self, request):
        r"""创建构建任务

        创建构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNewJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CreateNewJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CreateNewJobResponse`
        """
        http_info = self._create_new_job_http_info(request)
        return self._call_api(**http_info)

    def create_new_job_async_invoker(self, request):
        http_info = self._create_new_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_new_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNewJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_recycling_jobs_async(self, request):
        r"""删除回收站中的任务

        删除回收站中的任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRecyclingJobs
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteRecyclingJobsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteRecyclingJobsResponse`
        """
        http_info = self._delete_recycling_jobs_http_info(request)
        return self._call_api(**http_info)

    def delete_recycling_jobs_async_invoker(self, request):
        http_info = self._delete_recycling_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_recycling_jobs_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/job/recycling-deletion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecyclingJobsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_the_job_async(self, request):
        r"""删除任务

        删除任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTheJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteTheJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteTheJobResponse`
        """
        http_info = self._delete_the_job_http_info(request)
        return self._call_api(**http_info)

    def delete_the_job_async_invoker(self, request):
        http_info = self._delete_the_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_the_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/job/{job_id}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTheJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_the_job_async(self, request):
        r"""禁用任务

        禁用任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableTheJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DisableTheJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DisableTheJobResponse`
        """
        http_info = self._disable_the_job_http_info(request)
        return self._call_api(**http_info)

    def disable_the_job_async_invoker(self, request):
        http_info = self._disable_the_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_the_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/{job_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableTheJobResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def execute_job_async(self, request):
        r"""执行构建

        执行构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ExecuteJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ExecuteJobResponse`
        """
        http_info = self._execute_job_http_info(request)
        return self._call_api(**http_info)

    def execute_job_async_invoker(self, request):
        http_info = self._execute_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/execute",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_build_parameter_async(self, request):
        r"""详情页获取构建参数

        详情页获取构建参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuildParameter
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildParameterRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildParameterResponse`
        """
        http_info = self._list_build_parameter_http_info(request)
        return self._call_api(**http_info)

    def list_build_parameter_async_invoker(self, request):
        http_info = self._list_build_parameter_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_build_parameter_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/{build_no}/history-parameters",
            "request_type": request.__class__.__name__,
            "response_type": "ListBuildParameterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_job_async(self, request):
        r"""查看用户全部的构建任务列表

        查看用户全部的构建任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListJobResponse`
        """
        http_info = self._list_job_http_info(request)
        return self._call_api(**http_info)

    def list_job_async_invoker(self, request):
        http_info = self._list_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_order' in local_var_params:
            query_params.append(('sort_order', local_var_params['sort_order']))
        if 'creator_id' in local_var_params:
            query_params.append(('creator_id', local_var_params['creator_id']))
        if 'build_status' in local_var_params:
            query_params.append(('build_status', local_var_params['build_status']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_jobs_async(self, request):
        r"""查询项目任务列表

        查询项目任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectJobs
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListProjectJobsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListProjectJobsResponse`
        """
        http_info = self._list_project_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_project_jobs_async_invoker(self, request):
        http_info = self._list_project_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{project_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_order' in local_var_params:
            query_params.append(('sort_order', local_var_params['sort_order']))
        if 'creator_id' in local_var_params:
            query_params.append(('creator_id', local_var_params['creator_id']))
        if 'build_status' in local_var_params:
            query_params.append(('build_status', local_var_params['build_status']))
        if 'by_group' in local_var_params:
            query_params.append(('by_group', local_var_params['by_group']))
        if 'group_path_id' in local_var_params:
            query_params.append(('group_path_id', local_var_params['group_path_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_recycling_job_async(self, request):
        r"""查看回收站中删除的构建任务列表

        查看回收站中删除的构建任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecyclingJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListRecyclingJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListRecyclingJobResponse`
        """
        http_info = self._list_recycling_job_http_info(request)
        return self._call_api(**http_info)

    def list_recycling_job_async_invoker(self, request):
        http_info = self._list_recycling_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_recycling_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/recycling-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecyclingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_update_job_history_async(self, request):
        r"""获取修改历史

        获取修改历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUpdateJobHistory
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListUpdateJobHistoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListUpdateJobHistoryResponse`
        """
        http_info = self._list_update_job_history_http_info(request)
        return self._call_api(**http_info)

    def list_update_job_history_async_invoker(self, request):
        http_info = self._list_update_job_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_update_job_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/history",
            "request_type": request.__class__.__name__,
            "response_type": "ListUpdateJobHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def restore_recycling_jobs_async(self, request):
        r"""恢复回收站中的任务

        恢复回收站中的任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreRecyclingJobs
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.RestoreRecyclingJobsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.RestoreRecyclingJobsResponse`
        """
        http_info = self._restore_recycling_jobs_http_info(request)
        return self._call_api(**http_info)

    def restore_recycling_jobs_async_invoker(self, request):
        http_info = self._restore_recycling_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_recycling_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/recycling-restoration",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreRecyclingJobsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_keep_time_async(self, request):
        r"""设置回收站中的任务保留时间

        设置回收站中的任务保留时间,该接口需要租户账号才能访问，租户子账号无权限访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetKeepTime
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.SetKeepTimeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.SetKeepTimeResponse`
        """
        http_info = self._set_keep_time_http_info(request)
        return self._call_api(**http_info)

    def set_keep_time_async_invoker(self, request):
        http_info = self._set_keep_time_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_keep_time_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/keep-time",
            "request_type": request.__class__.__name__,
            "response_type": "SetKeepTimeResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_params_list_async(self, request):
        r"""编辑页获取参数类型的接口

        编辑页获取参数类型的接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildParamsList
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildParamsListRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildParamsListResponse`
        """
        http_info = self._show_build_params_list_http_info(request)
        return self._call_api(**http_info)

    def show_build_params_list_async_invoker(self, request):
        http_info = self._show_build_params_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_params_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/build-params",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildParamsListResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_copy_name_async(self, request):
        r"""复制任务名

        复制任务名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCopyName
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowCopyNameRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowCopyNameResponse`
        """
        http_info = self._show_copy_name_http_info(request)
        return self._call_api(**http_info)

    def show_copy_name_async_invoker(self, request):
        http_info = self._show_copy_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_copy_name_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/copy-name",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCopyNameResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_default_build_parameters_async(self, request):
        r"""获取编译构建默认参数

        获取编译构建默认参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDefaultBuildParameters
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowDefaultBuildParametersRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowDefaultBuildParametersResponse`
        """
        http_info = self._show_default_build_parameters_http_info(request)
        return self._call_api(**http_info)

    def show_default_build_parameters_async_invoker(self, request):
        http_info = self._show_default_build_parameters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_default_build_parameters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/default-parameters",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDefaultBuildParametersResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_default_project_permission_async(self, request):
        r"""获取当前项目默认角色权限矩阵信息

        获取当前项目默认角色权限矩阵信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDefaultProjectPermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowDefaultProjectPermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowDefaultProjectPermissionResponse`
        """
        http_info = self._show_default_project_permission_http_info(request)
        return self._call_api(**http_info)

    def show_default_project_permission_async_invoker(self, request):
        http_info = self._show_default_project_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_default_project_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/project/default-permission",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDefaultProjectPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_disable_async(self, request):
        r"""查询任务是否已禁用

        查询任务是否已禁用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDisable
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowDisableRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowDisableResponse`
        """
        http_info = self._show_disable_http_info(request)
        return self._call_api(**http_info)

    def show_disable_async_invoker(self, request):
        http_info = self._show_disable_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_disable_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/check/disable",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDisableResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_config_async(self, request):
        r"""获取构建任务详情

        获取构建任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobConfig
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobConfigRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobConfigResponse`
        """
        http_info = self._show_job_config_http_info(request)
        return self._call_api(**http_info)

    def show_job_config_async_invoker(self, request):
        http_info = self._show_job_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'get_all_params' in local_var_params:
            query_params.append(('get_all_params', local_var_params['get_all_params']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_config_diff_async(self, request):
        r"""获取构建任务配置的对比差异

        获取构建任务配置的对比差异
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobConfigDiff
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobConfigDiffRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobConfigDiffResponse`
        """
        http_info = self._show_job_config_diff_http_info(request)
        return self._call_api(**http_info)

    def show_job_config_diff_async_invoker(self, request):
        http_info = self._show_job_config_diff_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_config_diff_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/diff",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobConfigDiffResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'revisedl_no' in local_var_params:
            query_params.append(('revisedl_no', local_var_params['revisedl_no']))
        if 'original_no' in local_var_params:
            query_params.append(('original_no', local_var_params['original_no']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_info_async(self, request):
        r"""查看构建任务构建信息

        查看构建任务构建信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobInfoResponse`
        """
        http_info = self._show_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_job_info_async_invoker(self, request):
        http_info = self._show_job_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobInfoResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_notice_config_info_async(self, request):
        r"""获取通知信息

        获取通知信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobNoticeConfigInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobNoticeConfigInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobNoticeConfigInfoResponse`
        """
        http_info = self._show_job_notice_config_info_http_info(request)
        return self._call_api(**http_info)

    def show_job_notice_config_info_async_invoker(self, request):
        http_info = self._show_job_notice_config_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_notice_config_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/notice",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobNoticeConfigInfoResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_pipeline_info_async(self, request):
        r"""流水线查看构建任务信息

        流水线查看构建任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobPipelineInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobPipelineInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobPipelineInfoResponse`
        """
        http_info = self._show_job_pipeline_info_http_info(request)
        return self._call_api(**http_info)

    def show_job_pipeline_info_async_invoker(self, request):
        http_info = self._show_job_pipeline_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_pipeline_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/pipeline-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobPipelineInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'all' in local_var_params:
            query_params.append(('all', local_var_params['all']))
        if 'check_param_used' in local_var_params:
            query_params.append(('check_param_used', local_var_params['check_param_used']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_role_permission_async(self, request):
        r"""获取构建任务的角色权限矩阵信息

        获取构建任务的角色权限矩阵信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobRolePermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobRolePermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobRolePermissionResponse`
        """
        http_info = self._show_job_role_permission_http_info(request)
        return self._call_api(**http_info)

    def show_job_role_permission_async_invoker(self, request):
        http_info = self._show_job_role_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_role_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/permission/role",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobRolePermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_step_status_async(self, request):
        r"""查询任务状态

        查询任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobStepStatus
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobStepStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobStepStatusResponse`
        """
        http_info = self._show_job_step_status_http_info(request)
        return self._call_api(**http_info)

    def show_job_step_status_async_invoker(self, request):
        http_info = self._show_job_step_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_step_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobStepStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'build_no' in local_var_params:
            query_params.append(('build_no', local_var_params['build_no']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_system_parameters_async(self, request):
        r"""查看系统预定义参数

        查看系统预定义参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobSystemParameters
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobSystemParametersRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobSystemParametersResponse`
        """
        http_info = self._show_job_system_parameters_http_info(request)
        return self._call_api(**http_info)

    def show_job_system_parameters_async_invoker(self, request):
        http_info = self._show_job_system_parameters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_system_parameters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/system-parameters",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobSystemParametersResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_project_job_permission_async(self, request):
        r"""获取任务权限矩阵

        获取任务权限矩阵
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectJobPermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowProjectJobPermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowProjectJobPermissionResponse`
        """
        http_info = self._show_project_job_permission_http_info(request)
        return self._call_api(**http_info)

    def show_project_job_permission_async_invoker(self, request):
        http_info = self._show_project_job_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_job_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/permission",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectJobPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_running_status_async(self, request):
        r"""查看任务是否在构建

        查看任务是否在构建
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRunningStatus
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRunningStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRunningStatusResponse`
        """
        http_info = self._show_running_status_http_info(request)
        return self._call_api(**http_info)

    def show_running_status_async_invoker(self, request):
        http_info = self._show_running_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_running_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/running-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRunningStatusResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_the_job_async(self, request):
        r"""停止构建任务v1

        停止构建任务v1
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopTheJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.StopTheJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.StopTheJobResponse`
        """
        http_info = self._stop_the_job_http_info(request)
        return self._call_api(**http_info)

    def stop_the_job_async_invoker(self, request):
        http_info = self._stop_the_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_the_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/{job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopTheJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'build_no' in local_var_params:
            query_params.append(('build_no', local_var_params['build_no']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_new_job_async(self, request):
        r"""更新构建任务

        更新构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNewJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateNewJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateNewJobResponse`
        """
        http_info = self._update_new_job_http_info(request)
        return self._call_api(**http_info)

    def update_new_job_async_invoker(self, request):
        http_info = self._update_new_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_new_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNewJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_keystore_permission_async(self, request):
        r"""添加文件权限

        添加文件权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddKeystorePermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.AddKeystorePermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.AddKeystorePermissionResponse`
        """
        http_info = self._add_keystore_permission_http_info(request)
        return self._call_api(**http_info)

    def add_keystore_permission_async_invoker(self, request):
        http_info = self._add_keystore_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_keystore_permission_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/keystore/permission/add",
            "request_type": request.__class__.__name__,
            "response_type": "AddKeystorePermissionResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_keystore_async(self, request):
        r"""删除文件管理文件

        删除文件管理文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKeystore
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteKeystoreRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteKeystoreResponse`
        """
        http_info = self._delete_keystore_http_info(request)
        return self._call_api(**http_info)

    def delete_keystore_async_invoker(self, request):
        http_info = self._delete_keystore_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_keystore_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/keystore/{keystore_id}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKeystoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_keystore_permission_async(self, request):
        r"""文件管理删除权限

        文件管理删除权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKeystorePermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteKeystorePermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteKeystorePermissionResponse`
        """
        http_info = self._delete_keystore_permission_http_info(request)
        return self._call_api(**http_info)

    def delete_keystore_permission_async_invoker(self, request):
        http_info = self._delete_keystore_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_keystore_permission_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/keystore/permission/{permission_id}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKeystorePermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'permission_id' in local_var_params:
            path_params['permission_id'] = local_var_params['permission_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_keystore_by_name_async(self, request):
        r"""文件管理文件下载

        文件管理文件下载
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadKeystoreByName
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadKeystoreByNameRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadKeystoreByNameResponse`
        """
        http_info = self._download_keystore_by_name_http_info(request)
        return self._call_api(**http_info)

    def download_keystore_by_name_async_invoker(self, request):
        http_info = self._download_keystore_by_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_keystore_by_name_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/keystore/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadKeystoreByNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_keystore_async(self, request):
        r"""查询用户可使用文件

        查询用户可使用文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeystore
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreResponse`
        """
        http_info = self._list_keystore_http_info(request)
        return self._call_api(**http_info)

    def list_keystore_async_invoker(self, request):
        http_info = self._list_keystore_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_keystore_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/keystore/name",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeystoreResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_keystore_search_async(self, request):
        r"""查询租户下文件列表

        查询租户下文件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeystoreSearch
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreSearchRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreSearchResponse`
        """
        http_info = self._list_keystore_search_http_info(request)
        return self._call_api(**http_info)

    def list_keystore_search_async_invoker(self, request):
        http_info = self._list_keystore_search_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_keystore_search_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/keystore/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeystoreSearchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_keystore_permission_async(self, request):
        r"""文件管理查询权限

        文件管理查询权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKeystorePermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowKeystorePermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowKeystorePermissionResponse`
        """
        http_info = self._show_keystore_permission_http_info(request)
        return self._call_api(**http_info)

    def show_keystore_permission_async_invoker(self, request):
        http_info = self._show_keystore_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_keystore_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/keystore/permission/{keystore_id}/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKeystorePermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_keystore_async(self, request):
        r"""更新文件信息

        更新文件信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeystore
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateKeystoreRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateKeystoreResponse`
        """
        http_info = self._update_keystore_http_info(request)
        return self._call_api(**http_info)

    def update_keystore_async_invoker(self, request):
        http_info = self._update_keystore_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_keystore_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/keystore/update/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKeystoreResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_keystore_permission_async(self, request):
        r"""配置文件权限

        配置文件权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeystorePermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateKeystorePermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateKeystorePermissionResponse`
        """
        http_info = self._update_keystore_permission_http_info(request)
        return self._call_api(**http_info)

    def update_keystore_permission_async_invoker(self, request):
        http_info = self._update_keystore_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_keystore_permission_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/keystore/permission/edit",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKeystorePermissionResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upload_keystore_async(self, request):
        r"""上传文件

        上传文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadKeystore
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.UploadKeystoreRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.UploadKeystoreResponse`
        """
        http_info = self._upload_keystore_http_info(request)
        return self._call_api(**http_info)

    def upload_keystore_async_invoker(self, request):
        http_info = self._upload_keystore_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_keystore_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/keystore/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadKeystoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'privacy' in local_var_params:
            form_params['privacy'] = local_var_params['privacy']
        if 'description' in local_var_params:
            form_params['description'] = local_var_params['description']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_log_by_record_id_async(self, request):
        r"""下载构建日志(待下线)

        下载构建日志(待下线)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadLogByRecordId
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadLogByRecordIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadLogByRecordIdResponse`
        """
        http_info = self._download_log_by_record_id_http_info(request)
        return self._call_api(**http_info)

    def download_log_by_record_id_async_invoker(self, request):
        http_info = self._download_log_by_record_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_log_by_record_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{record_id}/download-log",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadLogByRecordIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_flow_graph_async(self, request):
        r"""获取构建记录的有向无环图(待下线)

        获取构建记录的有向无环图(待下线)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlowGraph
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowFlowGraphRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowFlowGraphResponse`
        """
        http_info = self._show_flow_graph_http_info(request)
        return self._call_api(**http_info)

    def show_flow_graph_async_invoker(self, request):
        http_info = self._show_flow_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_flow_graph_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{build_flow_record_id}/flow-graph",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlowGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'build_flow_record_id' in local_var_params:
            path_params['build_flow_record_id'] = local_var_params['build_flow_record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_record_info_async(self, request):
        r"""获取构建记录信息(待下线)

        获取构建记录信息(待下线)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRecordInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRecordInfoResponse`
        """
        http_info = self._show_record_info_http_info(request)
        return self._call_api(**http_info)

    def show_record_info_async_invoker(self, request):
        http_info = self._show_record_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/{build_no}/record-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_job_async(self, request):
        r"""停止构建任务(待下线)

        停止构建任务(待下线)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.StopJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.StopJobResponse`
        """
        http_info = self._stop_job_http_info(request)
        return self._call_api(**http_info)

    def stop_job_async_invoker(self, request):
        http_info = self._stop_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopJobResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_brief_record_async(self, request):
        r"""获取指定工程的简要构建信息

        获取指定工程的简要构建信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBriefRecord
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListBriefRecordRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListBriefRecordResponse`
        """
        http_info = self._list_brief_record_http_info(request)
        return self._call_api(**http_info)

    def list_brief_record_async_invoker(self, request):
        http_info = self._list_brief_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_brief_record_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/record/brief",
            "request_type": request.__class__.__name__,
            "response_type": "ListBriefRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_build_info_record_by_job_id_async(self, request):
        r"""获取任务构建记录列表v1

        获取任务构建记录列表v1
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuildInfoRecordByJobId
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildInfoRecordByJobIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildInfoRecordByJobIdResponse`
        """
        http_info = self._list_build_info_record_by_job_id_http_info(request)
        return self._call_api(**http_info)

    def list_build_info_record_by_job_id_async_invoker(self, request):
        http_info = self._list_build_info_record_by_job_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_build_info_record_by_job_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{job_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListBuildInfoRecordByJobIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_records_async(self, request):
        r"""获取指定工程的构建记录列表

        获取指定工程的构建记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecords
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListRecordsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListRecordsResponse`
        """
        http_info = self._list_records_http_info(request)
        return self._call_api(**http_info)

    def list_records_async_invoker(self, request):
        http_info = self._list_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{build_project_id}/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'build_project_id' in local_var_params:
            path_params['build_project_id'] = local_var_params['build_project_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'triggers' in local_var_params:
            query_params.append(('triggers', local_var_params['triggers']))
            collection_formats['triggers'] = 'csv'
        if 'branches' in local_var_params:
            query_params.append(('branches', local_var_params['branches']))
            collection_formats['branches'] = 'csv'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'csv'
        if 'from_date' in local_var_params:
            query_params.append(('from_date', local_var_params['from_date']))
        if 'to_date' in local_var_params:
            query_params.append(('to_date', local_var_params['to_date']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_info_record_async(self, request):
        r"""获取任务构建记录列表

        获取任务构建记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildInfoRecord
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildInfoRecordRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildInfoRecordResponse`
        """
        http_info = self._show_build_info_record_http_info(request)
        return self._call_api(**http_info)

    def show_build_info_record_async_invoker(self, request):
        http_info = self._show_build_info_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_info_record_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{job_id}/{build_no}/build-info-record",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildInfoRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_record_async(self, request):
        r"""查询指定构建记录详情

        查询指定构建记录详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildRecord
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordResponse`
        """
        http_info = self._show_build_record_http_info(request)
        return self._call_api(**http_info)

    def show_build_record_async_invoker(self, request):
        http_info = self._show_build_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_record_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{record_id}/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_record_build_script_async(self, request):
        r"""获取构建记录的构建脚本

        获取构建记录的构建脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildRecordBuildScript
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordBuildScriptRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordBuildScriptResponse`
        """
        http_info = self._show_build_record_build_script_http_info(request)
        return self._call_api(**http_info)

    def show_build_record_build_script_async_invoker(self, request):
        http_info = self._show_build_record_build_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_record_build_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{record_id}/build-script",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildRecordBuildScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_record_flow_graph_async(self, request):
        r"""获取构建记录的有向无环图

        获取构建记录的有向无环图
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildRecordFlowGraph
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordFlowGraphRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordFlowGraphResponse`
        """
        http_info = self._show_build_record_flow_graph_http_info(request)
        return self._call_api(**http_info)

    def show_build_record_flow_graph_async_invoker(self, request):
        http_info = self._show_build_record_flow_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_record_flow_graph_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{build_flow_record_id}/flow-graph",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildRecordFlowGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'build_flow_record_id' in local_var_params:
            path_params['build_flow_record_id'] = local_var_params['build_flow_record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_record_full_stages_async(self, request):
        r"""获取任务各阶段信息

        获取任务各阶段信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildRecordFullStages
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordFullStagesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordFullStagesResponse`
        """
        http_info = self._show_build_record_full_stages_http_info(request)
        return self._call_api(**http_info)

    def show_build_record_full_stages_async_invoker(self, request):
        http_info = self._show_build_record_full_stages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_record_full_stages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{record_id}/full-stages",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildRecordFullStagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []
        if 'cascade' in local_var_params:
            query_params.append(('cascade', local_var_params['cascade']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_build_record_detail_async(self, request):
        r"""获取构建记录信息

        获取构建记录信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobBuildRecordDetail
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildRecordDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildRecordDetailResponse`
        """
        http_info = self._show_job_build_record_detail_http_info(request)
        return self._call_api(**http_info)

    def show_job_build_record_detail_async_invoker(self, request):
        http_info = self._show_job_build_record_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_build_record_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{job_id}/{build_no}/record-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobBuildRecordDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_total_async(self, request):
        r"""构建历史页获取构建次数

        构建历史页获取构建次数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobTotal
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobTotalRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobTotalResponse`
        """
        http_info = self._show_job_total_http_info(request)
        return self._call_api(**http_info)

    def show_job_total_async_invoker(self, request):
        http_info = self._show_job_total_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_total_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{build_project_id}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobTotalResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'build_project_id' in local_var_params:
            path_params['build_project_id'] = local_var_params['build_project_id']

        query_params = []
        if 'from_date' in local_var_params:
            query_params.append(('from_date', local_var_params['from_date']))
        if 'to_date' in local_var_params:
            query_params.append(('to_date', local_var_params['to_date']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_junit_coverage_zip_async(self, request):
        r"""获取单元测试覆盖率报告压缩包

        获取单元测试覆盖率报告压缩包
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadJunitCoverageZip
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadJunitCoverageZipRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadJunitCoverageZipResponse`
        """
        http_info = self._download_junit_coverage_zip_http_info(request)
        return self._call_api(**http_info)

    def download_junit_coverage_zip_async_invoker(self, request):
        http_info = self._download_junit_coverage_zip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_junit_coverage_zip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/junit/coverage/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadJunitCoverageZipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'build_no' in local_var_params:
            query_params.append(('build_no', local_var_params['build_no']))
        if 'root_id' in local_var_params:
            query_params.append(('root_id', local_var_params['root_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_junit_coverage_summary_async(self, request):
        r"""获取单元测试覆盖率报告列表

        获取单元测试覆盖率报告列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJunitCoverageSummary
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListJunitCoverageSummaryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListJunitCoverageSummaryResponse`
        """
        http_info = self._list_junit_coverage_summary_http_info(request)
        return self._call_api(**http_info)

    def list_junit_coverage_summary_async_invoker(self, request):
        http_info = self._list_junit_coverage_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_junit_coverage_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/junit/coverage/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListJunitCoverageSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'build_no' in local_var_params:
            query_params.append(('build_no', local_var_params['build_no']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_repo_branch_async(self, request):
        r"""获取该任务所有分支信息

        获取该任务所有分支信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepoBranch
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListRepoBranchRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListRepoBranchResponse`
        """
        http_info = self._list_repo_branch_http_info(request)
        return self._call_api(**http_info)

    def list_repo_branch_async_invoker(self, request):
        http_info = self._list_repo_branch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repo_branch_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/branches",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepoBranchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'repository_name' in local_var_params:
            query_params.append(('repository_name', local_var_params['repository_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_repository_async(self, request):
        r"""查看仓库

        查看仓库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepository
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListRepositoryResponse`
        """
        http_info = self._list_repository_http_info(request)
        return self._call_api(**http_info)

    def list_repository_async_invoker(self, request):
        http_info = self._list_repository_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/{job_id}/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_build_success_ratio_async(self, request):
        r"""查询构建成功率

        查询构建成功率
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobBuildSuccessRatio
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildSuccessRatioRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildSuccessRatioResponse`
        """
        http_info = self._show_job_build_success_ratio_http_info(request)
        return self._call_api(**http_info)

    def show_job_build_success_ratio_async_invoker(self, request):
        http_info = self._show_job_build_success_ratio_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_build_success_ratio_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/ratio",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobBuildSuccessRatioResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'repository_name' in local_var_params:
            query_params.append(('repository_name', local_var_params['repository_name']))
        if 'branch' in local_var_params:
            query_params.append(('branch', local_var_params['branch']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_build_time_async(self, request):
        r"""洞察构建时长

        洞察构建时长
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobBuildTime
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildTimeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildTimeResponse`
        """
        http_info = self._show_job_build_time_http_info(request)
        return self._call_api(**http_info)

    def show_job_build_time_async_invoker(self, request):
        http_info = self._show_job_build_time_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_build_time_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/time",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobBuildTimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'repository_name' in local_var_params:
            query_params.append(('repository_name', local_var_params['repository_name']))
        if 'branch' in local_var_params:
            query_params.append(('branch', local_var_params['branch']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_report_summary_async(self, request):
        r"""获取覆盖率接口

        获取覆盖率接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReportSummary
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummaryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummaryResponse`
        """
        http_info = self._show_report_summary_http_info(request)
        return self._call_api(**http_info)

    def show_report_summary_async_invoker(self, request):
        http_info = self._show_report_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_report_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/{job_id}/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'build_no' in local_var_params:
            query_params.append(('build_no', local_var_params['build_no']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_template_async(self, request):
        r"""创建构建模板

        创建构建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplateResponse`
        """
        http_info = self._create_template_http_info(request)
        return self._call_api(**http_info)

    def create_template_async_invoker(self, request):
        http_info = self._create_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/template/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateResponse"
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

        auth_settings = ['apig-auth-iam']

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
        r"""删除构建模板

        删除构建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_async_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/template/{uuid}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_custom_template_async(self, request):
        r"""根据条件查询特定模板

        根据条件查询特定模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListCustomTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListCustomTemplateResponse`
        """
        http_info = self._list_custom_template_http_info(request)
        return self._call_api(**http_info)

    def list_custom_template_async_invoker(self, request):
        http_info = self._list_custom_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_custom_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/template/custom",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_official_template_async(self, request):
        r"""查询官方模版

        查询官方模版
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOfficialTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListOfficialTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListOfficialTemplateResponse`
        """
        http_info = self._list_official_template_http_info(request)
        return self._call_api(**http_info)

    def list_official_template_async_invoker(self, request):
        http_info = self._list_official_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_official_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/template/officialtemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ListOfficialTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_recommend_official_template_async(self, request):
        r"""获取官方推荐模板

        获取官方推荐模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecommendOfficialTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListRecommendOfficialTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListRecommendOfficialTemplateResponse`
        """
        http_info = self._list_recommend_official_template_http_info(request)
        return self._call_api(**http_info)

    def list_recommend_official_template_async_invoker(self, request):
        http_info = self._list_recommend_official_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_recommend_official_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/template/recommend",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecommendOfficialTemplateResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def save_template_used_info_async(self, request):
        r"""保存模板使用记录

        保存模板使用记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SaveTemplateUsedInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.SaveTemplateUsedInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.SaveTemplateUsedInfoResponse`
        """
        http_info = self._save_template_used_info_http_info(request)
        return self._call_api(**http_info)

    def save_template_used_info_async_invoker(self, request):
        http_info = self._save_template_used_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _save_template_used_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/template/used-info",
            "request_type": request.__class__.__name__,
            "response_type": "SaveTemplateUsedInfoResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_yaml_template_async(self, request):
        r"""获取代码化构建默认模板

        获取代码化构建默认模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowYamlTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowYamlTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowYamlTemplateResponse`
        """
        http_info = self._show_yaml_template_http_info(request)
        return self._call_api(**http_info)

    def show_yaml_template_async_invoker(self, request):
        http_info = self._show_yaml_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_yaml_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/template/{job_id}/default-template",
            "request_type": request.__class__.__name__,
            "response_type": "ShowYamlTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'default_host' in local_var_params:
            query_params.append(('default_host', local_var_params['default_host']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

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
